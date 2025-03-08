from fastapi import FastAPI

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
    return {"message": "Mimi's FastAPI workout 💪🔥"}

# Run the app with: uvicorn filename:app --reload
