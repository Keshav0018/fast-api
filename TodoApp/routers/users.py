from fastapi import APIRouter,Depends,HTTPException,Path
from typing import Annotated

from passlib.context import CryptContext
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import current_user

from ..models import Todos
from ..models import User
from starlette import status
from pydantic import BaseModel,Field
from .auth import get_current_user


from ..database import engine,SessionLocal



router = APIRouter(prefix="/user",tags=["user"])

class ChangePasswordRequest(BaseModel):
    password: str
    new_password: str

class ChangePhoneNumber(BaseModel):
    phone_number: str



def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()



db_dependency =  Annotated[Session,Depends(get_db)]
user_dependency = Annotated[dict,Depends(get_current_user)]
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.get("/",status_code=status.HTTP_200_OK)
async def get_user(user:user_dependency,db:db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Not authenticated")
    return db.query(User).filter(User.id == user['id']).first()

@router.put("/change_password", status_code=status.HTTP_200_OK)
async def change_password(
    user: user_dependency,
    db: db_dependency,
    request: ChangePasswordRequest
):
    if user is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)




    user_model = db.query(User).filter(User.id == user["id"]).first()

    if not user_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    if not bcrypt_context.verify(request.password, user_model.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Incorrect password")


    user_model.hashed_password = bcrypt_context.hash(request.new_password)
    db.commit()

    return {"detail": "Password updated successfully"}


@router.put("/change_phone_number", status_code=status.HTTP_200_OK)
async def update_phone_number(user: user_dependency,db: db_dependency,req: ChangePhoneNumber):
    if user is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

    user_model = db.query(User).filter(User.id == user["id"]).first()
    if not user_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    user_model.phone_number = req.phone_number
    db.commit()
    return user_model.phone_number