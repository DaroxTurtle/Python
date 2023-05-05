print('E3.2_040623.py')

# Excercise 3.2: Rewrite your pay program using try and except,
# so that your program handles non-numeric input gracefully by printing
# a message and exiting the program. The following shows two executions of
# the program.

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except: 
    print("Error, please enter numeric input.")
    quit()

if fh > 40:
    OTH = fh - 40           # Overtime Hours deducated from fh
    OTP = OTH * (fr * 1.5)  # Overtime Hours multiplied by rate
    fh = fh - OTH           # Standard Hours minus Overtime Hours to get = 40 for Sh
    Pay = (fh * fr) + OTP   # Pay rate for standard + Overtime pay
    print("Pay:", Pay)
else:
    Pay = fr * fh
    print ("Pay:", Pay)