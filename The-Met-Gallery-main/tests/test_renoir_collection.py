'''
Hao Niu
CS 5001, Fall 2023
Final Project

This is the test file of the RenoirCollection class
'''

import pytest
import requests
from unittest.mock import patch
from models.renoir_collection import RenoirCollection


@pytest.fixture()
def renoir():
    return RenoirCollection()


def test_renoir_init(renoir):
    assert renoir.ids is None


def test_renoir_fetch_with_right_path(renoir):
    with patch("models.renoir_collection.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "objectIDs": "233"
        }
        renoir.fetch()
        assert renoir.ids == "233"


def test_renoir_fetch_connection_error(renoir):
    with patch("models.renoir_collection.requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.ConnectionError()
        renoir.fetch()
        assert renoir.ids is None


def test_object_fetch_wrong_status_code(renoir):
    with patch("models.renoir_collection.requests.get") as mock_get:
        mock_get.return_value.status_code = 500
        mock_get.return_value.json.return_value = "233"
        renoir.fetch()
        assert renoir.ids is None
