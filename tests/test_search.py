""" Reed Test Module """

from os import environ
from requests import HTTPError
from pytest import fixture, raises
from reed import ReedClient


@fixture
def client():
    """ reed client fixture """
    return ReedClient(environ.get("REED_API_KEY"))


@fixture
def params():
    """ query string parameter fixture """
    return {'keywords': 'data scientist'}


@fixture
def job_id_int():
    """ integer job id fixture """
    return 1


@fixture
def job_id_str():
    """ string of job id fixture """
    return 's'


def test_search(client, params):
    """ Assert test on search returning `list` """
    assert isinstance(client.search(**params), list)


def test_search_missing_key(client, params):
    """ Test of missing api key on search raising `AttributeError` """
    del client.api_key
    with raises(AttributeError):
        client.search(**params)


def test_search_wrong_key(client, params):
    """ Test of wrong key on search raising `HTTPError`"""
    client.api_key = 'a'
    with raises(HTTPError):
        client.search(**params)


def test_job_details(client, job_id_int):
    """ Assert test on job_details returns a `dict`"""
    assert isinstance(client.job_details(job_id=job_id_int), dict)


def test_missing_job_id(client):
    """ Test of missing job id raising `TypeError`"""
    with raises(TypeError):
        client.job_details()


def test_job_details_wrong_type(client, job_id_str):
    """ Test of wrong type for job_details raising `ValueError`"""
    with raises(ValueError):
        client.job_details(job_id_str)


def test_job_details_missing_key(client, job_id_int):
    """ Test of missing api key on job details raising `AttributeError`"""
    del client.api_key
    with raises(AttributeError):
        client.job_details(job_id=job_id_int)
