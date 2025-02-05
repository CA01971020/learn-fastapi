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

def find_by_id(id:int):
    for item in items:
        if item.id == id:
            return item
    return None

def find_by_name(name:str):
    filtered_items = []
    for item in items:
        if name in item.name:
            filtered_items.append(item)
    return filtered_items

def create(item_create):
    new_item = Item(
        len(items) + 1,
        item_create.get("name"),
        item_create.get("price"),
        item_create.get("description"),
        ItemStatus.ON_SALE,
    )
    items.append(new_item)
    return(new_item)

def update(id:int, item_update):
    for item in items:
        if item.id == id:
            item.name = item_update.get("name",item.name)
            item.price = item_update.get("price",item.price)
            item.description = item_update.get("description",item.description)
            item.status = item_update.get("status",item.status)
            return item
    return None

def delete(id:int,):
    for i in range(len(items)):
        if items[i].id == id:
            delete_item = items.pop(i)
            return delete_item
    return None