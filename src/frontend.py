import streamlit as st
import datetime as dt

st.markdown("<h1 style='text-align: center; color: black;'>Ski Genius: A US Ski Resort Recommendation Tool</h1>", unsafe_allow_html=True)

location_option = st.selectbox('Select a Location Option', ('Current Location (City)', 'Resort Location (State)'))
location = st.text_input(location_option, '')
max_price = st.slider('Select a Max Price (USD)', 0, 300, 100)
skill_level = st.slider('Skill Level', 0, 100, 50)
target_date = st.date_input("Target Date", value=None)

if st.button('Get Results'):
    st.session_state['location_option'] = location_option
    st.session_state['location'] = location
    st.session_state['max_price'] = max_price
    st.session_state['skill_level'] = skill_level
    st.session_state['target_date'] = target_date
    # Query goes here

result = st.session_state['result'] if 'result' in st.session_state else ""