from fastapi import APIRouter
from backend.schemas import ChatGroup
from backend.service import CreateRoom,DeleteRoom,UpdateRoom
from fastapi import HTTPException,Depends
from sqlalchemy.orm import Session
from backend.database import get_db

RoomRouter = APIRouter()

@RoomRouter.post("/create")
async def createRoom(chatGroup:ChatGroup,db:Session = Depends(get_db)):
    result = CreateRoom(chatGroup,db)
    if not result:
        raise HTTPException(status_code=400,detail="Chat Room already existis")
    return {"message":"Room created with sucess"}

@RoomRouter.delete("/room/delete/{id}")
async def deleteRoom(id:int,db:Session = Depends(get_db)):
    result = DeleteRoom(id,db)
    if not result:
        raise HTTPException(status_code=400,detail="Chat Room Does not Exists or wrong id")
    return {"message":"Room deleted with sucess"}

@RoomRouter.put("/room/update/{id}")
async def udpateRoom(id:int,data:ChatGroup,db:Session = Depends(get_db)):
    result = UpdateRoom(id,data,db)
    if not result:
        raise HTTPException(status_code=400,detail="Chat Room Does not Exists or wrong id")
    return {"message":"Room updated with sucess"}


