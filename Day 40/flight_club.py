import requests

SHEETY_USERS_ENDPOINT = os.environ.get("SHEETY_USERS_ENDPOINT")
HEADERS = {
    "Authorization": os.environ.get('HEADERS')
}

print("Welcome to Tali's Flight Club.\nWe find the best flight deals and email you!")
first_name = input("What is your first name?")
last_name = input("What is your last name?")
email = input("What is your email ?")
email_check = input("Type your email again")

while email != email_check:
    print("Divergent emails, please type again")
    email = input("What is your email ?")
    email_check = input("Type your email again")

params = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email_check,
    }
}
response = requests.post(url=SHEETY_USERS_ENDPOINT, headers=HEADERS, json=params)
data = response.json()
print(data)



