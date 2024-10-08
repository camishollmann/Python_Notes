# Shortcuts for comments: Ctrl + K + C.
# Continue from 2:09:50 on Bro Code.

# We will now learn about variable scope in Python.
# The scope of a variable is the region that a variable is recognized.
# A variable is only avaible from inside the region it is created.
# A global and locally scoped versions of a variable can be created.

# Global scope:
name = "Camilla" # This is available inside and outside of functions.

# Local scope:
def display_name():
#    name = "Hollmann" # The variable "name" only exists inside this function.
    print(name)

display_name() # This uses the function to call the LOCAL variable.
print(name) # Printing the GLOBAL version.
# If tried to print the local, it youdl give the error
# "NameError: name 'name' is not defined".
# With the local "name" commented, the function will use the global version.