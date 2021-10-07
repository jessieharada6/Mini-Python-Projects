import requests
# you're only importing the datetime class
# a class within the module
# from module import class
#  from datetime import datetime
# whole module - import module as a-name-i-will-use
import datetime as datetime
from flight_data import FlightData

# Tequila:
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "JlEakkrsgnPDRyCKb1e0F6QkUoYibtma"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        # curl -X GET "https://tequila-api.kiwi.com/locations/query?term=paris&locale=en-US&location_types=airport&limit=10&active_only=true" -H  "accept: application/json" -H  "apikey: JlEakkrsgnPDRyCKb1e0F6QkUoYibtma"
        query = {
            "term": city_name,
            "location_types": "airport"
        }

        header = {
            "apikey": TEQUILA_API_KEY
        }

        result = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", headers=header, params=query)
        result.raise_for_status()
        response = result.json()["locations"][0]["id"]

        return response

    def check_flights(self, origin, destination):
        # https://tequila.kiwi.com/portal/docs/tequila_api/search_api
        tomorrow = (datetime.datetime.now() + datetime.timedelta(days = 1)).strftime("%d/%m/%Y")
        six_month_later = (datetime.datetime.now() + datetime.timedelta(days = 6 * 30)).strftime("%d/%m/%Y")
        query= {
            "fly_from": origin,
            "fly_to": destination,
            "date_from": tomorrow,
            "date_to": six_month_later,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "AUD"
        }

        header = {
            "apikey": TEQUILA_API_KEY
        }

        result = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=header, params=query)
        result.raise_for_status()

        try:
            response = result.json()["data"][0]
        except IndexError:
            print(f"No flight found for {destination}")
            return None

        flight_data = FlightData(
            price= response["price"],
            origin_city=response["router"][0]["cityFrom"],
            origin_airport=response["route"][0]["flyFrom"],
            destination_city=response["route"][0]["cityTo"],
            destination_airport=response["route"][0]["flyTo"],
            out_date=response["route"][0]["local_departure"].split("T")[0],
            return_date=response["route"][1]["local_departure"].split("T")[0]
        )

        print(f"{flight_data.destination_city}: AUD${flight_data.price}")
        return response


