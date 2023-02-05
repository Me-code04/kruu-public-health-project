conditions = ["Any reported allergies after taking a vaccine","Asthma","Hypertension","Liver Disease","Diabetes","Allergies","Pregnant","Under blood transfusion","Men having sex with men (MSM)","Immunocompromised","Haemophilia","Tubercolosis (TB)","Any sexually transmitted disease (STDs)","Sexually active","GBS (Guillain-Barré Syndrome)","Alcoholic","Smoker"]
HepA=[0,0,0,1,0,0,1,1,1,1,0,0,1,1,0,1,0]
HepB=[0,1,0,1,1,0,1,1,1,1,0,0,1,1,0,1,1]
MMR=[0,1,1,0,1,0,0,0,1,0,0,0,0,0,0,1,1]
Tdap=[0,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1]
Flu=[0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,1]
Pneumococai=[0,1,1,1,1,0,0,1,1,1,1,1,1,1,0,1,1]
HPV=[0,1,1,1,1,0,0,1,1,1,1,1,1,1,0,1,1]
Covid=[0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1]

NumConditionsMatchedHepA=0
NumConditionsMatchedHepB=0
NumConditionsMatchedMMR=0
NumConditionsMatchedTdap=0
NumConditionsMatchedFlu=0
NumConditionsMatchedPneumococai=0
NumConditionsMatchedHPV=0
NumConditionsMatchedCovid=0

def Compare(arrList):
    for index in range(len(arrList)):
        if arrList[index] == HepA[index]:
            NumConditionsMatchedHepA += 1
        elif arrList[index] == HepB[index]:
            NumConditionsMatchedHepB += 1
        elif arrList[index] == MMR[index]:
            NumConditionsMatchedMMR += 1
        elif arrList[index] == Tdap[index]:
            NumConditionsMatchedTdap += 1
        elif arrList[index] == Flu[index]:
            NumConditionsMatchedFlu += 1
        elif arrList[index] == Pneumococai[index]:
            NumConditionsMatchedPneumococai += 1
        elif arrList[index] == HPV[index]:
            NumConditionsMatchedHPV += 1
        elif arrList[index] == Covid[index]:
            NumConditionsMatchedCovid += 1
 
    ConditionsMatched = [NumConditionsMatchedHepA, NumConditionsMatchedHepB, NumConditionsMatchedMMR, NumConditionsMatchedTdap, NumConditionsMatchedFlu, NumConditionsMatchedPneumococai, NumConditionsMatchedHPV, NumConditionsMatchedCovid]
    return ConditionsMatched