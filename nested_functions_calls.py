# Shortcuts for comments: Ctrl + K + C.
# Continue from 2:07:10 on Bro Code.

# We will now learn about nested function calls in Python.
# Function calls inside other functions calls.
# The innermost function calls are resolved first.
# The returned value is used as an argument for the next outer function.

# Instead of writing all this:
num = input("Enter a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)

# You can just write this:
print(round(abs(float(input("Enter a whole positive number: ")))))