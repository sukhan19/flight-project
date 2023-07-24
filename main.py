from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager


flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()

sheet_data = data_manager.get_data()

for entry in sheet_data:
    if entry["iataCode"] == "":
        entry["iataCode"] = flight_search.city_code(entry["city"])

        data_manager.destination_data = sheet_data
        data_manager.edit_google_sheet()


for entry in sheet_data:
    current_data = flight_search.flight_searcher(entry["iataCode"])
    current_price = int(current_data["price"])
    dest = str(current_data["local_departure"])
    desti = dest.split("T")[0]

    if current_price < entry['lowestPrice']:
        notification_manager.send_message(current_price, current_data["cityFrom"],
                                          current_data["cityTo"], desti)

        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        message = "Super Savings !! \n"  f"The fare is ${current_price} from {current_data['cityFrom']} to" \
        f" {current_data['cityTo']} on {desti}\n"
        f"The lowest in 6 months time",

        notification_manager.send_emails(emails, message)

