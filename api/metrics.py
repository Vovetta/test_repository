from typing import List

from fastapi import APIRouter
from tortoise.functions import Max

from app.models import Model

metrics_router = APIRouter(
    prefix='/metrics'
)


@metrics_router.get('/', response_model=List)
async def temp(limit: int = 10, offset: int = 0) -> List:
    """"""
    pass

