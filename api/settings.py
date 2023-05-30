from pydantic import BaseSettings



class MongoSettings(BaseSettings):
    HOST: str = "localhost"
    USER: str = "roa"
    PASSWORD: str = "roa"
    PORT: int = 27017
    class Config:
        env_prefix = "ROA_DB_"
        env_file = ".env"


mongo_settings = MongoSettings()
