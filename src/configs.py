import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
STATIONS_FILE_PATH = BASE_DIR / 'charging_data' /'stations' / 'charging_stations.csv'
TIMESERIES_BASE_PATH = BASE_DIR / 'charging_data' / 'timeseries'
LOG_DIR = BASE_DIR / 'logs'
LOG_FILE = LOG_DIR / 'charging_data.log'
LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s — %(levelname)s — %(message)s'
)


URL = 'http://ich-tanke-strom.switzerlandnorth.cloudapp.azure.com:8080/geoserver/ich-tanke-strom/ows'
STATION_PROPERTIES = '_id,GeoCoordinates,Plugs,AccessibilityLocation,Accessibility,ChargingFacilities,lastUpdate'
STATION_STATUS = 'EvseStatus'


STATIONS_FILE_COLUMNS = [
    '_id', 'lastUpdate', 'ChargingFacilities', 'Plugs',
    'GeoCoordinates', 'Accessibility', 'AccessibilityLocation', 'valid_from', 'valid_until'
]

AVAILABILITY_MAP = {'Available': 0, 'Occupied': 1, 'Unknown': None}