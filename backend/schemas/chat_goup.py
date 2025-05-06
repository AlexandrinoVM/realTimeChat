from pydantic import BaseModel


class ChatGroup(BaseModel):
    id_chat:int
    name:str
