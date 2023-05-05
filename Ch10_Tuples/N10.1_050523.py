print('N10.1_050523.py')

# --- --- --- Tuples are like lists --- --- ---
# Tuples are another type of sequence that functions much like a list
# The elements in a Tuple starts at 0. 
x = ('Glenn', 'Sally', 'Joseph') # Tuples are code values stored in one single variable. Also, they are '()'.

# --- --- --- Difference in Tuples --- --- ---
# Once we create a Tuple, you cannot alter its contents.
# Compared to a list. Tuples can not be altered.

# --- --- --- Things not to do with Tuples --- --- ---
x = (3, 2, 1)
# try to sort, append, or reverse them. We can't alter them if they are a Tuple.
# Only .count() and .index() only use for Tuples.

# --- --- --- Tuples are more efficient --- --- ---
# Tuples are only useful if we make temporary variables to test.

# --- --- --- Tuples and Assignment --- --- ---
# We can assign a Tuple on the left-hand side of an assigment statement.
(x, y) = (4, 'fred') # There are two variables on the left hand side. "(x, y)"
print(y)

# --- --- --- Tuples and Dictionary --- --- ---
# The .items() method in dictionaries return a list of (key, value) in Tuples.
d = dict()
d['csev'] = 2
d['cwev'] = 4
for (k, v) in d.items():    # For Key and value in the dictionary.
    print(k, v)             # Print key and value from dictionary
tups = d.items()            # This will be Tuple
print(tups)       

# --- --- --- Tuples are Comparable --- --- ---
# The comparison operators work with tuples, and other sequences. If the first item in the Tuple is equal,
# Python goes on the next item until it finds items that are different. 
(0, 1, 2) < (5, 1, 2)       # Since 0 is less than 5. This will be True and it wont go to the other keys within the Tuple.
(0, 1, 20000) < (0, 3, 4)   # Similar with this one, since the first keys are 0 and 0. They are equal and will go to the next item which is 1 is less than 3, which is True.
('Jones', 'Sally') < ('Jones', 'Sam')   # In these strings in a Tuple, it will check which letter comes first. So, since both side have Jones. They will skip it and compare Sally and Sam.
                                        # Since Sally has a letter that goes first from a-z, which is the letter 'l' This is proven as True in Tuples, bc 'l' goes before 'm' in the alphabet.
('Jones', 'Sally') > ('Adams', 'Sam')   # Since A is greater than J this will be true. Due, to the alphabet. 

# In Tuples it does not matter what the next key is if the first key has been proven to be True or False.