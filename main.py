import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# for weather data
api_key = os.getenv("API_KEY")  # add API key
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"   # get 5 days data with 3 hour forcast

# for sending sms using twilio
account_sid = "AC03c62377f46e988a1246c5ea74575c5a"
auth_token = os.getenv("AUTH_TOKEN")

weather_params = {
    "lat": 27.7167,
    "lon": 85.3167,
    "appid": api_key,
}
response = requests.get(url=OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["list"][:7]    # get data for a day 24/3 i..e 8 data

will_rain = False

for hourly_data in weather_slice:
    condition_code = hourly_data["weather"][0]["id"]   # get hold of the weather condition "id"
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)    # set up the client to send message
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an Umbrella☔",
            from_='+14242752645',
            to='+977-9843624965'
    )
    print(message.status)
