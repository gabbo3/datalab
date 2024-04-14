import streamlit as st
st.title('Login')
with st.form(key='login'):
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    st.form_submit_button('Login')
st.page_link('pages/register.py', label='Register')
st.page_link('https://datariders.io', label='About Us')
