from contextlib import AbstractContextManager
from typing import Callable
from src.database.db import DbSession
from src.repository.base_repository import BaseRepository


ADMINS_MODEL_NAME = "admins"


class AdminRepository(BaseRepository):
    def __init__(
        self, db_session_factory: Callable[..., AbstractContextManager[DbSession]]
    ):
        super().__init__(db_session_factory, ADMINS_MODEL_NAME)
