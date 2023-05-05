print("E2.2_040523.py")
# Excercises 2.2 & 2.3

# --- --- --- Excercise 1 --- --- ---
# Write a program that uses input to prompt a user for their name and then welcomes them.
#name = input("Enter your name:" )
#print('Hello ', name)

# --- --- --- Excercise 2 --- --- ---
# Write a program to prompt the user for hours and rate per hour to compute gross pay.....
Hour = input("Enter Hours: ")
Rate = input("Enter Rate: ")
Pay = float(Hour) * float(Rate) #Since input is considered integer, to have user input converted to another type such as float you can use float(x)...
print("Pay:", Pay)
