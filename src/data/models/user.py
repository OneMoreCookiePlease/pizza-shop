from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel

# from src.data.models.order import Order


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    address: Optional[str] = None
    password_hast: str = Field(default=None, unique=True)

    # orders: List[Order] = Relationship(back_populates="user")
