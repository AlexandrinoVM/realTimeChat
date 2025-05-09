from sqlalchemy.orm import Session
from sqlalchemy import update
from backend.models import ChatRoomModel
from backend.schemas import ChatGroup

def CreateRoom(chatGroup:ChatGroup,db:Session):
    NewRoom = ChatRoomModel(**chatGroup.dict())

    exists = db.query(ChatRoomModel).filter(ChatRoomModel.name == NewRoom.name).first()

    if exists:
        return False
    else:
        db.add(NewRoom)
        db.commit()
        return True