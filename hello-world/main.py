from fastapi import FastAPI
from models import Item

items ={
    1: {"id": 1, "name": "Apple", "description": "Apple is a sweet, edible fruit produced by an apple tree."},
    2: {"id": 2, "name": "Banana", "description": "Banana is a long, curved fruit with a yellow skin and soft, creamy flesh."},
    3: {"id": 3, "name": "Cherry", "description": "Cherry is a small, round fruit with a hard pit in the center."},
}

app = FastAPI()

@app.get("/", 
         summary="My Hello World Endpoint", 
         description="Returns a simple Hello World message",
         responses={200: {"description": "A simple Hello World message"}},
         tags=["Static Endpoints"])
def helloWorld():
    return {"message": "Hello World"}

@app.get("/items", 
         summary="Get Items", 
         description="Returns a list of items",
         responses={200: {"description": "A list of items"}},
         tags=["Item Endpoints"])
def getItems():
    return list(items.values())

@app.get("/items/{item_id}",
            summary="Get Item by ID", 
            description="Returns an item by its ID",
            responses={200: {"description": "An item"}, 404: {"description": "Item not found"}},
            tags=["Item Endpoints"])
def getItemById(item_id: int):
    item = items.get(item_id)
    if item:
        return item
    return {"error": "Item not found"}

@app.post("/items",
          summary="Add Item",
          description="Adds a new item",
          responses={200: {"description": "The added item"}, 400: {"description": "Invalid item data"}},
          tags=["Item Endpoints"])
def addItem(item: Item):
    item_id = max(items.keys()) + 1 if items else 1
    if item_id in items:
        return {"error": "Item ID already exists"}
    items[item_id] = {"id": item_id, "name": item.name, "description": item.description}
    return items[item_id]

@app.put("/items/{item_id}",
         summary="Update Item",
         description="Updates an existing item",
         responses={200: {"description": "The updated item"}, 404: {"description": "Item not found"}},
         tags=["Item Endpoints"])
def updateItem(item_id: int, item: Item):
    existing_item = items.get(item_id)
    if existing_item:
        items[item_id] = {"id": item_id, "name": item.name, "description": item.description}
        return items[item_id]
    return {"error": "Item not found"}

@app.delete("/items/{item_id}",
            summary="Delete Item",
            description="Deletes an item by its ID",
            responses={200: {"description": "Item deleted"}, 404: {"description": "Item not found"}},
            tags=["Item Endpoints"])
def deleteItem(item_id: int):
    if item_id in items:
        del items[item_id]
        return {"message": "Item deleted"}
    return {"error": "Item not found"}