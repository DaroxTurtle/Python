print("E4.6_040823.py")

# Exercise 6: Rewrite your pay computation with time-and-a-half
# for overtime and create a function called 'computepay' which takes
# two parameters (hours and rate).

def computepay(hours, rate):
    # print("In computepay", hours, rate)
    if hours > 40 :
        OvertimeHour = hours - 40
        OvertimePay = OvertimeHour * (rate * 1.5)
        hours = hours - OvertimeHour
        Pay = hours * rate + OvertimePay
    else :
        Pay = rate * hours
    # print("Returning", Pay)
    return Pay

Hour = input("Enter Hours: ")
FloatingHour = float(Hour)
Rate = input("Enter Rate: ")
FloatingRate = float(Rate) 

xp = computepay(FloatingHour, FloatingRate)

print("Pay:", xp)

