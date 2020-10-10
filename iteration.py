# The "while loop" is better suited for indefinite loops
count = 1                   # initialize count
while count <= 5:          # should we continue
    count += 1              # add first the count, then
    print(count, end=' ')            # display count
print()                          # This will surpass the limit by 1

# The above is diff from the one below

counter = 1                 # initialize counter
while counter <= 5:        # should we continue
    print(counter, end=' ')          # display counter, then
    counter += 1            # increment counter
print()                     # This will NOT surpass the upper limit of 30


# The "for loop" is used for definite loops
for n in 1, 2, 3, 4, 5, 6, 7:
    print(n)
print()

for n in range(1, 8): # a much convenient way using the range function but the end is NOT included
    print(n)
print()

for n in range(30, 0, -5):
    print(n, end=' ') # displays in one horizontal line
print()


size = int(input('Please enter the table size: ')) # Getting no of rows n columns
for row in range(1, size + 1):
    for column in range(1, size + 1):
        product = row * column                  # compute product
        print('{0:6}'.format(product), end='')  # display product
    print()                                     # move cursor to next row


# Get the number of rows and columns in the table
size = int(input("Please enter the table size: "))
# Print a size x size multiplication table
# First, print heading: 1 2 3 4 5 etc.
print(" ", end='')                              # Print column heading
for column in range(1, size + 1):
    print('{0:4}'.format(column), end='')       # Display column number
print()                                         # Go down to the next line
# Print line separator: +-----------------
print("  +", end='')
for column in range(1, size + 1):
    print('----', end='')                       # Display line
print()                                         # Drop down to next line
# Print table contents
for row in range(1, size + 1):
    print('{0:3} |'.format(row), end='')        # Print heading for this row
    for column in range(1, size + 1):
        product = row*column                    # Compute product
        print('{0:4}'.format(product), end='')  # Display product
    print()                                     # Move cursor to next row


# Doing permutations
for q in 'xyz':
    for w in 'xyz':
        if w != q:
            for e in 'xyz':
                if e != q and e != w:
                    print(q, w, e)
