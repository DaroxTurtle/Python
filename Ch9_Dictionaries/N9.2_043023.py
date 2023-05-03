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
#ccca = 'csev1' in ccc # in operator used to see if a key is in the dictionary.
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