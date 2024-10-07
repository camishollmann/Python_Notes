# Shortcuts for comments: Ctrl + K + C.
# Continue from 1:31:00 on Bro Code.

# We will now learn about tuples in Python.
# It is a collection which is ordered and unchangeable, used 
# to group together related data.
# We can have itens of DIFFERENT DATA TYPES in the same tuple.
# Lists could do that too, but it's unusual.

# Let's create a student record:
student = ("Camilla", 26, "female") # For tuples, we use "()".

print(student.count("Camilla")) # Counts how many times an element appears within a tuple.
print(student.index("female")) # The "index()" function returns the index of a certain value. 

for x in student:
    print(x) # Prints the values in the tuple

if "Camilla" in student: # Checks if a certain value can be found in a iterable.
    print("Camilla is here!")