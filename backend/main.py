import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from backend.schemas import *

app = FastAPI()
@app.get("/")
def read_root():
    return {"hellp": "world"}

@app.post("/register")
def register(user:User):
    return user
    