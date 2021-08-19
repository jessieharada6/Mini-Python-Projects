import requests
import datetime as dt
#  API parameters: https://sunrise-sunset.org/api
#  https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400
MY_LAT = 27.2046
MY_LONG = 77.4977

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise, sunset)

time_now = dt.datetime.now()
print(time_now.hour)
