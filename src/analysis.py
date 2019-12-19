import pandas as pd
import pandas.io.sql as sqlio
import psycopg2
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn import linear_model
from sklearn.decomposition import PCA
from sklearn.preprocessing import RobustScaler, StandardScaler, OneHotEncoder
import xgboost as xgb
import pickle
from xgboost import XGBClassifier



def read_data(month=False, variance=False):
    """Function that connects to the database and reads the data

    :return: data , price
    :rtype: pd.DataFrame, pd.DataFrame
    """
    try:
        conn = psycopg2.connect("dbname='energyblast' user='postgres' host='159.89.232.46' password='postgres'")
    except:
        print("I am unable to connect to the database")

    sql = 'SELECT * FROM features_region_lags'
    try:
        data = sqlio.read_sql_query(sql, conn)
    except Exception as e:
        print(e)

    sql = 'SELECT * FROM month_price'
    try:
        price = sqlio.read_sql_query(sql, conn)
    except Exception as e:
        print(e)

    conn.close()

    data.set_index('Fecha', inplace=True)
    price.set_index('fecha', inplace=True)

    data['precio'] = price['precio']

    if variance:
        data['precio'] = data.precio - data['PRECIO$L01']
        data.drop(columns=['PRECIO$L01', 'PRECIO$L02'], inplace=True)
    else:
        data['PRECIO$L01'] = np.log(data['PRECIO$L01'] + 1)
        data['PRECIO$L02'] = np.log(data['PRECIO$L02'] + 1)
        data['precio'] = np.log(data['precio'] + 1)

    # Feature included for standardization


    if month:
        enc = OneHotEncoder(handle_unknown='ignore')
        enc.fit(data.index.month.values.reshape(-1, 1))
        months = enc.transform(data.index.month.values.reshape(-1, 1)).toarray()
        months_df = pd.DataFrame(months,
                                 columns=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov',
                                          'Dic'], index=data.index)

        data = pd.concat([months_df, data], axis=1)

    return data.iloc[:-1], price


def pre_process_data(data, price, fillna=True, standardize=True, random_split=True, split_size=0.15, n_components=None):
    """Function that connects to the database and reads the data

    :param data: features for model testing
    :param price: dependant variable for model testing
    :param fillna: whether to fill nans with zero
    :param standardize: whether to standardize the data
    :param random_split: choose type of split
    :param split_size: test size
    :param n_components: number of components for the PCA

    :return: X_train, X_test, y_train, y_test
    :rtype: pd.DataFrame, pd.DataFrame, pd.Series, pd.Series
    """

    # Drop candlestick features
    price = price.iloc[1:]

    if fillna:
        x = data.fillna(0)

    if standardize:
        transformer = StandardScaler().fit(x)
        x_scaled = transformer.transform(x)
        y_scaled = pd.Series(x_scaled[:, -1], name='precio')

        # Remove price from features
        x_scaled = pd.DataFrame(x_scaled, columns=data.columns).drop(columns='precio')

        x_scaled.index = data.index
        y_scaled.index = data.index

    else:
        y_scaled = data['precio']
        x_scaled = data.drop(columns='precio')

    # Split Train and Test Data
    if random_split:
        x_train, x_test, y_train, y_test = train_test_split(x_scaled, y_scaled, test_size=split_size, random_state=0)
    else:
        split = int((data.shape[0] + 1) * (1 - split_size))
        x_train = x_scaled.iloc[:split]
        x_test = x_scaled.iloc[split:]
        y_train = y_scaled.iloc[:split]
        y_test = y_scaled.iloc[split:]

    plt.figure(figsize=(15, 8))
    plt.scatter(y_train.index, y_train, label='Train')
    plt.scatter(y_test.index, y_test, c='red', label='Test')
    plt.title('Price vs Date', fontdict={'fontsize': 20})
    plt.xlabel('Date', fontdict={'fontsize': 16})
    plt.ylabel('Price', fontdict={'fontsize': 16})
    plt.legend(fontsize=14)
    plt.savefig('../figs/train_test_split_' + str(random_split) + '.png', bbox_inches='tight')
    plt.clf()
    plt.close()

    if n_components:
        pca = PCA(n_components=n_components)
        pca.fit(x_train)
        x_train = pca.transform(x_train)
        x_test = pca.transform(x_test)

        # Plot explained variance
        plt.figure(figsize=(15, 8))
        plt.plot(pca.explained_variance_ratio_, marker='o', linewidth=2, markersize=12)
        plt.title(
            'Variance explained: {0:.2f} - Number of Components: {1}\
            '.format(np.sum(pca.explained_variance_ratio_),
                     n_components), fontdict={'fontsize': 20}
        )
        plt.xlabel('Number of components', fontdict={'fontsize': 16})
        plt.ylabel('Ratio of variance explained', fontdict={'fontsize': 16})
        plt.savefig('../figs/pca' + str(random_split) + '.png', bbox_inches='tight')
        plt.clf()
        plt.close()

    return x_train, x_test, y_train, y_test


