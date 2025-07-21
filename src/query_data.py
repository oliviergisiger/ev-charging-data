import logging
from datetime import datetime, date
import ast
import pandas as pd
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parent.parent / 'charging_data'



def parse_list(x):
    """returns list representation of x, if is a 'stringified' list"""
    if isinstance(x, str) and x[0] == '[':
        return ast.literal_eval(x)
    return [x]



def get_time_series_data(_from: date, _to: date):
    daterange = pd.date_range(_from, _to, freq='d')
    files = [Path(f'{DATA_DIR}/timeseries/{d.year}/{str(d.month).zfill(2)}/{d.strftime("%Y%m%d")}.csv') for d in daterange]
    dfs = []
    no_data_dates = []
    for file in files:
        if file.exists():
            df = pd.read_csv(file)
            dfs.append(df)
        else:
            no_data_dates.append(datetime.strptime(file.name.replace('.csv', ''), '%Y%m%d').date())

    print(f'no files found for {[d.strftime("%Y-%m-%d") for d in no_data_dates]}')
    return pd.concat(dfs, ignore_index=True)


def get_station_data(_date: date):
    _date = datetime(_date.year, _date.month, _date.day, 0, 0, 0) # this is very stupid.
    df = pd.read_csv(DATA_DIR / 'stations' / 'charging_stations.csv')
    df['valid_from'] = pd.to_datetime(df.valid_from)
    df['valid_until'] = pd.to_datetime(df.valid_until)
    return df.loc[((df.valid_from < _date) | (df.valid_from.isna())) & (df.valid_until > _date), :]
