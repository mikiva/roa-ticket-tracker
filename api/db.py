from pymongo import MongoClient
from settings import mongo_settings

hostname = mongo_settings.HOST
port = mongo_settings.PORT
user = mongo_settings.USER
pw = mongo_settings.PASSWORD

COLLECTION = "tickets"


def get_database():
    CONN_STRING = f"mongodb://{user}:{pw}@{hostname}/"

    with MongoClient(CONN_STRING) as client:
        db = client["roa"]
        return db

