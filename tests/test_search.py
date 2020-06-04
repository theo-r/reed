import os

import pytest

from reed import ReedClient


@pytest.fixture
def setup_client():
    api_key = os.environ.get('API_KEY')
    client = ReedClient(api_key)
    return client


@pytest.fixture
def setup_params():
    params = {
        'keywords': 'data scientist'
    }
    return params


@pytest.fixture
def setup_job_id():
    job_id = 1
    return job_id


@pytest.fixture
def setup_job_id_str():
    job_id = 's'
    return job_id


def test_search(setup_client, setup_params):
    response = setup_client.search(**setup_params)
    assert type(response) is list


def test_search_missing_key(setup_client, setup_params):
    del setup_client.api_key
    with pytest.raises(AttributeError):
        setup_client.search(**setup_params)


def test_job_details(setup_client, setup_job_id):
    response = setup_client.job_details(job_id=setup_job_id)
    assert type(response) is dict


def test_missing_job_id(setup_client):
    with pytest.raises(TypeError):
        setup_client.job_details()


def test_job_details_wrong_type(setup_client, setup_job_id_str):
    with pytest.raises(ValueError):
        setup_client.job_details(setup_job_id_str)
