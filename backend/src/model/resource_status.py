from enum import Enum
from typing import Optional, Any, Dict, Union
import uuid

from pydantic import BaseModel

class ResourceStatusIn(BaseModel): 
    
    resource_id: str
    monitored_at: int
    monitor_success: bool