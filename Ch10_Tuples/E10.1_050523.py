print('E10.1_050523.py')

# Exercise 10.1
# Revise a prveious program as follows: Read and parse the "From" lines and pull out the addresses from the line.
# Count the number of messages from each person using a dictionary.

# After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary.
# Then sort the list in reverse order and print out the person who has the most commits.

histogram = dict()
Uinput = input('Enter a file name: ')

try:
    fhand = open(Uinput)
except:
    print('File does not exist.')
    quit()

for line in fhand:
    if line.startswith('From '):
        line = line.rstrip().split()
        mail = line[1]
        histogram[mail] = histogram.get(mail, 0) + 1

tmp = list()
for email, count in histogram.items():
    tmp.append( (count, email) )
tmp = sorted(tmp, reverse=True)
tmp = tmp[:1]

for count, email in tmp:
    print(email, count)