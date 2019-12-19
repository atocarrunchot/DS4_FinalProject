# -*- coding: utf-8 -*-
import pandas as pd
from rasterstats import zonal_stats
from geopandas import GeoDataFrame
import os
import re


def calc_zonal_statistics(shp_filename, raster_file, stats=None):
    """
    Calculates zonal statistics for a raster file based on a shapefile.

    :param shp_filename: filename path.
    :type shp_filename: str
    :param raster_file: filename raster.
    :type raster_file: str
    :param stats: list of statistics to calculate.
    :type stats: list
    :return: gpd.GeoDataFrame
    """
    if stats is None:
        stats = ['count', 'min', 'max', 'mean', 'median', 'std']

    results = zonal_stats(
        shp_filename,
        raster_file,
        nodata=-9999,
        stats=stats,
        all_touched=True,
        geojson_out=True,
        epsg=4326
    )
    gdf_stats = GeoDataFrame.from_features(results)

    return gdf_stats


def chirps_zonal_statistics():
    """

    :return:
    """
    shp_watersheds = '../shapes/sin_watersheds.shp'
    path_rasters = '../raster'
    list_rasters = os.listdir(path_rasters)
    dt_precipitation = {}

    pattern = re.compile(r'[0-9]{4}.[0-9]{2}')

    for rasterfile in sorted(list_rasters):
        print(rasterfile)
        date_raster = re.findall(pattern, rasterfile)[0].replace('.', '-')
        date_raster += '-01'
        raster_fullpath = f'{path_rasters}/{rasterfile}'
        gdf_stats = calc_zonal_statistics(shp_filename=shp_watersheds, raster_file=raster_fullpath, stats=['median'])
        dt_precipitation[date_raster] = gdf_stats[['Region', 'Planta', 'Embalse', 'median']]

    df_data = pd.concat(dt_precipitation)
    cols = ['Region', 'Recurso', 'Embalse', 'Precipitacion']
    df_data.columns = cols
    str_cols = ['Region', 'Recurso', 'Embalse']

    for str_col in str_cols:
        df_data[str_col] = df_data[str_col].str.upper()
        df_data[str_col] = df_data[str_col].str.replace(' ', '_')
        df_data[str_col] = df_data[str_col].str.replace(',', '_')
        df_data[str_col] = df_data[str_col].str.replace('.', '')

    df_data.reset_index(inplace=True)
    df_data['Fecha'] = pd.to_datetime(df_data['level_0'])
    df_data.set_index('Fecha', inplace=True)
    df_data.drop(['level_0', 'level_1'], axis=1, inplace=True)
    df_data.to_csv('../results/month_precipitation.csv')


if __name__ == '__main__':
    chirps_zonal_statistics()
    pass
