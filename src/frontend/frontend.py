import streamlit as st
from frontendutil import build_query_vector

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

    st.session_state['query'] = build_query_vector(st.session_state['skill_level'], st.session_state['location'], st.session_state['target_date'].month)
    if st.session_state['query'] == -1:
        st.error("Invalid Location")
    else:
        # Perform the search using st.session_state['query'] and st.session_state['max_price']
        pass