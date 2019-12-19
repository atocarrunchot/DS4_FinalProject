import pandas as pd


def vec_dt_replace(series, year=None, month=None, day=None):
    return pd.to_datetime(
        {'year': series.dt.year if year is None else year,
         'month': series.dt.month if month is None else month,
         'day': series.dt.day if day is None else day})


def monthly_offer():
    cols = ['0', 'Fecha', 'Recurso', 'Tipo', 'Agente', 'Oferta']
    str_cols = ['Recurso', 'Tipo', 'Agente']
    path_oferta = '../data/raw_data/oferta.csv'
    df_data = pd.read_csv(path_oferta, parse_dates=['Fecha'])
    df_data.columns = cols
    df_data.drop('0', axis=1, inplace=True)

    for str_col in str_cols:
        df_data[str_col] = df_data[str_col].str.upper()
        df_data[str_col] = df_data[str_col].str.replace(' ', '_')
        df_data[str_col] = df_data[str_col].str.replace(',', '_')
        df_data[str_col] = df_data[str_col].str.replace('.', '')

    df_res = df_data.groupby(['Agente', 'Tipo', 'Recurso', pd.Grouper(key='Fecha', freq='MS')]).sum()
    df_res.sort_index(level=['Fecha', 'Agente', 'Tipo', 'Recurso'], inplace=True)
    df_res.to_csv('../results/month_offer.csv')


def monthly_inflow():
    read_cols = ['Fecha', 'Region Hidrologica', 'Nombre Río', 'Aportes Energía kWh']
    cols = ['Fecha', 'Region', 'Rio', 'Aportes']
    str_cols = ['Region', 'Rio']
    path_oferta = '../data/raw_data/hidro_aportes_diario.csv'
    df_data = pd.read_csv(path_oferta, usecols=read_cols, parse_dates=['Fecha'])
    df_data.columns = cols

    for str_col in str_cols:
        df_data[str_col] = df_data[str_col].str.upper()
        df_data[str_col] = df_data[str_col].str.replace(' ', '_')
        df_data[str_col] = df_data[str_col].str.replace(',', '_')
        df_data[str_col] = df_data[str_col].str.replace('.', '')
        df_data[str_col] = df_data[str_col].str.replace('(', '')
        df_data[str_col] = df_data[str_col].str.replace(')', '')

    df_res = df_data.groupby(['Region', 'Rio', pd.Grouper(key='Fecha', freq='MS')]).sum()
    df_res.sort_index(level=['Fecha', 'Region', 'Rio'], inplace=True)
    df_res.to_csv('../results/month_inflow.csv')


def monthly_storage():
    read_cols = ['Fecha', 'Region Hidrologica', 'Nombre Embalse', 'Volumen Útil Diario Energía kWh']
    cols = ['Fecha', 'Region', 'Embalse', 'Vol_Util']
    str_cols = ['Region', 'Embalse']
    path_oferta = '../data/raw_data/hidro_reservas_diario.csv'
    df_data = pd.read_csv(path_oferta, parse_dates=['Fecha'], usecols=read_cols)
    df_data.columns = cols

    for str_col in str_cols:
        df_data[str_col] = df_data[str_col].str.upper()
        df_data[str_col] = df_data[str_col].str.replace(' ', '_')
        df_data[str_col] = df_data[str_col].str.replace(',', '_')
        df_data[str_col] = df_data[str_col].str.replace('.', '')

    df_res = df_data.groupby(['Region', 'Embalse', pd.Grouper(key='Fecha', freq='MS')]).last()
    df_res.sort_index(level=['Fecha', 'Region', 'Embalse'], inplace=True)
    df_res.to_csv('../results/month_storage.csv')


def monthly_spill():
    cols = ['Fecha', 'Region', 'Embalse', 'Vertimiento']
    str_cols = ['Region', 'Embalse']
    path_oferta = '../data/raw_data/hidro_vertimentos_diario.csv'
    df_data = pd.read_csv(path_oferta, parse_dates=['Fecha'])
    df_data.columns = cols

    for str_col in str_cols:
        df_data[str_col] = df_data[str_col].str.upper()
        df_data[str_col] = df_data[str_col].str.replace(' ', '_')
        df_data[str_col] = df_data[str_col].str.replace(',', '_')
        df_data[str_col] = df_data[str_col].str.replace('.', '')

    df_res = df_data.groupby(['Region', 'Embalse', pd.Grouper(key='Fecha', freq='MS')]).sum()
    df_res.sort_index(level=['Fecha', 'Region', 'Embalse'], inplace=True)
    df_res.to_csv('../results/month_spill.csv')


def monthly_demand():
    cols = ['Fecha', 'Demanda', 'Generacion']
    path_oferta = '../data/raw_data/demanda.csv'
    df_data = pd.read_csv(path_oferta, parse_dates=['Fecha'])
    df_data.columns = cols
    df_data.set_index('Fecha', inplace=True)
    df_res = df_data.resample('MS').sum()
    df_res.sort_index(inplace=True)
    df_res.to_csv('../results/month_demand.csv')


def monthly_noaa():
    path_noaa = '../data/raw_data/NOAA_df_Final.csv'
    df_data = pd.read_csv(path_noaa, parse_dates=True, sep=';')
    df_pivot = pd.pivot(data=df_data, index='Date', columns='Indice', values='Value')
    df_pivot.to_csv('../results/month_noaa.csv')


if __name__ == '__main__':
    # monthly_offer()
    # monthly_inflow()
    # monthly_storage()
    # monthly_spill()
    # monthly_demand()
    monthly_noaa()
    pass
