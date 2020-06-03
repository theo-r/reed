import os
from nose.tools import with_setup

import reed


api_key = os.environ.get('API_KEY')


def setup():
    client = ReedClient(api_key=api_key)
    params = {
        'keywords': 'data scientist',
        'locationName': 'London',
        'minimumSalary': 30000
    }


def teardown():
    client = None
    params = None

@with_setup(setup, teardown)
def test_search():
    response = client.search(**params)
    assert type(search_response) is dict
