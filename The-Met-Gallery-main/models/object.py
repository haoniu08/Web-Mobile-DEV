'''
Hao Niu
CS 5001, Fall 2023
Final Project

This is the file of class Object,
it contains its corresponding attributes
and methods.

Class - Object
Attributes: ids, details, image, title, artist, date, url, caption
Methods: __init__, fetch, set_attribute_values, set_img_url,
        set_title, set_artist_name, set_date, set_url, create_caption
'''
import requests


class Object:
    """
    A single Object from the entire collection
    """
    def __init__(self):
        self.id = None
        self.details = None
        self.image = None
        self.title = None
        self.artist = None
        self.date = None
        self.url = None
        self.caption = None

    def fetch(self):
        """
        Fetches the record for an object
        """
        url = f"https://collectionapi.metmuseum.org/pub\
lic/collection/v1/objects/{self.id}"
        try:
            response = requests.get(url)
            data = response.json()
        except requests.exceptions.ConnectionError:
            return
        if response.status_code != 200:
            return
        self.details = data

    def set_attribute_values(self):
        """
        Sets values to the object's attributes
        """
        self.id = self.details["objectID"]
        self.image = self.details["primaryImageSmall"]
        self.title = self.details["title"]
        self.artist = self.details["artistDisplayName"]
        self.date = self.details["objectDate"]
        self.url = self.details["objectURL"]

    def set_img_url(self):
        """
        Sets the object's img url from the record
        """
        self.image = self.details["primaryImageSmall"]

    def set_title(self):
        """
        Sets the object's title from the record
        """
        self.title = self.details["title"]

    def set_artist_name(self):
        """
        Sets the object's artist's name from the record
        """
        self.artist = self.details["artistDisplayName"]

    def set_date(self):
        """
        Sets the date of the object
        """
        self.date = self.details["objectDate"]

    def set_url(self):
        """
        Gets the url of the object
        """
        self.url = self.details["objectURL"]

    def create_caption(self):
        """
        Create the caption of an given object
        """
        self.caption = (
            f'<{self.details["title"]}>\n'
            f'{self.details["artistDisplayName"]}\n'
            f'{self.details["objectDate"]}'
        )
