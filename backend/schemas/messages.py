from pydantic import BaseModel

class Message(BaseModel):
    content:str
    user_id:str
    room_id:str
