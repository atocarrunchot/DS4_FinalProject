import pandas as pd
from db_utils import connect_pg, get_tables, get_table_cols
from itertools import combinations

conn_pg = connect_pg()
keys_order = ['region', 'tipo', 'agente', 'recurso', 'embalse', 'rio']

tables_agg = {
    'month_demand': 'sum',
    'month_inflow': 'sum',
    'month_offer': 'sum',
    'month_precipitation': 'mean',
    'month_price': 'mean',
    'month_spill': 'sum',
    'month_storage': 'sum',
    'month_noaa': 'mean'
}

tables_vars = {
    'month_demand': ['demanda', 'generacion'],
    'month_inflow': ['aportes'],
    'month_offer': ['oferta'],
    'month_precipitation': ['precipitacion'],
    'month_price': ['precio'],
    'month_spill': ['vertimiento'],
    'month_storage': ['vol_util'],
    'month_noaa': ['noaa']
}


def build_datasets():
    schema = 'public'
    df_tables = get_tables(schema=schema)
    tables = [i for i in df_tables['table_name'] if 'month_' in i]
    print(tables)

    for table in tables:
        df_cols = get_table_cols(table)
        df_total = pd.DataFrame()

        if df_cols['column_name'].isin(['region']).any():
            print(f"\n{table}")
            query = f"""
            SELECT *
            FROM {schema}.{table}
            """

            df_table = pd.read_sql(query, con=conn_pg, parse_dates=['fecha'])
            list_cols = df_table.dtypes[df_table.dtypes == 'object'].index

            for r in range(1, len(list_cols) + 1):
                combs = combinations(df_table.dtypes[df_table.dtypes == 'object'].index, r)

                for comb in combs:
                    if 'region' in comb:
                        list_group = [i for i in keys_order if i in comb]
                        dfg = df_table.groupby([pd.Grouper(key='fecha', freq='MS')] + list_group)
                        df = dfg.agg(tables_agg[table])
                        df.reset_index(inplace=True)
                        df['columns'] = df.apply(lambda i: '$'.join(i[list_group]), axis=1)

                        for target in tables_vars[table]:
                            df_pivot = df.pivot(index='fecha', columns='columns', values=target)
                            df_pivot.columns = [i + '$' + target.upper() for i in df_pivot.columns]
                            df_total = pd.concat([df_total, df_pivot], axis=1)

            df_total.to_sql('total_{}'.format(table), con=conn_pg, schema=schema, if_exists='replace')
            df_total.to_csv('../results/total_{}.csv'.format(table))


if __name__ == '__main__':
    build_datasets()
    pass
