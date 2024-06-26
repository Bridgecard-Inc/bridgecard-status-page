from contextlib import AbstractContextManager
import hashlib
from typing import Callable, Optional
from src.database.db import DbSession
from pymongo.collection import Collection
from src.utils import constants
from src.core.error import *
from src.utils.constants import (
    ADMINISTRATOR_DUPLICATE_ERROR_MESSAGE,
    ADMINISTRATOR_FETCH_ERROR_MESSAGE,
    ADMINISTRATOR_SET_ERROR_MESSAGE,
    ADMINISTRATOR_UPDATE_ERROR_MESSAGE,
)

from bson import json_util

from bson import ObjectId


class BaseRepository:
    def __init__(
        self,
        db_session_factory: Callable[..., AbstractContextManager[DbSession]],
        collection_name: str,
    ) -> None:
        with db_session_factory() as db_session:

            self.collection: Collection = db_session.db_client[collection_name]

    def fetch_all(self, context):

        try:
            pipeline = [{"$addFields": {"_id": {"$toString": "$_id"}}}]

            result = list(self.collection.aggregate(pipeline))

            return result

        except Exception as e:

            return None

    def read_by_id(self, id: str, context):
        try:
            data = self.collection.find_one({"_id": id})

            if not data:

                return {}
        
            return data
        
        except Exception as e:

            return None

    def read_attr(self, document_id: str, field: str, context):
        try:
            document = self.collection.find_one({"_id": document_id})
            if document:
                return document.get(field)
            return None
        except Exception as e:
            return ADMINISTRATOR_UPDATE_ERROR_MESSAGE

    def create(self, schema, context, id: Optional[str] = None):
        try:
            obj_in = schema.dict(exclude_none=True)

            obj_in["_id"] = ObjectId(id)

            result = self.collection.insert_one(obj_in)

            new_result = self.collection.find_one({"_id": result.inserted_id})

            return new_result

        except Exception as e:

            return None

    def update(self, id: str, schema, context):
        try:

            obj_in = schema.dict()

            id = ObjectId(hashlib.sha256(id.encode()).hexdigest()[:24])

            document = self.collection.find_one({"_id": id})

            if document:

                self.collection.update_one({"_id": id}, {"$set": obj_in})

            else:

                obj_in["_id"] = ObjectId(id)

                self.collection.insert_one(obj_in)  

            return True
        except Exception as e:
            return None

    # Implement other CRUD operations similarly
    # ...

    def filter_db(self, field: str, value: str, context):
        try:
            documents = self.collection.find({field: value})

            # Convert MongoDB cursor to a list of dictionaries
            dict_data = list(documents)

            if not dict_data:
                return ADMINISTRATOR_FETCH_ERROR_MESSAGE

            return dict_data[0]  # Returning the first document found

        except Exception as e:
            return ADMINISTRATOR_FETCH_ERROR_MESSAGE
