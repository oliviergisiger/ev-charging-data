# EV Charging Data

This repo loads data from ich-tanke-strom API and stores the data into different files. 
**At the moment, timeseries data is fetched every 15 minutes. To change the frequency, use the INTERVAL parameter from config. 
The cronjob must be set acordingly**

## Charging Stations
The file ```data/charging_stations/charging_stations.csv``` collects all stations available in the API. 
It uses an upsert logic on the field ``lastUpdated`` and sets validity periods to each station. \
### Columns
- ```_id```: unique station identifier
- ```lastUpdate```: last change to metadata
- ```ChargingFacilities```: list with outlets, containing ``Power``, ``Voltage``, ``PowerType`` for each outlet.
- ```Plugs```: Plug type (s)
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
- ```EvseStatus```: status of charging station: 0=```Available```, 2=```Occupied```; see configs for details. 

*For more information visit the [OICP GitHub Documentation](https://github.com/hubject/oicp/blob/master/OICP-2.3/OICP%202.3%20CPO/03_CPO_Data_Types.asciidoc)*


## Configs
In ```configs.py```, some configurations are defined: 
- relevant paths
- logging
- fields to fetch from API

## Notebook
The [Jupyter Notebook](notebook.ipynb) shows an example query to the stored data. 

