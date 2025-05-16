from sqlalchemy.orm import Session
from sqlalchemy import update
from models import MessageModel
from backend.schemas import Message


def CreateMessage(data:Message,db:Session):
    newMessage = MessageModel(
        content=data.content,
        user=data.user_id,
        room=data.room_id
    )


    db.add(newMessage)
    db.commit()
    db.refresh(newMessage)

    return newMessage

async def GetMessages(id:int,db:Session):
    messages = db.query(MessageModel).filter(MessageModel.room == id).all()
    return messages