
# API key: personal account number + pwd
# purpose: authorise access

import requests
import os

# https://api.openweathermap.org/data/2.5/onecall?lat=33.8688&lon=151.2093&exclude=minutely&appid=7a80cbe5ead36989f104ad0edfaa4991
endpoint = "https://api.openweathermap.org/data/2.5/onecall"
# "7a80cbe5ead36989f104ad0edfaa4991"
print(os.environ)
# api_key= os.getenv("OWM_API_KEY")
api_key="7a80cbe5ead36989f104ad0edfaa4991"
print(api_key)
parameters = {
    "lat": "51.507351",
    "lon": "0.127758",
    "exclude": "current,minutely,daily",
    "appid": api_key
}
response = requests.get(url=endpoint, params=parameters)
response.raise_for_status()
data = response.json()
next_12_hours = data["hourly"][:12]
# print(next_12_hours)

will_rain = False

for data in next_12_hours:
    condition_code = data["weather"][0]["id"]
    if condition_code < 800:
        will_rain = True

if will_rain:
    print("please bring an umbrella")

# Environment variables
# type in "env" in terminal

#  1. convenience
#  2. security: separate secrets from the code base

# import os
# set variable:
# export OWM_API_KEY=7a80cbe5ead36989f104ad0edfaa4991
# check if successful:
# env
# to get: won't work in the code as it's not the same shell
# os.environ.get("OWM_API_KEY")
# to delete:
# unset OWM_API_KEY