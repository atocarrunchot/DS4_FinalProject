import pandas as pd
import urllib, json
import pandas.io.sql as sqlio
import psycopg2
import numpy as np


def data_test():
    url = 'https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey_energy.json'
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    return data

#def data_precio():
#    df = pd.read_csv('/home/davidcparrar/Documents/ds4a_workshop/DS4_FinalProject/results/joins/precio_mensual.csv',index_col=0)
#
def read_data(month=False, precio_old=False):
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

    # Feature included for standardization
    data['precio'] = np.log(price['precio'] + 1)

    if precio_old:
        data['precio_prev'] = data.precio.shift()
        data = data[[x for x in data.columns if str(x[-3:]) in ['rev', 'cio', 'L01']]]

    if month:
        month=data.index.month
    #    months = enc.transform(data.index.month.values.reshape(-1, 1)).toarray()
    #    months_df = pd.DataFrame(months,
    #                             columns=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov',
                    #                      'Dic'], index=data.index)

    #    data = pd.concat([months_df, data], axis=1)
        data['month']=month

    return data.iloc[1:], price