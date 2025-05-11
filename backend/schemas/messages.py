from pydantic import BaseModel

class Message(BaseModel):
    content:str
    user_id:int
    room_id:int
