from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
from dependencies import ticket_service_provider

app = FastAPI()


@app.get("/api/shows/sold")
async def get_shows(request: Request, ticket_service=Depends(ticket_service_provider)):
    latest = ticket_service.get_latest_sold()
    return JSONResponse(latest)
