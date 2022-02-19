from typing import List

from fastapi import APIRouter

from api.metrics import metrics_router

routers: List[APIRouter] = [
    metrics_router
]
