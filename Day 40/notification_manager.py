from twilio.rest import Client
import smtplib
import os

TWILIO_SID = os.environ.get('TWILIO_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
GENERIC_NUMBER = os.environ.get('GENERIC_NUMBER')
PERSONAL_NUMER = os.environ.get('PERSONAL_NUMER')

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=GENERIC_NUMBER,
            to=PERSONAL_NUMER
        )
        print(message.status)


    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )