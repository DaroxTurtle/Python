print('E6.1_041323.py')
#DONE

# Exercise 1
# Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string,
# print each letter on a separate line, except backwards.
letters = "ABCDEFGHIJKLMNOP"
index = len(letters) - 1

while index >= 0: 
    letter = letters[index]
    print(letter)
    index = index - 1

