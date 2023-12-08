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

class APITOMONITOR(BaseModel): 
    
    api_url: str
    api_method: Optional[ApiMethod]