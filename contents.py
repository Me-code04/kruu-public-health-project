import streamlit as st

def HepAContent():
    with st.expander("Hepatitis A"):
        st.markdown("- Symptoms: Yellow skin or eyes, no appetite, stomach pain, throwing up, fever, diarrhea")
        st.markdown("- Vaccine required: Hepatitis A vaccine")
        st.markdown("- Transmission: Close contact, eating contaminated food or drinks")
        st.image("hepA.jpg")

def HepBContent():
    with st.expander("Hepatitis B"):
        st.markdown("- Symptoms: Fever, fatigue, no appetite, vomiting, dark urine, joint pain")
        st.markdown("- Vaccine required: Hepatitis B vaccine")
        st.markdown("- Transmission: Birth, close contact, sharing items with the infected")
        st.image("hepB.jpg")

def MMRContent():
    with st.expander("MMR - Measles, Mumps, Rubella"):
        st.markdown("- Symptoms: Fever, rash, headache, sore throat, muscle aches, loss of appetite")
        st.markdown("- Vaccine required: MMR vaccine")
        st.markdown("- Transmission: Through air and direct contact with the infected")
        st.image("mmr.jpg")

def TdapContent():
    with st.expander("Tdap - Tetanus, Diphtheria, Pertussis"):
        st.markdown("- Symptoms: painful stiffening of muscles. Difficulty breathing, heart failure")
        st.markdown("- Vaccine required: T dap vaccine")
        st.markdown("- Transmission: Through air(coughing and sneezing)")
        st.image("tdap.jpg")

def FluContent():
    with st.expander("Influenza - Flu"):
        st.markdown("- Symptoms: headaches, swelling, fever, body aches, wheezing")
        st.markdown("- Vaccine required: seasonal flu shot")
        st.markdown("- Transmission: through air")
        st.markdown("- Precautions: wear a mask around crowded places")
        st.image("flu.jpg")

def HPVContent():
    with st.expander("HPV - Human Papillovirus"):
        st.markdown("- Symptoms: pain growths or lumps around genitals")
        st.markdown("- Vaccine required: HPV vaccine")
        st.markdown("- Transmission: close contact( specially sex related)")
        st.markdown("- Precautions: Condoms are strongly recommended when having sex")
        st.image("hpv.jpg")

def CovidContent():
    with st.expander("Covid - 19"):
        st.markdown("- Symptoms: Fever, cough, lost sense of taste or smell, sore throat, fatigue, muscle aches")
        st.markdown("- Vaccine required: Moderna, Sinopharm, Pfizer, AstraZeneca, and many more options.")
        st.markdown("- Transmission: Through air")
        st.markdown("- Precautions: wear a mask around crowded places")
        st.image("covid19.jpg")

def PneumococaiContent():
    with st.expander("Pneumococai"):
        st.markdown("- Symptoms: Pneumonia and Lung Infection")
        st.markdown("- Vaccine required: PCV13, PCV15, or PCV20. Must ask medical consultant")
        st.markdown("- Transmission: Through air")
        st.markdown("- Precautions: wear a mask around crowded places")
        st.image("pcv.jpg")
