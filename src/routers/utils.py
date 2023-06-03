from fastapi import APIRouter

from src.utils import Tags

router = APIRouter()


@router.get("/utils/", tags=[Tags.utils])
async def hello_world():
    return {"message": "Hello World"}
