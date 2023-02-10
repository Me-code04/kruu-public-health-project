from add_bg_from_local import *
from FirstPage import *
from UserPersonalInputs import *
from medicalhistory import *

add_bg_from_local("black.jpg")

FirstTransition = MessageDisplay()
if FirstTransition:
    PersonalDataCollection()
    CalculateAge()
    StoringPersonalData()
    SecondTransition = st.button("I have finished!")
    if SecondTransition:
        medicalHistory()