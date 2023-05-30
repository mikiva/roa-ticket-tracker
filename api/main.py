from fastapi import FastAPI, Request, Depends, Header
from fastapi.responses import JSONResponse, HTMLResponse
from dependencies import ticket_service_provider, nortic_service_provider
from typing import Annotated

app = FastAPI()

cache_updated = None
today_cache = dict()


@app.get("/api/shows/sold")
async def get_shows(request: Request, ticket_service=Depends(ticket_service_provider)):
    latest = ticket_service.get_latest_sold()
    return JSONResponse(latest)


@app.get("/api/shows/sold/today")
async def get_shows(request: Request, accept: Annotated[str, Header()],
                    nortic_service=Depends(nortic_service_provider),
                    ticket_service=Depends(ticket_service_provider)):
    shows = nortic_service.get_all_shows_info()
    today = ticket_service.get_today_sold()

    for show in shows:
        sid = show.get("id")
        show["sold"] = today[sid]["current"]
        show["today"] = today[sid]["today"]

    return JSONResponse(shows)
