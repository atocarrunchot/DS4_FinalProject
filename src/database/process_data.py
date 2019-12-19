import pandas as pd
import numpy as np
import glob

def process_data(data_files, num_nas=280, print_info=False, cube='TRANS',col_skip=0):
    joint_df = []
    for file in data_files:
        data = pd.read_excel(file).head()
        skip = data[data.iloc[:,col_skip] == 'Fecha'].index.tolist()[0]
        data = pd.read_excel(file,skiprows = skip+1)
        count_nas = data.isnull().sum(axis = 0)

        to_drop = count_nas[count_nas > num_nas].index.tolist()
        if len(to_drop) != 0:
            data.drop(columns=to_drop, inplace = True)

        list_cols = data.columns

        if cube == 'TRANS':
            list_cols = [i for i in data.columns if (i not in map(str,range(0,24)) or i not in ['Fecha']) and not str(i).startswith('Unnam')]

        list_cols = [i for i in list_cols if not pd.isna(i)]
        data = data[list_cols]
        if print_info:
            print(file)
            print(list_cols)
            print(data.columns)
            print(data.head(1).values)
            print(data.shape)

        if cube == 'TRANS':
            if 'Version' not in data.columns:
                data['Version'] = np.nan

        if cube == 'HIDRO-APORTES':
            data.drop(columns=['Unnamed: 0'],inplace=True)

        if cube == 'HIDRO-VERT':
            data.columns = ['Fecha', 'Region Hidrologica', 'Nombre Embalse', 'Vertimientos Volumen miles m3', 'Vertimientos Energía kWh']

        joint_df.append(data)

    joint_df = pd.concat(joint_df, ignore_index = True, axis=0, sort=False)

    return joint_df

def process_precio():

    trans_files = glob.glob("../../data/Transacciones y Precio/Precio_Bolsa_Nacional_(*")
    # All files contain at least 289 rows

    # Read data
    joint_df = process_data(trans_files,print_info=False)

    # Process data
    joint_df = joint_df.melt(id_vars=['Fecha','Version'])
    joint_df = joint_df[~(pd.isna(joint_df.Fecha))]
    joint_df['Fecha'] = joint_df.apply(lambda x: str(x['Fecha'])+' {}:00:00'.format(x['variable']),axis=1)
    joint_df['Fecha'] = pd.to_datetime(joint_df['Fecha'])
    joint_df.sort_values(['Fecha'],inplace=True)
    joint_df.drop(columns=['variable'],inplace=True)
    joint_df.rename(columns={'value':'Precio'},inplace=True)

    joint_df.to_csv('../../results/joins/precio.csv')

def process_oferta():
    oferta_files = glob.glob("../../data/Oferta/Disponibilidad_Real_(kW)_*")
    # All files contain at least 289 rows

    # Read data
    joint_df = process_data(oferta_files, num_nas=100000000, print_info=False, cube='OFERTA')

    # Process data
    joint_df = joint_df.melt(id_vars=['Fecha', 'Recurso', 'Tipo Generación', 'Código Agente'])
    joint_df = joint_df[~(pd.isna(joint_df.Fecha))]
    joint_df['Fecha'] = joint_df.apply(lambda x: str(x['Fecha'])+' {}:00:00'.format(x['variable']),axis=1)
    joint_df['Fecha'] = pd.to_datetime(joint_df['Fecha'])
    joint_df.sort_values(['Fecha'],inplace=True)
    joint_df.drop(columns=['variable'],inplace=True)
    joint_df.rename(columns={'value':'Oferta'},inplace=True)

    joint_df.to_csv('../../results/joins/oferta.csv')

