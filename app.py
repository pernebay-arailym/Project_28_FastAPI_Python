from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI () # create api object

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str]=None

# GET GET AND RETURN SMTH

#@app.get("/") # define root
#def home(): # created function
#    return  {"Data": "Testing"} #python info - data

#@app.get("/about")
#def about():
#    return {"Data": "About"}

# POST SEND INFO TO THE POST/ADDING NEW USER
# PUT 
# DELETE

inventory = {}

@app.get("/get-item/{item_id}") #based on id return smth, id can be anythinght else
def get_item(item_id: int = Path(..., description="The ID of the item you would like to view")): #path-info for item id
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(name: str=Query(None, title="Name", description="Name of item.", max_length=50)):
    for item_id in inventory:
        if inventory[item_id].name== name:
            return inventory[item_id]
    return {"Data": "Not found"}

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists."}
    
    inventory[item_id]= item #{"name": item.name, "brand": item.brand, "price": item.price}
    return inventory[item_id]
