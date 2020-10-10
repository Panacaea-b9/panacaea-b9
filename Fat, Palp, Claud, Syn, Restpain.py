# Asking for Fatigue, Palpitations, Claudication, Syncope and Rest pain
# Done on 28th Spe 2020
# Inquiring, quantifying and affirming fatigue
fatigue_query = ['Are you doing less than you used to previously? ',
                 'Is there decrease in activity due to fatigue or is it some any other reason? ',
                 'What are some of the activities have you had to give up due to fatigue? ',
                 'What are you able to be before becoming tired? ']
for i in range(len(fatigue_query)):
    patientResponse = input(fatigue_query[i])
    if patientResponse.lower() == 'y':
        continue
    else:
        break
print()

# Inquiring for palpitations
palpitation_query = ['Do you have any awareness of your heart pumping? ',
                     'When did the sensation start and stop? ',
                     'How long did it last? ',
                     'Did it come gradually or suddenly? ',
                     'Did you black out? And if so, how long did it last? ',
                     'Was the heartbeat felt fast, slow, or some other pattern? ',
                     'What were you doing when the palpitations began? ',
                     'Is there any relationship between it and eating or drinking? ',
                     'Is it precipitated or terminated by any medication taken? ',
                     'Are there any associative features to the palpitations?(chest pain, breathlessness, nausea, dizziness) ',
                     'Did you have to stop all of your activities to lie down? ']
for i in range(len(palpitation_query)):
    patientResponse = input(palpitation_query[i])
    if patientResponse.lower() == 'y':
        continue
    else:
        break
print()

# Inquiring for syncope
syncope_query = ['Did you lose any consciousness? ',
                 'Was the loss of consciousness sudden or gradual? ',
                 'How long did you lose consciousness? ',
                 'Was there any preceding or associative symptom such as nausea, chest pain, sweating? ',
                 'Is there any correlation between the use of medication and the loss of consciousness? ',
                 'When you came around/regained consciousness, were there any symptoms remaining? ',
                 'Was there any tongue biting? ']
for i in range(len(syncope_query)):
    patientResponse = input(syncope_query[i])
    if patientResponse.lower() == 'y':
        continue
    else:
        break
print()

# Inquiring for claudication
claudication_query = ['Do you feel a tight cramp on any of your leg muscles? ',
                      'Where is the pain usually; calf, thigh, foot, buttock? ',
                      'When does it appear; during exercise or what activity is usually done? ',
                      'Does the pain disappear when you rest? ',
                      'Do you feel any numbness or pins n needles on the skin of the affected part? ']
for i in range(len(claudication_query)):
    patientResponse = input(claudication_query[i])
    if patientResponse.lower() == 'y':
        continue
    else:
        break
print()

# Inquiring for rest pain
restPain_query = ['Is the pain continuous, severe on the buttocks, thighs, calf, foot? ',
                  'Is the pain "aching" in nature? ',
                  'Does it last through the day or night? ',
                  'Do you loose sleep over the pain? ',
                  'Is there relief by the hanging effect of the affected leg? ']
for i in range(len(restPain_query)):
    patientResponse = input(restPain_query[i])
    if patientResponse.lower() == 'y':
        continue
    else:
        break
print()


