#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from flight_search import FlightSearch
from pprint import pprint
from flight_data import FlightData
from data_manager import DataManager

flight_search = FlightSearch()
flight_data = FlightData()
data_manager = DataManager()

ORIGIN_CITY_IATA = "SYD"

sheet_data = data_manager.get_destination_data()

for row in sheet_data:
    if row['iataCode'] == "":
        row['iataCode'] = flight_search.get_destination_code(row['city'])
        pprint(data_manager.destination_data)
    data_manager.update_destination_iata_code()

    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        row["iataCode"]
    )

# pprint(sheet_data)
# pprint(data_manager.destination_data)
# data_manager.destination_data  = sheet_data






