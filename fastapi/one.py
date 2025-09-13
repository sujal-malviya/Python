from fastapi import FastAPI
from fastapi.param_functions import Body
from pydantic import BaseModel

class Post(BaseModel):
    title:str
    content:str

app = FastAPI()

@app.get("/")
def user():
    return {"message":"hello everyone"}

@app.get("/posts")
def get_users():
    return {"data":"i am the user"}

# in api development here we make api's with the help of http methods like get , put , post , delete.here we use decorator for accessing the path with particular method
 
