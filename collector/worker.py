from settings import settings
from datetime import datetime
from db import get_database
from logging import getLogger
from requests import get

log = getLogger(__name__)

def fetch_sold_tickets():
    host = settings.NORTIC_API_HOSTNAME
    shows = settings.SHOWS
    org = settings.ORGANIZER
    key = settings.NORTIC_API_KEY
    log.info(f"FETCH SOLD TICKETS")

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
    log.info(f"UPDATE DATABASE")

    for show, sold in shows:
        entry = {
            "metadata": {
                "show_id": show,
            },
            "timestamp": tstmp,
            "sold": sold
        }
        entries.append(entry)

    db.insert_many(entries)


def fetch_and_update():
    database = get_database()
    collection = database["tickets"]

    sold = fetch_sold_tickets()
    update_database(collection, sold)
