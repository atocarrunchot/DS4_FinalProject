import pandas as pd
from config_utils import get_pars_from_ini


def connect_pg(login='db_login_arthur'):
    dt_db_login = get_pars_from_ini()
    host = dt_db_login[login]['host']
    port = dt_db_login[login]['port']
    dbname = dt_db_login[login]['dbname']
    user = dt_db_login[login]['user']
    password = dt_db_login[login]['pass']
    conn_pg = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"

    return conn_pg


def get_tables(schema='public'):
    conn_pg = connect_pg()
    query = f"""
    SELECT table_name
    FROM information_schema.tables 
    WHERE table_schema = '{schema}'
    """

    df_tables = pd.read_sql(sql=query, con=conn_pg)

    return df_tables


def get_table_cols(table, schema='public'):
    conn_pg = connect_pg()
    query = f"""
    SELECT column_name
    FROM information_schema.columns
    WHERE table_schema = '{schema}'
    AND table_name   = '{table}'
    """
    df_cols = pd.read_sql(query, con=conn_pg)

    return df_cols


if __name__ == '__main__':
    pass
