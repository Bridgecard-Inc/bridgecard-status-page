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

    db_host: str = os.environ.get("MONGODB_HOST", None)
    db_user: str = os.environ.get("MONGODB_USER", None)
    db_password: str = os.environ.get("MONGODB_PASSWORD", None)
    db_port: str = os.environ.get("MONGODB_PORT", None)
    db_name: str = os.environ.get("MONGODB_DATABASE_NAME", None)
    
    pass

elif ENVIRONMENT == "DEVELOPMENT" or ENVIRONMENT == "LOCAL":
    """
    set dev environment variables

    """

    db_host: str = os.environ.get("MONGODB_HOST", None)
    db_user: str = os.environ.get("MONGODB_USER", None)
    db_password: str = os.environ.get("MONGODB_PASSWORD", None)
    db_port: str = os.environ.get("MONGODB_PORT", None)
    db_port: str = os.environ.get("MONGODB_PORT", None)
    db_name: str = os.environ.get("MONGODB_DATABASE_NAME", None)

else:
    pass


class Settings(BaseSettings):
    """
    Set config variables on settings class

    """
    ENVIRONMENT = ENVIRONMENT
    API_TITLE: str = os.environ.get("API_TITLE", "BRIDGECARD MONITORING SERVICE API")
    API_ROOT_PATH: str = os.environ.get("API_ROOT_PATH", "/api")
    DB_HOST: str = db_host
    DB_USER: str = db_user
    DB_PASSWORD: str = db_password
    DB_PORT: int = db_port
    DB_NAME: str = db_name

    

    

settings = Settings()
