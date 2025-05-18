import os
from dotenv import load_dotenv
from datetime import timedelta,datetime
from typing import Annotated
from fastapi import APIRouter,Depends,HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from database import get_db
from backend.schemas import User,Token
from backend.models import UserModel
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from jose import jwt,JWTError

load_dotenv()

AuthRouter = APIRouter(
    prefix='/auth',
    tags=['auth']
)

SECRET_KEY=os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')

bcrypt_context = CryptContext(schemes=['bcrypt'],deprecated='auto')
oauth2_barear = OAuth2PasswordBearer(tokenUrl='auth/token')

#db_dependency= Annotated(Session,Depends(get_db))

@AuthRouter.post('/token')
async def login_for_acess_token(form_data:Annotated[OAuth2PasswordRequestForm,Depends()],db:Annotated[Session,Depends(get_db)]):
    user = authenticate_user(form_data.username,form_data.password,db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Could not validate user')
    token = create_acess_token(user.user,user.id,timedelta(minutes=20))

    return {'access_token':token,'token_type':'bearer'}

def authenticate_user(username:str,password:str,db):
    user = db.query(UserModel).filter(UserModel.user == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password,user.password):
        return False
    return user

def create_acess_token(username:str,user_id:int,expires_date:timedelta):
    encode = {'sub':username,'id':user_id}
    exprires = datetime.utcnow() + expires_date
    encode.update({'exp':exprires})
    return jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)

async def get_curr_user(token:Annotated[str,Depends(oauth2_barear)]):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username:str = payload.get('sub')
        user_id:str = payload.get('id')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Could not validate user')
        return {'username':username,'id':user_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Could not validate user')

