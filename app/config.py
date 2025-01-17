from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGODB_URL: str = "mongodb://localhost:27017"
    MONGODB_DB_NAME: str
    LOGFIRE_TOKEN: str
    class Config:
        env_file = ".env"

settings = Settings()