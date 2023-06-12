print('E8.5_042823.py')

# Exercise 8.5
# Open the file mbox-short.txt and read it line by line. 
# When you find a line that starts with 'From '
# You will parse the From line using split() and print out the second word in the line
# Then print out a countat the end.

fname = input("Enter file name: ")
fh = open(fname)
count = 0

for line in fh:
    line = line.rstrip()
    if line.startswith('From '):
        linesplit = line.split()
        count = count + 1
        print(linesplit[1])

print("There were", count, "lines in the file with From as the first word")
