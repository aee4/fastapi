from fastapi import FastAPI, Path
from fastapi.params import Query
from typing import Optional # makes the argument optional
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: int
    brand: Optional[str] = None
    

# Initialize a FastAPI app
app = FastAPI()

# HTTP methods:
# GET: Retrieve data
# POST: Create new data (e.g., user signup, login)
# PUT: Update existing data
# DELETE: Remove data

# '@' is a decorator that registers the function as a FastAPI route
# Without '@', app.method() is just a FastAPI method and requires manual registration
@app.get("/")
def home():
    return {"message": "Eyram's FastAPI workout 💪🔥"}

@app.get("/about")
def about():
    return {"message": "SA TA NA MA"}

# Run the app with: uvicorn filename:app --reload

#path parameters 
inventory = {
     1: {
         "name": "Apple",
         "price": 1.00,
         "quantity": 100
     },

     2: {
         "name": "Banana",
         "price": 0.50,
         "quantity": 50
       },

      3: {
          "name": "Orange",
          "price": 1.50,
          "quantity": 75
      } 
}

@app.get("/get-item-by-id/{item_id}")
def get_item(item_id : int = Path(..., description= "ID for the selected item", gt = 0 , lt = 45)):
    return inventory[item_id]

#the path parameters helps to give constraint to the id aside the type

    
  # query parameters
  # by default if the parameter of the fxn is not in the path to the endpoint, it'll be a query parameter  
@app.get("/get-item-by-name")
def get_item(test : int,item_name : Optional[str] = Query( min_length=2, max_length=50, description="Item name to search")):
# the Query() is a function that helps to give constraint to the query parameter
    for item_id in inventory:
        if inventory[item_id]["name"] == item_name:
            return inventory[item_id]
    
    return {"message": "Item not found"}  
#http://127.0.0.1:8000/get-item-by-name?item_name=Banana
#http://127.0.0.1:8000/get-item-by-name?item_name=Banana&test=value --- two query parameters

#request body
@app.post("/create-item")
def create_function(item: Item):
    return {}
