# The 'venv' folder creates a virtual enviroment
# which separates the enviroment's own packages
# from the "base" enviroment's packages.
# A virtual enviroment has it's own self-contained
# packages.
# Only the packages explicitly installed in the
# virtual enviroment are available.

# Continue from the beginning on Bro Code.

print("hello world")
print('hello world')

# As aspas podem ser simples ou duplas.
# You can use double or simple quotes.

# Part 1 - Variables 
# A variable is a container for a value. It behaves as the value
# that is contains.

# You can have things like:

x = "Bro" 
y = 21 
z = False 

# We're gonna see strings first
first_name = "Bro"

# Now, we will combine our string variable with another string
# while printing. 
print("Hello " + first_name)

# Let us print the variable type now. The result will be 
# <class 'str'>, indicating this is a string. 
print(type(first_name))

# You can combine variables together as longs as they're the 
# same data type.
# For variables, we use snake_case.

# Let us create another two variables now.
last_name = "Code"

# The third will be a combination of the other two AND A SPACE.
full_name = first_name + " " + last_name

print("Hello " + full_name)

# Now for integers/int.
age = 26
age += 1

print(age)
print(type(age))

# We must convert the integer to a string so we can
# concatenate it with another string. 
# This is called type casting. It is quite
# essential in python.
print("Your age is: " + str(age))

# We can print an integer by itself, though.
print(age)

# Now for floats.
height = 250.5

print("Your height is: " + str(height) + " cm")
# print(type(height))

# The last data type we are going to cover
# is the boolean data type.
human = True
print(human)
print(type(human))
print("Are you a human? " + str(human))

# This is it for variables.