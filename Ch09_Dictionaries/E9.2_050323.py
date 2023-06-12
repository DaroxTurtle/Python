print('E9.2_050323.py')

# Exercise 9.2
# Write a program that categorizes each mail message by which day of the week was the commit was done.
# To do this look for lines that start with 'From', then look for the third word and keep a running count
# of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

counter = dict()
Uinput = input('Enter a file name: ')

try:                                    # Try/Except
    fhand = open(Uinput)
except:
    print('File does not exist.')
    quit()

for line in fhand:                                  # For loop for finding the lines and counter
    if line.startswith('From '):                    # Finding lines that start with From.
        line = line.rstrip().split()                # Removing blank spaces
        days = line[2]                              # Line where the days are within the prompt
        counter[days] = counter.get(days, 0) + 1    # Counting the amount of days that was included

sortcounter = sorted(counter.items(), key=lambda x:x[1], reverse = True)    # Grabbed from the internet to sort dictionaries
convertedcounter = dict(sortcounter)                                        # Converting sorted counter
print(convertedcounter)
