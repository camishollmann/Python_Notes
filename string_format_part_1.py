# Shortcuts for comments: Ctrl + K + C.
# Continue from 2:21:20 on Bro Code.

# We will now learn about str.format() in Python.
# It's an optional method the gives users more control when 
# displaying output.

# The "format()" method is available for strings.

# Usual print:

animal = "cow"
item = "moon"

# print("The " + animal + " jumped over the " + item)

# Now with format:
print("The {} jumped over the {}".format("cow", item))
print("The {1} jumped over the {0}".format(animal, item)) # Positional argument.
# The order can be altered by indexing the curly braces "{}".
print("The {animal} jumped over the {item}".format(animal="cow", item="moon")) # Keyword argument.
# Here, I commented the variables declaration.
# The keyword argument's values can be accessed through their keys, making the declaration of 
# variables unnecessary outside the scope of the "print()" function.

# There is yet another, more elegant way to write this:
# We will turn our string into a variable.
text = "The {} jumped over the {}"
print(text.format(animal, item))

# String format uses FORMAT FIELDS (placeholders - "{}"), and can have the values
# passed through the "format()" method into these placeholders. They work IN ORDER.
# The values can be strings or variables.
