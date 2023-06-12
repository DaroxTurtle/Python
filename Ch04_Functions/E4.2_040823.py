print('E4.2_040823.py')

# Exercise 2: Move the last line of this program to the top,
# so the function call appears before the definitions.
# Run the program and see what error message you get.

# ORIGINAL FUNCTION
#def print_lyrics():
#    print("I'm a lumberjack, and I'm okay.")
#    print('I sleep all night and I work all day.')

#def repeat_lyrics():
#    print_lyrics()
#    print_lyrics()

#repeat_lyrics()

# Answer down below.

repeat_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

#Answer
# The error message I get is that repeat_lyrics1() is not defined. 
# This is due to that the function call is ran before the function is created.