def save_model(results, model, filename):
    # Save model results
    pickle.dump(results, open("../models/" + filename + ".pkl", "wb"))

    # Save model
    pickle.dump(model, open("../models/" + filename + ".sav", "wb"))


def plot_residuals(y_train, y_test, y_hat_train, y_hat_test, filename, r2_score):
    plt.figure(figsize=(15, 8))

    plt.scatter(y_train.index, y_train - y_hat_train, label='Train')
    plt.scatter(y_test.index, y_test - y_hat_test, c='red', label='Test')
    plt.title('Residuals', fontdict={'fontsize': 20})
    plt.xlabel('Date', fontdict={'fontsize': 16})
    plt.ylabel(f'Residuals - R2 ({r2_score:2f})', fontdict={'fontsize': 16})
    plt.legend(fontsize=14)
    plt.savefig('../figs/' + filename + ".png", bbox_inches='tight')
    plt.clf()
    plt.close()


def linear_model_fp(x_train, x_test, y_train, y_test, filename='PCA linear model', save=False):
    # Fit multiple linear regression to training data
    model = sm.OLS(y_train, sm.add_constant(x_train))
    model = model.fit()

    # Save model
    if save:
        y_hat_test = model.predict(sm.add_constant(x_test))
        y_hat_train = model.predict(sm.add_constant(x_train))

        results = {'r2_score': r2_score(y_test, y_hat_test),
                   'mean square error': mean_squared_error(y_test, y_hat_test),
                   'Summary': model.summary()}

        save_model(results, model, filename)
        plot_residuals(y_train, y_test, y_hat_train, y_hat_test, filename, results['r2_score'])

    return model


def run_pca(data, price, n_components=25):
    # Linear models
    data_properties = {'fillna': True, 'standardize': True, 'random_split': True, 'split_size': 0.15,
                       'n_components': n_components}

    if data_properties['n_components']:
        # PCA with random split
        x_train, x_test, y_train, y_test = pre_process_data(data, price, **data_properties)
        linear_model_fp(x_train, x_test, y_train, y_test, filename='PCA linear model - random_split = False', save=True)

        # PCA with sequential split
        data_properties['random_split'] = False
        x_train, x_test, y_train, y_test = pre_process_data(data, price, **data_properties)
        linear_model_fp(x_train, x_test, y_train, y_test, filename='PCA linear model - random_split = True', save=True)


def lasso_model(x_train, x_test, y_train, y_test, alpha=0.01, filename='Lasso model', save=False):
    model = linear_model.Lasso(alpha=alpha, fit_intercept=True, random_state=214, max_iter=10000)
    model = model.fit(x_train, y_train)

    # Save model
    if save:
        y_hat_test = model.predict(x_test)
        y_hat_train = model.predict(x_train)

        results = dict()
        results['r2_score'] = r2_score(y_test, y_hat_test)
        results['mean square error'] = mean_squared_error(y_test, y_hat_test)

        save_model(results, model, filename)
        plot_residuals(y_train, y_test, y_hat_train, y_hat_test, filename, results['r2_score'])

    return model


def ridge_model(x_train, x_test, y_train, y_test, alpha=180, filename='Ridge model', save=False):
    model = linear_model.Ridge(alpha=alpha, fit_intercept=True, random_state=214, max_iter=10000)
    model = model.fit(x_train, y_train)

    # Save model
    if save:
        y_hat_test = model.predict(x_test)
        y_hat_train = model.predict(x_train)

        results = dict()
        results['r2_score'] = r2_score(y_test, y_hat_test)
        results['mean square error'] = mean_squared_error(y_test, y_hat_test)

        save_model(results, model, filename)
        plot_residuals(y_train, y_test, y_hat_train, y_hat_test, filename, results['r2_score'])

    return model


