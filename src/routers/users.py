from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session, select

from src.data.models import User
from src.security import oauth2_scheme
from src.utils import Tags, get_session

router = APIRouter()


@router.get("/users/all", tags=[Tags.users])
async def get_users(
    token: Annotated[str, Depends(oauth2_scheme)],
    session: Session = Depends(get_session),
):
    statement = select(User)
    result = session.exec(statement).all()
    return result
