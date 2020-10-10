# Asking about cough and any expectorant coming from the nasal passages
# Done on 29th Sep 2020
coughDuration = eval(input('How long have you had the cough(in weeks)? '))
if coughDuration < 3:
    print('It is an ACUTE cough...')
    print('This could be LARYNGITIS, TRACHEITIS, EPIGLOTTITIS or  LRTI')
elif 3 >= coughDuration < 8:
    print('This is a SUBACUTE cough...')
    print('This could be USE OF ARBs ')
else:
    print('This is a CHRONIC cough...')
    print('This could be ASTHMA, OESOPHAGEAL REFLUX, PULMONARY OEDEMA, POSTNASAL DRIP, VIRAL INFECTION, INTERSTITIAL LUNG DISEASE, LUNG CANCER')
# Characterizations of cough
haemoptysis = input('Does the patient cough blood? Y=Yes, N=No: ')
if haemoptysis.lower() == 'y':
    print('Haemoptysis due to what? ')
    print('This could be INFECTION, BRONCHIECTASIS, CARCINOMA, PULMONARY EMBOLUS, PULMONARY VASCULITIS')


