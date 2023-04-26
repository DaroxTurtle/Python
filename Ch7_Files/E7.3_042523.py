print('E7.3_042523.py')

# Exercise 7.3
# Sometimes when programmers get bored or want to have a bit of fun,
# they add a harmless Easter Egg to their program. Modify the program that 
# prompts the user for the file name so that it prints a funny message when
# the user types in the exact file name "na na boo boo". The program
# should behave normally for all other files which exist and don't exist.

UI = input('Enter the file name: ')

# Having the easter egg before the try and except statement prevents it from
# causing an issue where it would still print the except statement.
if UI == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        quit()

try:
    FO = open(UI)
except:
    print("File cannot be opened:", UI)
    quit()

count = 0
for line in FO:
    if line.startswith('Subject:'):
        count = count + 1

print('There were', count, 'subject lines in', UI)