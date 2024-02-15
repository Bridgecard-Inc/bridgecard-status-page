from contextlib import AbstractContextManager
from typing import Callable
from src.database.db import DbSession
from src.repository.base_repository import BaseRepository


RESOURCES_STATUS_MODEL_NAME = "resources_status"


class ResourceStatusRepository(BaseRepository):
    def __init__(
        self, db_session_factory: Callable[..., AbstractContextManager[DbSession]]
    ):
        super().__init__(db_session_factory, RESOURCES_STATUS_MODEL_NAME)
        
    def update_downtime_id_on_affected_failed_resource_status(
        self, downtime_id, schema, context
    ):

        try:

            schema_dict = schema.dict()

            resource_ids = schema_dict.get("resource_ids")

            start_at = schema_dict.get("start_at")

            end_at = schema_dict.get("end_at")

            self.collection.update_many(
                {
                    "resource_id": {"$in": resource_ids},
                    "monitored_at": {"$gte": start_at, "$lte": end_at},
                    "monitor_success": False,
                },
                {"$set": {"downtime_id": downtime_id}},
            )

            return True

        except:

            return None
