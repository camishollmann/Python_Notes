# Shortcuts for comments: Ctrl + K + C.
# Continue from 25:15 on Bro Code.

# We are now going to learn about type casting. It consists
# on converting the data typeof a value to another data type.

x = 1 # int
y = 2.0 # float
z = "3" # str

# Converting float to int (will print "2"):
print(int(y))
# If you want the change to be PERMANENT, you have to reassign it.
print(z*3) # Because this is a string, it prints 3 three times (NOT "9").

print(type(x)) # This returns <class 'str'>.

y = int(y) # NOW it is permanent.
z = int(z) # Now it is an int and should print "9" on the next line.
x = float(x)

print(z*3)

# Now "x" will appear as a float("1.0"):
print(x)

# And to revert them to strings, we just use the "str" cast:
z = str(z)

print(z*3)

# This is useful when we need to print a variable along with a string, because
# you can't concatenate a string ("+") with a variable that has a different type.
print("X is: " + str(x))

# When you don't do that, you get the error:
# TypeError: can only concatenate str (not "float") to str.