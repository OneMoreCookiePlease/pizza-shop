from typing import List, Optional

from sqlmodel import Field, Relationship, Session, SQLModel, create_engine


class FoodOrderLink(SQLModel, table=True):
    # order_id: Optional[int] = Field(
    #     default=None, foreign_key="order.id", primary_key=True
    # )
    # food_id: Optional[int] = Field(
    #     default=None, foreign_key="food_item.id", primary_key=True
    # )
    quantity: int = Field(default=1, nullable=False)
