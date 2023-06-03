import uvicorn
from fastapi import FastAPI

from src import security
from src.data.database import create_db_and_tables, create_mock_data
from src.routers import food, orders, users, utils

app = FastAPI()

app.include_router(users.router)
app.include_router(food.router)
app.include_router(utils.router)
app.include_router(security.router)
app.include_router(orders.router)


@app.on_event("startup")
async def startup_event():
    create_db_and_tables()
    create_mock_data()


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
