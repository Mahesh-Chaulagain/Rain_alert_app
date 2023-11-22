import requests

api_key = ""  # add API key
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"   # get 5 days data with 3 hour forcast

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

for daily_data in weather_slice:
    condition_code = daily_data["weather"][0]["id"]   # get hold of the weather condition "id"
    if int(condition_code) < 700:
        will_rain = True



if will_rain:
    print("Bring an umbrella.")
