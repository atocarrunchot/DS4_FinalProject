import pickle
import pandas as pd


def set_region(sr_data):
    regions = ['ANTIOQUIA', 'CARIBE', 'CENTRO', 'ORIENTE', 'VALLE']
    sr_region = pd.Series(index=sr_data.index)

    for feature in sr_data.index:
        props = feature.split('$')

        for region in regions:
            if region in props:
                feature_region = region
                sr_region.loc[feature] = feature_region
                continue

    return sr_region


def set_dataset(sr_data):
    datasets = {
        'PRECIPITACION': 'PRECIPITATION',
        'APORTES': 'INFLOWS',
        'VOL_UTIL': 'STORAGE',
        'PRECIO': 'PRICE',
        'OFERTA': 'OFFER',
        'VERTIMIENTO': 'SPILL',
        'NOAA': 'MACROCLIMATE',
    }

    sr_dataset = pd.Series(index=sr_data.index)

    for feature in sr_data.index:
        props = feature.split('$')

        for dataset in datasets:
            if dataset == props[-2]:
                feature_dataset = dataset
                sr_dataset.loc[feature] = feature_dataset
                continue

    return sr_dataset


def set_properties(feature_importance):
    feature_importance.name = 'gain'
    df = pd.DataFrame(feature_importance.copy())
    df['gain'] /= df['gain'].sum()
    df['gain'] *= 100.
    df['region'] = set_region(sr_data=feature_importance)
    df['region'].fillna(value='OTHERS', inplace=True)
    df['dataset'] = set_dataset(sr_data=feature_importance)
    df['dataset'].fillna(value='MACROCLIMATE', inplace=True)
    df.sort_values('gain', ascending=False, inplace=True)

    return df


def test():
    model = pickle.load(open("../models/XGboost model_random.sav", "rb"))
    feature_importance = pd.Series(model.get_score(importance_type='gain'))
    df = set_properties(feature_importance)

    return df


if __name__ == '__main__':
    test()
    pass