def lambda_ridge(x_train_simplified, x_test_simplified, y_train, y_test, alpha_lasso):
    # Loop through different lambda values
    lambdas = np.arange(1, 1000.0, 1)

    mse_train = []
    mse_test = []
    for l in lambdas:
        ridge = linear_model.Ridge(alpha=l, fit_intercept=True)
        ridge.fit(x_train_simplified, y_train)
        mse_train.append(mean_squared_error(y_train, ridge.predict(x_train_simplified)))  # train data
        mse_test.append(mean_squared_error(y_test, ridge.predict(x_test_simplified)))  # test data

    fig, ax1 = plt.subplots(figsize=(15, 8))

    ax2 = ax1.twinx()
    ax1.plot(lambdas, mse_train, 'g-')
    ax2.plot(lambdas, mse_test, 'b-')

    ax1.set_xlabel('$\lambda$', fontdict={'fontsize': 16})
    ax1.set_ylabel('Train MSE', color='b', fontdict={'fontsize': 16})
    ax2.set_ylabel('Test MSE', color='r', fontdict={'fontsize': 16})

    plt.title(f'$\lambda$ values - lasso ({alpha_lasso})', fontdict={'fontsize': 20})

    plt.savefig(f'../figs/Ridge_parameter_alpha{alpha_lasso}.png', bbox_inches='tight')
    plt.clf()
    plt.close()

    # Loop through multiple values of lambda and record fit coefficients
    lambdas = np.logspace(-1, 7, 200)

    coefs = []
    for l in lambdas:
        ridge = linear_model.Ridge(alpha=l, fit_intercept=True)
        ridge.fit(x_train_simplified, y_train)
        coefs.append(ridge.coef_)

    fig, ax = plt.subplots(figsize=(15, 8))
    ax.plot(lambdas, coefs)
    ax.set_xscale('log')
    ax.set_xlim(ax.get_xlim())  # reverse axis
    plt.xlabel(f'$\lambda$', fontdict={'fontsize': 16})
    plt.ylabel("Coefficient values", fontdict={'fontsize': 16})
    plt.title(f'Ridge coefficients as a function of the regularization - lasso ({alpha_lasso})',
              fontdict={'fontsize': 20})
    plt.axis('tight')
    plt.savefig(f'../figs/Ridge_per_feature_alpha{alpha_lasso}.png', bbox_inches='tight')
    plt.clf()
    plt.close()


def run_lasso_ridge(data, x_train, x_test, y_train, y_test, alpha_lasso=0.01, alpha_ridge=180, filename_lasso=None,
                    filename_ridge=None):
    lasso = lasso_model(x_train, x_test, y_train, y_test, alpha=alpha_lasso, filename=filename_lasso, save=True)

    cols_to_drop = [x[0] for x in sorted(zip(data.columns, lasso.coef_), key=lambda x: x[1]) if x[1] == 0]

    x_train_simplified = x_train.drop(columns=cols_to_drop)
    x_test_simplified = x_test.drop(columns=cols_to_drop)

    if x_train.shape[1] > x_train.shape[0]:
        linear_model_fp(x_train, x_test, y_train, y_test,
                        filename=filename_lasso + '_linear', save=False)

    ridge_model(x_train_simplified, x_test_simplified, y_train, y_test, alpha_ridge, filename_ridge, save=True)
    lambda_ridge(x_train_simplified, x_test_simplified, y_train, y_test, alpha_lasso)


