from pydantic import BaseModel
from typing import Union

class User(BaseModel):
    name:str
    user:str
    password:str
