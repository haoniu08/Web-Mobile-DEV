'''
Hao Niu
CS 5001, Fall 2023
Final Project

This is the file of the page of the Masterpieces.
It displays the artworks and corresponding
features/links etc.
'''

import streamlit as st
from models.renoir_collection import RenoirCollection
from models.van_gogh_collection import VanGoghCollection
from models.manet_collection import ManetCollection
from helper_functions import (
    display_artworks_of_given_artist,
    initiate_bidding
)
from st_pages import hide_pages

hide_pages("bidding")
hide_pages("success")
hide_pages("unsuccessful")

user_name = st.session_state.user_name
st.write(f"Welcome {user_name}")
st.header("Met's Finest Collection")

# The bidding choice were initially designed to follow each item within
# the "display" loops, but streamlit functions like st.button and switch_page
# are all quite limited while working with loops
id = st.number_input("Please enter the id of the item you wish to bid", step=1)
c1, c2, c3 = st.columns(3, gap="medium")

# If user wishes to bid then prepares for corresponding information
if id:
    initiate_bidding(id)

with c1:
    # Shows the corresponding images and information
    # of artworks on column 1
    st.subheader("Vincent van Gogh")
    van_gogh = VanGoghCollection()
    van_gogh.fetch()
    list_of_van_gogh = van_gogh.ids
    artist = "Vincent van Gogh"
    display_artworks_of_given_artist(list_of_van_gogh, artist)

with c2:
    # Shows the corresponding images and information
    # of artworks on column 2
    st.subheader("Auguste Renoir")
    renoir = RenoirCollection()
    renoir.fetch()
    list_of_renoir = renoir.ids
    artist = "Auguste Renoir"
    display_artworks_of_given_artist(list_of_renoir, artist)

with c3:
    # Shows the corresponding images and information
    # of artworks on column 3
    st.subheader("Edouard Manet")
    manet = ManetCollection()
    manet.fetch()
    list_of_manet = manet.ids
    artist = "Edouard Manet"
    display_artworks_of_given_artist(list_of_manet, artist)