def elastic_net(data, x_train, x_test, y_train, y_test, alpha_lasso=0.1, filename='ElasticNet', l1_ratio=0.5):
    lasso = lasso_model(x_train, x_test, y_train, y_test, alpha=alpha_lasso)

    cols_to_drop = [x[0] for x in sorted(zip(data.columns, lasso.coef_), key=lambda x: x[1]) if x[1] == 0]

    x_train_simplified = x_train.drop(columns=cols_to_drop)
    x_test_simplified = x_test.drop(columns=cols_to_drop)

    # Compare progression of train and test errors and alpha varies
    alphas = np.logspace(-5, 1, 50)
    enet = linear_model.ElasticNet(random_state=0, l1_ratio=l1_ratio, fit_intercept=True, max_iter=50000)
    train_errors = list()
    test_errors = list()
    for alpha in alphas:
        enet.set_params(alpha=alpha)
        enet.fit(x_train_simplified, y_train)
        train_errors.append(enet.score(x_train_simplified, y_train))
        test_errors.append(enet.score(x_test_simplified, y_test))

    i_alpha_optim = np.argmax(test_errors)
    alpha_optim = alphas[i_alpha_optim]
    print("Optimal alpha regularization parameter : %.6f" % alpha_optim)

    # Estimate the coef_ on full data with optimal regularization parameter
    enet.set_params(alpha=alpha_optim)
    coef_ = enet.fit(pd.concat([x_train, x_test]),
                     pd.concat([y_train, y_test])).coef_

    # Plot R-squared as a function of alpha
    fig, ax = plt.subplots(figsize=(10, 5))
    plt.semilogx(alphas, train_errors, label='Train')
    plt.semilogx(alphas, test_errors, label='Test')
    plt.vlines(alpha_optim, plt.ylim()[0], np.max(test_errors), color='k', linewidth=3, label=r'Optimum $\alpha$')
    plt.legend(loc='lower left')
    plt.ylim([0, 1.0])
    plt.title(r'Elastic net performance as a function of the $\alpha$ parameter')
    plt.xlabel(r'$\alpha$')
    plt.ylabel(r'$R^2$');
    plt.savefig(f'../figs/' + filename + '.png', bbox_inches='tight')
    plt.close()


def xgboost_model(x_train, x_test, y_train, y_test, filename='XGboost model', save=False):
    dtrain = xgb.DMatrix(x_train, label=y_train)
    dtest = xgb.DMatrix(x_test, label=y_test)

    # "Learn" the mean from the training data
    mean_train = np.mean(y_train)  # Get predictions on the test set
    baseline_predictions = np.ones(y_test.shape) * mean_train
    # Compute MAE
    mae_baseline = mean_absolute_error(y_test, baseline_predictions)
    print("Baseline MAE is {:.2f}".format(mae_baseline))

    params = {'max_depth': 6, 'min_child_weight': 1, 'eta': .3, 'subsample': 1, 'colsample_bytree': 1,
              'objective': 'reg:linear', 'eval_metric': "mae"}

    num_boost_round = 999

    model = xgb.train(
        params,
        dtrain,
        num_boost_round=num_boost_round,
        evals=[(dtest, "Test")],
        early_stopping_rounds=10
    )

    cv_results = xgb.cv(
        params,
        dtrain,
        num_boost_round=num_boost_round,
        seed=42,
        nfold=5,
        metrics={'mae'},
        early_stopping_rounds=10
    )

    print('Minimum CV result: ', cv_results['test-mae-mean'].min())

    gridsearch_params = [
        (max_depth, min_child_weight)
        for max_depth in range(9, 12)
        for min_child_weight in range(5, 8)
    ]

    best_params = optimize_parameter_double(gridsearch_params, 'max_depth', 'min_child_weight', params, num_boost_round,
                                            dtrain)

    params['max_depth'] = best_params[0]
    params['min_child_weight'] = best_params[1]

    gridsearch_params = [
        (subsample, colsample)
        for subsample in [i / 10. for i in range(7, 11)]
        for colsample in [i / 10. for i in range(7, 11)]
    ]

    best_params = optimize_parameter_double(gridsearch_params, 'subsample', 'colsample_bytree', params, num_boost_round,
                                            dtrain)

    params['subsample'] = best_params[0]
    params['colsample_bytree'] = best_params[1]

    gridsearch_params = [
        (lambda_, alpha)
        for lambda_ in [0.1, 1, 10, 100, 500, 1000]
        for alpha in [0.5, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001]
    ]

    best_params = optimize_parameter_double(gridsearch_params, 'lambda', 'alpha', params, num_boost_round,
                                            dtrain)

    params['lambda'] = best_params[0]
    params['alpha'] = best_params[1]

    best_params = optimize_parameter_single([.3, .2, .1, .05, .01, .005], 'eta', params, num_boost_round,
                                            dtrain)

    params['eta'] = best_params

    model = xgb.train(
        params,
        dtrain,
        num_boost_round=num_boost_round,
        evals=[(dtest, "Test")],
        early_stopping_rounds=10
    )

    print("Best MAE: {:.2f} in {} rounds".format(model.best_score, model.best_iteration + 1))

    num_boost_round = model.best_iteration + 1

    best_model = xgb.train(
        params,
        dtrain,
        num_boost_round=num_boost_round,
        evals=[(dtest, "Test")]
    )
    # Save model
    if save:
        y_hat_test = best_model.predict(dtest)
        y_hat_train = best_model.predict(dtrain)

        results = dict()
        results['r2_score'] = r2_score(y_test, y_hat_test)
        results['mean square error'] = mean_squared_error(y_test, y_hat_test)

        save_model(results, model, filename)
        plot_residuals(y_train, y_test, y_hat_train, y_hat_test, filename, results['r2_score'])

    return best_model


