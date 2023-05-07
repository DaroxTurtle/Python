print('Autograder.py for Ch11')
# Enter the sum from the actual data and your Python code below:
import re

fhand = open('Actualdata.txt')
count = 0


for line in fhand:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        count = count + int(number)
print(count)