print('N12.5_050723.py')

# Continued of N12.4

# --- --- --- Using urllib in Python --- --- ---
# Since HTTP is so common, we have a library that does all the socket work for us and makes web pages look like a file

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

# No headers 

# --- --- --- Like a file --- --- ---
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts)

# --- --- --- Reading Web Pages --- --- ---

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())


# Continue to Parsing HTML.
