from pydantic import BaseSettings

from dotenv import load_dotenv
from typing import Optional

load_dotenv()


class Settings(BaseSettings):
    ORGANIZER = 672  # Scenknuten
    EVENT = 99999  # Rock of Ages
    SHOWS = [
    ]

    NORTIC_API_HOSTNAME: str = "https://74xd3rns6k.execute-api.eu-north-1.amazonaws.com"
    NORTIC_API_KEY: Optional[str] = None
    VERSION: Optional[str] = "prod"


    class Config:
        env_prefix = "ROA_"

class DBSettings(BaseSettings):
    DB_FILE_LOCATION: str = None
    WORKER_TIMEOUT: int = 10#300 #5 minutes
    ECHO: bool = False
    REDIS_HOST = "roa_redis"
    HOSTNAME: str = None
    class Config:
        env_prefix = "ROA_"

class InfluxDBSettings(BaseSettings):
    HOST: str = "roa_influx"
    BUCKET: str = "roa_tickets"
    TOKEN: str = "sallskap"


    class Config:
        env_prefix = "ROA_INFLUX_"



db_settings = DBSettings()
settings = Settings()