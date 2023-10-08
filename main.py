from enum import Enum
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

# deprecated=True
@app.get("/", description="This is our first route.")
async def base_get_router():
    return {"message": "[GET] Hello, world!"}

@app.post("/")
async def post():
    return {"message": "[POST] Hello, world!"}

@app.put("/")
async def put():
    return {"message": "[PUT] Hello, world!"}

@app.get("/users")
async def list_users():
    return {"message": "list users router"}

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}

@app.get("/users/me")
async def get_current_user():
    return {"message": "this is current user"}

class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"
    
@app.get("/foods/{food_nme}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "you are healthy"}
    
    if food_name == "fruits":
        return {
            "food_name": food_name,
            "message": "you are still healthy, but like sweet things",
        }

    return {"food_name": food_name, "message": "i like chocolate milk"}

fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"},
]

@app.get("/items")
async def list_items(skip: int=0, limit: int=10):
    return fake_items_db[skip: skip + limit]

@app.get("/items/{item_id}")
async def get_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "Chi co 2 thu ma thoi...!"}
        )
        
    return item

@app.get("/users/{user_id}/items/{item_id}")
async def get_user_item(user_id: str, item_id: str, q: str | None = None, short: bool=False):
    item = {"item_id": item_id, "owner_id": user_id}
    
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {
                "description": "Chi co 2 thu ma thoi...!"
            }
        )
        
