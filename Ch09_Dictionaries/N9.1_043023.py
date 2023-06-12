print('N9.1_043023.py')

# --- --- --- What is a Collection? --- --- --- 
# A Collection is where we can store multiple values in one variable.
# It acts as a storage that we can use.
# In a Collection it has many values in a single variable.

# --- --- --- What is NOT a Collection? --- --- ---
# A value that will be soon replaced or will be replaced in a variable.
# When a value or element found in a variable is replaced,
# this is not a Collection.
# If the old value of a variable is overwritten,
# then it is not considered a Collection.

# --- --- --- Definitions --- --- ---
# List
#   - A linear collection of values that stay in order.
#   - List is an organized collection.
#
# Dictionary 
#   - A "bag" of values, each with its own label.
#   - Dictionaries are un-organized Collection.
#   - It has a key or label found in a Collection,
#   - Then it can be retrieved from the Collection using the key/label you have created for them.

# --- --- --- Dictionaries --- --- ---
# In Python it allows to do fast database-like operations.
# In other languages dictionaries have different names:
#  Associate Arrays - Perl / PHP
#  Properoes or Map or HashMap - Java
#  Property Bag - C# / .Net

# Dictionaries are similar to bags with no order.
# We can use the "lookup tag or label" to find a label.
# Example
purse = dict()

purse['money'] = 12 # The ['money'] is an index we are labelling to the number 12.
purse['candy'] = 3
purse['tissues'] = 75

print(purse) # By printing,
# {'money': 12, 'candy': 3, 'tissues': 75} is the output.

# We can also find the lookup tag or label that we assigned to the value to search for the index.
print(purse['candy']) #['candy'] is the lookup tag or label.

# We can also modify the number found within the dictionary.
purse['candy'] = purse['candy'] + 2 # candy will have an addition of 2 integer value.

print(purse) # Printed output,
# {'money': 12, 'candy': 5, 'tissues': 75}

# --- --- --- Dictionary (Constants) --- --- ---
# In a Dictionary we can use curly braces as a constant. 
# In a curly brace '{}' we make the list by key : value pairs.
# We can make an empty dictionary using empty curly braces.
jjj = { 'chuck' : 1 , 'fred' : 42 , 'jan' : 100}
# 'chuck' is the key and the value for 'chuck' is 1.
