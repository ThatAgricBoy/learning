import requests
import datetime
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEET_TOKEN = os.environ.get("SHEET_TOKEN")
GENDER = "MALE"
WEIGHT_KG = 61.5
HEIGHT_CM = 171.9
AGE = 30

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

sheety_endpoint = "https://api.sheety.co/9a586a9d448d4610d5f145facb78c9f0/myWorkouts/workouts"
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
input_text = input("Describe the exercise you did today: ")
parameters = {
    "query": input_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=nutritionix_endpoint, json=parameters, headers=headers)
response.raise_for_status()
data = response.json()

exercise_date = datetime.date.today()
formatted_date = exercise_date.strftime("%d/%m/%Y")
exercise_time = datetime.datetime.now().time().strftime("%H:%M:%S")

for exercise in data["exercises"]:
    sheet_body = {
        "workout": {
            "date": formatted_date,
            "time": exercise_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_headers = {
    "Authorization": f"Bearer {SHEET_TOKEN}"
}
sheety_response = requests.post(url=sheety_endpoint, json=sheet_body, headers=sheet_headers)
print(sheety_response.text)