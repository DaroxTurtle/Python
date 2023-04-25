print('CodesDope.py LVL 1.3')
#DONE

# Take two integer values from user and print greatest among them.

print("Greatest among the numbers.")
Value1 = input("Please give a number: ")
FVal1 = int(Value1)
Value2 = input("Another number: ")
FVal2 = int(Value2)

if FVal1 > FVal2:
    print("The greater number is:", FVal1)
elif FVal1 < FVal2:
    print("The greater number is:", FVal2)
else:
    print("Both are equal.")