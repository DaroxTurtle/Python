print('E10.3_050523.py')
import string # allows for string.ascii_lowercase

# Exercise 10.3
# Write a program that reads a file and prints the letters in decreasing order of frequency.
# Your program should convert all the input to lower case and only count the letters a-z.
# Your program should not count, spaces, digits, punctuation, or anything other than the letters a-z.
# Find the text samples from several different languages and see how letter frequency varies between languages.
# Compare your results with the tables at wikipedia.org/wiki/Letter_frequencies.

Uinput = input('Enter a file: ')
fhand = open(Uinput)
dictionary = dict()

for text in fhand:
    text = text.lower()
    for line in text:
        if line in string.ascii_lowercase:
            dictionary[line] = dictionary.get(line, 0) + 1
        
for letters, counts in sorted(dictionary.items()):
    print(letters, counts)