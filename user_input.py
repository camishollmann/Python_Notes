# Shortcuts for comments: Ctrl + K + C.
# Continue from 36:50 on Bro Code.

# We will now see how user input works in Python.
# This is where the fun begins!

# When we accept user input, it's always of the STRING("str") data type.
name = input("What is your name?: ") 
age = input("How old are you?: ") # Stangely, this is a STRING, not an "int".
height = float(input("How tall are you?: ")) # Here, we change the input type to "float".

print("Hello " + name + ".")
print("you are " + str(age) + " years old.")
print("You are " + str(height) + "m tall.") # To print "height", must cast it to "str" type.

# In order to use "age" for mathematical operations, we have to cast it
# to "int" or "float":
age = int(age)
# Another option is to cast it on the input, like this:
# age = int(input("How old are you?: "))
age = age + 1

print(age) # It works.