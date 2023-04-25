print('CodesDope.py LVL 1.9')
#DONE

# Modify level 1.8 to allow student to sit if they have a medical cause.
# Ask user if they have medical cause with ('Y' or 'N') and print accordingly.

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
    MedC = input("(Y/N) However, do you have a medical reason: ")
    if MedC == "Y":
        print("You are allowed to partake on the exam.")
    elif MedC == "N":
        print("You are in-eligble to partake on the exam.")
    else:
        print("Enter Y/N.")