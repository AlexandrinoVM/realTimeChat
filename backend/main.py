import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)

from backend.database import Base,db
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from backend.router import router
import backend.models 

Base.metadata.create_all(bind=db)

app = FastAPI()
@app.get("/")
def read_root():
    return {"hellp": "world"}

app.include_router(router)
    