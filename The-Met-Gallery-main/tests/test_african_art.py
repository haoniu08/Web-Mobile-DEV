'''
Hao Niu
CS 5001, Fall 2023
Final Project

This is the test file of the AfricanArt class
'''

import pytest
import requests
from unittest.mock import patch
from models.african_art import AfricanArt


@pytest.fixture()
def african_art():
    return AfricanArt()


def test_african_art_init(african_art):
    assert african_art.ids is None


def test_african_art_fetch_with_right_path(african_art):
    with patch("models.african_art.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "objectIDs": "233"
        }
        african_art.fetch()
        assert african_art.ids == "233"


def test_african_art_fetch_connection_error(african_art):
    with patch("models.african_art.requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.ConnectionError()
        african_art.fetch()
        assert african_art.ids is None


def test_object_fetch_wrong_status_code(african_art):
    with patch("models.african_art.requests.get") as mock_get:
        mock_get.return_value.status_code = 500
        mock_get.return_value.json.return_value = "233"
        african_art.fetch()
        assert african_art.ids is None
