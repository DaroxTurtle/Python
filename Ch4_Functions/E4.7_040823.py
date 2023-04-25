print('E4.7_040823.py')

# Exercise 7: Rewrite the grade program from the previous chapter using a function
# called computegrade that takes a score as its parameter and returns a grade 
# as a string.

def computegrade(Score):
    try:
        Score = float(Score) # If input is an integer or float.
    except:
        print("Bad score") # If input not float then <-
        quit()
    # print("In computegrade", Score)
    if Score >= 1.01:                  
        return "Bad score"          
    elif Score <= 0.0:                 
        return "Bad score"           
    elif Score >= 0.9:
        return "A"
    elif Score >= 0.8:
        return "B"
    elif Score >= 0.7:
        return "C"
    elif Score >= 0.6:
        return "D"
    elif Score < 0.6:
        return "F"
    else:
        return "Bad score"
    # return Score

Score = input("Enter score: ")  # User input
finalscore = computegrade(Score) # using defined function computegrade.

print(finalscore)



