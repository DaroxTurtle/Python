print('E8.1_042623.py')

# Exercise 8.1 
# Write a function called 'chop' that takes a list and modifies it, removing the first and last elements,
# and returns 'None'. Then write a function called 'middle' that takes a list and returns a new list that contains
# all but the first and last elements.

# -- -- -- For Chop Function -- -- --
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

def chop(lst):
    del lst[-1]
    del lst[0]

print('NoneChop:', chop(letters)) # Prints out None.
chop(letters)
print('NormalChop:', letters) # Prints Normal without the first and last elements.

# -- -- -- For Middle Function -- -- --
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

def middle(a):
    return a[1:-1]

print('Unchanged Middle:', letters) # This is the unmodified letters.
Mletters = middle(letters)
print('Changed Middle:', Mletters) # Modified letters without first and last elements.