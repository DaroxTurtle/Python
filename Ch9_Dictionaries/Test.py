print('Test.py is where I modify my exercises to make them more proper.')

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
