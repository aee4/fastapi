from fastapi import FastAPI, Path

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

@app.get("/get-item/{item_id}")
def get_item(item_id : int = Path(..., description= "ID for the selected item", gt = 0 , lt = 45)):
    return inventory[item_id]

#the path parameters helps to give constraint to the id aside the type

    
  # query parameters  
