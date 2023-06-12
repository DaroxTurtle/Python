print('N11.1_050623.py')

# --- --- --- Regular Expressions --- --- ---
# A sequence of characters that forms a search pattern

# --- --- --- Regular Expression Quick Guide --- --- --- 
# ^         Matches the beginning of a line
# $         Matches the end of the line
# .         Matches any character
# /s        Matches whitespace
# /S        Matches any non-whitespace character
# *         Repeats a character zero or more times
# *?        Repeats a character zero or more times (non-greedy)
# +         Repeats a character one or more times
# +?        Repeats a character one or more times (non-greedy)
# [aeiou]   Matches a single character in the listed set
# [^XYZ]    Matches a single character not in the listed set
# [a-z0-9]  The set of charactes can include a range
# (         Indicates where string extraction is to start
# )         Indicates where string extraction is to end

# --- --- --- Regular Expression Module --- --- ---
# Before we can use a regular expression in a program, we have to import the library using "import re"
# We can use re.search() to see if a string matches a regular expression, it is similar to using find() method for strings.
# We can use re.findall() to extract portions of a string that matches the regular expression, similar to a combination of find() and slicing var[5:10].

# -- Example --
# Before without Regular Expressions
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)
# After with Regular Expressions 
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)

# --- --- --- Wild-Card Characters --- --- --- 
# The dot(.) makes any character
# If you add the asterisk(*), the character is any number of times.