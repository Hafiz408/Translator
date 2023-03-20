import streamlit as st
from utils import *

def show_translation_from_text_page():

    cols=st.columns([2,4,2])
    cols[1].image("icon.png",width=250)
    cols=st.columns([2,8,2])
    cols[1].title("|..... Translatorried  ....|")
    st.write("")

    st.subheader("Enter the text you want to translate :")
    text=st.text_area("",placeholder="Type or paste the text to be translated...",  label_visibility="collapsed", height=100)
    st.write("")

    cols=st.columns([4,3,1])
    cols[0].subheader("Select the target language :")
    lang= cols[1].selectbox("",['French','Hindi'], label_visibility="collapsed")

    st.write("")
    cols = st.columns([2,1,2])
    ok = cols[1].button("Translate")

    if ok:
        if len(text) !=0:
            output = translate(text, lang)
            cols=st.columns([1,3,1])
            st.subheader(" Translation :")
            st.write(output)
        else:
            st.warning("No text found. Try again !!")

def show_translation_from_img_page():
    cols=st.columns([2,4,2])
    cols[1].image("icon.png",width=250)
    cols=st.columns([2,8,2])
    cols[1].title("|..... Translatorried  ....|")
    st.write("")

    st.subheader("Choose the preferred method to input the image :")
    cols=st.columns([1,3])
    input = cols[1].radio('',['Upload the image', 'Capture the image'], horizontal=True, label_visibility="collapsed")
    
    upload_img, cam_img = None, None
    if input == 'Upload the image':
        upload_img = st.file_uploader('Choose an image')
    else:
        cam_img = st.camera_input("Take a picture !!")

    st.write("")
    cols=st.columns([4,3,1])
    cols[0].subheader("Select the target language :")
    lang= cols[1].selectbox("",['French','Hindi'], label_visibility="collapsed")

    st.write("")
    cols = st.columns([2,1,2])
    ok = cols[1].button("Translate")

    if ok:
        if upload_img != None:
            text = get_text_from_img(upload_img)
            output = translate(text, lang)
            cols=st.columns([1,3,1])
            st.subheader(" Translation :")
            st.write(output)
        elif cam_img != None:
            text = get_text_from_img(cam_img)
            output = translate(text, lang)
            cols=st.columns([1,3,1])
            st.subheader(" Translation :")
            st.write(output)
        else:
            st.warning("No text found. Try again !!")