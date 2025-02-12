from enum import Enum
from typing import Optional
from pydantic import BaseModel,Field

# 商品の状態
class ItemStatus(Enum):
    ON_SALE = "ON_SALE"
    SOLD_OUT = "SOLD_OUT"

class ItemCreate(BaseModel):
    name:str  = Field(min_length=2,max_length=20,examples=["商品名"])
    price:int = Field(gt=0,examples=[1000])
    description:Optional[str] = Field(None,examples=["説明"])

class ItemUpdate(BaseModel):
    name:Optional[str] = Field(None,min_length=2,max_length=20,examples=["商品名"])
    price:Optional[int] = Field(None,gt=0, examples=[1000])
    description:Optional[str] = Field(None,examples=["説明"])
    status:Optional[ItemStatus] = Field(None,examples=[ItemStatus.SOLD_OUT])