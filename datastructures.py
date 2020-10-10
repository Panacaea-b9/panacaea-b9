            # LISTS
# A Tale of 2 Loops
friends = ['Joseph', 'Glenn', 'Sally']

for friend in friends: # Method 1
    print('Happy New Year:', friend)

for i in range(len(friends)): # Method 2
    friend = friends[i]
    print('Happy New Year:', friend)

jon_snow = ['Jon Snow', 'Winterfell', 30]
print(jon_snow)

print(jon_snow[1]) # Indexing

print(len(jon_snow)) # Length of list

print(jon_snow[2])
jon_snow[2] += 3
print(jon_snow[2]) # Data in lists are mutable or modifiable

num_seq = range(0, 10) # A sequence from 0 to 9
num_list = list(num_seq) # The list() method casts the sequence into a list
print(num_list)

num_seq = range(3, 20, 3) # A sequence from 3 to 19 with a step of 3
print(list(num_seq))

world_cup_winners = [[2006, 'Italy'], [2010, 'Spain'], [2014, 'Germany'], [2018, 'France']]
print(world_cup_winners) # This is List-Ception

# Sequence indexing
print(world_cup_winners[1]) # Accessing '[2010, 'Spain']'
print(world_cup_winners[1][1]) # Accessing 'Spain'
print(world_cup_winners[1][1][0]) # Accessing 'S'

part_A = [1, 2, 3, 4, 5]
part_B = [6, 7, 8, 9, 10]
merged_list = part_A + part_B
print(merged_list)
part_A.extend(part_B) # Using the extend() property
print(part_A)

            # Common List operations
# Adding elements
num_list = [] # Empty list
num_list.append(1) # Adding 1
num_list.append(2)
num_list.append(3)
print(num_list)

# Removing elements
houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
last_house = houses.pop() # The last element
print(last_house) # Outputs the last element
print(houses)

print(houses)
houses.remove('Ravenclaw') # For a particular element in a list
print(houses)

# For nested list
populations = [["Winterfell", 10000], ["King's Landing", 50000], ["Iron Islands", 2000]]
print(populations)
populations.remove(["King's Landing", 50000])
print(populations)

# List Slicing
num_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(num_list[2:5])
print(num_list[0::2])

# Index Search - Gives a boolean value
cities = ["Nairobi", "Paris", "Kampala", "Dar es Salaam", "Rome"]
print(cities.index("Dar es Salaam"))
print("Nairobi" in cities)
print("Dubai" in cities)
print("Seoul" not in cities)

# List Sort
num_list = [20, 10, 40, 50.4, 100, 5]
num_list.sort()
print(num_list)

# List Comprehension
nums = [10, 20, 30, 40, 50]
nums_double = [n * 2 for n in nums if n % 4 == 0]
print(nums)
print(nums_double)

list_1 = [30, 50, 110, 40, 15, 75]
list_2 = [10, 60, 20, 50]

sum_list = [(n1, n2) for n1 in list_1 for n2 in list_2 if n1 + n2 > 100]
print(sum_list)

eti = "Learning to code is Awesome"
wat = eti.split() # Breaks into parts and produces a list of strings
print(wat)
print(len(wat))
print(wat[2])
for i in wat:
    print(i)

            # TUPLES
car = ("Mercedes Benz", "GT-R", 2020, "Magno grey")
print(len(car)) # Length
print(car[1]) # Indexing
print(car[2:]) # Slicing

# Merging Tuples
hero_1 = ("Ironman", "Tony Stark")
hero_2 = ("Spiderman", "Peter Parker")
hero_3 = ("Captain Marvel", "Carol Denvers")
awesome_team = hero_1 + hero_2 + hero_3
print(awesome_team)

# Nested Tuples
hero_1 = ("Ironman", "Tony Stark")
hero_2 = ("Spiderman", "Peter Parker")
hero_3 = ("Captain Marvel", "Carol Denvers")
awesome_team = (hero_1, hero_2, hero_3)
print(awesome_team)

# Searching whether an element exists
cities = ("Nairobi", "Paris", "Kampala", "Dar es Salaam", "Rome")
print("Moscow" in cities)
print(cities.index("Rome"))

            # DICTIONARIES
empty_dict = {} # Empty Dictionary
print(empty_dict)

phone_book = {"Batman": 468426,
             "Cersei": 237734,
             "Ghostbusters": 446789}
print(phone_book)

empty_dict = dict()
print(empty_dict)

phone_book = dict(Batman = 468426, Cersei = 237734, Ghostbusters = 446789) # Keys automatically converted to strings
print(phone_book)

# Accessing a key
phone_book = {"Batman": 468426,
             "Cersei": 237734,
             "Ghostbusters": 446789}

print(phone_book["Batman"]) # Method 1
print(phone_book.get("Cersei")) # Method 2

# Dictionary operations
phone_book = {"Batman": 468426,
             "Cersei": 237734,
             "Ghostbusters": 446789}

phone_book["Godzilla"] = 545667 # Adding
print(phone_book)
phone_book["Godzilla"] = 999985 # Updating
print(phone_book)
del phone_book["Batman"] # Removing
print(phone_book)
cersei = phone_book.pop("Cersei") # Outputs the value of the corresponding key
print(phone_book)
print(cersei)

last_added = phone_book.popitem() # Outputs the last added entry as a tuple
print(last_added)

phone_book = {"Batman": 468426,
             "Cersei": 237734,
             "Ghostbusters": 446789}

print(len(phone_book)) # Length of dictionary
print("Batman" in phone_book) # Existence check
print("Gypsy Danger" in phone_book)

phone_book = {"Batman": 468426,
            "Cersei": 237734,
            "Ghostbusters": 44678}

second_phone_book = {"Catwoman": 67423, "Jaime": 237734, "Godzilla": 37623}

phone_book.update(second_phone_book) # Copying contents
print (phone_book)

# Dictionary comprehension
houses = {1: "Gryffindor", 2: "Slytherin", 3: "Hufflepuff", 4: "Ravenclaw"}
new_houses = {n**2: house + "!" for (n, house) in houses.items()}
print (houses)
print (new_houses)


            # SETS
random_set = {"Educative", 1408, 3.142,
              (True, False)}
print (random_set)
print (len(random_set)) # Length of the set

empty_set = set()
print (empty_set)

random_set = set({"Educative", 1408, 3.142, (True, False)})
print (random_set)






