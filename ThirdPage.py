import streamlit as st

def MessageDisplayB():
    st.header("Awesome! You’re ready to roll!")
    st.subheader("The main page shows you your current health status, recommended vaccination and other options that are free for you to explore!")
    st.subheader("You can add a vaccine once you’ve taken it, update your medical records, ask questions from our staff and learn all about viruses and vaccine! Don’t forget to update your personal data often!")

    TransitionAAA = st.checkbox("I understand that this section shows my results based on my medical conditions.")
    TransitionBBB = st.button("Show results")
    return (TransitionAAA or TransitionBBB)