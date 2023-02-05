from add_bg_from_local import *
import streamlit as st
import csv

add_bg_from_local("vax8.jpg")
st.title("Welcome to the Medical History section! :wave: ")
st.subheader("Here, we want to know your medical condition before recommending any vaccination. In Sri Lanka :flag-lk:, we are dealing with a variety of diseases that you can be immuned from through vaccines. As adults, these diseases can be life-threatning and lead to a unhealthy life or death. ")
st.header("With no further ado, let's begin by ticking any of the following below based on your medical history! :point_down:")

col1, col2 = st.columns(2)
with col1:
    st.checkbox("Any reported allergies after taking a vaccine")
    st.checkbox("Asthma")
    st.checkbox("Hypertension")
    st.checkbox("Liver Disease")
    st.checkbox("Diabetes")
    st.checkbox("Allergies")
    st.checkbox("Pregnant")
    st.checkbox("Under blood transfusion")
with col2:
    st.checkbox("Men having sex with men (MSM)")
    st.checkbox("Immunocompromised")
    st.checkbox("Haemophilia")
    st.checkbox("Tubercolosis (TB)")
    st.checkbox("Any sexually transmitted disease (STDs)")
    st.checkbox("Sexually active")
    st.checkbox("GBS (Guillain-Barré Syndrome)")
    st.checkbox("Alcoholic")
    st.checkbox("Smoker")