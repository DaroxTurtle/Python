print('E11.1_050623.py')
import re

hand = open('mbox.txt')

Uinput = input('Enter a regular expression: ')

for line in hand:
    line = line.rstrip()
    find = re.findall(Uinput, line)

print(find)