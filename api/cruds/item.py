from enum import Enum
from typing import Optional

# 商品の状態
class ItemStatus(Enum):
    ON_SALE = "ON_SALE"
    SOLD_OUT = "SOLD_OUT"

# 商品のクラス
class Item:
    def __init__(
        self,
        id:int,
        name:str,
        price:int,
        description:Optional[str],
        status:ItemStatus
    ):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.status = status

# 商品の定義
items = [
    Item(1,"PC",108000,"在庫処分",ItemStatus.ON_SALE),
    Item(2,"スマートフォン",68000,None,ItemStatus.ON_SALE),
    Item(3,"Python入門書",1000,"中古品",ItemStatus.SOLD_OUT)
]

# 全ての商品を取得する関数
def find_all():
    return items