print('N3.2_040623.py')

# Chapter 3 Part 2
# --- --- --- More Conditional Statements --- --- ---

# Multi-way Statements
# Introduction to elif statement

#MW penis size
MWi = 21
if MWi <= 4 : # If MWi is less than or equal to 4. Meaning it can be -inf to 4
    print('Very Small')
elif MWi <= 9 : # If MWi is less than or equal to 9. Meaning it can be 5 to 9.
    print('Average')
elif MWi <= 20 : # Same rule to line 13.
    print('BIG')
else : # If MWi does not follow the rules above.
    print('Bruh?')

# --- --- --- The try / except Structure --- --- ---
# Useful if code is not able to run. For example,
astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1

print ('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr)