print('E10.2_05023.py')

# Exercise 10.2
# This program counts the distribution of the hour of the day for each of the messages.
# You can pull the hour from the "From" line by finding the time string and then splitting that string into parts using the colon character.
# Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

# Removed try / except was unnecessary on code.

Uinput = input('Enter a file name: ')
fhand = open(Uinput)
dictionary = dict()

for line in fhand:
    if line.startswith('From '):
        line = line.rstrip().split()
        hour = line[5]
        hour = hour.split(":")
        hour = hour[0]
        dictionary[hour] = dictionary.get(hour, 0) + 1

for h, c in sorted(dictionary.items()):
    print(h, c)