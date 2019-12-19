import pandas as pd
import matplotlib.pyplot as plt
from db_utils import connect_pg, get_tables
import seaborn as sns
from scipy.stats import pearsonr, ttest_ind, ttest_1samp
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
sns.set(rc={'figure.figsize': (11., 8.5)})
alpha = 0.05 / 12.  # Bonferroni Correction


def plot_autocorrelation(y):
    fig, axs = plt.subplots(2)
    fig.suptitle('Energy Generation Price')
    plot_acf(y, ax=axs[0])
    plot_pacf(y, ax=axs[1])
    plt.savefig('../figs/Price_Autocorrelation.png')
    plt.close()


def calc_correlation(features, y):
    corr = pd.Series(index=features.columns)
    pvalue = pd.Series(index=features.columns)

    for col in features.columns:
        x_corr = features[col].dropna().copy()
        y_corr = y[x_corr.index].copy()

        try:
            corr[col], pvalue[col] = pearsonr(x_corr, y_corr)
        except ValueError:
            pass

    return corr, pvalue


def rem_seasonality_monthly(df_data):
    df_output = df_data.copy()

    months = range(1, 13)

    for month in months:
        idx_month = df_data.index.month == month
        means = df_data.loc[idx_month].mean()
        df_output.loc[idx_month] = df_data.loc[idx_month] / means

    return df_output


def plot_correlation(df_corr, df_pval):
    df_txt = pd.DataFrame(index=df_dataset.columns, columns=lags, data='')
    df_txt[df_pval < alpha] = '*'
    sns.heatmap(df_corr, vmin=-1, vmax=1, cmap='bwr', annot=df_txt)
    plt.title('Cross correlation between Energy Price and {}'.format(dataset), fontsize='x-large')
    plt.xlabel('Time lag')
    plt.tight_layout()
    plt.savefig('../figs/Cross_Correlation_{}.png'.format(dataset))
    plt.close()


datasets = {
    'Precipitation': 'total_month_precipitation',
    'Spills': 'total_month_spill',
    'Storage': 'total_month_storage',
    'Inflows': 'total_month_inflow',
    'Demand': 'month_demand',
    'Offer': 'total_month_offer',
    'Macroclimatic Data': 'total_month_noaa'
}

dt_season = {
    'Precipitation': True,
    'Spills': False,
    'Storage': False,
    'Inflows': True,
    'Demand': False,
    'Offer': False,
    'Macroclimatic Data': False
}

dt_diff = {
    'Precipitation': False,
    'Spills': False,
    'Storage': False,
    'Inflows': False,
    'Demand': True,
    'Offer': True,
    'Macroclimatic Data': False
}

schema = 'public'
conn_pg = connect_pg()
df_price = pd.read_sql_table('month_price', con=conn_pg, parse_dates='fecha', index_col='fecha')
y = df_price['precio']
# plot_autocorrelation(y)

lags = range(12, 0, -1)
df_features_lags = pd.DataFrame()
df_features_lags = pd.concat([df_features_lags, y.shift(1).dropna()], axis=1)
df_features_lags = pd.concat([df_features_lags, y.shift(2).dropna()], axis=1)
df_features_lags.columns = ['PRECIO$L01', 'PRECIO$L02']

for dataset in datasets:
    print(dataset)
    table = datasets[dataset]
    df_dataset = pd.read_sql_table(table_name=table, con=conn_pg, parse_dates='fecha', index_col='fecha')

    if dt_season[dataset]:
        df_dataset = rem_seasonality_monthly(df_dataset)

    if dt_diff[dataset]:
        df_dataset = df_dataset.diff()

    # df_dataset.columns = data_new_cols[dataset]
    df_corr = pd.DataFrame(index=df_dataset.columns, columns=lags)
    df_pval = pd.DataFrame(index=df_dataset.columns, columns=lags)

    for lag in lags:
        df_lag = df_dataset.shift(lag)
        df_corr[lag], df_pval[lag] = calc_correlation(df_lag, y)

    df_selected = df_corr[df_pval < alpha]

    for feature in df_selected.index:
        sel_lags = df_selected.loc[feature].dropna()

        for sel_lag in sel_lags.index:
            col_name = '{}$L{:02}'.format(feature, sel_lag)
            print(col_name)
            df_shift = df_dataset[[feature]].shift(sel_lag).dropna()
            df_shift.columns = [col_name]
            df_features_lags = pd.concat([df_features_lags, df_shift], axis=1)

df_features_lags.index.name = 'Fecha'
df_features_lags.index = df_features_lags.reset_index()['Fecha'].dt.normalize()
df_features_lags.to_sql('features_region_lags', con=conn_pg, schema=schema, if_exists='replace')
df_features_lags.to_csv('../results/features_region_lags.csv')
