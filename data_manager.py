import requests
sheety_endpoint = "https://api.sheety.co/4586df84d54404652ebf88c261018ff8/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://docs.google.com/spreadsheets/d/1cIAkg7ZFswCTU1RShnn7zRvvaW17zInnGeA9FLkEDXY/edit#gid=1357409584"

class DataManager:
    def __init__(self):
        self.destination_data = {}
    def get_data(self):
        response = requests.get(url=sheety_endpoint)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def edit_google_sheet(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode" : city["iataCode"]
                }
            }
            response = requests.put(url=f"{sheety_endpoint}/{city['id']}", json=new_data)
    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data

