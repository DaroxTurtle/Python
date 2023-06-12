print('N11.2_050623.py')
import re

# I dont get Regular Expressions crying T.T

# --- --- --- Matching and Extracting Data --- --- ---
# re.search() returns a True/False depending whether the string matches the regular expression.
# If we actually want the matching strings to be extracted, we use re.findall()

x = 'My 2 favore numbers are 19 and 42'
y = re.findall('[0-9]+', x)
# + is Repeats a character one or more times
# the [0,9]+ is finding one or more digit strings which are 2,19, and 42.
y = re.findall('[AEIOU]+', x)
# + is repeat a character one or more times
# The [AEIOU] is looking at the letters(AEIOU) and they must be in caps.

# --- --- --- Greedy Matching --- --- ---
# If there is more than one strings that are similar, 
# Greedy matching chooses the largest possible string.
x = 'From: Using the : character'
# In x there is 2 colons. However, Greedy Matching will skip the first one and go to the next one.

y = re.findall('^F.+:', x) 
# ('^F.+:')
# (^F - first character in the match is an F)
# the . is any next character
# + is repeat 
# : is the last character to match
# so .+: is repeat until the last character matches the ':'.

# -- -- -- Preventing Non-Greedy Matching -- -- --
# To prevent Greedy Matching, we can add the '?' character.
y = re.findall('^F.+?:', x)
# By adding ? we only pick the first one.

# --- --- --- Fine-Tuning String Extraction --- --- ---
# To refine the match for re.findall() and seperately determine which portion of the match is to be extracted by using parenthesis.
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@\S+', x)
# ('\S+@\S+')
# \S is atleast one non-whitespace character
# So the code is to look for @ and copy the text that has it starting before the space and until the next space.
# in x, it will copy 'stephen.marquard@uct.ac.za' 

# Parenthesis are not part of what to look for but it tells you where to start and stop with what string to extract.
y = re.findall('^From (\S+@\S+)', x)
# Look for line with From and only find the @.
# What is inside the parenthesis will be extracted.
