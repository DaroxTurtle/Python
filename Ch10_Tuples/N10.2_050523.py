print('N10.2_050523.py')

# --- --- --- Sorting Lists of Tuples --- --- ---
# We can take advantage of the ability to sort a list of Tuples to get a sorted dictionary.
# Firstly, we sort the dictionary by the Key using .items() method and sorted() function.
a = {'a':10, 'b':1, 'c':22}
print(a)

print(a.items())
# By using .items() we can generate a Tuple from the Dictionary.

print(sorted(a.items()))
# Use the sorted() function to sort the Tuple.

# --- --- --- Using sorted() --- --- ---
# We can do this even more directly using the built in function sorted
# that takes a sequence as a parameter and returns a sorted sequence.
b = {'a':10, 'b':1, 'c':22}
for k, v in sorted(b.items()):  # .sorted() by Key.
    print(k, v)

# -- -- -- Sort by Value instead of Key -- -- --
# If we construct a list of tuples of the form (value, key) we could sort by value.
# We do this with a for loop that creates a list of tuples.
c = {'a':10, 'b':1, 'c':22}
tmp = list()                    # A temporary Tuple.
for k, v in c.items():          # I converted c variable to be a Tuple
    tmp.append( (v, k) )        # I did the opposite instead of doing (k, v), I did (v, k) so we can sort the values instead of the keys.
                                # However, this is still not sorted. We placed the values first. So we can sort them using sorted() function.
tmp = sorted(tmp) # reverse=True allows us to have a descending order of values in a Tuple. So, instead of (v, k) the reverse=True allowed me to reorder them to (k, v). 
print(tmp)                      # This will have 