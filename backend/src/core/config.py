import os
from pathlib import Path
from typing import List

from dotenv import load_dotenv
from pydantic import BaseSettings

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
    superadmin_username: str = os.environ.get("SUPERADMIN_USERNAME", None)
    superadmin_password: str = os.environ.get("SUPERADMIN_PASSWORD", None)
    jwt_secret_key: str = os.environ.get("JWT_SECRET_KEY", None)
    jwt_algorithm: str = os.environ.get("JWT_ALGORITHM", None)
    access_token_expire_minutes: str = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", None)
    
    pass

elif ENVIRONMENT == "DEVELOPMENT" or ENVIRONMENT == "LOCAL":
    """
    set dev environment variables

    """

    db_host: str = os.environ.get("MONGODB_HOST", None)
    db_user: str = os.environ.get("MONGODB_USER", None)
    db_password: str = os.environ.get("MONGODB_PASSWORD", None)
    db_port: str = os.environ.get("MONGODB_PORT", None)
    db_name: str = os.environ.get("MONGODB_DATABASE_NAME", None)
    superadmin_username: str = os.environ.get("SUPERADMIN_USERNAME", None)
    superadmin_password: str = os.environ.get("SUPERADMIN_PASSWORD", None)
    jwt_secret_key: str = os.environ.get("JWT_SECRET_KEY", None)
    jwt_algorithm: str = os.environ.get("JWT_ALGORITHM", None)
    access_token_expire_minutes: str = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", None)

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
    SUPERADMIN_USERNAME: str = superadmin_username
    SUPERADMIN_PASSWORD: str = superadmin_password
    JWT_SECRET_KEY: str = jwt_secret_key
    JWT_ALGORITHM: str = jwt_algorithm
    ACCESS_TOKEN_EXPIRE_MINUTES: int = access_token_expire_minutes
    

    

settings = Settings()
