# type: ignore
import os
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    App Environemnt Variables
    """

    model_config = SettingsConfigDict(env_file=".env")

    # App Settings
    DEBUG: bool = os.environ.get("DEBUG")

    # Database
    DYNAMO_URL: str = os.environ.get("DYNAMO_URL")

    # AWS
    A_ARCHIVE_BUCKET: str = os.environ.get("A_ARCHIVE_BUCKET")
    A_REGION: str = os.environ.get("A_REGION")
    A_ACCESS_KEY_ID: str = os.environ.get("A_ACCESS_KEY_ID")
    A_SECRET_ACCESS_KEY: str = os.environ.get("A_SECRET_ACCESS_KEY")


@lru_cache
def get_settings():
    """
    Get settings obj
    """
    return Settings()
