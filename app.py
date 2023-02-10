from add_bg_from_local import *
from FirstPage import *
from UserPersonalInputs import *
from medicalhistory import *

add_bg_from_local("black.jpg")

FirstTransition = MessageDisplay()
if FirstTransition:
    PersonalDataCollection()
    CalculateAge()
    SecondTransition = StoringPersonalData()
    
    if SecondTransition:
        medicalHistory()