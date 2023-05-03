print('E9.3_050323.py')

# Exercise 9.3
# Write a program to read through a mail log, build a histogram using a dictionary
# to count how many messages have come form each email address and print the dictionary.

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

print(dictionary) 
# While the output is very similar, but their order is not similar.
# Idk how to fix it xd