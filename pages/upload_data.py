import pandas as pd
import streamlit as st
st.set_page_config(layout='wide')


st.title('Upload Data')
uploaded_file = st.file_uploader('File uploader', type=['xlsx', 'csv'])

if uploaded_file is not None:
    if uploaded_file.name.split('.')[-1] == 'csv':
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    st.dataframe(df, height=400, hide_index=True)
