from pymongo import MongoClient

hostname = "localhost"
port = "27017"
user = "roa"
pw = "roa"


# TODO: Consider time series
def get_database():
    CONN_STRING = f"mongodb://{user}:{pw}@{hostname}/"

    client = MongoClient(CONN_STRING)

    db = client["roa"]
    colls = db.list_collection_names()
    if "tickets" not in colls:
        timeseries = {
            "timeField": "timestamp",
            "metaField": "metadata",
            "granularity": "minutes"
        }
        db.create_collection('tickets', timeseries=timeseries)

    return db
