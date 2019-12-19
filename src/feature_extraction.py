import numpy as np
import pandas as pd
from xgboost import XGBRegressor, plot_importance
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


def feature_importance():
    """Obtains the most important features using XGBoosts
    """
    dataset = pd.read_csv('../results/dataframe_final_project.csv', index_col=0)
    dataset['Precio_Precio'] = np.log(dataset['Precio_Precio'])
    X = dataset.drop(columns=['Precio_Precio','Precio_Open','Precio_Low','Precio_Close','Precio_High','Fecha']).values
    y = dataset['Precio_Precio'].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    xgb_reg = XGBRegressor()

    xgb_reg_fit = xgb_reg.fit(X_train,y_train)
    y_hat = xgb_reg.predict(X_test)

    print('score:',r2_score(y_test,y_hat))
    print(xgb_reg.get_booster().get_score(importance_type="gain"))
    plot_importance(xgb_reg, importance_type='gain',max_num_features=20, height=0.8,)
    plt.savefig('../figs/feature_importance.png')


def PCA_preprocessing(X):
    """PCA preprocessing step, does not work on nxm if n<m

    """

    pca = PCA(X.shape[1])

    pca.fit(np.nan_to_num(X))

    explained_var = pca.explained_variance_ratio_
    print('='*30)
    print('Explained variance: ',np.sum(explained_var))
    print('='*30)
    plt.plot(range(1,len(explained_var)+1), explained_var, '-o')
    plt.savefig('../figs/explained_var.png')
    plt.xlabel('Explained Variance')
    plt.ylabel('Number of components')

    return pca


if __name__ == '__main__':
    feature_importance()
