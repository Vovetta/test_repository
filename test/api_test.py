from collections import Generator

from fastapi.testclient import TestClient
from pytest import fixture


@fixture(scope='module')
def client() -> Generator:
    from app.service import service

    with TestClient(service) as client:
        yield client


def test_first_case(client: TestClient):
    pass
