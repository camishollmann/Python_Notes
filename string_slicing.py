# Shortcuts for comments: Ctrl + K + C.
# Continue from 51:55 on Bro Code.

# Now we will learn methods for string slicing.
# Slicing means creating a substring by extracting elements from another string.

# Use "indexing[]" operator or "slice ()" function.
# Three optional arguments/fields: [start:stop:step].

name = "Camilla Hollmann"

first_name = name[0:6]

print(first_name) # This will print "Camill". 
# Now, why didn't it print the letter on index 6?
# This happens because the STOPPING index is EXCLUSIVE, and does 
# not include the character it stops on.
# For this to print "Camilla", we must use 7 as a stop index.

first_name = name[0:7]

print(first_name) # This will print "Camilla".

# If you leave the start argument blank, it will be assumed as "0" by Python.

last_name = name[8:16]

print(len(name)) # The name lenght is 16.
print(last_name) # This will print "Hollmann".

# You can also leave the stop point blank, and it will go all the way:

last_name = name[8:]

print(last_name) # This will print "Hollmann".

# Now for step: "step" is how much we are increasing our index by
# beetwing "start" and "stop". We can create a substring that will count 
# only every second caracter after the first. It is "1" by default.

funky_name = name[::2]

print(funky_name) # This will print "CmlaHlmn".

# Now we will see how we can reverse a string in Python.

reversed_name = name[::-1] # This is like counting backwards while covering the string.

print(reversed_name) # This will print "nnamlloH allimaC".

# Now we will learn about the "slice()"" function. This creates a reusable "slice()"
# object, which can be quite useful.

website1 = "http://google.com" # We will slice so we can have only "google".

# In the slice function, we have (start,stop,step), separated by a comma.

# For the "stop" here, we will use the negative index of a string character, and
# it begins with -1, on the character most right of the string. 
# It then goes to -2, -3 and -4. Like counting backwards.
# We will use this because website names vary. For getting ".com" we will
# get the NEGATIVE INDEX of -4. We will combine it with normal indexes.
slice = slice(7,-4) # This is a slice object. It works as an index object.

print(website1[slice]) # The "slice" is used as an index. Will print "google".

# We will now test another website.
website2 = "http://wikipedia.com"

print(website2[slice]) # Will print "wikipedia"

