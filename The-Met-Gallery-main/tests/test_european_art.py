'''
Hao Niu
CS 5001, Fall 2023
Final Project

This is the test file of the EuropeanArt class
'''

import pytest
import requests
from unittest.mock import patch
from models.european_art import EuropeanArt


@pytest.fixture()
def european_art():
    return EuropeanArt()


def test_european_art_init(european_art):
    assert european_art.ids is None


def test_european_art_fetch_with_right_path(european_art):
    with patch("models.european_art.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "objectIDs": "233"
        }
        european_art.fetch()
        assert european_art.ids == "233"


def test_european_art_fetch_connection_error(european_art):
    with patch("models.european_art.requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.ConnectionError()
        european_art.fetch()
        assert european_art.ids is None


def test_object_fetch_wrong_status_code(european_art):
    with patch("models.european_art.requests.get") as mock_get:
        mock_get.return_value.status_code = 500
        mock_get.return_value.json.return_value = "233"
        european_art.fetch()
        assert european_art.ids is None
