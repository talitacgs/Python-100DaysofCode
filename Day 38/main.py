import requests
from datetime import datetime
import os

API_ID = os.environ.get('API_ID')
API_KEY = os.environ.get('API_KEY')
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

post_request_body = {
 "query": input("Tell me which exercises you did: "),
 "gender": "female",
 "weight_kg": 50,
 "height_cm": 153.64,
 "age": 27
}

response = requests.post(url=nutritionix_endpoint, json=post_request_body, headers=headers)
data = response.json()

sheety_endpoint = os.environ.get('sheety_endpoint')

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in data["exercises"]:
    sheety_requests = {
      "workout": {
        "date": today_date,
        "now": now_time,
        "exercise": exercise["name"].title(),
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"],
      }
    }

headers = {
    "Authorization": os.environ.get('Authorization')
}

sheety_response = requests.post(url=sheety_endpoint, json=sheety_requests, headers=headers)
print(sheety_response.text)
