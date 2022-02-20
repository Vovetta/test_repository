from asyncio import run
from typing import cast

from hypercorn.asyncio import serve, Config
from hypercorn.typing import ASGI3Framework

from app.service import service
from config import Service


def create_config() -> Config:
    """
    Creating configuration for Hypercorn from Service configuration

    :return: Hypercorn configuration
    """
    config = Config()

    config.bind = [f'{Service.host}:{Service.port}']
    config.accesslog = '-'
    config.errorlog = '-'

    return config


if __name__ == '__main__':
    run(serve(cast(ASGI3Framework, service), config=create_config()))
