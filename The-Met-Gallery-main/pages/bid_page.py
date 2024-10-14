'''
Hao Niu
CS 5001, Fall 2023
Final Project

This is bidding page which contains corresponding logics
for the bidding process
'''


import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages

hide_pages("bidding")
hide_pages("success")
hide_pages("unsuccessful")

id = st.session_state.id
img = st.session_state.img
user_name = st.session_state.user_name

st.subheader(f"Good luck {user_name}!")
try:
    st.image(img, use_column_width="always")
    user_bid = st.number_input(
        "Please place your bid, but one chance only \
due to the 'Silent Auction' rule.",
        step=1000
    )
    # The bidding process itself is really just randomly processed
    # It used the object ID as the "base" for calculation
    if user_bid:
        if user_bid > id / 10:
            switch_page("success")
        elif user_bid < id / 10:
            switch_page("unsuccessful")
except Exception as err:
    st.write(f"{err}. Sorry that was an invalid item id.")
