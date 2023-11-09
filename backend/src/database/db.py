from contextlib import AbstractContextManager, contextmanager
from typing import Any, Callable
import firebase_admin
from firebase_admin import db, credentials
from src.core.config import Settings
from src.utils.decode_base_64_to_json_helper import decode_base_64_to_json
from src.core.config import settings
from pydantic import BaseModel


class DbSession(BaseModel):
    admin_db_app: Any


class Database:
    def __init__(self, config: Settings) -> None:
        self._cred = credentials.Certificate(
            decode_base_64_to_json(config.GOOGLE_CONFIG_BASE64)
        )
        self._firebase_app = firebase_admin.initialize_app(
            self._cred,
            {
                "databaseURL": settings.DATABASE_URL,
                "storageBucket": settings.STORAGE_BUCKET_URL,
            },
        )
        self._admin_db_app = firebase_admin.initialize_app(
            self._cred,
            {"databaseURL": settings.ADMIN_DATABASE_URL},
            name="admin_db_app",
        )

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[DbSession]]:
        db_session = DbSession(admin_db_app=self._admin_db_app)
        try:
            yield db_session
        except Exception:
            # Handle exceptions and cleanup if needed
            raise
        finally:
            # Perform cleanup actions here if needed
            ...
