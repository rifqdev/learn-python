import os
import requests
from twilio.rest import Client

api_key = os.environ.get("OWM_API_KEY")
lat = -7.575830
long = 108.765121

parameters = {
    "lat": lat,
    "lon": long,
    "appid": api_key,
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

condition_codes = [item["weather"][0]["id"] for item in weather_data["list"]]
will_rain = [item for item in condition_codes if item < 701]

if len(will_rain) > 0:
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    message = client.messages.create(from_=os.environ.get("FROM_PHONENUMBER"), body="It's going to rain today. Remember to bring an ☔️", to=os.environ.get("TO_PHONENUMBER"))
    print(message.sid)