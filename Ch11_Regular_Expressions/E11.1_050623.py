print('E11.1_050623.py')
import re

# Exercise 11.1
# Write a simple program to simulate the operation of the grep command on Unix.
# Ask the user to enter a regular expression and count the number of lines that matched the regular expression.
count = 0

hand = open('mbox.txt')
Uinput = input('Enter a regular expression: ')


for line in hand:
    find = re.findall(Uinput, line)
    if len(find) > 0:
        count = count + 1

print('mbox.txt had', count, ' lines that matched', Uinput)