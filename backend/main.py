from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from SPAService import SPAService

app = FastAPI()






app.mount("/", app=SPAService(directory="/app/spa", html=True), name="ui")