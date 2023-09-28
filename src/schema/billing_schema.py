

from typing import Optional
from pydantic import BaseModel


class CheckAdminBillStatus(BaseModel):
    token: str
    bill_type: str
    description: Optional[str] = None
    long_address: str
    latitude: float
    longitude: float



class FetchAllBusiness(BaseModel):
    page: int
    page_size: int

class FetchBusinessById(BaseModel):
    id: str


class UpdateBusiness(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    long_address: str
    latitude: float
    longitude: float


class DeleteBusinessById(BaseModel):
    id: str