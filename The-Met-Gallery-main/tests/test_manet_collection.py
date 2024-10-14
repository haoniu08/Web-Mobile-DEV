'''
Hao Niu
CS 5001, Fall 2023
Final Project

This is the test file of the ManetCollection class
'''

import pytest
import requests
from unittest.mock import patch
from models.manet_collection import ManetCollection


@pytest.fixture()
def manet():
    return ManetCollection()


def test_manet_init(manet):
    assert manet.ids is None


def test_manet_fetch_with_right_path(manet):
    with patch("models.manet_collection.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "objectIDs": "233"
        }
        manet.fetch()
        assert manet.ids == "233"


def test_manet_fetch_connection_error(manet):
    with patch("models.manet_collection.requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.ConnectionError()
        manet.fetch()
        assert manet.ids is None


def test_object_fetch_wrong_status_code(manet):
    with patch("models.manet_collection.requests.get") as mock_get:
        mock_get.return_value.status_code = 500
        mock_get.return_value.json.return_value = "233"
        manet.fetch()
        assert manet.ids is None
