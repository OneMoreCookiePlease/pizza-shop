from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from src.data.models import Food
from src.utils import Tags, get_session

router = APIRouter()


@router.get("/food/all", tags=[Tags.food])
async def get_food(session: Session = Depends(get_session)):
    statement = select(Food)
    result = session.exec(statement).all()
    return result
