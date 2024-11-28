from fastapi import FastAPI

app = FastAPI () # create api object

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

inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": "Regular"
    }
}

@app.get("/get-item/{item_id}") #based on id return smth, id can be anythinght else
def get_item(item_id: int):
    return inventory[item_id]
