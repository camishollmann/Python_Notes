# Shortcuts for comments: Ctrl + K + C.
# Continue from 2:02:00 on Bro Code.

# We will now learn about return statements in Python.
# Functions send Python values/objects back to the caller.
# These values/objects are known as the function's return value.

def multiply(number1, number2):
    return number1 * number2
# You do not need a variable sometimes, you can just return the result directly.
# This uses less lines of code and looks prettier.

x = multiply(6, 8)
print(x)

# Can also use:
print(multiply(6, 8))
# Without the need to keep it in a variable.