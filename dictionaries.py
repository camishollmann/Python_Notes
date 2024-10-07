# Shortcuts for comments: Ctrl + K + C.
# Continue from 1:40:05 on Bro Code.

# We will now learn about dictionaries.
# A dictionary is a changeable, unordered collection of unique key:value pairs.
# They are very fast because they use hashing, allowing quick access of a value.

# Writing: {"key1":value1,
#           "key2":value2,
#           "key3":value3}

capitals = {"USA":"Washington DC",
           "India":"New Dehli",
           "China":"Beijing",
           "Russia":"Moscow"}

# You can with:
# print(capitals["Russia"])

# A safer way to access a key (it checks the existence) is to use the "get()" method:
print(capitals.get("Germany")) # Returns "None" (key doesn't exist).
print(capitals.get("China")) # Returns "Beijing".

# We have an "update()" method for dictionaries. 
# To add a pais, one must use "{key:value}" formatting between the brackets ("()").
# Let us add new key:value pairs to it:
capitals.update({"Germany":"Berlin"})
# It can also be used to update/change values that already are on the dictionary:
capitals.update({"USA":"Las Vegas"}) # Use: ({"existing_key":"new_value"})

# If you want to print all the keys in a dictionary use the "keys()" method:
print(capitals.keys()) # Prints only the keys and not the values.

# We can also print the values present in a dictionary, without the keys.
# For that, we use the "values()" method:
print(capitals.values())

# For printing keys AND values, you can use the "itens()" method. This prints YOUR ENTIRE DICTIONARY:
print(capitals.items()) # Display every item in a dictionary (keys and their values).

# We have the "pop()" method for dictionaries. It removes a SPECIFIED key (and returns it).
# REMEMBER: dictionaries are UNORDERED and the value MUST BE SPECIFIED in "pop()":
capitals.pop("China") # This will remove the key:value pair of the specified key (MUST BE A KEY).

capitals.clear() # This clears the dictionary (REMOVES EVERYTHING).

# Another way to print the entire dictionary is to use a "for" loop. 
# This prints without the separators ((), [], ''):
for key, value in capitals.items():
    print(key, value)

