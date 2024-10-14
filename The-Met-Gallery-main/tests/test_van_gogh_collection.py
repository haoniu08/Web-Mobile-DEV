'''
Hao Niu
CS 5001, Fall 2023
Final Project

This is the test file of the VanGoghCollection class
'''

import pytest
import requests
from unittest.mock import patch
from models.van_gogh_collection import VanGoghCollection


@pytest.fixture()
def van_gogh():
    return VanGoghCollection()


def test_van_gogh_init(van_gogh):
    assert van_gogh.ids is None


def test_van_gogh_fetch_with_right_path(van_gogh):
    with patch("models.van_gogh_collection.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "objectIDs": "233"
        }
        van_gogh.fetch()
        assert van_gogh.ids == "233"


def test_van_gogh_fetch_connection_error(van_gogh):
    with patch("models.van_gogh_collection.requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.ConnectionError()
        van_gogh.fetch()
        assert van_gogh.ids is None


def test_object_fetch_wrong_status_code(van_gogh):
    with patch("models.van_gogh_collection.requests.get") as mock_get:
        mock_get.return_value.status_code = 500
        mock_get.return_value.json.return_value = "233"
        van_gogh.fetch()
        assert van_gogh.ids is None
