from pymongo import MongoClient
from settings import mongo_settings

hostname = mongo_settings.HOST
port = mongo_settings.PORT
user = mongo_settings.USER
pw = mongo_settings.PASSWORD


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
