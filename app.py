from add_bg_from_local import *
from datetime import datetime, date
import streamlit as st
import csv

add_bg_from_local("vax6.jpg")
st.title("Hi! :wave: Welcome to the Public Health Web Platform! We are here to help you with what vaccines you need to get!")
st.header("To begin, please fill in your details below! :point_down:")
name = st.text_input("Enter your name")
dateOfBirth = st.date_input("Enter your date of birth")
print(type(dateOfBirth))
gender = st.selectbox("What is your gender?", ["Male","Female","Other"])
if gender == "Male":
    st.header(":male-office-worker:")
elif gender == "Female":
    st.header(":female-office-worker:")

NIDorPP = st.text_input("Enter your National ID or Passport Number")
cityORmunicipality = st.text_input("Enter the city/municipality you are living in")
district = st.text_input("Enter the district you are living in")

#CALCULATE Age
today = date.today()
age = today.year - dateOfBirth.year

if (name != "") & (NIDorPP != "") & (cityORmunicipality != "") & (district != ""):
    if gender:
        st.subheader("Hi " + name + " ! :wave: Nice to have you here! Thank you for writing your details! To continue, please click on the 'Complete' button below! :point_down:")
        complete = st.button("Complete!", key="alpha123", help="You will go to the next section after this on click!")

        rows = [[NIDorPP, name, dateOfBirth, age, gender, cityORmunicipality, district]]
        # name of csv file
        filename = "UserData.csv"
 
        # writing to csv file
        with open(filename, 'w') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)
     
            # writing the data rows
            csvwriter.writerows(rows)