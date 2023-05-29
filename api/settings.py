from pydantic import BaseSettings



class MongoSettings(BaseSettings):
    HOST: str = "localhost"
    USER: str = "roa"
    PASSWORD: str = "roa"
    PORT: str = "27017"
    class Config:
        env_prefix = "ROA_DB_"


mongo_settings = MongoSettings()