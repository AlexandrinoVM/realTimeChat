from fastapi import APIRouter
from backend.schemas import ChatGroup
from backend.service import CreateRoom,DeleteRoom,UpdateRoom,GetRooms
from fastapi import HTTPException,Depends,status
from sqlalchemy.orm import Session
from backend.database import get_db
from .auth import get_curr_user
RoomRouter = APIRouter()

@RoomRouter.post("/room/create")
async def createRoom(chatGroup:ChatGroup,userlog:dict =Depends(get_curr_user),db:Session = Depends(get_db)):
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

@RoomRouter.get('/room/get')
async def get_rooms(db:Session = Depends(get_db)):
    rooms =await GetRooms(db)
    return rooms
