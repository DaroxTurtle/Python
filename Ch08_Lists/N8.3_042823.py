print('N8.3_042823.py')

# --- --- --- How strings and lists are related --- --- ---

abc = 'With three words'
print(abc)
# We can use .split() function to split the 3 words.
stuff = abc.split()
# This will split them onto 3 individual words to a list.
print(stuff)
# This will print them as a list.

for w in stuff :
    print(w)
# We can use a for loop to print the elements inside stuff,
# to print them on a seperate line.

# .split() function on default it removes spaces and make them onto a new line
# However, if we place what needs to be removed inside the parenthesis - '()'. 
# We can remove and split the elements.
# For ex.
line = 'first;second;third'
thing = line.split()
print(thing)
# This will not remove the semi colons as in default it removes spaces. 
# However, we can do .split(;) to remove the semi colons.
thing = line.split(';')
print(thing)
# This will remove the semi colons and make them onto 3 individual words in a list.

