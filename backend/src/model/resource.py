from enum import Enum
from typing import Optional, Any, Dict, Union
import uuid

from pydantic import BaseModel


class ApiMethod(str, Enum):
    POST = "POST"
    GET = "GET"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"

class ResourceIn(BaseModel): 
    
    tag: str
    title: str
    url: str
    api_method: Optional[ApiMethod]
    expected_response_status_code: int