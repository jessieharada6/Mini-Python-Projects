import requests
from datetime import datetime

#  https://docs.google.com/spreadsheets/d/12vU8EeKZoLF0fDTzUmGZCA7UNRnZPzd7UQUh9n6OTTc/edit#gid=0
#
# Nutrionix
APP_ID= "7fc26cf4"
API_KEY= "7af6341ad283b496aa82e351d2350d94"

food_endpoint = "https://trackapi.nutritionix.com/v2/natural/nutrients"

exercise_text = input("What did Peanut eat: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

parameters = {
    "query": exercise_text
}

response = requests.post(url=food_endpoint, json=parameters, headers=headers)
response.raise_for_status()
result = response.json()
print(result)

sheet_endpoint = "https://api.sheety.co/c4504dc6da609c2729739ac319df310e/peanutFoodLog/workouts"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for food in result['foods']:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "food": food['food_name'].title(),
            "quantity": food['serving_qty'],
            "unit": food['serving_unit'],
            "sugar":food['nf_sugars']
        }
    }

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs)

# https://docs.google.com/spreadsheets/d/12vU8EeKZoLF0fDTzUmGZCA7UNRnZPzd7UQUh9n6OTTc/edit#gid=0