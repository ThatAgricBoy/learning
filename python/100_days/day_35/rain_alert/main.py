import requests
import os
from twilio.rest import Client

acc_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH")

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = os.environ.get("OWM_API")
weather_parameters = {
    "lat": 7.35,
    "lon": 3.88,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
condition = weather_data["weather"][0]["id"]
if condition > 700:
    client = Client(acc_sid, auth_token)
    message = client.messages.create(
        body="Hello from Dev Samurai‍💻",
        from_="+13613265660",
        to="+2348138133145"
    )
    print(message.status)