'''
Hao Niu
CS 5001, Fall 2023
Final Project

This is the file of class RenoirCollection,
it contains its corresponding attributes
and methods.

Class - RenoirCollection
Attributes: ids
Methods: __init__, fetch
'''
import requests


class RenoirCollection:
    """
    A collection of Renoir's works
    """
    def __init__(self):
        self.ids = None

    def fetch(self):
        """
        Fetches the list of ids
        contains "Auguste Renoir" as search result
        """
        url = "https://collectionapi.metmuseum.org/public/col\
lection/v1/search?hasImages=true&q=Auguste Renoir"
        try:
            response = requests.get(url)
            data = response.json()
        except requests.exceptions.ConnectionError:
            return
        if response.status_code != 200:
            return
        self.ids = data["objectIDs"]
