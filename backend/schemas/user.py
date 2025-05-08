from pydantic import BaseModel
from typing import Union

class User(BaseModel):
    user:str
    password:str
