# Shortcuts for comments: Ctrl + K + C.
# Continue from 1:13:05 on Bro Code.

# We will now learn about foor loops in Python. It's a statement that will 
# execute it's block of code a limited amount of times.
# We are going to create a countdown timer.

# The while loop = can be unlimited.
# The for loop = only limited.

import time 

# This will print numbers 1 to 10:
for i in range(10):
    print(i+1)

# We can also have range(start, stop). "Stop" is exclusive and "start" is inclusive.
# This wil count 50 to 100. It will iterate 51 times, thoug (but will be right).
# It starts at 0, so we add 1 to "stop" to include the last number
# Can also be done while printing.
for i in range(50, 100 + 1):
    print(i)

# You can also have a "step" argument, adding a third argument to the range.
# We will use "2":
for i in range(50, 100 + 1, 2):
    print(i)

# We can iterate through anything that is considered iterable. Like a string, for 
# an example. This will print each letter of my name, each in a different line:
for i in "Camilla Hollmann":
    print(i) # Printing letter by letter.

# Now, for our counter, we will use the "time" library.
# This is a countdown:
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1) # Makes the program wait 1 sec after each iteration.
print("Happy New Year!") # Prints after exiting the loop.