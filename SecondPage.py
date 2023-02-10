import streamlit as st

def MessageDisplayA():
    st.header("Great! That’s one down.")
    st.subheader("Next up is your medical history. To give you the safest and most effective recommendation, we need you to provide us with any medical records that you can provide.")
    st.subheader("To prevent double dosing, we also need to know which vaccines you’ve already taken. Please include the brand and name of the vaccine. Click below to proceed to the next step!")

    TransitionAA = st.checkbox("I understand that this section is based on my medical conditions, if any.")
    TransitionBB = st.button("Continue")
    return (TransitionAA or TransitionBB)
