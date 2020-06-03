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


def test_search(setup_client, setup_params):
    response = setup_client.search(**setup_params)
    assert type(response) is list
