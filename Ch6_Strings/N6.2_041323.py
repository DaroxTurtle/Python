print('N6.2_041323.py')

# --- --- --- Operational Strings --- --- ---

# -- -- -- Slicing Strings -- -- --
# Pulling multiple letters in a string
# We can also look at any continous section of a string using a colon operator.
# When using ":" it will only go the previous letter that u had the number for.
# The second number is one beyond the end of slice -"up to but not including"

s = 'Monty Python'
# M o n t y _ P y t h  o n
# 0 1 2 3 4 5 6 7 8 9 10 11
print(s[0:4]) # It only prints Mont even though Y is the 4th number.
# >> Mont
print(s[6:7])
# >> P
print(s[6:20]) # If the second number is beyond the end of the string, it stops at the end.
# >> Python 

# If we leave off the first number or the last number of the slice, it is assumed to be the beginning or end of the string respectively.
print(s[:2])
# >> Mo
print(s[8:])
# >> thon
print(s[:])
# >> Monty Python

# -- -- -- String Concatenation -- -- --
# When the '+' operator is applied to strings it means concatenation.
a = "Hello"
b = "There"
print(a + b)

# -- -- -- String Library -- -- --
# Python has a number of string functions which are in the string library.

# These functions are already built into every string.
greet = 'Hello Bob'
zap = greet.lower() # This is similar to greet however it will be lower cased.

print(zap)
print(greet)
print('Hi There'.lower())

# -- -- -- Search and Replace -- -- --
# The replace() function is very useful to replace something found within a variable.
greet = 'Hello Bob'
nstr = greet.replace('Bob', 'June') # What ever is in the parenthesis of replace. It will be similar to greet.replace(replace this, with this)
print(nstr)