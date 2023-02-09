conditions = ["Any reported allergies after taking a vaccine","Asthma","Hypertension","Liver Disease","Diabetes","Allergies","Pregnant","Under blood transfusion","Men having sex with men (MSM)","Immunocompromised","Haemophilia","Tubercolosis (TB)","Any sexually transmitted disease (STDs)","Sexually active","GBS (Guillain-Barré Syndrome)","Alcoholic","Smoker"]
HepA=[0,0,0,1,0,0,1,1,1,1,0,0,1,1,0,1,0]
HepB=[0,1,0,1,1,0,1,1,1,1,0,0,1,1,0,1,1]
MMR=[0,1,1,0,1,0,0,0,1,0,0,0,0,0,0,1,1]
Tdap=[0,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1]
Flu=[0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,1]
Pneumococai=[0,1,1,1,1,0,0,1,1,1,1,1,1,1,0,1,1]
HPV=[0,1,1,1,1,0,0,1,1,1,1,1,1,1,0,1,1]
Covid=[0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1]

def Compare(arrList):
    conditionsMatched = [0,0,0,0,0,0,0,0]
    for index in range(len(arrList)):
        if arrList[index] == HepA[index]:
            conditionsMatched[0] += 1
        if arrList[index] == HepB[index]:
            conditionsMatched[1] += 1
        if arrList[index] == MMR[index]:
            conditionsMatched[2] += 1
        if arrList[index] == Tdap[index]:
            conditionsMatched[3] += 1
        if arrList[index] == Flu[index]:
            conditionsMatched[4] += 1
        if arrList[index] == Pneumococai[index]:
            conditionsMatched[5] += 1
        if arrList[index] == HPV[index]:
            conditionsMatched[6] += 1
        if arrList[index] == Covid[index]:
            conditionsMatched[7] += 1
 
    return conditionsMatched