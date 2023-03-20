import streamlit as st
from translator import show_translation_from_text_page, show_translation_from_img_page
from doc_page import doc

col1,col2 = st.sidebar.columns([1,5])
col2.image("icon.png",width=180)
col2.write("")

col1,col2 = st.sidebar.columns([2,6])
col2.title(""" Translatorried """)      

col1,col2 = st.sidebar.columns([1,8])
col2.title("Menu")

col1,col2 = st.sidebar.columns([2,10])
menu = col2.radio('', ['Translate', 'Brief'], key='menu', horizontal=True, label_visibility="collapsed")

col1,col2 = st.sidebar.columns([1,8])
col2.title("Translate")

col1,col2 = st.sidebar.columns([2,8])
choice = col2.selectbox("",['from text','from image'], key='translate_option', label_visibility="collapsed")

if menu == 'Translate':
    if choice == 'from text':
        show_translation_from_text_page()
    else:
        show_translation_from_img_page()
elif menu == 'Brief':
    doc()