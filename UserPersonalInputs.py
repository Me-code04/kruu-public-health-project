from datetime import datetime, date
import streamlit as st
import csv

def PersonalDataCollection():
    global name, dateOfBirth, gender, NIDorPP, cityORmunicipality, district
    st.title("Hi! :wave: Welcome to the Public Health Web Platform! We are here to help you with what vaccines you need to get!")
    st.header("To begin, please fill in your details below! :point_down:")
    name = st.text_input("Enter your name")
    dateOfBirth = st.date_input("Enter your date of birth")
    gender = st.selectbox("What is your gender?", ["Male","Female","Other"])
    if gender == "Male":
        st.header(":male-office-worker:")
    elif gender == "Female":
        st.header(":female-office-worker:")

    NIDorPP = st.text_input("Enter your National ID or Passport Number")
    cityORmunicipality = st.text_input("Enter the city/municipality you are living in")
    district = st.text_input("Enter the district you are living in")

age = 0
def CalculateAge():
    today = date.today()
    age = today.year - dateOfBirth.year

def StoringPersonalData():
    if (name != "") & (NIDorPP != "") & (cityORmunicipality != "") & (district != ""):
        if gender:
            st.subheader("Hi " + name + " ! :wave: Nice to have you here! Thank you for writing your details! To continue, please click on the 'Complete' button below! :point_down:")
            TransitionA = st.checkbox("I have fill out my personal data properly!")
            TransitionB = st.button("Complete")
    
            rows = NIDorPP+" "+name+" "+str(dateOfBirth)+" "+str(age)+" "+gender+" "+cityORmunicipality+" "+district
            ThisFile = open("UserData.txt", 'w')
            ThisFile.write(rows)
            ThisFile.close()           
            return (TransitionA or TransitionB)