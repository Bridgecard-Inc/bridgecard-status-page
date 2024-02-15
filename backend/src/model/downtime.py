from enum import Enum
from typing import List, Optional, Any, Dict, Union
import uuid

from pydantic import BaseModel


class DowntimeIn(BaseModel): 
    
    resource_ids: List[str]
    title: str
    description: str
    start_at: int
    end_at: int