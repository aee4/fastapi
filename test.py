from fastapi import FastAPI

#Initializes a new FastAPI app.
app = FastAPI()

#http methods : get, post, put, delete...

#get method returns data
#post method creates new data ; user login , user signup 
#put method modifies the data 
#delete method deletes the data


# without '@' app.method() is just a fastapi method
#@ is a decorator that registers the fxn as a route in FastApi
#it can be done manually but thats extra code
#the function another the endpoint determines what should happen
@app.get("/")
def home():
    return {"message": "mimi's fastapi workout"}

#to run this : uvicorn filename: app --reload
 