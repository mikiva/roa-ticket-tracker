from settings import settings
from datetime import datetime
from db import get_database

from requests import get


def fetch_sold_tickets():
    host = settings.NORTIC_API_HOSTNAME
    shows = settings.SHOWS
    org = settings.ORGANIZER
    key = settings.NORTIC_API_KEY

    base_url = f"{host}/api/json/organizer/{org}/show"

    sold = []

    for show in shows:
        url = f"{base_url}/{show}"
        result = get(url).json()
        s = result.get("soldEvents", {}).get("amountSold")
        sold.append((show, s))
    return sold


def update_database(db, shows):
    tstmp = datetime.utcnow()
    entries = []

    for show, sold in shows:
        entry = {
            "metadata": {
                "show_id": show,
            },
            "timestamp": tstmp,
            "sold": sold
        }
        entries.append(entry)
        print(entry)

    db.insert_many(entries)


def fetch_and_update():
    database = get_database()
    collection = database["tickets"]

    sold = fetch_sold_tickets()
    update_database(collection, sold)

    # settings = DB

# entry = {
#     "metadata": {
#         "show_id": "123",
#     },
#     "timestamp": tstmp,
#     "sold": sold
# }
# collection.insert_one(entry)
#    db = client.get_list_database()
#    print(db)
