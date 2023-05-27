from typing import Optional

from sqlmodel import Field, SQLModel, create_engine


class Courier(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
