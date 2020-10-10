X = [10, 20, 20, 20]  # A single no. in each array that would add to 70
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]

sum_70 = [(n1, n2, n3) for n1 in X for n2 in Y for n3 in Z if n1 + n2 + n3 == 70]
print(sum_70)

def permute(nums):  # No. triad that is different from a given array of no.
  result_perms = [[]]
  for n in nums:
    new_perms = []
    for perm in result_perms:
      for i in range(len(perm)+1):
        new_perms.append(perm[:i] + [n] + perm[i:])
        result_perms = new_perms
  return result_perms

my_nums = [4,5,6]
print("Original Collection: ",my_nums)
print("Collection of distinct numbers:\n",permute(my_nums))


def pythagoras(opposite_side, adjacent_side, hypotenuse):  # Finding the third side of triangle
    if opposite_side == str("x"):
        return "Opposite = " + str(((hypotenuse ** 2) - (adjacent_side ** 2)) ** 0.5)
    elif adjacent_side == str("x"):
        return "Adjacent = " + str(((hypotenuse ** 2) - (opposite_side ** 2)) ** 0.5)
    elif hypotenuse == str("x"):
        return "Hypotenuse = " + str(((opposite_side ** 2) + (adjacent_side ** 2)) ** 0.5)
    else:
        return "You know the answer!"


print(pythagoras(3, 4, 'x'))

five_seven = []  # No. divisible by 5 and 7 between 1500 and 2700

for r in range(1500, 2701):
    if r %5 == 0 and r %7 == 0:
        five_seven.append(r)
print(five_seven)

temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")  # Temp conversion
degree = float(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
  result = float((9 * degree) / 5 + 32)
  o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
  result = float((degree - 32) * 5 / 9)
  o_convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", o_convention, "is", result, "degrees.")

word = input('Type your word: ')  # Reversed wording
str_len = len(word)
for s in range(str_len - 1, -1, -1):
    print(word[s], end='')

m,n = 0,1  # Fibonacci numbers

while n < 50:
    print(n)
    m,n = n, m+n

print("Input lengths of the triangle sides: ")  # Check for triangle type
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
	print("Equilateral triangle")
elif x==y or y==z or z==x:
	print("isosceles triangle")
else:
	print("Scalene triangle")


import datetime  # Display current date n time
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


filename = input("Input the Filename: ")  # Printing the file extension entered by user
f_extensions = filename.split(".")
print ("The extension of the file is : " + repr(f_extensions[-1]))


from datetime import date  # Diff btwn 2 dates
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)


def histogram( items ):  # drawing a histogram
    for n in items:
        output = ''
        times = n
        while times > 0:
          output += '*'
          times = times - 1
        print(output)

histogram([2, 3, 6, 5])


color_list_1 = set(["White", "Black", "Red"]) # Print out colour that is in list 1 but not in list 2
color_list_2 = set(["Red", "Green"])

print(color_list_1.difference(color_list_2))


def personal_details():  # Displaying each variable in its own line
    name, age = "Simon", 19
    address = "Bangalore, Karnataka, India"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

personal_details()


import math  # Distance btwn 2 points
p1 = [4, 0]
p2 = [6, 6]
distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

print(distance)


import random  # Diff combinations with repeating a single character
char_list = ['a','e','i','o','u']
random.shuffle(char_list)
print(''.join(char_list))
































