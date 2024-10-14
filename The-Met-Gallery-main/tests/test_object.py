'''
Hao Niu
CS 5001, Fall 2023
Final Project

This is the test file of the Object class
'''

import pytest
import requests
from unittest.mock import patch
from models.object import Object


@pytest.fixture
def object():
    return Object()


@pytest.fixture
def object2():
    object2 = Object()
    object2.details = {
        "primaryImageSmall": 1,
        "title": 2,
        "artistDisplayName": 3,
        "objectDate": 4,
        "objectURL": 5
    }
    return object2


def test_object_init(object):
    assert object.id is None
    assert object.details is None
    assert object.image is None
    assert object.title is None
    assert object.artist is None
    assert object.date is None
    assert object.url is None
    assert object.caption is None


def test_object_fetch_with_right_path(object):
    with patch("models.object.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = "233"
        object.fetch()
        assert object.details == "233"


def test_object_fetch_connection_error(object):
    with patch("models.object.requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.ConnectionError()
        object.fetch()
        assert object.details is None


def test_object_fetch_wrong_status_code(object):
    with patch("models.object.requests.get") as mock_get:
        mock_get.return_value.status_code = 500
        mock_get.return_value.json.return_value = "233"
        object.fetch()
        assert object.details is None


def test_object_set_attribute_values(object2):
    object2.set_attribute_values()
    assert object2.image == 1
    assert object2.title == 2
    assert object2.artist == 3
    assert object2.date == 4
    assert object2.url == 5


def test_object_set_img_url(object2):
    object2.set_img_url()
    assert object2.image == 1


def test_object_set_title(object2):
    object2.set_title()
    assert object2.title == 2


def test_object_set_artist_name(object2):
    object2.set_artist_name()
    assert object2.artist == 3


def test_object_set_date(object2):
    object2.set_date()
    assert object2.date == 4


def test_object_set_url(object2):
    object2.set_url()
    assert object2.url == 5


def test_object_create_caption(object2):
    object2.create_caption()
    assert object2.caption == (
        '<2>\n'
        '3\n'
        '4'
    )
