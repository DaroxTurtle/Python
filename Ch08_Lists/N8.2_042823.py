print('N8.2_042823.py')

# --- --- --- Concatenating lists using the operator '+' --- --- ---
# The + operator can be used on list to concatenate.

# --- --- --- List can be sliced --- --- ---
# We can use [:] on lists.
# the 2nd number for slicing will not be included.
t = [9, 41, 12, 3, 74, 15]
print(t[1:3]) # Upto the 3rd one but not including.

# --- --- --- Building a list from Scratch --- --- ---
# We can create an empty list then add elements using the append method.
# The list stays in order on the elements that are added will be added to the list.
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
# Will print book first then 99.
stuff.append('Cookie')
print(stuff)
# This will be the last text printed.

# .append() is a method to use to add elements in a list.
# However, with .append() it is by order.

# --- --- --- Finding something in a list --- --- ---
# To find something in a list we can use 'in' and 'not in' operators.
# They only return logical operators, meaning True or False.
# They do not modify the list.
some = [1, 9, 21, 10, 16]
a = 9 in some
print(a)

b = 15 in some
print(b)

c = 20 not in some
print(c)

# --- --- --- Lists are in Order --- --- ---
# A list can hold multiple items and keep those items in the order until we modify them.
# A list can be sorted, using .sort().
# .sort() will sort by a-z.
friends = [ 'Joseph', 'Glenn', 'Sally']
print(friends)

friends.sort()
print(friends)

# --- --- --- Built-in Functions and Lists --- --- ---
# There are multiple of functions built in Python that takes lists are parameters.
nums = [3, 41, 12, 9, 74, 15]
print(len(nums)) # Number of text in nums
print(max(nums)) # Highest number in nums
print(min(nums)) # Lowest number in nums
print(sum(nums)) # Sum of nums
print(sum(nums)/len(nums)) # Average of nums

# -- -- -- Instead of writing -- -- --
total = 0
count = 0
while True :
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    count = count + 1
    total = total + value

average = total / count
print(average)

# -- -- -- We can write this instead -- -- --
numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print(average)
# The numbers we enter using a list() will be stored, however this 
# uses more memory than using total and count method.

