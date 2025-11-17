#!/usr/bin/python3

import logging
from pathlib import Path
from datetime import date, datetime
import pandas as pd
from base_get_data import get_data
from configs import STATION_PROPERTIES, STATIONS_FILE_PATH, STATIONS_FILE_COLUMNS


STATIONS_FILE = Path(STATIONS_FILE_PATH)
MAX_DATE = datetime(2099, 12, 31)


def read_current_stations_file():
    if STATIONS_FILE_PATH.is_file():
        df = pd.read_csv(STATIONS_FILE_PATH, parse_dates=['valid_from', 'valid_until'])
        df['lastUpdate'] = pd.to_datetime(df['lastUpdate'], utc=True).dt.tz_convert(None)
        return df
    return pd.DataFrame(columns=STATIONS_FILE_COLUMNS)

def upsert_stations(df_new, valid_from):
    df_old = read_current_stations_file()
    df_new['lastUpdate'] = pd.to_datetime(df_new.lastUpdate)
    df_new['lastUpdate'] = df_new.lastUpdate.fillna(datetime(2000, 1, 1))
    df_new.loc[:, 'valid_until'] = MAX_DATE
    merged = pd.merge(df_new, df_old[df_old.valid_until == MAX_DATE], on='_id', how='left', suffixes=('_new', '_old'))
    changed = merged[(merged['lastUpdate_new'] != merged['lastUpdate_old']) | (merged['lastUpdate_old'].isna()) ].copy()
    invalids = changed['_id'].unique()
    df_old.loc[(df_old['_id'].isin(invalids)) & (df_old['valid_until'] == MAX_DATE), 'valid_until'] = valid_from
    df_new_valid = df_new[df_new['_id'].isin(invalids)].copy()
    df_new_valid['valid_from'] = valid_from
    df_new_valid['valid_until'] = MAX_DATE
    df_upserted = pd.concat([df_old, df_new_valid], ignore_index=True)
    return df_upserted


def save_stations_data(data, timestamp: datetime):
    df_new = pd.DataFrame(data)[STATION_PROPERTIES.split(',')]
    df_new.loc[~df_new.lastUpdate.isna(), 'lastUpdate'] = df_new.lastUpdate.str[:10]
    df_new.loc[:, 'valid_until'] = datetime(2099, 12, 31)
    df_upserted = upsert_stations(df_new, timestamp.date())
    df_upserted.to_csv(STATIONS_FILE_PATH, index=False)


def workflow():
    logging.info('start getting stations')
    timestamp = datetime.now()
    data = get_data(STATION_PROPERTIES)
    save_stations_data(data, timestamp)
    logging.info('end getting stations')


if __name__ == '__main__':
    workflow()

