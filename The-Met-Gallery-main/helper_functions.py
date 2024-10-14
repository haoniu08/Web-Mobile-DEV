'''
Hao Niu
CS 5001, Fall 2023
Final Project

This is the file of helper functions.
It contains corresponding helper functions
that will be used mostly to clean data and
display artwork information
'''

import streamlit as st
from models.object import Object
from streamlit_extras.switch_page_button import switch_page


def check_if_image_available(object: Object) -> bool:
    """
    Check if an object's img url is available
    """
    if "https:" in object.image:
        return True


def check_if_artist_name_is_correct(
        object: Object,
        artist: str
) -> bool:
    """
    Check if an object is from a certain artist
    """
    if object.artist == artist:
        return True


def create_artwork_details(object: Object) -> None:
    """
    Creates the details of a given artwork
    """
    st.image(object.image)
    st.write("ID: ", object.id)
    st.write("Title: ", object.title)
    st.write("Artist: ", object.artist)
    st.write("Date: ", object.date)
    st.write("[For more detail](%s)" % object.url)


@st.cache_data(experimental_allow_widgets=True)
def display_art_work_details(
        start_index: int,
        end_index: int,
        id_list: list
) -> None:
    """
    Displays the corresponding artwork information on
    the web pages
    """
    for i in range(start_index, end_index):
        object = Object()
        object.id = id_list[i]
        object.fetch()
        object.set_attribute_values()
        if check_if_image_available(object):
            create_artwork_details(object)
        else:
            i -= 1
            continue


@st.cache_data(experimental_allow_widgets=True)
def display_artworks_of_given_artist(
    id_list: list,
    artist: str,
    start_index=1,
    end_index=11
) -> None:
    """
    Displays the corresponding artwork information of a given
    artist on the web pages
    """
    for i in range(start_index, end_index):
        object = Object()
        object.id = id_list[i]
        object.fetch()
        object.set_attribute_values()
        if (
            check_if_image_available(object) and
            check_if_artist_name_is_correct(
                object,
                artist
            )
        ):
            create_artwork_details(object)
        else:
            i -= 1
            continue


def initiate_bidding(id):
    """
    Initiates the bidding process
    """
    st.session_state.id = id
    object = Object()
    object.id = id
    object.fetch()
    object.set_attribute_values()
    st.session_state.img = object.image
    switch_page("bidding")
