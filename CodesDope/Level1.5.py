print('CodesDope.py LVL 1.5')
#Done

# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

UIGrade = input("Enter grade score(0-100): ")
intGrade = int(UIGrade)

if intGrade <= 25:
    print("Grade F")
elif intGrade <= 45:
    print("Grade E")
elif intGrade <= 50:
    print("Grade D")
elif intGrade <= 60:
    print("Grade C")
elif intGrade <= 80:
    print("Grade B")
elif intGrade <= 100:
    print("Grade A")
else:
    print("Error")