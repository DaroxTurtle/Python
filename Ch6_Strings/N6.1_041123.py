print("N6.1_041123.py")

# --- --- --- Strings --- --- ---

# String Data Type

# A string is a sequence of characters
# A string literal uses quotes 'Hello' or "Hello"
# For string, + means "concatenate"
# When a string contains numbers, it is still a string
# We can convert numbers in a string by using int()

# Reading and Converting
# This is the point where you can convert inputs to different type such as int and float.
# In Python we prefer to read data in using strings and then parse then convert the data to another type.

# Looking Inside Strings
# Strings are numbered starting from 0 as the first character.
# B a n a n a
# 0 1 2 3 4 5
# Index operator: x[0], useful to grab a letter in a custom variable.
# IT WILL BE AN ERROR IF YOU ARE TRYING TO LOOKING INSIDE A STRING IF IT IS LONGER THAN THE CHARACTER.

# Built in function called len() gives us the length of a string.
fruit = 'banana'
x = len(fruit)
print(x) # This will print the amount of letters found in fruit.

# -- -- -- Looping Through Strings -- -- --

# Using a while statement and an iteration variable, and the len function,
# we can construct a loop to look at each of the letters in a string individually.
index = 0
while index < len(fruit):   # while statement and len function
    letter = fruit[index]
    print(index, letter)
    index = index + 1       # Iteration Variable
# When we print this, this will print each individual letter from fruit variable.

# A definite loop using a for statement is much more elegant
# The iteration variable is completely taken care of by the foor loop
for letter in fruit:
    print(letter)

# -- -- -- Looping and Counting -- -- --
# To count how many letters are found in a custom variable,
# We can follow this similar code.
word = 'banana'
count = 0
for letter in word :
    if letter == 'a' :
        count = count + 1
print(count)
