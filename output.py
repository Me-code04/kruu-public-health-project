import streamlit as st
from add_bg_from_local import *
 
add_bg_from_local("vax9.jpg")
ThisFile = open("UserVAXData.txt",'r')
vaxConditonsNum = ThisFile.readline().split()
if vaxConditonsNum[0] > 5:
    HepAContent()
if vaxConditonsNum[1] > 5:
    HepBContent()
if vaxConditonsNum[2] > 5:
    MMRContent()
if vaxConditonsNum[3] > 5:
    TdapContent()
if vaxConditonsNum[4] > 5:
    FluContent()
if vaxConditonsNum[5] > 5:
    PneumococaiContent()
if vaxConditonsNum[6] > 5:
    HPVContent()
if vaxConditonsNum[7] > 5:
    CovidContent()