import streamlit as st

def doc():
    st.balloons()
    cols=st.columns([2,4,2])
    cols[1].title("Hello guys !!")
    st.write("")
    st.write("""
    #
    #### Translatorried, a language translator which can convert English to French or Spanish. 
    #### It is developed with deep learning network using LSTM encoder decoder architecture.
    #""")

    st.write("""
    #### Click the below link, for the Github repo.
    #### https://github.com/Hafiz408/Translator
    """)
        