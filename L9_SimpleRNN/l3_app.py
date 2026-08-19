from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model
import streamlit as st

word_index = imdb.get_word_index()
reverse_word_index = {value: key for key, value in word_index.items()}
model = load_model('imdb_rnn_model.h5')

def decode_review(encoded_review):
    decoded_review = ' '.join([reverse_word_index.get(i-3, '?') for i in encoded_review])
    return decoded_review

def preprocess_input(user_input):
    words = user_input.lower().split()
    encoded_review = [word_index.get(word, 2) + 3 for word in words]
    # Pad the sequence to ensure consistent input length
    padded_review = sequence.pad_sequences([encoded_review], maxlen=500)
    return padded_review

def predict_sentiment(preprocessed_input):
    prediction = model.predict(preprocessed_input)
    sentiment = "Looks like you liked the movie!" if prediction[0][0] > 0.5 else "Looks like you didn't like the movie :("
    return sentiment

st.title("IMDB Movie Review Sentiment Analysis")

st.subheader("Enter a movie review:")
user_input = st.text_area("Review", "")

preprocessed_input = preprocess_input(user_input)

if st.button("Analyze Sentiment"):
    sentiment = predict_sentiment(preprocessed_input)
    st.write(sentiment)