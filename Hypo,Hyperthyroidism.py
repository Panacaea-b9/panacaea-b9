# A patient with hypothyroidism or hyperthyroidism
# Done on 23rd Sep 2020
# Looking at symptomatology
# Wt loss or gain
wt = input('Have you lost(L) or gained weight(G)? ')
# Appetite loss or gain
appetiteLossGain = input('Have you lost/anorexia(L) or gained appetite(G)? ')
# Temp tolerance
tempTolerance = input('Are you allergic to heat(H) or cold(C)? ')
# Bowel habits
bowelHabits = input('Do you have constipation(C) or diarrhoea(D)? ')
# Menstrual changes
menses = input('Do you have increased menstrual flows/menorrhagia(M) or reduced to none/oligomenorrhoea(O)? ')
# ease of movement and mobility
mvmt = input('Do you often feel tired/fatigue(F) or restless/akathisia(R)? ')
# Mental stability
mentalState = input('Do you often feel depressed(D) or irritable/ easily angered(I)? ')
# Eye features
eyeComplaints = input('Do you have puffy eyes(P) or visual problems(G)? ')
# Skin changes
skin = input('Is your skin dry(D) or sweaty(S)? ')
print()
# Processing responses
# Checking for Hyperthyroidism
if wt.upper() == 'L' and appetiteLossGain.upper() == 'G' and tempTolerance.upper() == 'H' and bowelHabits.upper() == 'D' and menses.upper() == 'O' and mvmt.upper() == 'R' and mentalState.upper() == 'I' and eyeComplaints.upper() == 'G' and skin.upper() == 'S':
    print('It is Hyperthyroidism')
# Checking for Hypothyroidism
if wt.upper() == 'G' and appetiteLossGain.upper() == 'L' and tempTolerance.upper() == 'C' and bowelHabits.upper() == 'C' and menses.upper() == 'M' and mvmt.upper() == 'F' and mentalState.upper() == 'D' and eyeComplaints.upper() == 'P' and skin.upper() == 'D':
    print('It is  Hypothyroidism')


