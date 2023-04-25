print('E6.5_042423.py')

# Exercise 5: Take the following Python code that stores a string:
text = 'X-DSPAM-Confidence: 0.8475 '

# Use 'find()' and string slicing to extract the portion of the string after the colon character and then use the 'float()' function to convert the
# extracted string into a floating point number.

BColon = text.find('X')
#print(BColon)

AColon = text.find(': ')
#print(AColon)

#print(text[0:19])

fstr = float(text[19:30])
print(fstr, type(fstr))