print('E9.2_050323.py')

# Exercise 9.2
# Write a program that categorizes each mail message by which day of the week was the commit was done.
# To do this look for lines that start with 'From', then look for the third word and keep a running count
# of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

dictionary = dict()
Uinput = input('Enter file name: ')
try:
    fhand = open(Uinput)
except:
    print('File does not exist.')
    quit()

for line in fhand:
    line = line.rstrip()

    if line.startswith('From '):    # Finding From header
        split = line.split()
        Day = split[2]              # grabbing day from the file

        if Day not in dictionary:   # If the day is not in the dictionary.
            dictionary[Day] = 1     # Adding day to the dictionary
        else:
            dictionary[Day] = dictionary[Day] + 1   # If day is already in dictionary, add + 1.

sorteddictionary = sorted(dictionary.items(), key=lambda x:x[1], reverse=True) # sorting dictionary from highest value to lowest value
converted_dictionary = dict(sorteddictionary)   # Converting sorted dictionary
print(converted_dictionary)

