# Shortcuts for comments: Ctrl + K + C.
# Continue from 2:28:10 on Bro Code.

# We will now learn about str.format() in Python.
# It's an optional method the gives users more control when 
# displaying output.

# The "format()" method is available for strings.

# We will learn how to add PADDING:
name = "Camilla"

print("Hello, my name is {} Hollmann".format(name))
print("Hello, my name is {:10} Hollmann".format(name))
print("Hello, my name is {:<10} Hollmann".format(name)) # Left allign with ":<".
print("Hello, my name is {:>10} Hollmann".format(name)) # Right allign with ":>".
print("Hello, my name is {:^10} Hollmann".format(name)) # Center with ":^".

# Add a colon ":" to the format field and the amount of space you want to the 
# desired side to do it.