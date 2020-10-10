
            # THESE ARE BUILT IN FUNCTIONS
print(int("12")) # the string has to made up of numbers
print(int(23.5)) # truncates the decimal part and outputs the whole number
print(int(True)) # returns a boolean value and here it's a 1

print(ord('y')) # outputs the unicode value of lower case y

print(float(24)) # gives a decimal part of the whole number
print(float("11.4"))
print(float(False)) # gives the boolean value a decimal part

print(str(False))
print(str(75.6))

print(bool(10)) #  whole numbers given a True
print(bool(10.5)) # whole numbers with floating points given a True
print(bool(0)) # given a False hold a 0 value
print(bool(0.0)) # given a False as above
print(bool(0.3)) # given a True
print(bool("hello")) # strings are given a True

print(complex(12)) # such as algebraic expressions
print(hex(1235))

def yell_it(phrase):
    print(phrase.upper() + '!')
yell_it('weewe') # Parameter passed when the function is called

def shout_it(phrase = 'WEEWE'): # Parameter already initialized in a default setting
    print(phrase + '!')
shout_it()

def holla_it(phrase = str(input('Enter your phrase: '))): # Allows the user to pass a parameter
    print(phrase.upper() + '!')
holla_it()

            # THESE ARE LAMBDAS
pentable = lambda num : num * 5 # assigning a lambda to a variable
print(pentable(15)) # calling the lambda

concat_strings = lambda a, b, c : a[0] + b[0] + c[0] # used for concatenation too
print(concat_strings("World", "Wide", "Web"))

my_lambda = lambda num : "High" if num > 70 else "Low" # can be used for conditionals
print(my_lambda(89))

            # FUNCTIONS AS ARGUMENTS : MAKING A CALCULATOR

def add (n1, n2):
    return n1 + n2

def subtract (n1, n2):
    return n1 - n2

def multiply (n1, n2):
    return n1 * n2

def divide (n1, n2):
    return n1 / n2

def calculator (operation, n1, n2):
    return operation(n1, n2) # using 'operation' argument as a function

result = calculator(multiply, 23, 24) # using 'multiply' function as an argument
print(result)
print(calculator(divide, 1001, 7))

            # USING LAMBDAS
# For calculator
def calculator (operation, n1, n2):
    return operation(n1, n2)

result = calculator(lambda n1, n2: n1 / n2, 20, 30)

print(result)

# Another example
num_list = [0, 1, 2, 3, 4, 5]

double_list = map (lambda n: n * 2, num_list)

print(double_list) # this doesn't show
print(list(double_list)) # works but easy to forget the list keyword

int_list = [-30, 14, 4.5, 101, -23.5]

greater_than_0 = list(filter(lambda n: n > 0, int_list)) # much cleaner when  list is used in one line

print(greater_than_0)

def count_to_n(n):
    for i in range(1, n + 1):
        print(i, end=' ')
    print()

print('Just count to ten . . . ')
count_to_n(10)

def triple(n):
    return n * 3

w = triple(9)
print(w)

def count_to_z(z):
    for x in range(1, z + 1, 4):
        print(x, end=' ')

count_to_z(30)

def count_to_n(n):
    for i in range(1, n + 1):
        print(i, end=' ')
    print() # Outputs in a cascading manner

for i in range(1, 10):
    count_to_n(i)

import turtle
import random

def polygon(sides, length, x, y, color):
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()
    turtle.color()
    turtle.begin_fill()
    for i in range(sides):
        turtle.forward(length)
        turtle.left(360 // sides)
    turtle.end_fill()

# Disable rendering to speed up drawing
turtle.hideturtle()
turtle.tracer(0)

# Draw 20 random polygons with 3-11 sides, each side ranging
# in length from 10-50, located at random position (x, y).
# Select a color at random from red, green, blue, black, or yellow.
for i in range(20):
    polygon(random.randrange(3, 11), random.randrange(10, 51),
            random.randrange(-250, 251), random.randrange(-250, 251),
            random.choice(("red", "green", "blue", "black", "yellow")))
turtle.update()  # Render image
turtle.exitonclick() # Wait for user's mouse click




