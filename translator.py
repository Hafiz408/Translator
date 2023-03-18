import streamlit as st
import pickle
import collections
import numpy as np

from keras import Input, Sequential
from keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.models import Model, load_model
from keras.layers import GRU, Input, Dense, TimeDistributed, Activation, RepeatVector, Bidirectional, LSTM
from tensorflow.keras.layers import Embedding
from keras.optimizers import Adam
from keras.losses import sparse_categorical_crossentropy


x, y = np.load('saved_model/preproc_english_sentences.npy'), np.load('saved_model/preproc_french_sentences.npy')
with open('saved_model/english_tokenizer.pickle', 'rb') as handle:
    x_tk = pickle.load(handle)
with open('saved_model/french_tokenizer.pickle', 'rb') as handle:
    y_tk = pickle.load(handle)

model = load_model('saved_model/final_model.h5')

def logits_to_text(logits, tokenizer):
    """
    Turn logits from a neural network into text using the tokenizer
    :param logits: Logits from a neural network
    :param tokenizer: Keras Tokenizer fit on the labels
    :return: String that represents the text of the logits
    """
    index_to_words = {id: word for word, id in tokenizer.word_index.items()}
    index_to_words[0] = '<PAD>'

    return ' '.join([index_to_words[prediction] for prediction in np.argmax(logits, 1) if index_to_words[prediction]!='<PAD>'] )

def translate(sentence):
    
    sentence = [x_tk.word_index[word] for word in sentence.split()]
    sentence = pad_sequences([sentence], maxlen=x.shape[-1], padding='post')
    sentences = np.array([sentence[0], x[0]])
    predictions = model.predict(sentences, len(sentences))
    translation = logits_to_text(predictions[0], y_tk)
    return translation

def show_translation_page():

    cols=st.columns([2,4,2])
    cols[1].image("icon.png",width=250)
    cols=st.columns([2,8,2])
    cols[1].title("|..... Translatorried  ....|")
    st.write("")

    st.subheader("Enter the text you want to translate :")
    text=st.text_area("",placeholder="Type or paste the text to be translated...",height=100)

    st.write("")
    cols = st.columns([2,1,2])
    ok = cols[1].button("Translate")

    if ok:
        if len(text) !=0:
            output = translate(text)
            # output=text
            cols=st.columns([1,3,1])
            st.subheader(" Translation :")
            st.write(output)
        else:
            st.warning("No text found. Try again !!")

    