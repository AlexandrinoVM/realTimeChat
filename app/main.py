from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    user:str
    age: int
    password:str


@app.get("/")
def read_root():
    return {"hellp": "world"}

@app.post("/register")
async def register(user:User):
    return user
    