from contextlib import AbstractContextManager
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




class BaseRepository:
    def __init__(
        self,
        db_session_factory: Callable[...,  AbstractContextManager[DbSession]],
        collection_name: str,
    ) -> None:
        self.collection: Collection = db_session_factory().db_client[collection_name]

    def read_by_id(self, document_id: str, context):
        try:
            return self.collection.find_one({"_id": document_id})
        except Exception as e:
            return ADMINISTRATOR_FETCH_ERROR_MESSAGE

    def read_attr(self, document_id: str, field: str, context):
        try:
            document = self.collection.find_one({"_id": document_id})
            if document:
                return document.get(field)
            return None
        except Exception as e:
            return ADMINISTRATOR_UPDATE_ERROR_MESSAGE

    def create(self, document_id: str, schema, context):
        try:
            obj_in = schema.dict()

            if self.collection.find_one({"_id": document_id}):
                return ADMINISTRATOR_DUPLICATE_ERROR_MESSAGE

            obj_in["_id"] = document_id
            self.collection.insert_one(obj_in)
            return True
        except Exception as e:
            return ADMINISTRATOR_SET_ERROR_MESSAGE

    def update(self, document_id: str, schema, context):
        try:
            obj_in = schema.dict()

            self.collection.update_one({"_id": document_id}, {"$set": obj_in})
            return True
        except Exception as e:
            return ADMINISTRATOR_UPDATE_ERROR_MESSAGE

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