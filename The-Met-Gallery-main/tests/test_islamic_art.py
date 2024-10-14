'''
Hao Niu
CS 5001, Fall 2023
Final Project

This is the test file of the IslamicArt class
'''

import pytest
import requests
from unittest.mock import patch
from models.islamic_art import IslamicArt


@pytest.fixture()
def islamic_art():
    return IslamicArt()


def test_islamic_art_init(islamic_art):
    assert islamic_art.ids is None


def test_islamic_art_fetch_with_right_path(islamic_art):
    with patch("models.islamic_art.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "objectIDs": "233"
        }
        islamic_art.fetch()
        assert islamic_art.ids == "233"


def test_islamic_art_fetch_connection_error(islamic_art):
    with patch("models.islamic_art.requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.ConnectionError()
        islamic_art.fetch()
        assert islamic_art.ids is None


def test_object_fetch_wrong_status_code(islamic_art):
    with patch("models.islamic_art.requests.get") as mock_get:
        mock_get.return_value.status_code = 500
        mock_get.return_value.json.return_value = "233"
        islamic_art.fetch()
        assert islamic_art.ids is None
