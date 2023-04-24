from pymongo import MongoClient

hostname = "localhost"
port = "27017"
user = "roa"
pw = "roa"

# TODO: Consider time series
def get_database():
    CONN_STRING = f"mongodb://{user}:{pw}@{hostname}/"

    client = MongoClient(CONN_STRING)

    return client["roa"]

