from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session
from starlette import status

from src.data.database import engine
from src.data.models import User
from src.security import (ACCESS_TOKEN_EXPIRE_MINUTES, Token,
                          authenticate_user, create_access_token,
                          get_password_hash, get_user)
from src.utils import Tags

router = APIRouter()


@router.post("/token", response_model=Token, tags=[Tags.utils])
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.name}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/register", tags=[Tags.utils])
async def register(username: str, password: str):
    if get_user(username):
        return "User already exists in DB"

    with Session(engine) as session:
        user = User(name=username, password_hash=get_password_hash(password))
        session.add(user)
        session.commit()
    return "User has been registered"


@router.get("/utils/", tags=[Tags.utils])
async def hello_world():
    return {"message": "Hello World"}
