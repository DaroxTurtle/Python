hours = 40
rate = 35
pay = hours * rate
print (pay)

tax = 0.80
taxed = pay * tax
print (taxed)

Dedication = 0
while Dedication < 10:
    Dedication = Dedication + 1
    print (Dedication)

if Dedication == 10:
    print ('Good job! :) ')


eee = 'hello ' + 'there'
eee = eee + 1
# Will produce an error since python can't add an integer to a string.
type(eee)
# class 'str'

type('hello')
# class 'str'

type(1)
# class 'int' = integer means numbers.
# type() can be used to know what type of class it is.

# --- --- --- SEVERAL Types of Numbers --- --- ---
# Numbers have two main types - INTEGERS AND FLOAT

# Integers are whole numbers:
    # -14, -2, 0, 1, 100, 401233
    # THESE HAS NO DECIMALS.

# Floating Point numbers have decimals:
    # -2.5, 0.0, 98.6, 14.0
    # THESE HAVE DECIMALS.

# While there are other number types
# They are variations on float and integer.

# --- --- --- Type Conversions --- --- ---
# CONVERTING INTEGER TO FLOAT.

# When putting an integer and floating point in an expression:
# print(float(99) + 100)
# This will print 199.0, since it is listed on the name to print float of 99 + 100.

# --- --- --- Integer Division --- --- ---
# In Python 3.0, Dividing integers will result in a floating point.
# Ex. print(10 / 2)
# Outcome 5.0, instead of 5.

# --- --- --- String Conversion --- --- ---
# You can use int() and float() to convert between strings and integers.
# As long as the string is numbers then it can be converted onto an integer.

# Ex. sval = '123'
# type(sval) will be <class 'str'>

# However, if you do "ival = int(sval)" this will make ival as a string of sval.
# Meaning the outcome will be converted integer of sval which is ival.
# type(ival) will be <class 'int'>
# Now you can use math on ival since it is an integer.

# HOWEVER, YOU CANT CONVERT A STRING TO A INTEGER IF IT DOES NOT HAVE NUMBERS.

# --- --- --- User Input --- --- ---
# To have user input, we can use input() function.
# Ex. nam = input('Who are you? ')
# print('Welcome', nam)

# --- --- --- Converting User Input --- --- ---
# Using input() will be in string, however if you want to convert the input as integer.
# You can use, "int(x)." x is your variable.
