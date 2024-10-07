# Shortcuts for comments: Ctrl + K + C.
# Continue from 1:21:08 on Bro Code.

# A list is used to store multiple itens in a single variable.
# Basically an array.

food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]

food[0] = "sushi" # Replaces "pizza" with "sushi".

food.append("ice cream") # This will put an element on the END of the list.
food.remove("hotdog") # Will remove the desired element from the list.
food.pop() # Will remove (and return) the last element of the list.
food.insert(0, "cake") # Will insert a desired element in a desired index (index, element).
food.sort() # Will sort a list ALPHABETICALLY or IN ASCENDING ORDER.
food.clear() # Removes ALL elements of a list. Now it's empty.

# Printing all the elements in a list:
for x in food:
    print(x) # Prints all elements, jumping a line after each.