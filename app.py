from add_bg_from_local import *
from FirstPage import *
from UserPersonalInputs import *
from medicalhistory import *

add_bg_from_local("black.jpg")

FirstTransition = MessageDisplay()
st.write(FirstTransition)
if FirstTransition == True:
    FirstTransition = True
    SecondTransition = PersonalDataCollection()
    CalculateAge()
    StoringPersonalData()
    
    if SecondTransition:
        SecondTransition = True
        medicalHistory()