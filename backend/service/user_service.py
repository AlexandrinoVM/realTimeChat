from sqlalchemy.orm import Session
from backend.models import UserModel
from backend.schemas import User

def Register(user:User,db:Session):
    user_db = UserModel(**user.dict())
    db.add(user_db)
    db.commit()
    db.close()

def DeleteUser(id:int,db:Session):
    user = db.query(UserModel).filter(UserModel.id == id).first()
    if user:
        db.delete(user)
        db.commit()
        return True;
    else:
        return False