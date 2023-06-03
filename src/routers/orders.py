from collections import Counter
from typing import Annotated, List

from fastapi import APIRouter, Depends, Security
from sqlmodel import Session, select

from src.data.database import get_food_by_id
from src.data.models import Order, User
from src.security import get_current_active_user
from src.utils import Tags, get_session

router = APIRouter()


@router.get("/orders", tags=[Tags.orders])
async def get_orders(
    current_user: Annotated[User, Security(get_current_active_user, scopes=["admin"])],
    session: Session = Depends(get_session),
):
    statement = select(Order)
    return session.exec(statement).all()


@router.post("/orders/new", tags=[Tags.orders])
async def new_order(
    food_id: List[int],
    current_user: Annotated[User, Security(get_current_active_user, scopes=["user"])],
    session: Session = Depends(get_session),
):
    order = Order()
    for meal in food_id:
        order.food.append(get_food_by_id(meal))
    session.add(order)
    session.refresh(order)

    session.commit()
    return "Done"
