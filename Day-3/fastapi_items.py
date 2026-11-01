from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class ItemCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0)

class ItemOut(BaseModel):
    id: int
    name: str
    price: float

items = {}

@app.post("/items", response_model=ItemOut, status_code=201)
def create_item(item: ItemCreate):
    item_id = len(items) + 1

    new_item = {
        "id": item_id,
        "name": item.name,
        "price": item.price
    }

    items[item_id] = new_item
    return new_item

@app.get("/items/{item_id}", response_model=ItemOut)
def get_item(item_id: int):
    if item_id <= 0:
        raise HTTPException(
            status_code=400,
            detail="Item ID must be positive"
        )

    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    return items[item_id]

@app.get("/items")
def list_items(limit: int = 20):
    if limit < 1 or limit > 100:
        raise HTTPException(
            status_code=400,
            detail="Limit must be between 1 and 100"
        )

    return list(items.values())[:limit]
