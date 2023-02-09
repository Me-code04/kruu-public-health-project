import streamlit as st

def MessageDisplay():
    global Transition1
    st.markdown("""Welcome to Vax App! 
               This app shows your current vaccination status and recommendations to how you can improve your stance against viruses.
               We cross check your data with our database of medical symptoms and vaccine recommendations to tell you whether to get your vaccines or not! 
               Click below to input your details!""")

    Transition1 = st.button("Get Started")
