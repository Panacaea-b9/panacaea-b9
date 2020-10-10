# Patient coming with breathlessness
# This done on 26th Sep 2020
# Asking of questions about dyspnoea, orthopnoea and paroxysmal nocturnal dyspnoea
dyspnoea_query = ['Do you have an abnormal awareness of your breathing? ',
                  'How many pillows do you sleep with? ',
                  'Do you wake up at night to catch a breath? ']
dyspnoea_answer = ['Confirmed dyspnoea', 'Orthopnoea', 'Paroxysmal nocturnal dyspnoea']
for i in range(len(dyspnoea_query)):
    patientResponse = input(dyspnoea_query[i])
    if patientResponse.lower() == 'y':
        print(dyspnoea_answer[i])
        break
    else:
        continue

# Asking for tolerance when walking
marchTolerance = input('How far can you walk on a level ground before getting tired? ')
# Asking for arthritis in order to rule it out
vitalNegatives = input('Are you sure that you stop due to breathlessness or some other condition e.g Arthritis? ')

# Grading of the breathlessness using the New York Heart Association(NYHA/ nYHA)
nYHA_query = ['Nil at rest but some breathlessness on vigorous activity? Yes(Y), No(N): ',
            'Nil at rest but some breathlessness on moderate activity/ exertion? Yes(Y), No(N): ',
            'Mild breathlessness at rest and worse on mild activity/ exertion? Yes(Y), No(N): ',
            'Significant breathlessness at rest and worse on even the slightest activity? Yes(Y), No(N): ']
nYHA_classification = ['I', 'II', 'III', 'IV']
for i in range(len(nYHA_query)):
    patientResponse = input(nYHA_query[i])
    if patientResponse.lower() == 'y':
        print(nYHA_classification[i])
        break
    else:
        continue
print()


