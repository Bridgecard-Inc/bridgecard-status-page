from enum import Enum
from typing import List, Optional
import uuid

from pydantic import BaseModel

class API_TO_MONITOR(BaseModel): 
    api_id: Optional[str] = uuid.uuid4().hex
    api_url: str