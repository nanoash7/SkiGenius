import streamlit as st

st.markdown("<h1 style='text-align: center; color: black;'>Ski Resort Recommendation Tool</h1>", unsafe_allow_html=True)

state = st.text_input('State', '')
price_range = st.slider('Select a Price Range (USD)', 0.0, 300.0, (100.0, 150.0))

if st.button('Get Results'):
    # Query goes here
    st.session_state['state'] = state
    st.session_state['price_range'] = price_range
    
st.text_area(label="Results", value="Show Results Here", height=200)