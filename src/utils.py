from enum import Enum

from sqlmodel import Session

from src.data.database import engine


def get_session():
    with Session(engine) as session:
        yield session


class Tags(Enum):
    food = "food"
    users = "users"
    orders = "orders"
    couriers = "couriers"
    utils = "utils"
    security = "security"
