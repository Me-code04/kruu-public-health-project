import streamlit as st

def MessageDisplay():
    st.header("Welcome to Vax App!")
    st.subheader("This app shows your current vaccination status and recommendations to how you can improve your stance against viruses.")
    st.subheader("We cross check your data with our database of medical symptoms and vaccine recommendations to tell you whether to get your vaccines or not! Click below to input your details!")

    TransitionA = st.checkbox("I understand that this is a recommendation system based on my medical data.")
    TransitionB = st.button("Get Started")
    return (TransitionA or TransitionB)
