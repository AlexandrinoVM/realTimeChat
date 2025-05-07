from fastapi import APIRouter
from backend.schemas import User


router = APIRouter()

@router.post("/register")
def RegisterUser(user:User):
    return user
    