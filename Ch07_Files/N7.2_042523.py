print('N7.2_042523.py')

# --- --- --- File Handle as a Sequence --- --- ---
# File handle can be treated as a database/sequence of strings is on a sequence.
# We can use the 'for' statement to iterate the file handle sequence.
# Remember - A sequence is an ordered set.

# --- --- --- Counting Lines in a File --- --- ---
# To count lines in a file use the 'for' loop to read each line.
# Ex.
fhand = open('mbox.txt')
count = 0                   # Count is used to count the number of lines in mbox.txt
for line in fhand:
    count = count + 1
print('Line Count:', count)

# --- --- --- Reading the *Whole* File --- --- ---
fhand = open('mbox-short.txt')
inp = fhand.read()          # read() is a function that reads all of the text found in mbox-short
                            # and compresses mbox-short.txt to be an individual line with \n's on it.
print(len(inp)) 

# --- --- --- Searching Through a File --- --- ---
# To search through a file we can use 'if' statements in our 'for' loop to only print lines that matches the criteria.
fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From'):
        print(line)
# However, the printed lines from mbox-short will have blank lines.
# This is because inside the file the end of the lines have a newline on them. (\n).
# The print statement also adds a newline to each line afterwards.

# --- --- --- Searching Through a File (Removing of black lines) --- --- ---
# To remove \n or newlines on searching through we can use 'rstrip()' function.
# The newline is considered as a "white space" and will be stripped using 'rstrip()'
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()    # We use 'rstrip()' function to remove the newlines.
    if line.startswith('From:') :
        print(line)

# -- -- -- Skipping with continue -- -- --
# We can also rewrite searching through a file
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):    # If the line does not start with 'From:'
        continue                        # Then this will continue and find one that starts with from.
    print(line)

# --- --- --- Selecting lines using 'in' --- --- ---
# To select lines we can use 'in' that searches for its selected criteria.
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)

# --- --- --- Counting Subject lines --- --- ---
fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)

# --- --- --- Bad File names --- --- ---
fname = input('Enter the file name: ')

# IF FILE CAN NOT BE FOUND THEN WE USE TRY AND EXCEPT.
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
    
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)

