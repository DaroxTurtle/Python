print('E8.4_042823.py')

# Exercise 8.4
# Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using split() method.
# The program should build a list of words. For each word on each line
# check to see if the word is already in the list and if not append it to
# the list. When the program completes, sort and print the resulting words
# in python sort() order as shown in the desired output.

Uinput = input('Enter file name: ')
Fopen = open(Uinput)

lst = list()

for line in Fopen:
    line_split = line.rstrip().split()
    for word in line_split:
        if word in lst:
            continue
        else:
            lst.append(word)
lst.sort()
print(lst)


