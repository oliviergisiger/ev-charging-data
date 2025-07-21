#!/usr/bin/python3

import logging
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd
from base_get_data import get_data
from configs import STATION_STATUS, TIMESERIES_BASE_PATH, AVAILABILITY_MAP, INTERVAL

TIMESERIES_BASE_PATH = Path(TIMESERIES_BASE_PATH)


def format_timeseries_data(df):
    df.loc[:, 'EvseStatus'] = df.EvseStatus.map(AVAILABILITY_MAP)
    return df[['DateTime', '_id', 'EvseStatus']]


def floor_sampling(dt: datetime, interval: int):
    interval = timedelta(minutes=interval)
    return dt - (dt - dt.replace(minute=0, second=0, microsecond=0)) % interval


def get_timeseries_data(timestamp, interval: int):
    data = get_data(STATION_STATUS)
    df = pd.DataFrame(data)
    df.loc[:, 'DateTime'] = floor_sampling(timestamp, interval)
    return format_timeseries_data(df)



def save_timeseries_data(df, _date):
    file_path = Path(TIMESERIES_BASE_PATH, str(_date.year), str(_date.month).zfill(2), _date.strftime('%Y%m%d') + '.csv')
    file_path.parent.mkdir(parents=True, exist_ok=True)
    write_header = not file_path.exists()
    df.to_csv(file_path, mode='a', index=False, header=write_header)


def workflow():
    timestamp = datetime.now()
    data = get_timeseries_data(timestamp, interval=INTERVAL)
    save_timeseries_data(data, timestamp.date())
    logging.info('updated availabilities')


if __name__ == '__main__':
    workflow()

