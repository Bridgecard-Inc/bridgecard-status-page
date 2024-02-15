from contextlib import AbstractContextManager, contextmanager
from typing import Any, Callable
from pymongo import MongoClient
from src.core.config import Settings
from src.core.config import settings
from pydantic import BaseModel
from urllib.parse import quote_plus


class DbSession(BaseModel):
    db_client: Any


class Database:

    def __init__(self, config: Settings) -> None:

        endpoint = 'mongodb://{0}:{1}@{2}'.format(quote_plus(config.DB_USER),
                                              quote_plus(config.DB_PASSWORD), config.DB_HOST)

        db_client = MongoClient(endpoint, config.DB_PORT)

        self.db_client = db_client[config.DB_NAME]


    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[DbSession]]: # type: ignore
        db_session = DbSession(db_client=self.db_client)
        try:
            yield db_session
        except Exception:
            # Handle exceptions and cleanup if needed
            raise
        finally:
            # Perform cleanup actions here if needed
            ...
