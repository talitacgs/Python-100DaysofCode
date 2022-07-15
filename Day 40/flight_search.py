import requests
import os

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
TEQUILA_API = {
    'apikey': os.environ.get('TEQUILA_API')
}


class FlightSearch:
    def get_destination_code(self, city_dict):
        query_params = {
            "term": city_dict["city"],
            "location_types": "city",
        }
        response = requests.get(url=TEQUILA_ENDPOINT, headers=TEQUILA_API, params=query_params)
        result = response.json()["locations"]
        code_result = result[0]["code"]
        return code_result

    def check_flights(self, origin_city, destination_city, from_time, to_time):
        query_params = {
            "fly_from": origin_city,
            'fly_to': destination_city,
            'date_from': from_time.strftime("%d/%m/%Y"),
            'date_to': to_time.strftime("%d/%m/%Y"),
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'max_fly_duration': 48,
            'flight_type': 'round',
            'adults': 1,
            'children': 0,
            'adult_hold_bag': '1',
            'adult_hand_bag': '1',
            'one_for_city': 1,
            'max_stopovers': 0,
            'max_sector_stopovers': 0,
            'sort': 'price',
            'limit': 2,
            "curr": "GBP"
        }

        response = requests.get(url='https://tequila-api.kiwi.com/v2/search', headers=TEQUILA_API, params=query_params)
        try:
            result = response.json()["data"][0]
        except IndexError or KeyError:
            query_params["max_stopovers"] = 1
            response = requests.get(url='https://tequila-api.kiwi.com/v2/search', headers=TEQUILA_API, params=query_params)
            result = response.json()["data"][0]
            print(result)
            return result

        else:
            return result
