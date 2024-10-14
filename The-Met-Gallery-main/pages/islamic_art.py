'''
Hao Niu
CS 5001, Fall 2023
Final Project

This is the file of the page of Islamic Art.
It displays the artworks and corresponding
features/links etc.
'''

import streamlit as st
from models.islamic_art import IslamicArt
from helper_functions import (display_art_work_details, initiate_bidding)
from st_pages import hide_pages

hide_pages("bidding")
hide_pages("success")
hide_pages("unsuccessful")

user_name = st.session_state.user_name
st.write(f"Welcome {user_name}")
st.header("Islamic Artwork Collection")

# The bidding choice were initially designed to follow each item within
# the "display" loops, but streamlit functions like st.button and switch_page
# are all quite limited while working with loops
id = st.number_input("Please enter the id of the item you wish to bid", step=1)
c1, c2, c3 = st.columns(3, gap="medium")
islamic_art = IslamicArt()
islamic_art.fetch()
list_of_islamic_art = islamic_art.ids

# If user wishes to bid then prepares for corresponding information
if id:
    initiate_bidding(id)

with c1:
    # Shows the corresponding images and information
    # of artworks on column 1
    start_index = 0
    end_index = 9
    display_art_work_details(start_index, end_index, list_of_islamic_art)

with c2:
    # Shows the corresponding images and information
    # of artworks on column 2
    start_index = 11
    end_index = 21
    display_art_work_details(start_index, end_index, list_of_islamic_art)

with c3:
    # Shows the corresponding images and information
    # of artworks on column 3
    start_index = 21
    end_index = 30
    display_art_work_details(start_index, end_index, list_of_islamic_art)