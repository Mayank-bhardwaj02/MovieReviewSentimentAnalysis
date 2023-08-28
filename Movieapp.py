# Import necessary libraries
import streamlit as st
import base64

# importing the function from the machine learning model python file
from MovieScript import predict_sentiment  


# Title of your app
st.title("Movie Review Analyzer")

# Textbox for user input
user_input = st.text_input("Enter the movie review:")

# Button to trigger prediction
if st.button("Analyze"):
    # Use the model to predict the sentiment
    result = predict_sentiment(user_input)
    # Display the result
    if result == 'positive':
        st.write(f"It seems you had a good time watching the movie")
        st.write(f"Thanks for the feedback")
    else:
        st.write(f"It looks like the movie didn't live up to your expectations")
        st.write(f"Thanks for the feedback")
