print('E3.3_040623.py')

# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0
# If the score is out of ragne, print an error message. If the score is
# between 0.0 and 1.0, print a grade using the following table.
# >= 0.9    A
# >= 0.8    B
# >= 0.7    C
# >= 0.6    D
# < 0.6     F

Score = input("Enter score: ")  # User input
try:                            # Try is used to determine whether the user input
    FS = float(Score)           # was an integer or a float.
except:                         # if user input was an integer then,
    print("Bad score")          
    quit()

if FS >= 1.01:                  # If input score is higher than 1.01,
    print("Bad score")          # Then bad score
elif FS <= 0.0:                 # If input score is lower than 0.0,
    print("Bad score")          # Then bad score.
elif FS >= 0.9:
    print("A")
elif FS >= 0.8:
    print("B")
elif FS >= 0.7:
    print("C")
elif FS >= 0.6:
    print("D")
elif FS < 0.6:
    print("F")
else:
    print("Bad score")