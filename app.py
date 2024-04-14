import streamlit as st

st.title('Data Riders APP')

cols = st.columns(4)
with cols[0]:
    login = st.button("Login", help='Here to login')
with cols[1]:
    help = st.button("Help")
with cols[2]:
    unavailable = st.button("Unavailable",disabled=True)
with cols[3]:
    demo = st.button("Demo")

    
if login:
    st.switch_page('pages/login.py')
if help:
    st.switch_page('pages/help.py')
if demo:
    st.switch_page('pages/demo.py')
if st.button('Upload data'):
    st.switch_page('pages/upload_data.py')