print('E10.1_050523.py')

# Exercise 1: Revise a prveious program as follows: Read and parse the "From" lines and pull out the addresses from the line.
# Count the number of messages from each person using a dictionary.

# After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary.
# Then sort the list in reverse order and print out the person who has the most commits.

Uinput = input('Enter a file name: ')

try:
    fhand = open(Uinput)
except:
    print('File does not exist.')
    quit()

for line in fhand:
    if line.startswith('From '):
        line = line.rstrip().split()
        print(line)