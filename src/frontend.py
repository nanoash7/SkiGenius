import streamlit as st

st.markdown("<h1 style='text-align: center; color: black;'>US Ski Resort Recommendation Tool</h1>", unsafe_allow_html=True)

state = st.text_input('State', '')
price_range = st.slider('Select a Price Range (USD)', 0.0, 300.0, (100.0, 150.0))

if st.button('Get Results'):
    # Query goes here
    st.session_state['state'] = state
    st.session_state['price_range'] = price_range

result = st.session_state['result'] if 'result' in st.session_state else ""
st.text_area(label="Results", value=result, height=200)