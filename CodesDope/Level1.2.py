print('CodesDope.py LVL 1.2')
#DONE

# Take values of length and width of a rectangle from user and check if it is sqaure or not.

print('SQUARE CHECKER')
length = input('Please enter length of square: ')
flength = float(length)
width = input('Please enter width of square: ')
fwidth = float(width)

if flength == fwidth:
    print("This is a square.")
else:
    print("This is not a square.")