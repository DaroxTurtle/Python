print('CodesDope.py LVL 1.7')
#DONE

# Write a program to print absolute value of a number entered by the user.
# E.g. -    Input: 1   Output: 1
#           Input: -1  Output: 1

Ival = input("Input: ")
Fval = int(Ival)

if Fval < 0:
    print("OUTPUT: ", Fval * -1)
else:
    print("OUTPUT: ", Fval)
