from sqlalchemy.orm import Session
from sqlalchemy import update
from backend.models import ChatRoomModel
from backend.schemas import ChatGroup

def CreateRoom(chatGroup:ChatGroup,db:Session):
    NewRoom = ChatRoomModel(name=chatGroup.name)

    exists = db.query(ChatRoomModel).filter(ChatRoomModel.name == NewRoom.name).first()

    if exists:
        return False
    else:
        db.add(NewRoom)
        db.commit()
        return True

def DeleteRoom(id:int,db:Session):
    exists = db.query(ChatRoomModel).filter(ChatRoomModel.id == id).first()

    if not exists:
        return False
    else:
        db.delete(exists)
        db.commit()
        return True

def UpdateRoom(id:int,data:ChatGroup,db:Session):
    updateData = data.dict()
    exists = db.query(ChatRoomModel).filter(ChatRoomModel.id == id).first()

    if not exists:
        return False
    else:
        stmt = (update(ChatRoomModel).where(ChatRoomModel.id == id).values(**updateData))
        db.execute(stmt)
        db.commit()
        return True
