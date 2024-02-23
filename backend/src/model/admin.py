from enum import Enum
from typing import List, Optional, Any, Dict, Union
import uuid

from pydantic import BaseModel


class AdminIn(BaseModel): 
    
    username: str
    password: str