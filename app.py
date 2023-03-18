import streamlit as st
from translator import show_translation_page
from doc_page import doc


col1,col2 = st.sidebar.columns([1,5])
col2.image("icon.png",width=180)
col2.write("")

col1,col2 = st.sidebar.columns([2,6])
col2.title(""" Translatorried """)      

col1,col2 = st.sidebar.columns([1,8])
col2.title("Menu")

col1,col2 = st.sidebar.columns([2,8])
choice = col2.radio("",['Translate','Brief'])

if choice == 'Translate':
    show_translation_page()
else:
    doc()