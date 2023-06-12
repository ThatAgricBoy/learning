import requests
import os
from twilio.rest import Client

acc_sid = "AC85a20e5d95c93260fe0ba47ebab5bd7f"
auth_token = "61566226bd5e0a6e9c0c5f4407e456df"

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "4515857ef455714ff0542f2a728fc3a3"
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