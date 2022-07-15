from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_destination_data()
notification_manager = NotificationManager()
ORIGIN_CITY = "LON"

for i in range(0, len(sheet_data)):
    if sheet_data[i]["iataCode"] == "":
        response = flight_search.get_destination_code(sheet_data[i])
        sheet_data[i]["iataCode"] = response
        data_manager.update_code(sheet_data[i])

tomorrow = datetime.now()
six_month = datetime.now() + timedelta(days=(6*30))

for destination in sheet_data:
    flight = flight_search.check_flights(ORIGIN_CITY, destination["iataCode"], tomorrow, six_month)

    if flight is None:
        continue

    if flight['price'] < destination["lowestPrice"]:

        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        out_date = flight["route"][0]["local_departure"].split("T")[0]
        return_date = flight["route"][1]["local_departure"].split("T")[0]

        message = f"Low price ! Only £{flight['price']} to fly from {flight['cityFrom']}-{flight['cityCodeFrom']} " \
                  f"to {flight['cityTo']}-{flight['cityCodeTo']}, from {out_date} to {return_date} "
        print(message)

        if flight['max_stopovers'] > 0:
            via_city = flight["route"][0]["cityTo"]
            message += f"\nFlight has {flight['max_stopovers']} stop over, via {via_city}"

        origin_airport = flight["route"][0]["flyFrom"]
        destination_airport = flight["route"][1]["flyTo"]

        link = f"https://www.google.co.uk/flights?hl=en#flt={origin_airport}.{destination_airport}.{out_date}*{origin_airport}.{origin_airport}.{return_date}"
        notification_manager.send_emails(emails, message, link)
