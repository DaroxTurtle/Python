print('E11.2_050623.py')
import re

# Exercise 11.2
# Write a program to look for lines of the form:
# New Revision: 39772

# Extract the number from each of the lines using a regular expression and the findall() method.
# Compute the average of the numbers and print out the average as an integer.

Uinput = input('Enter file:')

fhand = open(Uinput)

count = 0
number = 0
total = 0

for line in fhand:
    line = line.rstrip()
    if re.findall('^New .*Revision:\s([^\s]*)', line):
        print(line)
        count = count + 1
        if count >= 1:
            line = line.split()
            number = int(line[2])
            total = total + number

print(int(total / count))
# I tried utilizing what I learned previously from chapters. But I dont think I did lol