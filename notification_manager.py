from twilio.rest import Client
import requests
import smtplib
MY_EMAIL = "sukhangill852@gmail.com"
MY_PASSWORD = "MY_PASS"
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"



auth_token = "c59978ff13ffb4545c4b32f403482ecc"
account_sid = "ACcc75a5ba09f2efbcd5189c602c19f1bd"
num = +14178073724



class NotificationManager:


    def send_message(self, price, from_place, to , time):
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"Super Savings !! \n"
                 f"The fare is ${price} from {from_place} to {to} on {time}\n"
                 f"The lowest in 6 months time",
            from_=num,
            to="NUMBER"
        )

    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
