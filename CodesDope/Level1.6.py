print('CodesDope.py LVL 1.6')
#DONE

# Take 3 age inputs from 3 people by the user, and determine the oldest and youngest among them.

Age1 = input("Please enter age of one person: ")
Age2 = input("Please enter age of 2nd person: ")
Age3 = input("Please enter age of last person: ")
try:
    FA1 = int(Age1)
    FA2 = int(Age2)
    FA3 = int(Age3)
except:
    print("Please enter numeric input.")
    exit()

if FA1 < FA2 and FA1 < FA3:
    print("Person 1 is the youngest.")
elif FA2 < FA1 and FA2 < FA3:
    print("Person 2 is the youngest.")
elif FA3 < FA2 and FA3 < FA1:
    print("Person 3 is the youngest.")

if FA1 > FA2 and FA1 > FA2:
    print("Person 1 is the oldest.")
elif FA2 > FA1 and FA2 > FA3:
    print("Person 2 is the oldest.")
elif FA3 > FA2 and FA3 > FA2:
    print("Person 3 is the oldest.")

