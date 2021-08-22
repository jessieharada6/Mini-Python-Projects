import requests
from datetime import datetime
import time
import smtplib

MY_LAT = 27.2046 # Your latitude
MY_LONG = 77.4977 # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5):
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour = time_now.hour

    sunrise = 24 if sunrise == 0 else sunrise
    sunset = 24 if sunset == 0 else sunset
    if hour >= sunset and hour <= sunrise:
        return True

def send_email(content):
    my_email = "testemailsonlynojoke@gmail.com"
    password = "1234abcd()"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Look up!\n\n{content}")

# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        send_email("The ISS is above you in the sky!")





