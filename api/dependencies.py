from fastapi import Depends
from pymongo import MongoClient
from settings import mongo_settings
from services.ticketservice import TicketService
from services.norticservice import NorticService

hostname = mongo_settings.HOST
port = mongo_settings.PORT
user = mongo_settings.USER
pw = mongo_settings.PASSWORD

COLLECTION = "tickets"
CONN_STRING = f"mongodb://{user}:{pw}@{hostname}:{port}"


async def mongo_client_provider():
    db = MongoClient(CONN_STRING)
    # db = client["roa"]
    return db


async def mongo_collections_provider(client=Depends(mongo_client_provider)):
    return client[COLLECTION]


async def ticket_service_provider(client=Depends(mongo_client_provider)) -> TicketService:
    ticket_service = TicketService(client)
    yield ticket_service
    ticket_service.close_db()


async def nortic_service_provider() -> NorticService:
    service = NorticService()
    yield service