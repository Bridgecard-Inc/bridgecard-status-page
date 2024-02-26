from enum import Enum
from typing import List, Optional, Any, Dict, Union
import uuid

from pydantic import BaseModel


class AdminIn(BaseModel):

    username: str
    password: str


class AdminSettingsIn(BaseModel):

    company_name: str
    company_accent_color: str
    company_logo_url: str
