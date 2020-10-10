# This is for a patient coming with suspected heart arrhythmia
# This is done on 1st Oct 2020
# Asking of questions
arrhythmia_query = ['Does the patient have an awareness of their heart beating(palpitations)? Y=Yes, N=No: ',
                    'Does the patient have Chest pain? Y-Yes, N=No: ',
                    'Does the patient feel they are about to lose consciousness(presyncope) or lost consciousness(syncope)? Y=Yes, N=No: ',
                    'Does the patient feel lightheaded and at times blurred vision(hypotension)? Y=Yes, N=No: ',
                    'Does the patient have shortness of breath when lying down, unusual fatigue and cough with frothy sputum(pulmonary oedema)? Y=Yes, N=No: ']
for i in range(len(arrhythmia_query)):
    patientResponse = input(arrhythmia_query[i])
    if patientResponse.lower() == 'y':
        continue
    else:
        continue
print()

# More information needed about the above symptoms
history = ['What were the precipitating factors? ',
           'Onset/offset of the symptoms...',
           'What was the nature of the symptoms(fast or slow, regular or irregular? ',
           'What was the duration of the symptoms? ',
           'What are the associated symptoms(chest pain, breathlessness, collapse)? ',
           'Review the drud history...']

for i in range(len(history)):
    patientResponse = input(history[i])
    if patientResponse.lower() == input():
        continue
    else:
        continue
print()


