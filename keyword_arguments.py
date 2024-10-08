# Shortcuts for comments: Ctrl + K + C.
# Continue from 2:05:00 on Bro Code.

# We will now learn about keyword arguments in Python.
# They are arguments preceded by an identifier when we pass them to a function
# The order of the arguments doesn't matter, unlike positional arguments
# Python knows the names of the arguments that our function receives.

# The order DOES NOT MATTER, for these arguments are KEYwords. 

def hello(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)

hello(last="da Silva", middle="Hollmann", first="Camilla")