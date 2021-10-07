import requests
#This class is responsible for talking to the Google Sheet.

SHEETY_ENDPOINT = "https://api.sheety.co/c4504dc6da609c2729739ac319df310e/flightDeals/prices"
class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        result = requests.get(url=SHEETY_ENDPOINT)
        result.raise_for_status()
        self.destination_data = result.json()['prices']
        return self.destination_data

    def update_destination_iata_code(self):
        response = None
        for city in self.destination_data:
            body = {
                "price": {
                    "iataCode": city['iataCode']
                }
            }
            result = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=body)
            result.raise_for_status()
            response = result.json()
            #  must not return within for loop, it will only run once
        return response


