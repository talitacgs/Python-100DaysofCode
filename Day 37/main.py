import requests
from datetime import datetime

USERNAME = "talitacgs"
TOKEN = "asdasdasd"
ID = "graph1"

#create user
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
#response = requests.post(url=pixela_endpoint,json=user_params)
#print(response.text)

#create graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": ID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

#update with data
post_endpoint = f"{graph_endpoint}/{ID}"

today = datetime.now()
TODAY = today.strftime("%Y%m%d")

post_config = {
    "date": TODAY,
    "quantity": input("How many kilometers did you cycle today? "),
}

response = requests.post(url=post_endpoint, json=post_config, headers=headers)
print(response.text)

#Only in case to edit a data
post_edit_endpoint = f"{post_endpoint}/{TODAY}"
post_edit_config = {
    "quantity": "23"
}
#response = requests.put(url=post_edit_endpoint, json=post_edit_config, headers=headers)
#print(response.text)

#Only in case to delete a data
delete_pixel_endpoint = f"{post_edit_endpoint}"
#response = requests.delete(url=delete_pixel_endpoint, json=post_edit_config, headers=headers)
#print(response.text)

