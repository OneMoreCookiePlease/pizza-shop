from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel

# from src.data.models.order import Order
# from src.data.models.food_order import FoodOrderLink


class FoodItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: int = Field(default=0)

    # food_orders: List[Order] = Relationship(back_populates="orders", link_model=FoodOrderLink)
