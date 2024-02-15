from contextlib import AbstractContextManager
from typing import Callable
from src.database.db import DbSession
from src.repository.base_repository import BaseRepository


RESOURCES_MODEL_NAME = "resources"


class ResourceRepository(BaseRepository):
    def __init__(
        self, db_session_factory: Callable[..., AbstractContextManager[DbSession]]
    ):
        super().__init__(db_session_factory, RESOURCES_MODEL_NAME)

    def fetch_all(self, context):
        try:
            pipeline = [
                {
                    "$lookup": {
                        "from": "resources_status",
                        "let": {"resourceId": {"$toString": "$_id"}},
                        "pipeline": [
                            {
                                "$match": {
                                    "$expr": {"$eq": ["$resource_id", "$$resourceId"]}
                                }
                            }
                        ],
                        "as": "status",
                    }
                },
                {
                    "$addFields": {
                        "_id": {"$toString": "$_id"},
                        "status": {
                            "$map": {
                                "input": "$status",
                                "as": "stat",
                                "in": {
                                    "_id": {"$toString": "$$stat._id"},
                                    "resource_id": "$$stat.resource_id",
                                    "monitored_at": "$$stat.monitored_at",
                                    "monitor_success": "$$stat.monitor_success",
                                    "downtime_id": "$$stat.downtime_id",
                                },
                            }
                        },
                    }
                },
            ]

            resources_with_statuses = list(self.collection.aggregate(pipeline))

            return resources_with_statuses

        except Exception as e:

            return None
