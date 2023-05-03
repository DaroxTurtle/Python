print('N9.2_043023.py')

# --- --- --- Most Common Name (Making Histogram) --- --- ---
# Finding/Counting how many times a name shows up.
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)

ccc['cwen'] = ccc['cwen'] + 1
print(ccc)

# --- --- --- An error when a key is not in a dictionary --- --- ---
# When a key does not exist found in a dictionary, it will be an error.
# We can use the in operator to see if a key is in the dictionary.

#print(ccc['csev1'])
#ccca = 'csev1' in ccc # the in operator is used to see if a key is in the dictionary.
#print(ccca)

# -- -- -- Preventing if a key does not exist -- -- --
# We can avoid the traceback by doing a for loop, and if the key does not exist.
# It will be added.
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

# --- --- --- Get Method for dictionaries --- --- ---
# The pattern of checking to see if a key is in a dictionary
# and assuming a default value if the key is not there is so common
# that a method called .get() that does this for us.

# Default value if key does not exist(and no Traceback).
x = counts.get(name, 0) # In the parenthesis (name, 0). The 'name' is to see if it exists, and 0 is a value if it doesnt.
                        # This does not give a traceback if it does not exist.

# -- -- -- Simplified counting with get() -- -- --
# We can use get() and provide a default value of zero when the key is not in the dictionary, and just add one.
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
    # The get(name, 0) shows that if the name does not exist in counts dictionary. Then it will have be given the value of 1.
    # That's why it is .get(name, 0) + 1. The 0 indicates that if it does not exist give it a value of zero, then
    # the outside parenthesis which is + 1. Shows that key will be given a value of one.
    # Then if it exists, then it will already have a value of 1 then plus outside parenthesis + 1.
print(counts)