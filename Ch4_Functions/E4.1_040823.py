import random

print("E4.1_040823.py")

# Exercise 1: Run the program on your system and see what numbers you get.
# Run the program more than once and see what numbers you get.

RandomNumber = random.randint(5, 10) #(low, high)
# The random function is only of one many functions that handle random numbers.
# The function .randint() takes the parameters low and high,
# and returns an integer between low and high.

print(RandomNumber)

# To choose an element from a set of numbers at random, you can use .choice() function.
t = [1, 2, 3,]
y = random.choice(t) 
print(y)
