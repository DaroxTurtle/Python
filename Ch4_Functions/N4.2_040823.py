print('N4.2_040823.py')

# Chapter 4 Section 2
# --- --- --- OUR OWN FUNCTIONS --- --- ---
# We create our own new function by using the "def" keyword followed by
# optional parameters in parentheses.

# We ident the body of the function.

# This creates the function but it wont execute what is inside of the def function.
# Example:

x = 5
print('Hello')

def print_lyrics(): # <--- We are defining print_lyrics. However this wont execute.
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
# Python is storing the stored code^. So it does not run when this line of code is executed.

print('Yo')

# -- -- -- Definitions and Uses -- -- --
# Once we create our own defined function, we can use it as many times as we want to.
# Meaning there is no limit on how many times we can use our "def" code.

# This is called the store and reuse pattern.
# Example on line below.
print_lyrics() 
# ^ Since we are adding this to our code. This will run as how we defined it.
# Refer to line with def print_lyrics().

x = x + 2
print(x)

# --- --- --- Arguments --- --- ---
# An argument is a value that is inside a function, also called the input.
# We use arguments so we can direct the function to do different kinds of work,
# What is inside the parentheses is called the argument.
# We put the arguments in parentheses after the name of the function.

# Example on line below.
# big = max('Hello world') <-- Argument.
# In this function we are looking for the biggest word. Which would be 'w'.

# --- --- --- Parameters --- --- ---
# A parameter is a variable which we use in the function definition.
# It is a "handle" that allows the code in the function to access
# the arguments for a particular function invocation.

# Example line below
def greet(lang) :       # The parameter and placeholder is (lang). 
    if lang == 'es':    
        print('Hola')
    elif lang == 'fr' :
        print('Bonjour')
    else:
        print('Hello')

greet('es')            # Since we replaced lang with 'es'. It prints Hola.
                       # Because we defined that if lang == 'es' ^

# --- --- --- Return Values --- --- ---
# Often a function will take its arguments. return is used in a function to define that it is the end of the statement.

# Example line below.
def Greeting(lang1) : 
    if lang1 == 'es':
        return 'Hola'
    elif lang1 == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

Name = input("Hello what is your name? ")
print(Greeting('en'), Name)
# A "fruitful" function is one that produces a result (or return value)
# The return statement ends the function execeution and sends back the result of the function.

# CONCLUSION,
# TO FUNCTION OR NOT TO FUNCTION...
# Organize your code into "paragraphs" capture a complete thought and "name it."
# Don't repeat yourself - make it work once and then reuse it.
# If something gets too long or complex, break it up into logical chunks and put those chunks in functions.
