# Shortcuts for comments: Ctrl + K + C.
# Continue from 1:47:25 on Bro Code.

# We will now learn about the index operator "[]".
# It gives acess to a sequence's element (str, list, tuples).

name = "camilla Hollmann!"

# Checking if the first element of our sequence (in this case, a string)
# is lower case. For that, we use the "islower()" method:
if (name[0].islower()):
    name = name.capitalize() # Capitalizes (upper case) the first Letter of a string.

print(name) # Prints "Camilla Hollmann!".

# We use indexes for creating substrings:
first_name = name[:7].upper() # You don't need to put "0" if you wish to start there.
# This is getting only "Camilla", then putting it to upper case (CAMILLA).

print(first_name) # Will print "CAMILLA"

# This time we will create a last name substring:
last_name = name[8:].lower() # Maeking it all lower case.
# We can leave the end index blank, for we wish to use the entire end of the string.

print(last_name)

# You can access the last element in a sequence by using negative indexes, too:
last_character = name[-1] # The first element from right to left.

print(last_character)