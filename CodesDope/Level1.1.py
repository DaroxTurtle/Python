print('CodesDope.py LVL 1.1')
#DONE

# A company decided to give bonus of 5% to their employee. Only if their years of service is more than 5 years.
# Ask the user for their salary and year of service and print the net bonus amount.

Sal = input("Please enter your annual salary: ")
YOS = input("Please enter your years of service: ")
Salfloat = float(Sal)
YOSfloat = float(YOS)
Bonus = 0

if YOSfloat >= 5:
    Bonus = Salfloat * 0.05
    print(Salfloat, '+', Bonus, '=', Salfloat + Bonus)
else:
    print('You are in-eligible for bonus.')
    print(Salfloat)
