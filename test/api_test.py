from datetime import date
from typing import Generator

from fastapi.testclient import TestClient
from pytest import fixture

from app.service import service


@fixture(scope='module')
def client() -> Generator:
    with TestClient(service) as client:
        yield client


def test_query_params(client: TestClient):
    response_first = client.get('/metrics?columns=id&columns=channel&columns=country').json()
    response_second = client.get('/metrics?columns=id,channel,country').json()
    assert response_first == response_second, 'Query parameter lists parsing'


def test_columns(client: TestClient):
    response = client.get('/metrics?columns=id,channel,country').json()
    metric_keys = tuple(response[0].keys())
    assert metric_keys == ('id', 'channel', 'country'), 'Returning selected columns'


def test_filter(client: TestClient):
    response = client.get('/metrics?country=US&columns=country').json()
    assert all(metric['country'] == 'US' for metric in response), 'Filtering by exact value'

    response = client.get('/metrics?country=US,CA&columns=country').json()
    assert all(metric['country'] in ('US', 'CA') for metric in response), 'Filtering by list of values'

    response = client.get('/metrics?date_from=2017-05-25&columns=date').json()
    date_from = date.fromisoformat('2017-05-25')
    assert all(
        date.fromisoformat(metric['date']) >= date_from
        for metric in response
    ), 'Filtering by date_from'

    response = client.get('/metrics?date_to=2017-06-10&columns=date').json()
    date_to = date.fromisoformat('2017-06-10')
    assert all(
        date.fromisoformat(metric['date']) <= date_to
        for metric in response
    ), 'Filtering by date_to'

    response = client.get('/metrics?date_from=2017-05-25&date_to=2017-06-10&columns=date').json()
    assert all(
        date_from <= date.fromisoformat(metric['date']) <= date_to
        for metric in response
    ), 'Filtering by date range'


def test_group_by(client: TestClient):
    response = client.get('/metrics?group_by=country&columns=country').json()
    unique_values = {metric['country'] for metric in response}
    assert len(response) == len(unique_values), 'Grouping by one column'

    response = client.get('/metrics?group_by=date,country&columns=date,country').json()
    unique_values = {(metric['date'], metric['country']) for metric in response}
    assert len(response) == len(unique_values), 'Grouping by several columns'


def test_order_by(client: TestClient):
    response = client.get('/metrics?order_by=clicks&columns=clicks').json()
    assert response[0]['clicks'] <= response[1]['clicks'], 'Ordering by column in ascending order'

    response = client.get('/metrics?order_by=-clicks&columns=clicks').json()
    assert response[0]['clicks'] >= response[1]['clicks'], 'Ordering by column in descending order'
