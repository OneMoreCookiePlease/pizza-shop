from datetime import datetime
from typing import List, Optional

from sqlalchemy import Column, DateTime, func
from sqlmodel import Field, Relationship, SQLModel

# from src.data.models.food_item import FoodItem
# from src.data.models.food_order import FoodOrderLink
# from src.data.models.user import User


class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    time_added: datetime = Column(DateTime(timezone=True), onupdate=func.now())
    time_closed: datetime = Field(nullable=True)
    total: int = Field(default=0, nullable=False)
    # courier_id = Field(default=None, foreign_key="courier.id", nullable=True)

    # food_orders: List[FoodItem] = Relationship(back_populates="food", link_model=FoodOrderLink)

    # user: Optional[User] = Relationship(back_populates="orders")