def process_hidro():
    hidro_files = glob.glob("../../data/Hidrología/Aportes_Diario_*")

    # Read data
    joint_df = process_data(hidro_files, num_nas=100000000, print_info=False, cube='HIDRO-APORTES',col_skip=1)

    # Process data
    joint_df['Fecha'] = pd.to_datetime(joint_df.Fecha)
    joint_df.sort_values(['Fecha'],ascending=True,inplace=True)

    # Aportes =  0
    joint_df = joint_df[~((joint_df.isnull().sum(axis = 1) > 1) & (joint_df['Aportes Caudal m3/s'] <= 0))]

    joint_df.to_csv('../../results/joins/hidro_aportes_diario.csv')

    hidro_files = glob.glob("../../data/Hidrología/Reservas_Diario_*")

    # Read data
    joint_df = process_data(hidro_files, num_nas=100000000, print_info=False, cube='HIDRO-RESERVA')

    # Process data
    joint_df['Fecha'] = pd.to_datetime(joint_df.Fecha)
    joint_df.sort_values(['Fecha'],ascending=True,inplace=True)

    # Maybe remove Nas, not clear ... Volumen Util -> NaN but Volumen -> data
    # joint_df = joint_df[~(joint_df.isnull().sum(axis = 1) > 2)]
    joint_df.to_csv('../../results/joins/hidro_reservas_diario.csv')

    hidro_files = glob.glob("../../data/Hidrología/Vertimentos_Diario_*")

    # Read data
    joint_df = process_data(hidro_files, num_nas=100000000, print_info=True, cube='HIDRO-VERT')

    # Process data
    joint_df['Fecha'] = pd.to_datetime(joint_df.Fecha)
    joint_df.sort_values(['Fecha'],ascending=True,inplace=True)

    # Maybe remove Nas, not clear ... Vertimentos Volumen -> NaN but Vertimentos Energía -> data and visceversa
    # joint_df = joint_df.loc[(joint_df.isnull().sum(axis = 1) > 0)]
    joint_df.to_csv('../../results/joins/hidro_vertimentos_diario.csv')

def process_demanda():

    demanda_files = glob.glob("../../data/Demanda/Demanda Nacional/Demanda_Energia_SIN_*")

    # Read data
    joint_df = process_data(demanda_files, num_nas=100000000, print_info=False, cube='DEMANDA')

    # Process data
    joint_df['Fecha'] = pd.to_datetime(joint_df.Fecha)
    joint_df.sort_values(['Fecha'],ascending=True,inplace=True)

    joint_df.to_csv('../../results/joins/demanda.csv')

