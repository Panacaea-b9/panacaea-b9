# Done on 12th October 2020
# A patient questioned on suspected rheumatic fever
# Use of the Jones criteria. There must be a streptococcal infection plus 2 majors or 1 major n 2 minors
# Asking of questions?
# Major criteria
count = 0
jonesMajor = ['Has the patient ever had their heart beat faster than normal(Carey Coomb murmurs/ CARDITIS)? Y=Yes, N=No: ',
              'Has the patient ever felt migrating joint pains(Flitting ARTHRITIS)? Y=Yes, N=No: ',
              'Does the patient have small, subcutaneous, painless nodules on extensor surfaces of joints and spine(NODULES)? Y=Yes, N=No: ',
              'Does the patient have geographical-type rash with red, raised edges and clear centre(ERYTHEMA MARGINATUM)? Y=Yes, N=No: ',
              'Does the patient have any involuntary semi-purposeful movements(SYDENHHAM CHOREA)? Y=Yes, N=No: ']

for i in range(len(jonesMajor)):
    patientResponse = input(jonesMajor[i])
    if patientResponse.lower() == 'y':
        continue
        count += 1
    elif patientResponse.lower() == 'y' and count >= 2:
        break
    else:
        continue
    print()

if patientResponse.lower() == 'y' and count >= 2:
    print('This could be RHEUMATIC FEVER...')


