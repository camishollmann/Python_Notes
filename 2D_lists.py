# Shortcuts for comments: Ctrl + K + C.
# Continue from 1:27:05 on Bro Code.

# We will now learn about 2D lists in Python.
# They are lists of lists.
# Entire lists are always printed between "[]".

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

print(food) # This will print a list made of the three lists.
# Prints all of the elements from each list, grouped on their own lists.

# If you want to access only one of the lists, you add an index with the
# desired list:
print(food[0]) # Will only print drinks.

# If you only want a specific element from a list, you add another index ("[]"):
print(food[0][1]) # Will only print "soda".
print(food[1][1]) # Will only print "hamburger". We changed the list, see?

# Make sure you don't try to reach something that isn't there.