#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch

dm = DataManager()
fs = FlightSearch()


sheet_data = dm.get_data()
empty_iata = [item for item in sheet_data if item["iataCode"] == ""]

if len(empty_iata) > 0:
    for row in empty_iata:
        city_name = row["city"]
        iata_code = fs.get_iata_code(city=city_name)
        row["iataCode"] = iata_code
        
        payload = {
            "price": {
                "iataCode": row["iataCode"]
            }
        }
        
        dm.update_iata(payload=payload, id=row["id"])

flight_data = [item for item in sheet_data if item["iataCode"] != ""]

if len(flight_data) > 0:
    for row in flight_data:
        iata_code = row["iataCode"]
        fs.find_cheapest_flight(destination=iata_code)


