import requests

import requests
from datetime import datetime
import os

GENDER = "female"
WEIGHT_KG = 60
HEIGHT_CM = 171
AGE = 30

# google sheet:
# https://docs.google.com/spreadsheets/d/17t0toTUFKPwtXEw62DLRsxPMV8iS25HG5GBmNrvNlBo/edit?skip_itp2_check=true&pli=1#gid=0

# APP_ID = os.environ["YOUR_APP_ID"]
# API_KEY = os.environ["YOUR_API_KEY"]
# Nutritionix
APP_ID= "7fc26cf4"
API_KEY= "7af6341ad283b496aa82e351d2350d94"


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
response.raise_for_status()
result = response.json()
print(result)

# Sheety
# https://dashboard.sheety.co/projects/6127612831fba85ba3ec2e37/auth
sheet_endpoint = "https://api.sheety.co/c4504dc6da609c2729739ac319df310e/day38MyWorkouts/workouts"

today_date = datetime.now().strftime("%d/%m/%Y")
# 17:41:00
now_time = datetime.now().strftime("%X")
print(today_date, now_time)

# "workout" is from the /workouts, but singular
# generate texts
for exercise in result['exercises']:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            # title case: Running
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }

    #  make a call for each exercise item
    # No Auth
    # sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs)

    #Basic Auth
    # sheet_response = requests.post(
    #     url=sheet_endpoint,
    #     json=sheet_inputs,
    #     auth=(
    #         # username, password
    #         'workouts', 'workouts'
    #
    #     )
    # )
    # sheet_response = requests.post(
    #     sheet_endpoint,
    #     json=sheet_inputs,
    #     auth=(
    #         os.environ["USERNAME"],
    #         os.environ["PASSWORD"],
    #     )
    # )

    #Bearer Token: It is part of headers
    # token authentication is an HTTP authentication scheme t
    # hat involves security tokens.
    # The name “Bearer authentication”
    # basically means “give access to the bearer of this token.”
    # a cryptic string
    # bearer_headers = {
    # "Authorization": f"Bearer {os.environ['TOKEN']}"
    # }

    bearer_token_header  = {
        "Authorization" : "Bearer workoutswoohoo"
    }
    sheet_response = requests.post(
        url=sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_token_header
    )

#     print(sheet_response.text)