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
# If we construct a list of Tuples of the form (Value, Key) we could sort by Value.
# We do this with a for loop that creates a list of Tuples.
c = {'a':10, 'b':1, 'c':22}
tmp = list()                    # A temporary Tuple.
for k, v in c.items():          # I converted c variable to be a Tuple
    tmp.append( (v, k) )        # I did the opposite instead of doing (k, v), I did (v, k) so we can sort the Values instead of the Keys.
                                # However, this is still not sorted. We placed the Values first. So we can sort them using sorted() function.
tmp = sorted(tmp, reverse=True) # reverse=True allows us to have a descending order of Values in a Tuple. Since, it will show the b Key to be first and c Key to be the last.

for v, k in tmp:
    print(k, v)                 # To sort them to (k, v), instead of (v,k)

# --- --- --- Even Shorter Version --- --- ---
d = {'a':10, 'b':1, 'c':22}
print( sorted( [ (v,k) for k,v in d.items() ] ) )
# List comprehension creates a dynamic list. In this case,
# we made a list of reversed tuples and then sort it.