def monthly_data(precio_adj=False,unpivoted=False):

    # Read files
    oferta = pd.read_csv('../../results/joins/oferta.csv',parse_dates=['Fecha'], index_col=0)
    if  precio_adj:
        precio = pd.read_csv('../../results/joins/precios_adj.csv',parse_dates=['Fecha'], index_col=0)
    else:
        precio = pd.read_csv('../../results/joins/precio.csv',parse_dates=['Fecha'], index_col=0)
    demanda = pd.read_csv('../../results/joins/demanda.csv',parse_dates=['Fecha'], index_col=0)
    hidro_aportes = pd.read_csv('../../results/joins/hidro_aportes_diario.csv',parse_dates=['Fecha'], index_col=0)
    hidro_reservas = pd.read_csv('../../results/joins/hidro_reservas_diario.csv',parse_dates=['Fecha'], index_col=0)
    hidro_vert = pd.read_csv('../../results/joins/hidro_vertimentos_diario.csv',parse_dates=['Fecha'], index_col=0)

    # Processing monthly_data
    oferta['YYYY-MM'] = oferta.apply(lambda x: x['Fecha'].strftime('%Y-%m'), axis=1)

    if unpivoted:
        oferta_pivot = oferta.groupby(['YYYY-MM', 'Tipo Generación','Código Agente', 'Recurso']).sum()
    else:
        oferta_pivot = pd.pivot_table(oferta, values='Oferta', index=['YYYY-MM', 'Tipo Generación'],columns=['Recurso'], aggfunc=np.sum)
        oferta_pivot.reset_index(inplace=True)
        oferta_pivot = oferta_pivot.groupby(['YYYY-MM', 'Tipo Generación']).sum()

    oferta_pivot.reset_index(inplace=True)
    oferta_pivot.rename(columns={'YYYY-MM':'Fecha'},inplace=True)

    if unpivoted:
        oferta_pivot.to_csv('../../results/joins/oferta_mensual_unpivoted.csv')
    else:
        oferta_pivot.to_csv('../../results/joins/oferta_mensual.csv')

    # precio.dropna(subset=['Precio'],inplace=True)
    # precio['YYYY-MM'] = precio.apply(lambda x: x['Fecha'].strftime('%Y-%m'), axis=1)
    # precio_groupped = precio.groupby(['YYYY-MM'])
    #
    # data_precio = []
    # for index,sub in precio_groupped:
    #     open_precio = sub.sort_values(['Fecha']).head(1)['Precio'].values[0]
    #     close_precio = sub.sort_values(['Fecha'],ascending=False).head(1)['Precio'].values[0]
    #     high = sub.Precio.max()
    #     low = sub.Precio.min()
    #     data = pd.Series(data={'YYYY-MM':index,'Precio':sub.Precio.mean(),'Open':open_precio,'close':close_precio,'high':high,'low':low})
    #
    #     data_precio.append(data)
    #
    # data_precio = pd.DataFrame(data_precio)
    # data_precio.rename(columns={'YYYY-MM':'Fecha'},inplace=True)
    # data_precio.to_csv('../../results/joins/precio_mensual.csv')

    demanda['YYYY-MM'] = demanda.apply(lambda x: x['Fecha'].strftime('%Y-%m'), axis=1)
    demanda_groupped = demanda.groupby(['YYYY-MM']).sum()
    demanda_groupped.reset_index(inplace=True)
    demanda_groupped.rename(columns={'YYYY-MM':'Fecha'},inplace=True)
    demanda_groupped.to_csv('../../results/joins/demanda_mensual.csv')

    hidro_aportes['YYYY-MM'] = hidro_aportes.apply(lambda x: x['Fecha'].strftime('%Y-%m'), axis=1)

    if unpivoted:
        hidro_aportes_pivot = hidro_aportes_pivot.groupby(['YYYY-MM']).sum()
    else:
    hidro_aportes_pivot = pd.pivot_table(hidro_aportes, values='Aportes Energía kWh', index=['YYYY-MM'],columns=['Region Hidrologica','Nombre Río'], aggfunc=np.sum)
    hidro_aportes_pivot.reset_index(inplace=True)
    hidro_aportes_pivot = hidro_aportes_pivot.groupby(['YYYY-MM']).sum()
    hidro_aportes_pivot.reset_index(inplace=True)
    hidro_aportes_pivot.rename(columns={'YYYY-MM':'Fecha'},inplace=True)
    hidro_aportes_pivot.to_csv('../../results/joins/hidro_aportes_mensual.csv')

    hidro_reservas = hidro_reservas[['Fecha','Region Hidrologica','Nombre Embalse','Volumen Útil Diario Energía kWh']]
    hidro_reservas['YYYY-MM'] = hidro_reservas.apply(lambda x: x['Fecha'].strftime('%Y-%m'), axis=1)
    hidro_reservas_pivot = pd.pivot_table(hidro_reservas, values='Volumen Útil Diario Energía kWh', index=['YYYY-MM'],columns=['Region Hidrologica','Nombre Embalse'], aggfunc=np.sum)
    hidro_reservas_pivot.reset_index(inplace=True)
    hidro_reservas_pivot = hidro_reservas_pivot.groupby(['YYYY-MM'])#.sum()

    data_reservas = []
    for index,sub in hidro_reservas_pivot:
        data = dict()
        subset = sub[sub['YYYY-MM'] == index].copy()

        subset.drop(columns=['YYYY-MM'],inplace=True)
        data['YYYY-MM'] = index
        for col in subset.columns:

            value = sub[col].tail(1).values
            if len(value) > 0:
                data[col] = value[0]
            else:
                data[col] = np.nan

        data_reservas.append(pd.Series(data))
    print(data_reservas)
    data_reservas = pd.DataFrame(data_reservas)
    data_reservas.rename(columns={'YYYY-MM':'Fecha'},inplace=True)
    data_reservas.to_csv('../../results/joins/hidro_reservas_mensual.csv')

    hidro_vert['YYYY-MM'] = hidro_vert.apply(lambda x: x['Fecha'].strftime('%Y-%m'), axis=1)
    hidro_vert_pivot = pd.pivot_table(hidro_vert, values='Vertimientos Energía kWh', index=['YYYY-MM'],columns=['Region Hidrologica','Nombre Embalse'], aggfunc=np.sum)
    hidro_vert_pivot.reset_index(inplace=True)
    hidro_vert_pivot = hidro_vert_pivot.groupby(['YYYY-MM']).sum()
    hidro_vert_pivot.reset_index(inplace=True)
    hidro_vert_pivot.rename(columns={'YYYY-MM':'Fecha'},inplace=True)
    hidro_vert_pivot.to_csv('../../results/joins/hidro_vertimentos_mensual.csv')

if __name__ == '__main__':
    #process_precio()
    #process_oferta()
    #process_hidro()
    #process_demanda()
    monthly_data(False,True)
