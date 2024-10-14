'''
Hao Niu
CS 5001, Fall 2023
Final Project

This is the test file of the AsianArt class
'''

import pytest
import requests
from unittest.mock import patch
from models.asian_art import AsianArt


@pytest.fixture()
def asian_art():
    return AsianArt()


def test_asian_art_init(asian_art):
    assert asian_art.ids is None


def test_asian_art_fetch_with_right_path(asian_art):
    with patch("models.asian_art.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "objectIDs": "233"
        }
        asian_art.fetch()
        assert asian_art.ids == "233"


def test_asian_art_fetch_connection_error(asian_art):
    with patch("models.asian_art.requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.ConnectionError()
        asian_art.fetch()
        assert asian_art.ids is None


def test_object_fetch_wrong_status_code(asian_art):
    with patch("models.asian_art.requests.get") as mock_get:
        mock_get.return_value.status_code = 500
        mock_get.return_value.json.return_value = "233"
        asian_art.fetch()
        assert asian_art.ids is None
