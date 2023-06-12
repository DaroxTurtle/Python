print('N5.4_041023.py')

# -- -- -- Counting in a Loop -- -- --
# To count how many times we execute a loop,
# we introduce a counter variable that starts at 0
# and we add one to each time through the loop.

numbers = [9, 41 ,12, 3, 74, 15]

zork = 0    # In mnemonic variables zork is called count.

print('Before', zork)
for thing in numbers :
    zork = zork + 1
    print(zork, thing)
print('After', zork)

# -- -- -- Summing in a Loop -- -- --
# To add up a value we encounter in a loop,
# we introduce a sum variable that starts at 0
# and we add the value to the sum each time through the loop.

count = 0
print('Before', count)
for SL in numbers:
    count = count + SL
    print(count, SL)
print('After', count)

# -- -- -- Finding the Average in a Loop -- -- --
# An average just combines the counting(AC) and sum(AS) patterns
# and divides when the loop is done.

AC = 0
AS = 0

print('Before', AC, AS)
for value in numbers:
    AC = AC + 1
    AS = AS + value
    print(AC, AS, value)
print('After', AC, AS, AS / AC)

# -- -- -- Filtering in a Loop -- -- --
# We use an if statement in the loop to catch / filter
# the values we are looking for.

# Filtering a loop uses if
print('Before')
for value in numbers:
    if value > 20:
        print('Large number', value)
print('After')

# -- -- -- Search using a Boolean Variable -- -- --
# If we want to search and know if a value was found, we use a variable
# that starts at False and is set to True as soon as we find the value.

found = False
print('Before', found)
for value in numbers:
    if value == 3:          # We are looking for 3 on numbers.
        found = True
        print(found, value)
        break
    #print(found, value)
print('After', found)

# -- -- -- Finding the smallest value -- -- --
# NEW TYPE called None. None is a variable that is None.
# and "is" it is a greater use than the = sign.

smallest_so_far = None
print('Before', smallest_so_far)
for thing in numbers:
    if smallest_so_far is None:
        smallest_so_far = value
    elif value < smallest_so_far:
        smallest_so_far = thing
    print(smallest_so_far, thing)
print('After', smallest_so_far)

# -- -- -- Is and is not Operators -- -- --
# Python has an is operator that can be used in logical expressions.
# Implies 'is the same as'
# Similar to, == but stronger than.
# is not is also a logical operator.
