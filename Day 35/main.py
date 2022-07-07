import requests
from twilio.rest import Client
import os

api_url = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")

TWILIO_SID = os.environ.get("SID_TWILIO")
TWILIO_AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

LATITUDE = 42.899979
LONGITUDE = 125.129967

weather_params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": api_key,
}

response = requests.get(api_url, params=weather_params)
data = response.json()
weather_data = data["hourly"][:12]

will_rain = False

for hour_data in weather_data:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages \
        .create(
        body="It's going to rain today in Liaoyuan, China. Remember to bring an ☂️🌂 ",
        from_=os.environ.get("GENERIC_NUMBER"),
        to=os.environ.get("PERSONAL_NUMBER"),
    )
    print(message.status)