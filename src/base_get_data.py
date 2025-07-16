#!/usr/bin/python3

import logging
import requests
from configs import URL



def get_data(fields):
    params = {
        'service': 'WFS',
        'version': '1.0.0',
        'request': 'GetFeature',
        'typeName': 'ich-tanke-strom:evse',
        'outputFormat': 'application/json',
        'propertyName': fields
    }

    response = requests.get(url=URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return [feature.get('properties') for feature in data['features']]
    logging.info(f'request return status code {response.status_code}')
