import requests
from datetime import datetime
import os 

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
AUTHORIZATION = os.environ.get("AUTHORIZATION")

EXERCISE_API = os.environ.get("EXERCISE_API")
ADD_ROW_API = os.environ.get("ADD_ROW_API")

payload = {
    "query": input("Tell me wich exercise you did: ")
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

response = requests.post(url=EXERCISE_API, json=payload, headers=headers)
exercise_data = response.json()["exercises"]

# add row 
today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

payload = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise_data[0]["name"].title(),
        "duration": exercise_data[0]["duration_min"],
        "calories": exercise_data[0]["nf_calories"]
    }
}

response = requests.post(url=ADD_ROW_API, json=payload, auth=AUTHORIZATION)
print(response.text)