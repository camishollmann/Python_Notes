# Shortcuts for comments: Ctrl + K + C.
# Continue from 41:00 on Bro Code.

# Now we will get to know the mathematical functions 
# from the math library.

# Functions from the .math library: ceil, floor, sqrt.
# Functions that are native to Python: round, abs, pow, max, min.

import math

pi = 3.14

# The round functions rounds a number, eliminating the decimals.
# So, this will print "3". It is a built-in function.
print(round(pi))

# Now we can round a number UP, by using the "ceil()" function.
# This gets the ceiling/teto of the number. This will print "4".
print(math.ceil(pi)) # Available through the math library.

# We can use the "floor()" function to get the lower part 
# or floor/chão of a variable. This will print "3".
print(math.floor(pi)) # Available through the math library.

minus_pi = -3.14

# We have the "abs()" function for absolute values of a variable.
# Even if minus_pi is negative, it will become positive (absolute).
print (abs(pi)) # Will print "3.14".

# Now we have "pow()" ou power function. This elevates a variable 
# to a desired number. Write is as pow(base, exponent).
print(pow(pi, 2)) # This will print pi to the 2nd power or pi^2.

# Next we have square root or "sqrt()" function. This gives
# us the square root of a certain number, as a float.
print(math.sqrt(pi))

x = 1
y = 2
z = 3
elements = [0, 5, 3, 1] # This is a list. 
# A list is a changeable sequence of elements, normaly used for 
# keeping itens of a same data type.
# You can use [] or the list() builder.
# Examples: list ("abc") or list((1, 2, 3)).


# Obs: iterable types in python are lists, tuples, sets and dict (dictionaries).

# The max() function returns the largest value among a number of 
# individual variables or a iterable, like a list or a tuple. 
print(max(elements)) # This prints "5".

# The "min()" function returns the lowest value among a number of 
# individual variables or a iterable, like a list or a tuple.
print(min(elements)) # This prints "0".
print(min(x, y, z)) # This prints "1".
