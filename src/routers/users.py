from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from src.data.models import User
from src.utils import Tags, get_session

router = APIRouter()


@router.get("/users/all", tags=[Tags.users])
async def get_users(session: Session = Depends(get_session)):
    statement = select(User)
    result = session.exec(statement).all()
    return result
