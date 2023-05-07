print('N11.3_050623.py')
import re

# NVM I am slowly getting regular expressions. 
# They could have been useful for E10.3 as it was asking to find lowercase alphabet,
# and make a letter frequency.

# --- --- --- Even Cooler Regex Version --- --- ---
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('@([^ ]*)', line)
# @ is look through the string until you find an @.
# Then [^ ] non-blank characters. 
# * then 0 or more times until it finds a blank

# Refining
y = re.findall('^From .*@([^ ]*)')