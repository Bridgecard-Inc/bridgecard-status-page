
from enum import Enum
from typing import List, Optional
import uuid

from pydantic import BaseModel


class RewardType(str, Enum):
    DEAL = "DEAL"
    PROMO_CODE = "PROMO_CODE"


class DEAL(BaseModel):
    reward_id: Optional[str] = uuid.uuid4().hex
    reward_type: RewardType
    product_images: List[str]
    old_price: str
    new_price: str
    currency: str
    product_name: str
    discount: str
    merchant: str
    description: str
    product_link: Optional[str]
    success_record: int
    is_available: bool
    upvotes: Optional[int] = 0
    downvotes: Optional[int] = 0
    coupon_code: str
    created_on: str
    valid_till: int
    valid_till_date: str


class PROMO_CODE(BaseModel):
    reward_id: Optional[str] = uuid.uuid4().hex
    reward_type: RewardType
    coupon_code: str
    description: str
    merchant: str
    created_on: str
    valid_till: int
    valid_till_date: str
    success_record: int
    is_available: bool
    upvotes: Optional[int] = 0
    downvotes: Optional[int] = 0
    product_link: Optional[str]

    
class UploadReward(BaseModel):
    reward_id: Optional[str] = uuid.uuid4().hex
    reward_type: RewardType
    DEAL: Optional[DEAL]
    PROMO_CODE: Optional[PROMO_CODE]