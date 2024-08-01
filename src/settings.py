from enum import StrEnum

from pydantic_settings import BaseSettings, SettingsConfigDict

class Environment(StrEnum):
    DEV = "development"
    PRD = "production"

class Settings(BaseSettings):
    DB_URI: str
    ENV: str = Environment.DEV

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()