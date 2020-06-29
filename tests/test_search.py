import os
from requests import HTTPError

import pytest

from reed import ReedClient


@pytest.fixture
def client():
    api_key = os.environ.get('API_KEY')
    client = ReedClient(api_key)
    return client


@pytest.fixture
def params():
    params = {
        'keywords': 'data scientist'
    }
    return params


@pytest.fixture
def job_id_int():
    job_id = 1
    return job_id

@pytest.fixture
def job_id_str():
    job_id = 's'
    return job_id


def test_search(client, params):
    response = client.search(**params)
    assert type(response) is list


def test_search_missing_key(client, params):
    del client.api_key
    with pytest.raises(AttributeError):
        client.search(**params)


def test_search_wrong_key(client, params):
    client.api_key = 'a'
    with pytest.raises(HTTPError):
        client.search(**params)


def test_job_details(client, job_id_int):
    response = client.job_details(job_id=job_id_int)
    assert type(response) is dict


def test_missing_job_id(client):
    with pytest.raises(TypeError):
        client.job_details()


def test_job_details_wrong_type(client, job_id_str):
    with pytest.raises(ValueError):
        client.job_details(job_id_str)


def test_job_details_missing_key(client, job_id_int):
    del client.api_key
    with pytest.raises(AttributeError):
        client.job_details(job_id=job_id_int)


