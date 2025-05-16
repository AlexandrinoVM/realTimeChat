from fastapi import APIRouter
from backend.schemas import Message
from backend.service import CreateMessage,GetMessages
from fastapi import HTTPException,Depends
from sqlalchemy.orm import Session
from backend.database import get_db

MessageRouter = APIRouter()

@MessageRouter.post("/messages/create")
async def createMessage(data:Message,db:Session = Depends(get_db)):
    messages = CreateMessage(data,db)
    return {"data":{messages}}


@MessageRouter.get("/messages/get/{id}")
async def getMessages(id:int,db:Session = Depends(get_db)):
    messages =await GetMessages(id,db)
    return messages