from sqlalchemy.orm import relationship
from sqlmodel import Session, SQLModel, create_engine

from src.data.models import Courier, Food, Order, User

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    print("DB created")


def create_mock_data():
    create_mock_food()
    create_mock_user()
    create_mock_courier()


def create_mock_food():
    with Session(engine) as session:
        meal = Food(name="pizza mozzarella", price=15)
        session.add(meal)
        session.commit()


def create_mock_user():
    try:
        with Session(engine) as session:
            user = User(name="bob", password_hash="abc")
            session.add(user)
            session.commit()
    except:
        print("Unique values expected")


def create_mock_courier():
    with Session(engine) as session:
        courier = Courier(name="billy")
        session.add(courier)
        session.commit()
