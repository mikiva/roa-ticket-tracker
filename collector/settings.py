from pydantic import BaseSettings

from dotenv import load_dotenv
from typing import Optional

load_dotenv()


class Settings(BaseSettings):
    ORGANIZER = 672  # Scenknuten
    EVENT = 47696  # Rock of Ages
    SHOWS = [
        189743,
        189744,
        189746,
        189747,
        189748,
        189749,
        189750,
        189751
    ]

    NORTIC_API_HOSTNAME: str = "https://www.nortic.se"
    NORTIC_API_KEY: Optional[str] = None
    VERSION: Optional[str] = "prod"
    WORKER_TIMEOUT: int = 300 #5 minutes

    class Config:
        env_prefix = "ROA_"

class MongoSettings(BaseSettings):
    HOST: str = "localhost"
    USER: str = "roa"
    PASSWORD: str = "roa"
    PORT: str = "27017"
    
    class Config:
        env_prefix = "ROA_DB_"


class DBSettings(BaseSettings):
    DB_FILE_LOCATION: str = None
    WORKER_TIMEOUT: int = 300 #5 minutes
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
mongo_settings = MongoSettings()
settings = Settings()
