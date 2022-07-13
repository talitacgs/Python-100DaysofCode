import requests
import os

SHEETY_ENDPOINT = os.environ.get('SHEETY_ENDPOINT')

HEADERS = {
    "Authorization": os.environ.get('HEADERS')
}

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=HEADERS)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_code(self, city_dict):
        row_id = city_dict["id"]
        row_code = city_dict["iataCode"]
        SHEETY_UPDATE = f"{SHEETY_ENDPOINT}/{row_id}"
        params = {
            "price": {
                "iataCode": row_code
            }
        }
        update_row = requests.put(url=SHEETY_UPDATE, json=params, headers=HEADERS)
        print(update_row.text)
