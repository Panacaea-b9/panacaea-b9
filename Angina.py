# A simple anginal episode
# The patient is asked three questions and responses captured
# Written on 18th Sep 2020 by Jeff
# Asking questions
# Heaviness of the chest
chestHeaviness = input('Does the patient feel heaviness in your chest? Y=Yes, N=No: ')
# Physical exertion
physicalExertion = input('Did the patient do some hard work e.g walking up a stairs or lift heavy objects? Y=Yes, N=No: ')
# The use of GTN
useGTN = input('Has the patient used GTN and if so, was there relief? Y=Yes, N=No: ')

# Processing the responses
# Check for Typical Angina(TA)
if chestHeaviness.upper() == 'Y' and physicalExertion.upper() == 'Y' and useGTN.upper() == 'Y':
    print('Differential diagnosis for Typical Angina')
# Check for Not Angina
if chestHeaviness.upper() == 'N' and physicalExertion.upper() == 'N' and useGTN.upper() == 'N':
    print('This is NOT Angina')
# Checking for Atypical Angina(ATA)
if chestHeaviness.upper() == 'Y' and physicalExertion.upper() == 'Y' and useGTN.upper() == 'N':
    print('Differential diagnosis for Atypical Angina')
if chestHeaviness.upper() == 'Y' and physicalExertion.upper() == 'N' and useGTN.upper() == 'Y':
    print('Differential diagnosis for Atypical Angina')
if chestHeaviness.upper() == 'N' and physicalExertion.upper() == 'Y' and useGTN.upper() == 'Y':
    print('Differential diagnosis for Atypical Angina')
# Checking other diseases
if chestHeaviness.upper() == 'Y' and physicalExertion.upper() == 'N' and useGTN.upper() == 'N':
    print('This is Another Disease/ Non-anginal chest pain')
if chestHeaviness.upper() == 'N' and physicalExertion.upper() == 'Y' and useGTN.upper() == 'N':
    print('This is Another Disease/ Non-anginal chest pain')
if chestHeaviness.upper() == 'N' and physicalExertion.upper() == 'N' and useGTN.upper() == 'Y':
    print('This is Another Disease/ Non-anginal chest pain')
print()

# The doctor has to try n find the root cause if angina is suspected
atheroma_query = ['Is the patient overweight or obese? ',
                  'Has the patient ever had an issue with cholesterol? ',
                  'Has the patient gone for any check up on any metabolic imbalances like high cholesterol? ',
                  'Is the patient compliant with the medications given? ']

for i in range(len(atheroma_query)):
    patientResponse = input(atheroma_query[i])
    if patientResponse.lower() == 'y':
        continue
    else:
        break
print()

# Further inquiry for the type of Angina
angina_query = ['Is the chest pain induced by effort and then disappears with rest? ',
                'Does the chest pain increase with frequency and severity with minimal effort or even rest? ',
                'Is the chest pain precipitated with lying flat? ',
                'Does the patient look in good health yet experiencing chest pain but resolves rapidly with GTN? ']
angina_type = ['STABLE ANGINA', 'UNSTABLE ANGINA', 'DECUMBITUS ANGINA', 'VASOSPASTIC/PRIZMENTAL ANGINA']

for i in range(len(angina_query)):
    patientResponse = input(angina_query[i])
    if patientResponse.lower() == 'y':
        print('This could be', angina_type[i])
        break
    else:
        continue
print()

# Here, the doctor may need to add more information about the patient's condition
causation = ['']
patientInput = input("Patient's other causes... ")
causation.append(patientInput)
print()

# Prompting of the doctor for tests according to causative agents in order of highest suspicion to lowest
tests_to_be_done = ['ECG',
                    'Blood tests',
                    'EchoCG',
                    'Chest X-ray',
                    'If needed, further investigations needed to confirm an IHD diagnosis']

for i in range(len(tests_to_be_done)):
    print(tests_to_be_done[i])
print()

# For management of patient, the system may prompt management options based on established causative agents
# Needs more agility in selection of management options
management = ['Address exacerbating factors',
              'Secondary prevention of cardiovascular disease like',
              '\tStop smoking, regular exercise, dietary advice, hypertension and diabetes control',
              '\t75mg of Aspirin if not contraindicated',
              '\tAddress hyperlipidaemia',
              '\tConsider ACE inhibitors e.g If Diabetic',
              'PRN symptomatic relief',
              'Antianginal medication, 1st-line being beta blockers and calcium chanel blockers',
              'Revascularization']

for i in range(len(management)):
    print(management[i])
print()


