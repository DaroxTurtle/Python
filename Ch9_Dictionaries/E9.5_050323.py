print('E9.5_050323.py')

# Exercise 9.5
# This program records the domain name (instead of the address) where the message was sent from instead
# of who the mail came from. At the end of the program, print out the conents of your dictionary.

# Code came from E9.3 & E9.5,
domaindict = dict()     # Domain Dictionary
Uinput = input('Enter file name: ')

try:                                    # Try and Except so if file doesn't exist no traceback.
    fhand = open(Uinput)
except:
    print('The file does not exist.')
    exit()

for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        split = line.split()
        
        email = split[1].split('@')     # Splitting email address
        domain = email[1]               # Address of who it came from

        if domain not in domaindict:    # Adding domain to domaindict
            domaindict[domain] = 1
        else:
            domaindict[domain] = domaindict[domain] + 1

print(domaindict)