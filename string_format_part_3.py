# Shortcuts for comments: Ctrl + K + C.
# Continue from 2:30:45 on Bro Code.

# We will now learn about str.format() in Python.
# It's an optional method the gives users more control when 
# displaying output.

# The "format()" method is available for strings.

# Let's format some NUMBERS:
number = 3.14159
number2 = 1000


# We want to print only the two first decimal digits.
print("The number pi is {:.2f}".format(number))
# We add ":.2f" . The "f" is for floats. Remember: A DOT, followed by the number of decimal digits
# and the letter "f".
print("The number is {:,}".format(number2)) # Here, we show how to add a comma "," to all the 1000's places.
print("The number is {:b}".format(number2)) # This is how we display a number as a BINARY.
print("The number is {:o}".format(number2)) # This is how we display a number as an OCTAL NUMBER.
print("The number is {:X}".format(number2)) # This is how we display a number as a HEXADECIMAL (upper case).
print("The number is {:x}".format(number2)) # This is how we display a number as a HEXADECIMAL (lower case).
print("The number is {:e}".format(number2)) # This is how we display a number in scientific notation (lower case).
print("The number is {:E}".format(number2)) # This is how we display a number in scientific notation (upper case).


