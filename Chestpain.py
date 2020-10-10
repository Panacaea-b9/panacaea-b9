# Patient coming with a chest complaint
# This done on 25th Sep 2020
# Asking of questions to describe the pain
# Using SOCRATES as our guide

# Asking the site of the pain
sitePain = input('Where is the pain located? ')
# Asking the onset of the pain
onsetPain = input('How and when did the pain begin? ')
# Asking the character of the pain
characterPain = input('What was the nature of the pain? ')
# Asking whether the pain radiates to any other part of the body
radiatePain = input('Do you feel the pain moving and settle to another part of the body? ')
# Asking what relieves the pain
alleviatePain = input('What do you do to relieve  the pain? ')
# Asking the time that the pain appears
timingPain = input('When does the pain appear? ')
# Asking what exacerbates the pain
exacerbatePain = input('What worsens the pain? ')
# Asking the severity of the pain
severityPain = input('What score would you give the pain or rate the pain? ')
# Asking for other associations with the pain
associationPain = input('Are there any associations with the pain? ')

# Processing the responses
# Checking for Angina
if sitePain.lower() == 'retrosternal' or sitePain.lower() == 'retro' or sitePain.lower() == 'mid chest' and characterPain.lower() == 'crushing' or characterPain.lower() == 'heaviness' or characterPain.lower() == 'tightness' and alleviatePain.lower() == 'rest' or alleviatePain.lower() == 'gtn' or alleviatePain.lower() == 'ntg' and exacerbatePain.lower() == 'physical exertion' or exacerbatePain.lower() == 'emotional weight' or exacerbatePain.lower() == 'cold':
    print('This is ANGINA')
# Checking for MI/ Heart Attack
if sitePain.lower() == 'retrosternal' or sitePain.lower() == 'retro' or sitePain.lower() == 'mid chest' and characterPain.lower() == 'crushing' or characterPain.lower() == 'persistent' and associationPain.lower() == 'nausea' or associationPain.lower() == 'vomiting' or associationPain.lower() == 'sweating' or associationPain.lower() == 'feeling of impending doom or death':
    print('This is MYOCARDIAL INFARCTION')
# Checking for Pericarditis
if sitePain.lower() == 'retrosternal' or sitePain.lower() == 'retro' or sitePain.lower() == 'mid chest' and characterPain.lower() == 'soreness' and alleviatePain.lower() == 'sitting forward' and exacerbatePain.lower() == 'inspiration':
    print('This is PERICARDITIS')
# Checking for Oesophageal spasm
if sitePain.lower() == 'retrosternal' or sitePain.lower() == 'retro' or sitePain.lower() == 'mid chest' and onsetPain.lower() == 'sudden' and characterPain.lower() == 'burning' and alleviatePain.lower() == '20 gtn'and timingPain.lower() == 'after eating' or timingPain.lower() == 'after drinking' and associationPain.lower() == 'hx of dysphagia' or associationPain.lower() == 'hx of dyspepsia':
    print('This is OESOPHAGEAL SPASM')
# Checking for GERD
if sitePain.lower() == 'retrosternal' or sitePain.lower() == 'retro' or sitePain.lower() == 'mid chest'  and characterPain.lower() == 'burning' and alleviatePain.lower() == 'antacids' and timingPain.lower() == 'after eating':
    print('This is GERD')
# Checking for Pleuritic Pain
if sitePain.lower() == 'one side' and characterPain.lower() == 'sharp' and exacerbatePain.lower() == 'inspiration' or exacerbatePain.lower() == 'coughing' and associationPain.lower() == 'breathlessness' or associationPain.lower() == 'cyanosis':
    print('This is PLEURITIC PAIN')
# checking for Musculoskeletal Pain
if sitePain.lower() == 'one side' and associationPain.lower() == 'injury' or associationPain.lower() == 'fracture' or associationPain.lower() == 'sore ribs':
    print("This is TIETZE'S SYNDROME")
# checking for Dissecting Aortic Aneurysm
if sitePain.lower() == 'retrosternal' or sitePain.lower() == 'retro' or sitePain.lower() == 'mid chest' and onsetPain.lower() == 'sudden'and characterPain.lower() == 'tearing' and severityPain.lower() == 'extreme':
    print('This is DISSECTING AORTIC ANEURYSM')
print()

# Face n Neck features


