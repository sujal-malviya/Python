from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")

items = []

class Item(BaseModel):
    name:str
    description:str
    
    
@app.post("\items/",response_model=Item)

def create_item(item:Item):
    items.append(item)
    return item