print('CodesDope.py LVL 1.4')
#DONE

# A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# JUdge and print total cost for user.

print("One unit will cost 100,")
print("If quantity purchased is more than 1000. Then there will be 10% discount.")
Quantity = input("Please enter quantity for the wanted number of units: ")

FQuantity = float(Quantity)
UnitC = 100
Discount = 0.90

if FQuantity >= 1000:
    UnitC = (FQuantity * UnitC) * Discount
    print("Total discounted cost:", UnitC)
else:
    UnitC = FQuantity * UnitC
    print("Total cost:", UnitC)

