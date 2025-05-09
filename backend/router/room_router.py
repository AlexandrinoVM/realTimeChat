from fastapi import APIRouter
from backend.schemas import ChatGroup
from backend.service import Register,Deleteuser,UpdateUser,CreateRoom
from fastapi import HTTPException,Depends
from sqlalchemy.orm import Session
from backend.database import get_db

RoomRouter = APIRouter()

@RoomRouter.post("/create")
async def createRoom(chatGroup:ChatGroup,db:Session = Depends(get_db)):
    result = CreateRoom(chatGroup,db)
    if not result:
        raise HTTPException(status_code=400,detail="User already existis")
    return {"message":"user created with sucess"}

