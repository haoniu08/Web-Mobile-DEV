'''
Hao Niu
CS 5001, Fall 2023
Final Project

This is page where the user will be directed if
the user successfully bid an object
'''

import streamlit as st
from st_pages import hide_pages

hide_pages("bidding")
hide_pages("success")
hide_pages("unsuccessful")

user_name = st.session_state.user_name
st.header(f"Congrats {user_name}! You were the highest bidder!")
user_contact = st.number_input("Please enter your contact number here", step=1)
if user_contact:
    st.subheader("Thank you! Our agents will contact you shorly!")
img_url = st.session_state.img
st.image(img_url)
