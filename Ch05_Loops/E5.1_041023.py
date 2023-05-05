print("E5.1_041023.py")

# Exercise 1: Write a program which repeatedly reads numbers until the user enters "done".
# Once "done" is entered, print out the total, count, and average of the numbers. If the user enters
# anything other than a number, detect their mistake using try and except and print an error message
# and skip to the next number.
count = 0
total = 0

while True:
    user = input('Enter a number: ')
    if user == 'done':
        break
    try:
        fuser = int(user)
    except:
        print("Invalid input")
        continue
    #print(user)
    count = count + 1
    total = total + fuser
print('Done!')
print(total, count, total / count)
