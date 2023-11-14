import os
from pathlib import Path
from typing import List

from dotenv import load_dotenv
from pydantic import BaseSettings, AnyHttpUrl
from pydantic.networks import EmailStr

path = Path.cwd()

env_path = path / ".env"

load_dotenv(dotenv_path=env_path)

ENVIRONMENT = os.environ.get("ENVIRONMENT", "DEVELOPMENT")


if ENVIRONMENT == "PRODUCTION":
    """
    set prod environment variables

    """
    database_url: str = os.environ.get("DATABASE_URL", None)
    storage_bucket_url: str = os.environ.get("STORAGE_BUCKET_URL", None)
    google_config_base64 = os.environ.get("GOOGLE_CONFIG_BASE64", None)
    firebase_web_api_key = os.environ.get("FIREBASE_WEB_API_KEY", None)
    admin_database_url: str = os.environ.get("ADMIN_DATABASE_URL", None)
    bridgecard_issuing_live_authorization_token: str = os.environ.get("BRIDGECARD_ISSUING_LIVE_AUTHORIZATION_TOKEN", None)
    db_host: str = os.environ.get("MONGODB_HOST", None)
    db_user: str = os.environ.get("MONGODB_USER", None)
    db_password: str = os.environ.get("MONGODB_PASSWORD", None)
    db_port: str = os.environ.get("MONGODB_PORT", None)
    
    pass

elif ENVIRONMENT == "DEVELOPMENT" or ENVIRONMENT == "LOCAL":
    """
    set dev environment variables

    """
    database_url: str = os.environ.get("DATABASE_URL", None)
    storage_bucket_url: str = os.environ.get("STORAGE_BUCKET_URL", None)
    google_config_base64 = os.environ.get("GOOGLE_CONFIG_BASE64", None)
    firebase_web_api_key = os.environ.get("FIREBASE_WEB_API_KEY", None)
    admin_database_url: str = os.environ.get("ADMIN_DATABASE_URL", None)
    bridgecard_issuing_live_authorization_token: str = os.environ.get("BRIDGECARD_ISSUING_LIVE_AUTHORIZATION_TOKEN", None)
    db_host: str = os.environ.get("MONGODB_HOST", None)
    db_user: str = os.environ.get("MONGODB_USER", None)
    db_password: str = os.environ.get("MONGODB_PASSWORD", None)
    db_port: str = os.environ.get("MONGODB_PORT", None)

else:
    pass


class Settings(BaseSettings):
    """
    Set config variables on settings class

    """
    ENVIRONMENT = ENVIRONMENT
    API_TITLE: str = os.environ.get("API_TITLE", "BRIDGECARD MONITORING SERVICE API")
    API_ROOT_PATH: str = os.environ.get("API_ROOT_PATH", "/api")
    DATABASE_URL: str = database_url
    GOOGLE_CONFIG_BASE64: str = google_config_base64
    FIREBASE_WEB_API_KEY: str = firebase_web_api_key
    ADMIN_DATABASE_URL: str = admin_database_url
    STORAGE_BUCKET_URL: str = storage_bucket_url
    BRIDGECARD_ISSUING_LIVE_AUTHORIZATION_TOKEN: str = bridgecard_issuing_live_authorization_token
    DB_HOST: str = db_host
    DB_USER: str = db_user
    DB_PASSWORD: str = db_password
    DB_PORT: str = db_port

    

    

settings = Settings()
