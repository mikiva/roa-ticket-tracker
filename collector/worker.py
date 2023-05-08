from settings import db_settings
from datetime import datetime
from db import get_database

from random import choice

url = "fetch_url"

sold = 100

added = [0, 0, 1, 2, 3]


def fetch_and_update():
    global sold
    database = get_database()
    collection = database["tickets"]

    sold += choice(added)

    tstmp = datetime.utcnow()

    entry = {
        "metadata": {
            "show_id": "123",
        },
        "timestamp": tstmp,
        "sold": sold
    }
    collection.insert_one(entry)
#    db = client.get_list_database()
#    print(db)
