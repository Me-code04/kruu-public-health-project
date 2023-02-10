from add_bg_from_local import *
import streamlit as st
from AnalysisAndComparison import *

def input_international():
    st.slider("Estimated frquency of travelling in a year:", 1, 12, 1, 1)
    st.selectbox("Most frequently traveled region:", ["South Asia", "South East Asia", "North America", "Latin America", "South America", "East Asia", "Central Asia", "Russia", "Europe", "North Africa and Middle East", "Sub-Saharan Africa", "Australia", "Antartic"])

def dataOutput():
    storageFile = open("UserVAXData.txt",'a')
    strFactor = ""
    for i in range(len(factors)):
        strFactor += " " + str(factors[i])
    storageFile.write(strFactor)
    storageFile.close()

def medicalHistory():
    st.title("Welcome to the Medical History section! :wave: ")
    st.subheader("Here, we want to know your medical condition before recommending any vaccination. In Sri Lanka :flag-lk:, we are dealing with a variety of diseases that you can be immuned from through vaccines. As adults, these diseases can be life-threatning and lead to a unhealthy life or death. ")
    st.header("With no further ado, let's begin by ticking any of the following below based on your medical history! :point_down:")

    col1, col2 = st.columns(2)
    with col1:
        ReportedAllergies=st.checkbox("Any reported allergies after taking a vaccine")
        Asthma=st.checkbox("Asthma")
        HTN=st.checkbox("Hypertension")
        LiverDisease=st.checkbox("Liver Disease")
        Diabetes=st.checkbox("Diabetes")
        Allergies=st.checkbox("Allergies")
        Pregnant=st.checkbox("Pregnant")
        BloodTransfusion=st.checkbox("Under blood transfusion")
        st.checkbox("Senior Citizen")
    with col2:
        MSM=st.checkbox("Men having sex with men (MSM)")
        Immunocompromised=st.checkbox("Immunocompromised")
        Haemophilia=st.checkbox("Haemophilia")
        TB=st.checkbox("Tubercolosis (TB)")
        STD=st.checkbox("Any sexually transmitted disease (STDs)")
        SexActive=st.checkbox("Sexually active")
        GBS=st.checkbox("GBS (Guillain-Barré Syndrome)")
        Alcoholic=st.checkbox("Alcoholic")
        Smoker=st.checkbox("Smoker")

    userCondtion =[ReportedAllergies,Asthma,HTN,LiverDisease,Diabetes,Allergies,Pregnant,BloodTransfusion,MSM,Immunocompromised,Haemophilia,TB,STD,SexActive,GBS,Alcoholic,Smoker]
    userCondtionNumerated = []
    for idx in range(len(userCondtion)):
        if userCondtion[idx]:
            userCondtionNumerated.append(1)
        else:
            userCondtionNumerated.append(0)

    factors = Compare(userCondtionNumerated)


    st.header("We also want to know about your travel history internationally!")
    st.markdown("Have you travelled internationally within the past 1 year?")
    yes=st.checkbox("Yes, I have!")
    if yes:
        input_international()

    st.header("Have you taken any of the following vaccines previously?")
    col3, col4 = st.columns(2)
    with col3:
        st.checkbox("Hepatitis A")
        st.checkbox("Hepatitis B")
        st.checkbox("HPV - Human Papillomavirus")
        st.checkbox("Seasonal Flu (Influenza)")
    with col4:
        st.checkbox("MMR - Measles-mumps-rubella")
        st.checkbox("Pneumococcai")
        st.checkbox("Tdap - Tetanus, Diphtheria, and Pertussiss")
        st.checkbox("Covid-19 (with Booster or not)")

    st.subheader("Thank you for writing your details! To continue, please click on the 'Complete' button below! :point_down:")
    complete = st.button("Complete!", key="beta23", help="You will go to the next section after this on click!")
    if complete:
        dataOutput()
        return complete