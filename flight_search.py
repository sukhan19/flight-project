import requests
import datetime as dt
API_KEY_KIWI = "UvrP2TaiFfUUSg0nZF4NX9ijsf4sXl83"
API_KIWI_CITY = "oF4XmZSRcus1heMegKVOGUbmiPzp9P3x"
kiwi_endpoint = "https://api.tequila.kiwi.com/locations/query"
kiwi_endpoint_city = "https://tequila-api.kiwi.com/v2/search"
headers = {"apikey" : API_KEY_KIWI,'accept': 'application/json',}

date_depart_start = dt.datetime.now() + dt.timedelta(days=1)
date_depart_start_fin = date_depart_start.strftime("%d/%m/%Y")
date_depart_end = dt.datetime.now() + dt.timedelta(days=180)
date_depart_end_fin = date_depart_end.strftime("%d/%m/%Y")

class FlightSearch:
    def __init__(self):
        pass

    def city_code(self, city):
        params_kiwi = {"term": city}
        response = requests.get(url=kiwi_endpoint, params= params_kiwi, headers=headers)
        return response.json()["locations"][0]["code"]
    def flight_searcher(self, city):
        parameter = {
            'fly_from': 'LON',
            'fly_to': city,
            'date_from': date_depart_start_fin,
            'date_to': date_depart_end_fin,
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'curr': "GBP",
            "max_stopovers": 0,
            "ret_to_diff_city": False
        }
        header = {
            'apikey': API_KIWI_CITY,
        }
        response = requests.get(headers=header, url=kiwi_endpoint_city, params=parameter, )

        price = response.json()["data"][0]["price"]
        print(response.json()["data"][0])

        return (response.json()["data"][0])



