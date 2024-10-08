# Shortcuts for comments: Ctrl + K + C.
# Continue from 2:13:30 on Bro Code.

# We will now learn about *args in Python.
# They are parameters that will pack all arguments into a tuple.
# They're useful because they can make a function accept a varying 
# amount of arguments.

# You see, "args" is short for "arguments".
# Using "*" initializes the values to a tuple. If it were "**", it would be 
# "kwargs" which initializes them as a dictionary.

def add(*args): # With that, we can use as many arguments as we want.
    sum = 0
    args = list(args) # We can cast it into a list, so we are able to modify it.
    args[0] = 0 # This actually works.
    for i in args:
        sum += i
    return sum

print(add(1, 2, 3, 4, 5, 6)) # Use as many arguments as you like!

# You can name "*args" however you want! It could be 
# "*stuff" (as long as you have "*"). A common convention is to just name
# it "*args".