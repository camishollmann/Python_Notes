# Shortcuts for comments: Ctrl + K + C.
# Continue from 1:33:50 on Bro Code.

# We will now learn about sets.
# It is an unordered, unindexed collection.
# It DOES NOT accept duplicated values. 
# ALL ITENS ARE UNIQUE. 
# Sets use "{}".

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

# Useful methods:
utensils.add("napkin") # Adds a certain value to a set. Sets have no indexes.
utensils.remove("fork") # Removes an item from a set.
utensils.clear() # Removes all itens (clears) from the set.
utensils.update(dishes) 
# The "update" function adds a value (like a set) to a targeted set. 
# This adds "dishes" to "utensils".
# Use: targeted_set.update(new_item)
dinner_table = utensils.union(dishes) 
# The "union" function joins two sets together in one.

for x in dinner_table:
    print(x) 
# This prints the itens in a different order every time you run the program.
# It is unordered, and won't follow the declaration.
# This is faster for checking if something is present.

# Let's see what's in a set that is not on the other:
print(utensils.difference(dishes)) 
# The "difference" function does that. Prints what "utensils" has that "dishes"
# doesn't, in this case, "{'spoon', 'napkin'}".

# We can also see what they have in common, with "intersection()":
print(utensils.intersection(dishes))
# Prints "knife".