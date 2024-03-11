"""
This module runs the code for the streamlit front end application.

Usage: From the root directory -> "streamlit run src/frontend.py"
"""

import math

import streamlit as st
import pandas as pd

# pylint: disable=import-error
from frontendutil import build_query_vector
from query_unit import query

NUM_RESULTS = 15

st.markdown("""<h1 style='text-align: center; color: black;'>
            Ski Genius: A US Ski Resort Recommendation Tool</h1>""", unsafe_allow_html=True)

location_option = st.selectbox('Select a Location Option', ('Current Location (City)',
            'Resort Location (State)'))
location = st.text_input(location_option, '')
max_price = st.slider('Select a Max Price (USD)', 0, 300, 100)
skill_level = st.slider('Skill Level', 0, 100, 50)
target_date = st.date_input("Target Date", value=None)


def create_display(result):
    """
    This function takes the db output and parses it for display.
    The parsed output is stored in the streamlit session state for 
    future retrieval.

    Parameters:
        result: List of dictionaries corresponding to the output from the db query.

    Returns:
        No return value.
    """
    if len(result) == 0:
        st.session_state['result'] = None
        return

    df = pd.DataFrame(result)
    df.rename(columns={'Name': 'Resort Name'}, inplace=True)

    # Get relative pricing
    mn_price = min(df["Price"])
    mx_price = max(df["Price"])

    def get_token_price(price):
        if mn_price == mx_price:
            return "Relative Price Unavailable"
        return "$" * math.floor((1 + 4 * (price - mn_price) / (mx_price - mn_price)))

    df["Relative Price"] = df["Price"].apply(get_token_price)

    df = df.drop(columns= ['_id', 'Snow', 'score', "Price"])
    df = df.reset_index(drop=True)
    st.session_state['result'] = df

if st.button('Get Results'):
    st.session_state['location_option'] = location_option
    st.session_state['location'] = location
    st.session_state['max_price'] = max_price
    st.session_state['skill_level'] = skill_level
    st.session_state['target_date'] = target_date

    st.session_state['query'] = build_query_vector(st.session_state['skill_level'],
                st.session_state['location'], st.session_state['target_date'].month)
    if st.session_state['query'] == -1:
        st.error("Invalid Location")
    else:
        # Perform the query
        query_result = query(st.session_state['query'], st.session_state['max_price'], NUM_RESULTS)
        create_display(query_result)

if 'result' in st.session_state:
    st.markdown("""<h3 style='text-align: center; color: black;'>
                Curated results based on your location,
                experience level, price constraints, and
                projected snow quality</h1>""", unsafe_allow_html=True)
    if st.session_state['result'] is None:
        st.error("No results found")
    else:
        st.table(st.session_state['result'])
