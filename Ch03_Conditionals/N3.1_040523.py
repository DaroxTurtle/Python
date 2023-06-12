print('N3.1_040523.py')

# Chapter 3 Part 1
# --- --- --- Conditional Steps --- --- ---
# Allowing python to decide conditions for us

# Program Ex.
# x = 5

# if x < 10:
#   print('Smaller')
# IF X is less than 10 then it will run this one.

# if x > 20:
#   print('Bigger')
# However, if X is greater than 20, then it will run this one.

# print('Finis')
# Knowing the code ran properly.



# --- --- --- Comparison Operators --- --- ---
# They look at variables but do not change the variables
# This is useful for Boolean expressions to evaluate True / False or Yes / No answers.

# Program Ex.
# x = 5
# if x == 5 : 
#   print('Equals 5') # If X is equal to 5, then it prints...
# if x > 4 :
#   print('Greater than 4') # If X is greater than 4, then it prints...
# if x >= 5 :
#   print('Greater than or Equals 5') # If X is greater than or equal to 5, then it prints...
# if x < 6 :
#   print('Less than 6') # If X is less than 6, then it prints...
# if x <= 5 :
#   print('Less than or Equals 5') # If X is less than or equals to 5, then it prints...
# if x =! 6 :
#   print('Not equal 6') # If X does not equal to 6, then it prints...

co = input('Give me a number from 0-5: ' )
cox = int(co)
if cox <= 0 :
    print('Number must be in between 1-5.')
if cox == 1 :
    print('Equals to 1')
if cox == 2 : 
    print('Equals to 2')
if cox == 3 : 
    print('Equals to 3')
if cox == 4 : 
    print('Equals to 4')
if cox == 5 :
    print('Equals to 5')
if cox >= 6 :
    print('Number must be in between 1-5.')
print('Done.')

# --- --- --- Identation --- --- ---
# Increase indent after an if statement or for statement (after : )
# Identation is used on if and for statements.

# -- -- -- WARNING TURN OFF TABS -- -- --
# Tab key is 4 spaces not identations.
# Using tabs in Python will cause an indentation error.
# It is hard to figure out if they are both mixed.

###############################################
