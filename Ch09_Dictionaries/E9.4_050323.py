print('E9.4_050323.py')

# Exercise 9.4
# Add code to the above program to figure out who has the most messages in the file.
# After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop
# to find who has the most messages and print how many messages the person has.

# Code came from E9.3,
histogram = dict()
uinput = input('Enter file name: ')

try: # Try / Except
    fhand = open(uinput)
except:
    print('The file does not exist.') 
    quit()

for line in fhand:
    if line.startswith('From '):
        line = line.rstrip().split()
        email = line[1]
        histogram[email] = histogram.get(email, 0) + 1

lsf = -1        # Largest so far
lsfword = None  # Word from lsf
for k, v in histogram.items():          # for entry and value in histogram which is {x, y}
    if v > lsf:                         # if value is greater than largest so far,
        lsfword = k                     # then lsfword will be entry
        lsf = v                         # then lsf will be value

print(lsfword, lsf)