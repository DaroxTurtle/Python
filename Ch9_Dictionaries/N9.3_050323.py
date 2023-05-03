print('N9.3_050323.py')
# I stopped studying for awhile bc I got busy and lazy :P
# I'll make some thought notes or updates of my life at the same time. Lol
# I can't believe we're almost half way of 2023 already.

# We are given a prompt of three paragraphs found within the book that Charles' uses.
# In this Part of Chapter 9. We will be trying to figure out how to count the amount of texts,
# found within the paragraphs.

# --- --- --- Counting Words in Text --- --- ---

# A general pattern to count the words in a line of text is to split() the line into words,
# then loop through the words and use a dict() to track the count of each word independently.
# -- -- -- Counting Pattern -- -- --
counts = dict()
line = input('Enter a line of text: ') 
words = line.split()

print('Words:', words)
print('Counting...')

for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)

# --- --- --- Definite Loops and Dictionaries --- --- ---

# Even though dictionaries are not stored in order, we can write a for loop that goes through
# all the entries in a dictionary and looks up the values.

counts1 = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
for entry in counts1:
    print(entry, counts1[entry])

# -- -- -- Retrieving lists of Entries and Values -- -- -- 
# We can also use .keys() to retrieve their entry names and .values() to retrieve their values.
# .keys() is useful to retrieve the x in {x : y}. While .values() is to retrieve the y in {x : y}.
# .items() can also be used to retrieve both of the x values.
print(list(counts1))        # We can also use list() to retrieve similar to .keys()
print(counts1.keys())       # Retrieve the x on {x : y}
print(counts1.values())     # Retrieve the y on {x : y}
print(counts1.items())      # Retrieve both x and y on {x : y}

# --- --- --- Two Iteration Variables --- --- ---
# In a dictionary they are a key-value pairs using two iteration avariables.
# Each iteration, the first variable is the key and the second is the value.
jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}

for aaa, bbb in jjj.items(): # the aaa corresponds to the keys, while bbb is the value.
    print(aaa, bbb) # It only works if we use .items() in the for loop.