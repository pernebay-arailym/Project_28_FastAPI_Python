from fastapi import FastAPI

app = FastAPI () # create api object

# GET GET AND RETURN SMTH
# POST SEND INFO TO THE POST/ADDING NEW USER
# PUT 
# DELETE

@app.get("/") # define root
def home(): # created function
    return  {"Data": "Testing"} #python info - data

@app.get("/about")
def about():
    return {"Data": "About"}