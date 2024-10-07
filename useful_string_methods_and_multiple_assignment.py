# Continue from 20:25 on Bro Code.
# Shortcuts for comments: Ctrl + K + C.

# Our next theme is multiple assignment.
# It allows us to assign multiple variables at
# the same time in one line of code.

# Standard assignment:
# name = "Camilla"
# age = 26
# attractive = True

# Multiple assignment:
name, age, attractive = "Camilla", 26, True

print(name)
print(age)  
print(attractive)

# Now we are going to assign the SAME value to multiple variables:
Spongebob = Patrick = Sandy = Squidward = 30

# We will now see some useful string methods.
name = "Camilla Hollmann"

# Now we use len() to print the lenght (how long it is) of our string. 
# It displays the number of characters.
print(len(name))

# Now we have the find() method (IT STARTS WITH INDEX ZERO(0)). It tells
# us the FIRST index of the character we are looking for, working as a counter
# for the characters on the string.
print(name.find("H"))

# Now for capitalize(). It makes the FIRST LETTER OF THE STRING 
# turn into a capital letter.
print("camilla hollmann".capitalize())

# Next we have upper(). It will make all the characters
# on a string to turn into upper case letters.
print(name.upper())

# Next is lower(). It will make all the characters lower case.
print(name.lower())

# Next we have isdigit(). It returns true if the string is a digit/number.
# In this case, it is false.
print(name.isdigit())

# Next we have isalpha(). It returns True if the string is composed of 
# alphabetical letters only. It does NOT count space (" ") as an alphabet letter.
print(name.isalpha())

# The next method is count, and it counts the number of times a certain
# character appears on a string. You have to specify a letter.
print(name.count("a"))

# Now for the replace() method. It allows us to replace characters on a string.
# Use: replace("old character", "new character").
print(name.replace("a","o"))

# There's a fun thing about python: you can MULTIPLY STRINGS. 
# If you want to print a string 3 times, just do it *3.
print(name*3)