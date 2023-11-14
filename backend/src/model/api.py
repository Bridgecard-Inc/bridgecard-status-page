from enum import Enum
from typing import List, Optional
import uuid

from pydantic import BaseModel

class APITOMONITOR(BaseModel): 
    api_id: Optional[str] = uuid.uuid4().hex
    api_url: str