print('E7.2_042523.py')

# Exercise 7.2
# Write a program that prompts for a file name, then opens that file
# and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence: 08475
# Count these lines and extract the floating point values from each of
# the lines and compute the average of those values and produce an 
# output as shown below. Do not use the sum() function or a variable
# named sum in your solution.

UI = input('Enter a file name: ')
FO = open(UI)
# User input and opening the file

count = 0
TotalFvalue = 0
# To find average and sum of X-DSPAM-Confidence.

for line in FO:
    if not line.startswith('X-DSPAM-Confidence: '):
        continue
    # If line doesnt include what we're looking for it is skipped.

    count = count + 1
    Fvalue = float(line[19:40])
    # If we find line we add 1 to the count and remove string to change it to float.

    TotalFvalue = TotalFvalue + Fvalue
    # Summing total value of X-DSPAM-Confidence
    
    Average = TotalFvalue / count
print('Average spam confidence:', Average)