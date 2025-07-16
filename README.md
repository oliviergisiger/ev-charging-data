# EV Charging Data

This repo loads data from ich-tanke-strom API and stores the data into different files: 

## Charging Stations
The file ```data/charging_stations/charging_stations.csv``` collects all stations available in the API. 
It uses an upsert logic on the field ``lastUpdated`` and sets validity periods to each station. \
### Columns
- ```_id```: unique station identifier
- ```lastUpdate```: last change to metadata
- ```ChargingFacilities```: list with outlets, containing ``Power``, ``Voltage``, ``PowerType`` for each outlet.
- ```Plugs```: Plug type
- ```GeoCoordinates```: dict, coordinates degree: lat, lon
- ```Accessibility```: One of: ```Free publicly accessible```, ```Paying publicly accessible```, ```Restricted access```, ```Test Station```, ```Unspecified```
- ```AccessibilityLocation```: One of: ```OnStreet```, ```ParkingLot```, ```UndergroundParkingGarage```, ```ParkingGarage```
- ```valid_from```: Date indicating validity start or nan.
- ```valid_until```: Date indicating validity end; when valid,  ``valid_until == 2099-12-31``

## Timeseries
 For each ```_id``` in the stations file, hourly data is stored in a single file per day; this allows the creation of timeseries. 
### Columns
- ```_id```: unique station identifier corresponding to ```_id``` in stations file
- ```DateTime```: date time
- ```EvseStatus```: status of charging station: 0=```Available```, 1=```Occupied```, NA=```Unknown```