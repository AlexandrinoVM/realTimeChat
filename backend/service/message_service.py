from sqlalchemy.orm import Session
from sqlalchemy import update
from models import MessageModel
from backend.schemas import Message


def CreateMessage(data:Message,db:Session):
    newMessage = MessageModel(data.content)
    newMessage.user = data.user_id
    newMessage.room = data.room_id

    db.add(newMessage)
    db.commit()
    db.refresh(newMessage)

    return newMessage