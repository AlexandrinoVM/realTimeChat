from fastapi import APIRouter
from backend.schemas import User
from backend.service import Register,Deleteuser,UpdateUser
from fastapi import HTTPException,Depends
from sqlalchemy.orm import Session
from backend.database import get_db

UserRouter = APIRouter()

@UserRouter.post("/register")
async def RegisterUser(user:User,db: Session = Depends(get_db)):
    Register(user,db)

@UserRouter.delete("/delete/{id}")
async def DeleteUser(id:int,db: Session = Depends(get_db)):
    sucess = Deleteuser(id,db)
    try:
        if not sucess:
            raise HTTPException(status_code=400,detail="User not found")
        return {"message":"user deleted successfully"} 
    except Exception as e:
         raise HTTPException(status_code=500,detail="Could not delete user")

@UserRouter.put("/update/{id}")
async def updateUser(id:int,user:User,db: Session = Depends(get_db)):
    sucess = UpdateUser(id,user,db)
    print(sucess)
    try:
        if not sucess:
            raise HTTPException(status_code=400,detail="User not found")
        return {"message":"user updated with sucess"}
    except Exception as e:
        raise HTTPException(status_code=500,detail="Could not update user")