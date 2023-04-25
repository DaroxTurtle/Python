print('E3.1_040623.py')

# Excercise 1: Rewrite your pay computation to give the employee
# 1.5 times the hourly rate for hours worked above 40 hours.

Hour = input("Enter Hours: ")
FloatingHour = float(Hour) # Float converted of Hour

Rate = input("Enter Rate: ")
FloatingRate = float(Rate) # Float converted of Rate

if FloatingHour > 40 :
    # print('Overtime')
    OvertimeHour = FloatingHour - 40
    OvertimePay = OvertimeHour * (FloatingRate * 1.5)
    FloatingHour = FloatingHour - OvertimeHour
    Pay = FloatingHour * FloatingRate + OvertimePay
    print("Pay:", Pay)
    # print(OvertimePay)
else :
    # print('Regular Time')
    Pay = FloatingRate * FloatingHour
    print("Pay:", Pay)

