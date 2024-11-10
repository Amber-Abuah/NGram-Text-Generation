import streamlit as st
from Ngram import predict_next_word

if "text" not in st.session_state:
    st.session_state["text"] = "I thought that"
    st.session_state["error"] = ""

def predict():
    st.session_state["text"] = text
    words = st.session_state["text"]
    prediction = predict_next_word(words, N, num_predict)

    if prediction == None:
        st.session_state.error = "Error using N=" + str(N) + ". Please use a lower N or try a different sequence of word(s)."
    else:
        st.session_state.error = ""
        st.session_state.text += " " + prediction

 
st.title("Text Autocomplete Using N-grams")
N = st.radio("N=", [2, 3, 4], horizontal=True)
num_predict = st.number_input("Number of words to predict", 1, 50, step=1)
text = st.text_area("Input Text:", st.session_state.text, height=300)
st.button("Predict next word(s)", on_click=predict)
st.text(st.session_state.error)