# It is absolutely a bad idea to put all the models in 1 file,
# but doing otherwise is very error-prone from SQLMODEL side.
# Namely, the actual need for circular import if you want to do many-to-many tables.


from datetime import datetime
from typing import List, Optional

from sqlalchemy import Column, DateTime, func
from sqlmodel import Field, Relationship, SQLModel


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    address: Optional[str] = None
    password_hash: str = Field(default=None, unique=True)

    orders: list["Order"] = Relationship(back_populates="user")


class Courier(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    orders: list["Order"] = Relationship(back_populates="courier")


class FoodOrderLink(SQLModel, table=True):
    order_id: Optional[int] = Field(
        default=None, foreign_key="order.id", primary_key=True
    )
    food_id: Optional[int] = Field(
        default=None, foreign_key="food.id", primary_key=True
    )


class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    time_added: datetime = Column(DateTime(timezone=True), onupdate=func.now())
    time_closed: datetime = Field(nullable=True)
    total: int = Field(default=0, nullable=False)

    courier_id: Optional[int] = Field(default=None, foreign_key="courier.id")
    courier: Optional[Courier] = Relationship(back_populates="orders")

    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    user: Optional[User] = Relationship(back_populates="orders")

    food: List["Food"] = Relationship(back_populates="orders", link_model=FoodOrderLink)


class Food(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    orders: List[Order] = Relationship(back_populates="food", link_model=FoodOrderLink)
