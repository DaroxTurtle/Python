print('E4.3_040823.py')

# Exercise 3: Move the function call back to the bottom
# and move the defintion of print_lyrics after the defintion of
# repeat_lyrics. What happens when you run this program?

# ORIGINAL FUNCTION
#def print_lyrics():
#    print("I'm a lumberjack, and I'm okay.")
#    print('I sleep all night and I work all day.')

#def repeat_lyrics():
#    print_lyrics()
#    print_lyrics()

#repeat_lyrics()

# Answer down below.

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

repeat_lyrics()

#Answer
# When I ran the program it does not change what so ever.
# This is due to the flow of execution.
# The flow of execution always starts at the first statement of the program, from top to bottom.
# Function definitions do not alter the flow of execution of the program, however the statements
# found inside the def functions are not executed until it is called.


