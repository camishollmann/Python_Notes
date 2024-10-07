# Shortcuts for comments: Ctrl + K + C.
# Continue from 57:05 on Bro Code.

# We will now learn about if statements in Python. It is a block of code 
# that will execute if it's condition is true.

age = int(input("How old are you?: "))
# We cast this as "int" so it does not return a "str" variable.

if age == 100: # If this is false, it will be skipped and the program will continue.
    print("You are a century old!")
elif age >= 18:
    print("You are and adult!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You are a child!")

# You can use an "if" by itself, an "if" with just an "else", or the "if" with one or
# more "elif" and an "else".

# The comparison operator is DOUBLE EQUALS ("==").
# The order of your statements DOES MATTER.