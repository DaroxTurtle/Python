print('E9.5_050323.py')

# Exercise 9.5
# This program records the domain name (instead of the address) where the message was sent from instead
# of who the mail came from. At the end of the program, print out the conents of your dictionary.

# Code came from E9.3 & E9.4,
domains = dict()
uinput = input('Enter file name: ')

try: # Try / Except
    fhand = open(uinput)
except:
    print('The file does not exist.') 
    quit()

for line in fhand:
    if line.startswith('From '):
        line = line.rstrip().split()                    # Removing blank spaces and new lines
        email = line[1].split('@')                      # Making emails to two pieces, the username and the address
        domain = email[1]                               # Grabbing the address, after the @, @'gmail.com'
        domains[domain] = domains.get(domain, 0) + 1    # If domain does not exist in domains(dictionary), then place it there

print(domains)
