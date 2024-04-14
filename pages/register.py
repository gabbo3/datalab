import streamlit as st
st.set_page_config(layout='centered')

def validate_password(password, password_confirm):
    if len(password) <= 0:
        st.error("Invalid Password!")
        return False 
    if password == password_confirm:
        return True
    st.error("Passwords doesn't match.")
    return False

def validate_username(username):
    return len(username) > 0 

st.title('Register')
with st.form(key='register'):
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    password_confirm = st.text_input('Confirm password', type='password')
    continuar = st.form_submit_button('Continue')

if continuar:
    if validate_username(username):
        st.success("Username is valid!")
    else:
        st.error('Invalid Username')
    if validate_password(password, password_confirm):
        st.success("Password is valid!")
