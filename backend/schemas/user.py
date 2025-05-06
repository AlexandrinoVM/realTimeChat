from pydantic import BaseModel
from typing import Union
from backend.teste import calc 

class User(BaseModel):
    name:str
    user:str
    password:str
