from settings import db_settings
from datetime import datetime
from db import get_database


def fetch_and_update():
    database = get_database()
    collection = database["tickets"]
    tstmp = datetime.utcnow()
    entry = {
        "show_id": "123",
        "entry_id": "321",
        "total_sold": 100,
        "total_booked": 40,
        "createdAt": tstmp
    }
    collection.insert_one(entry)
#    db = client.get_list_database()
#    print(db)
