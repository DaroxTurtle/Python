print("N5.1_040923.py")

# --- --- --- Loops and Iterations --- --- ---
# Loops starts with the "while x" variable.
# While loops are useful for codes that needs to have a sequence of numbers.

# -- -- -- Repeated Loop -- -- --
# Ex.
n = 5 

while n > 0 :   # Since n = 5, this is true. n is greater than 0. While this is true the indented part of the code will run, until n is not greater than 0.
    print(n)    # This prints the current number of n.
    n = n - 1   # this subtracts the current number of n with one.

print('Blastoff!') # This will run only after n is not greater than 0.
print(n)

# -- -- -- Infinite Loop -- -- --
# Ex.
#a = 5

#while a > 0 :   # Since a = 5, this will run until a is greater than 0.
#    print('Lather')
#    print('Rinse')

#print('Dry off') # WILL NEVER RUN BC THIS IS A FOREVER LOOP DUE TO no a = a - 1.

# -- -- -- Breaking Out of a Loop -- -- --
# The "break" statement ends the current loop and jumps to the statement immediately following the loop.
# It is like a loop test that can happen anywhere in the body of the loop.
while True:
    line = input('> ')
    if line == 'done' :
        break
    print(line)
print('Done!')

# -- -- -- Finishing an Iteration with continue -- -- --
# The "continue" statement ends the current iteration and jumps to the top of the loop and starts the next iteration.
while True:
    line = input('> ')
    if line[0] == '#' : # This is stating like a comment, this won't print line.
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')

# -- -- -- Indefinite Loops -- -- --
# Depends on the user until the loops is done.