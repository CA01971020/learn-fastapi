from typing import Optional
from api.schemas import ItemCreate,ItemStatus,ItemUpdate

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

def create(item_create:ItemCreate):
    new_item = Item(
        len(items) + 1,
        item_create.name,
        item_create.price,
        item_create.description,
        ItemStatus.ON_SALE,
    )
    items.append(new_item)
    return(new_item)

def update(id:int, item_update:ItemUpdate):
    for item in items:
        if item.id == id:
            item.name = item.name if item_update.name is None else item_update.name
            item.price = item.price if item_update.price is None else item_update.price
            item.description = item.description if item_update.description is None else item_update.description
            item.status = item.status if item_update.status is None else item_update.status
            return item
    return None

def delete(id:int,):
    for i in range(len(items)):
        if items[i].id == id:
            delete_item = items.pop(i)
            return delete_item
    return None