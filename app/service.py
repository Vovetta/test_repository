from urllib.parse import urlencode

from fastapi import FastAPI
from fastapi.requests import Request
from tortoise.contrib.fastapi import register_tortoise

from api import routers
from config import Sqlite, Service

service = FastAPI(debug=Service.debug)

for router in routers:
    service.include_router(router)


@service.middleware("http")
async def query_string_to_list(request: Request, call_next):
    flattened = []
    for key, value in request.query_params.multi_items():
        flattened.extend((key, entry) for entry in value.split(','))

    request.scope["query_string"] = urlencode(flattened, doseq=True).encode("utf-8")
    return await call_next(request)

register_tortoise(
    service,
    db_url=f'sqlite://{Sqlite.database}',
    modules={'models': ['app.orm_models']}
)
