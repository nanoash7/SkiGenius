import math

import streamlit as st
import pandas as pd

from frontendutil import build_query_vector
from query_unit import query

NUM_RESULTS = 15

st.markdown("<h1 style='text-align: center; color: black;'>Ski Genius: A US Ski Resort Recommendation Tool</h1>", unsafe_allow_html=True)

location_option = st.selectbox('Select a Location Option', ('Current Location (City)', 'Resort Location (State)'))
location = st.text_input(location_option, '')
max_price = st.slider('Select a Max Price (USD)', 0, 300, 100)
skill_level = st.slider('Skill Level', 0, 100, 50)
target_date = st.date_input("Target Date", value=None)

def create_display(result):
    df = pd.DataFrame(result)
    df.rename(columns={'Name': 'Resort Name'}, inplace=True)

    # Get relative pricing
    min_price = min(df["Price"])
    max_price = max(df["Price"])

    def get_token_price(price):
        if min_price == max_price:
            return "Relative Price Unavailable"
        return "$" * math.floor((1 + 4 * (price - min_price) / (max_price - min_price)))

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

    st.session_state['query'] = build_query_vector(st.session_state['skill_level'], st.session_state['location'], st.session_state['target_date'].month)
    if st.session_state['query'] == -1:
        st.error("Invalid Location")
    else:
        # Perform the query
        result = query(st.session_state['query'], st.session_state['max_price'], NUM_RESULTS)
        create_display(result)

if 'result' in st.session_state:
    st.markdown("<h3 style='text-align: center; color: black;'>Curated results based on your location, experience level, price constraints, and projected snow quality</h1>", unsafe_allow_html=True)
    st.table(st.session_state['result'])