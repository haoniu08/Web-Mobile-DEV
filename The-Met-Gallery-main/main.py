'''
Hao Niu
CS 5001, Fall 2023
Final Project

This is the file of the main page
'''

import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import Page, show_pages, hide_pages
st.header("Met's Gallery")
st.write("Powered by The Metropolitan Museum of Art")

show_pages(
    [
        Page("main.py", "The home page"),
        Page("pages/the_masters.py", "From the Masters"),
        Page("pages/european_art.py", "The European Collection"),
        Page("pages/asian_art.py", "The Asian Collection"),
        Page("pages/african_art.py", "The African Collection"),
        Page("pages/islamic_art.py", "The Islamic Collection"),
        Page("pages/bid_page.py", "bidding"),
        Page("pages/successful_bid.py", "success"),
        Page("pages/unsuccessful_bid.py", "unsuccessful"),
    ]
)

hide_pages("bidding")
hide_pages("success")
hide_pages("unsuccessful")

masters = st.button("For the Masterpieces")
if masters:
    switch_page("From the Masters")

european_art = st.button("To view European artworks")
if european_art:
    switch_page("The European Collection")

asian_art = st.button("To view Asian artworks")
if asian_art:
    switch_page("The Asian Collection")

african_art = st.button("To view African artworks")
if african_art:
    switch_page("The African Collection")

islamic_art = st.button("To view Islamic artworks")
if islamic_art:
    switch_page("The Islamic Collection")

with st.form("user_info"):
    user_name = st.text_input("How would you like to be addressed?")
    st.session_state.user_name = user_name
    sumbit = st.form_submit_button()
    if sumbit:
        st.write(f"Welcome {user_name}!")
