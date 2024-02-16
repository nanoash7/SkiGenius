import streamlit as st

st.markdown("<h1 style='text-align: center; color: black;'>Ski Resort Recommendation Tool</h1>", unsafe_allow_html=True)

city = st.text_input('Location (City)', '')
price_range = st.slider('Select a Price Range (USD)', 0.0, 300.0, (100.0, 150.0))

if st.button('Get Results'):
    # Query goes here
    st.session_state['city'] = city
    st.session_state['price_range'] = price_range
    
st.write("City: " + (st.session_state['city'] if 'city' in st.session_state else ""))
st.write("Price Range: " + 
    (str(st.session_state['price_range'][0]) + " to " + str(st.session_state['price_range'][1]) if 'price_range' in st.session_state else ""))