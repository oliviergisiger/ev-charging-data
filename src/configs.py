URL = 'http://ich-tanke-strom.switzerlandnorth.cloudapp.azure.com:8080/geoserver/ich-tanke-strom/ows'
STATION_PROPERTIES = 'GeoCoordinates,Plugs,AccessibilityLocation,Accessibility,ChargingFacilities,lastUpdate'
STATION_STATUS = 'EvseStatus'
STATIONS_FILE = '../charging_data/stations/charging_stations.csv'
STATIONS_FILE_COLUMNS = [
    '_id', 'lastUpdate', 'ChargingFacilities', 'Plugs',
    'GeoCoordinates', 'Accessibility', 'AccessibilityLocation', 'valid_from', 'valid_until'
]
TIMESERIES_BASE_PATH = '../charging_data/timeseries'
AVAILABILITY_MAP = {'Available': 0, 'Occupied': 1, 'Unknown': None}