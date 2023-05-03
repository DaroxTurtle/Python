print('E9.4_050323.py')

# Exercise 9.4
# Add code to the above program to figure out who has the most messages in the file.
# After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop
# to find who has the most messages and print how many messages the person has.

# Code came from E9.3,
dictionary = dict()
Uinput = input('Enter file name: ')

try:                                    # Try and Except so if file doesn't exist no traceback.
    fhand = open(Uinput)
except:
    print('The file does not exist.')
    exit()

for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        split = line.split()
        email = split[1]
        if email not in dictionary:
            dictionary[email] = 1
        else:
            dictionary[email] = dictionary[email] + 1

bigword = None
bigcount = None

for largest, most in dictionary.items():
    if bigcount is None or most > bigcount:
        bigcount = most
        bigword = largest

print(bigword, bigcount)