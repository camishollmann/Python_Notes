# Shortcuts for comments: Ctrl + K + C.
# Continue from 1:17:15 on Bro Code.

# We will now learn about loop control statements in Python.
# These things change a loop's execution from it's normal sequence.

# We have:
# 1) break - used to terminate the loop entirely.
# 2) continue - skips to the next iteration of the loop.
# 3) pass - does nothing, acts as a placeholder

# First is "break":
while True:
    name = input("Enter your name: ")
    if name != "":
        break # Exits the loop.

# Now for "continue":
phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue # This makes the loop jump to the next step without executing this one.
    print(i, end="") # Will print "1234567890" withou any "-".

# Now "pass":

for i in range(1, 21): # Will iterate to 1 through 20 ("stop" is exclusive).
    if i == 13:
        pass # Does nothing when the number is 13, so it will not print "13".
    else:
        print(i) # Prints "1 2 3 4 5 6 7 8 9 10 11 12 14 15 16 17 18 19 20"
