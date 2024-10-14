'''
Hao Niu
CS 5001, Fall 2023
Final Project

This is the file of class AfricanArt,
it contains its corresponding attributes
and methods.

Class - AfricanArt
Attributes: ids
Methods: __init__, fetch
'''
import requests


class AfricanArt:
    """
    The African artworks
    """
    def __init__(self):
        self.ids = None

    def fetch(self):
        """
        Fetches the list of ids of African artworks
        """
        url = "https://collectionapi.metmuseum.org/pub\
lic/collection/v1/search?hasImages=true&q=department=african"
        try:
            response = requests.get(url)
            data = response.json()
        except requests.exceptions.ConnectionError:
            return
        if response.status_code != 200:
            return
        self.ids = data["objectIDs"]
