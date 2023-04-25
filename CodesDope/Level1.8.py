print('CodesDope.py LVL 1.8')
#DONE

# A student will not be allowed to sit in the exam if their attendance is less than 75%
# Take following input from user
# Number of classes held
# Number of classes attended
# print percentage of class attended
# Print if student is allowed to sit in exam or not.

CH = input("Please enter number of classes held: ")
fH = int(CH)
CA = input("Please enter classes attended: ")
fA = int(CA)

Percentage = (fA / fH)*100
print("Percentage of classes attended:", int(Percentage),"%")

if Percentage >= 75:
    print("You are allowed to partake on the exam.")
else:
    print("You are in-eligble to partake on the exam.")