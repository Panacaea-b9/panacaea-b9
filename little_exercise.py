num_array = (2, 3, 4, 5, 0, 7, 8, 9)
even = 0
odd = 0
for i in num_array:
        if not i % 2:
            even  += 1
        else:
            odd += 1
print(even)
print(odd)

for x in range(0, 7):
    if x == 3 or x == 6:
        continue
    print(x)

m,n = 0,1

while n < 50:
    print(n, end=' ')
    m,n = n, m+n

for i in range(1, 51):
    if i %3 == 0 and i %5 ==0:
        print('FizzBuzz')
    elif i %3 == 0:
        print('Fizz')
    elif i %5 ==0:
        print('Buzz')
    else:
        print(i)

result_str=""
for row in range(0,7):
    for column in range(0,7):
        if ((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (1 < column < 5)):
            result_str=result_str+"*"
        else:
            result_str=result_str+" "
    result_str=result_str+"\n"
print(result_str)

result_str=""
for row in range(0,7):
    for column in range(0,7):
        if column == 1 or ((row == 0 or row == 6) and ( 1 < column < 5)) or (column == 5 and row != 0 and row != 6):
            result_str=result_str+"*"
        else:
            result_str=result_str+" "
    result_str=result_str+"\n"
print(result_str)

result_str=""
for row in range(0,7):
    for column in range(0,7):
        if column == 1 or ((row == 0 or row == 3 or row == 6) and (1 < column < 6)):
            result_str=result_str+"*"
        else:
            result_str=result_str+" "
    result_str = result_str + "\n"
print(result_str)

str = ""
for row in range(0,7):
    for column in range(0,7):
        if column == 0 or row == 6:
            str += "*"
        else:
            str +=" "
    str += "\n"
print(str)

str = ""
for row in range(0,7):
    for column in range(0,7):
        if column == 1 or column == 5 or (row == 2 and (column == 2 or column == 4) or (column == 3 and row == 3)):
            str += "*"
        else:
            str += " "
    str += "\n"
print(str)

str = ""
for row in range(0,7):
    for column in range(0,7):
        if ((column == 1 or column == 5) and (row != 0 or row != 6)) or ((row == 0  or row == 6) and 1 < column < 5):
            str += "*"
        else:
            str += " "
    str += "\n"
print(str)

dog_human = int(input('Enter human years: '))
first_two = 10.5
dog_dog = None
if dog_human <= 2:
    dog_dog = dog_human * first_two
elif dog_human > 2:
    dog_dog = 21 + ((dog_human - 2) * 4)
print(f'{dog_dog} yrs')

l = input("Input a letter of the alphabet: ")

if l in ('a', 'e', 'i', 'o', 'u'):
    print("%s is a vowel." % l)
elif l == 'y':
    print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
    print("%s is a consonant." % l)

no = int(input("Enter yo no: "))

for i in range(0, no + 1):
    for j in range(0, no + 1):
        table = i * j
        print('{0:3}'.format(table), end=' ')
    print()
