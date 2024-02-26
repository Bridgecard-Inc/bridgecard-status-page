from contextlib import AbstractContextManager
import hashlib
from typing import Callable
from bson import ObjectId
from src.database.db import DbSession
from src.repository.base_repository import BaseRepository


ADMINS_MODEL_NAME = "admins"


class AdminRepository(BaseRepository):
    def __init__(
        self, db_session_factory: Callable[..., AbstractContextManager[DbSession]]
    ):
        super().__init__(db_session_factory, ADMINS_MODEL_NAME)

    def read_admin_by_id(self, id: str, context):
        try:
            id = ObjectId(hashlib.sha256(id.encode()).hexdigest()[:24])

            data = self.collection.find_one({"_id": id})

            if not data:

                return {}

            data["_id"] = str(data["_id"])

            return data

        except Exception as e:

            return None
