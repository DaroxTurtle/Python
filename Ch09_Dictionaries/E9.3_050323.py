print('E9.3_050323.py')

# Exercise 9.3
# Write a program to read through a mail log, build a histogram using a dictionary
# to count how many messages have come from each email address and print the dictionary.

histogram = dict()
uinput = input('Enter file name: ')

try: # Try / Except
    fhand = open(uinput)
except:
    print('The file does not exist.') 
    quit()

for line in fhand:
    if line.startswith('From '):                            # Seperating texts with From
        line = line.rstrip().split()                        # Removing blank spaces and \n's.
        email = line[1]                                     # Grabbing email from lines
        histogram[email] = histogram.get(email, 0) + 1      # Counting how many messages came from that email.

print(histogram)
# While the output is very similar, but their order is not similar.
# Idk how to fix it xd