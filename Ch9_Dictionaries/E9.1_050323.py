print('E91_050323.py')

# Exercise 9.1
# Write a program that reads the words in words.txt and stores them as keys in a dictionary.
# It doesn't matter what the values are. Then you can use the in operator as a fast way to check
# whether a string is in the dictionary.

counts = dict()
File = open('words.txt')

for line in File:           # first for line loop is to split all the sentences to individual words
    split = line.split()    # .split() to make them individal words

    for word in split:                         # Putting them on dictionary
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] = counts[word] + 1

Uinput = input('Check whether string is in the dictionary: ')
print('Checking...')
Uoutput = Uinput in counts
try:
    print('It is on the dictionary and it appears:', counts[Uinput], 'time/s on the dictionary.')
except:
    print('It is not on the dictionary.')