def optimize_parameter_single(values, label, params, num_boost_round, dtrain):
    min_mae = float("Inf")
    best_params = None
    for param in values:
        print("CV with " + label + "={}".format(param))  # We update our parameters
        params[label] = param  # Run and time CV
        cv_results = xgb.cv(
            params,
            dtrain,
            num_boost_round=num_boost_round,
            seed=42,
            nfold=5,
            metrics=['mae'],
            early_stopping_rounds=10
        )  # Update best score
        mean_mae = cv_results['test-mae-mean'].min()
        boost_rounds = cv_results['test-mae-mean'].argmin()
        print("\tMAE {} for {} rounds\n".format(mean_mae, boost_rounds))
        if mean_mae < min_mae:
            min_mae = mean_mae
            best_params = param

    print("Best params: {}, MAE: {}".format(best_params, min_mae))
    return best_params


def optimize_parameter_double(grid, label1, label2, params, num_boost_round, dtrain):
    min_mae = float("Inf")
    best_params = None
    for param1, param2 in grid:
        print("CV with " + label1 + "={0}, " + label2 + "={1}".format(
            param1,
            param2))  # Update our parameters
        params[label1] = param1
        params[label2] = param2  # Run CV
        cv_results = xgb.cv(
            params,
            dtrain,
            num_boost_round=num_boost_round,
            seed=42,
            nfold=5,
            metrics={'mae'},
            early_stopping_rounds=10
        )  # Update best MAE
        mean_mae = cv_results['test-mae-mean'].min()
        boost_rounds = cv_results['test-mae-mean'].argmin()
        print("\tMAE {} for {} rounds".format(mean_mae, boost_rounds))
        if mean_mae < min_mae:
            min_mae = mean_mae
            best_params = (param1, param2)

    print("Best params: {}, {}, MAE: {}".format(best_params[0], best_params[1], min_mae))

    return best_params


def full_dataset():
    data, price = read_data()

    run_pca(data, price)

    # Linear models
    data_properties = {'fillna': True, 'standardize': True, 'random_split': True, 'split_size': 0.15,
                       'n_components': None}

    # Random split
    x_train, x_test, y_train, y_test = pre_process_data(data, price, **data_properties)

    for alpha_lasso in [0.5, 0.1, 0.01, 0.001, 0.0001, 0.00001]:
        alpha_ridge = 180
        filename_lasso = f'Lasso_alpha:{alpha_lasso}_random_split'
        filename_ridge = f'Lasso_alpha:{alpha_ridge}_random_split'

        run_lasso_ridge(data, x_train, x_test, y_train, y_test, alpha_lasso, alpha_ridge, filename_lasso,
                        filename_ridge)

    for l1_ratio in [0.1, 0.3, 0.5, 0.7, 0.9]:
        elastic_net(data, x_train, x_test, y_train, y_test, filename=f'ElasticNet_random{l1_ratio}', l1_ratio=l1_ratio)

    xgboost_model(x_train, x_test, y_train, y_test, filename='XGboost model_random', save=True)

    # Sequential split
    data_properties['random_split'] = False
    x_train, x_test, y_train, y_test = pre_process_data(data, price, **data_properties)

    for alpha_lasso in [0.5, 0.1, 0.01, 0.001, 0.0001, 0.00001]:
        alpha_ridge = 180
        filename_lasso = f'Lasso_alpha:{alpha_lasso}_sequential_split'
        filename_ridge = f'Lasso_alpha:{alpha_ridge}_sequential_split_after_lasso'

        run_lasso_ridge(data, x_train, x_test, y_train, y_test, alpha_lasso, alpha_ridge, filename_lasso,
                        filename_ridge)

    for l1_ratio in [0.1, 0.3, 0.5, 0.7, 0.9]:
        elastic_net(data, x_train, x_test, y_train, y_test, filename=f'ElasticNet_sequential{l1_ratio}',
                    l1_ratio=l1_ratio)

    xgboost_model(x_train, x_test, y_train, y_test, filename='XGboost model_sequential', save=True)


