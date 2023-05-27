from sqlmodel import SQLModel, create_engine

from src.data.models.courier import Courier
from src.data.models.food_item import FoodItem
from src.data.models.food_order import FoodOrderLink
from src.data.models.order import Order
from src.data.models.user import User

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    print("DB created")
