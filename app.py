from add_bg_from_local import *
from FirstPage import *
from UserPersonalInputs import *
from SecondPage import *
from medicalhistory import *
from ThirdPage import *
from output import *

add_bg_from_local("black.jpg")

st.image("logo.jpg")
FirstTransition = MessageDisplay()
if FirstTransition:
    FirstTransition = True
    PersonalDataCollection()
    CalculateAge()
    SecondTransition = StoringPersonalData()
    
    if SecondTransition:
        SecondTransition = True
        ThridTransition = MessageDisplayA()

        if ThridTransition:
            ThridTransition = True
            FourthTransition = medicalHistory()

            if FourthTransition:
                FourthTransition = True
                FifthTransition = MessageDisplayB()

                if FifthTransition:
                    FifthTransition = True
                    st.subheader("Based on the data provided, here's your result. We strongly request you to show the whole page to a medical official for further consultancy!")
                    OutputContent()