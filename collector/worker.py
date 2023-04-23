from settings import db_settings

from influxdb import InfluxDBClient

client = InfluxDBClient("localhost" , 8086, "admin", "password", "tickets")

def fetch_and_update():
    db = client.get_list_database()
    print(db)