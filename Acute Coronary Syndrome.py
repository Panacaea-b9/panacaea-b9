# A patient coming with suspected ACS
# Done on 30th Sep 2020
# This includes unstable angina and myocardial infarction
# Asking of questions
# Acute chest pain
chestPain = input('Does the patient have acute  central chest pain? Y=Yes, N=No: ')
# Duration
durationPain = input('Does the pain last more than 20 min? Y=Yes, N=No: ')
# other symptoms accompanying the main symptom
associativeSymptoms = input('Is the pain accompanied by Nausea, Sweatiness, Dyspnoea or Palpitation? Y=Yes, N=No: ')

# Processing of responses
if chestPain.lower() == 'y' and durationPain.lower() == 'y' and associativeSymptoms.lower() == 'y':
    print('This is Definitely ACS. \nUNSTABLE ANGINA or MYOCARDIAL INFARCTION.')
if chestPain.lower() == 'n' and durationPain.lower() == 'n' and associativeSymptoms.lower() == 'n':
    print('This is Definitely NOT ACS.')
if chestPain.lower() == 'y' and durationPain.lower() == 'n' and associativeSymptoms.lower() == 'n':
    print('This is NON-ANGINAL CHEST PAIN')
if chestPain.lower() == 'n' and durationPain.lower() == 'y' and associativeSymptoms.lower() == 'n':
    print('This is ANOTHER DISEASE')
if chestPain.lower() == 'n' and durationPain.lower() == 'n' and associativeSymptoms.lower() == 'y':
    print('This is ANOTHER DISEASE')
if chestPain.lower() == 'y' and durationPain.lower() == 'y' and associativeSymptoms.lower() == 'n':
    print('This is could be ACS.')
if chestPain.lower() == 'y' and durationPain.lower() == 'n' and associativeSymptoms.lower() == 'y':
    print('This is could be ACS')
if chestPain.lower() == 'n' and durationPain.lower() == 'y' and associativeSymptoms.lower() == 'y':
    print('This is ANOTHER DISEASE')

# Further information needed to get confirmation that is might be ACS
riskFactors = ['']
patientInput = input('More clerking to gain info...')
riskFactors.append(patientInput)
print()