def xgboost_month():
    data, price = read_data(True)

    data_properties = {'fillna': True, 'standardize': True, 'random_split': True, 'split_size': 0.15,
                       'n_components': None}

    # Random split
    x_train, x_test, y_train, y_test = pre_process_data(data, price, **data_properties)

    xgboost_model(x_train, x_test, y_train, y_test, filename='XGboost model_random_ month', save=True)

    # Sequential split
    data_properties['random_split'] = False
    x_train, x_test, y_train, y_test = pre_process_data(data, price, **data_properties)

    xgboost_model(x_train, x_test, y_train, y_test, filename='XGboost model_sequential_ month', save=True)

def xgboost_month_lasso():
    data, price = read_data(True)

    data_properties = {'fillna': True, 'standardize': True, 'random_split': True, 'split_size': 0.15,
                       'n_components': None}

    # Random split
    x_train, x_test, y_train, y_test = pre_process_data(data, price, **data_properties)

    model = lasso_model(x_train, x_test, y_train, y_test, alpha=0.1, save=False)

    cols_to_drop = [x[0] for x in sorted(zip(data.columns, model.coef_), key=lambda x: x[1]) if x[1] == 0]

    x_train_simplified = x_train.drop(columns=cols_to_drop)
    x_test_simplified = x_test.drop(columns=cols_to_drop)

    xgboost_model(x_train_simplified, x_test_simplified, y_train, y_test, filename='XGboost model_random_ month lasso',
                  save=True)


    # Sequential split
    data_properties['random_split'] = False
    x_train, x_test, y_train, y_test = pre_process_data(data, price, **data_properties)

    model = lasso_model(x_train, x_test, y_train, y_test, alpha=0.1, save=False)

    cols_to_drop = [x[0] for x in sorted(zip(data.columns, model.coef_), key=lambda x: x[1]) if x[1] == 0]

    x_train_simplified = x_train.drop(columns=cols_to_drop)
    x_test_simplified = x_test.drop(columns=cols_to_drop)

    xgboost_model(x_train_simplified, x_test_simplified, y_train, y_test, filename='XGboost model_sequential_ month', save=True)


def model_analysis():
    pass


def xgboost_month_price():

    data, price = read_data(True, True)

    data_properties = {'fillna': True, 'standardize': True, 'random_split': True, 'split_size': 0.15,
                       'n_components': None}

    # Random split
    x_train, x_test, y_train, y_test = pre_process_data(data, price, **data_properties)

    #model = lasso_model(x_train, x_test, y_train, y_test, alpha=0.1, save=False)

    #cols_to_drop = [x[0] for x in sorted(zip(data.columns, model.coef_), key=lambda x: x[1]) if x[1] == 0]

    #x_train_simplified = x_train.drop(columns=cols_to_drop)
    #x_test_simplified = x_test.drop(columns=cols_to_drop)

    model = xgboost_model(x_train, x_test, y_train, y_test, filename='XGboost model_random_month_price',
                  save=True)
    print(model.feature_importances_)
# plot
    pyplot.bar(range(len(model.feature_importances_)), model.feature_importances_)
    pyplot.show()
    # Sequential split
    # data_properties['random_split'] = False
    # x_train, x_test, y_train, y_test = pre_process_data(data, price, **data_properties)
    #
    # model = lasso_model(x_train, x_test, y_train, y_test, alpha=0.1, save=False)
    #
    # cols_to_drop = [x[0] for x in sorted(zip(data.columns, model.coef_), key=lambda x: x[1]) if x[1] == 0]
    #
    # x_train_simplified = x_train.drop(columns=cols_to_drop)
    # x_test_simplified = x_test.drop(columns=cols_to_drop)
    #
    # xgboost_model(x_train, x_test, y_train, y_test, filename='XGboost model_sequential_ month', save=True)

if __name__ == '__main__':
    data, price = read_data(True, variance=True)

    full_dataset()