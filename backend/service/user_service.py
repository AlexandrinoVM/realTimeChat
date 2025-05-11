from sqlalchemy.orm import Session
from sqlalchemy import update
from models import UserModel
from backend.schemas import User
from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=['bcrypt'],deprecated='auto')

def Register(user:User,db:Session):
    exist = UserAlreadyExists(user,db)
    if exist:
        return False
    user_db = UserModel(user=user.user,password=bcrypt_context.hash(user.password))
    db.add(user_db)
    db.commit()
    return user_db

def UserAlreadyExists(user:User,db:Session):
    exist = db.query(UserModel).filter(UserModel.user == user.user).first()
    if exist:
        return True
    return False

def Deleteuser(id:int,db:Session):
    user = db.query(UserModel).filter(UserModel.id == id).first()
    if user:
        db.delete(user)
        db.commit()
        return True;
    else:
        return False

def UpdateUser(id:int,user:User,db:Session):
    user_update = user.dict()
    stmt = (update(UserModel).
                where(UserModel.id == id).
                values(**user_update))
    result = db.execute(stmt)
    db.commit()

    return result.rowcount >0
