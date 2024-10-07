# Shortcuts for comments: Ctrl + K + C.
# Continue from 1:07:35 on Bro Code.

# We will now learn about while loops. It is a statement that will execute it's
# block of code, as long as it's condition remains true.

# Infinite loop:
# while 1 == 1:
#    name = print("Help! I'm stuck in a loop!")

# This little program will keep asking for a name until the user types something:
name = ""

while len(name) == 0:
    name = input("Enter your name: ")

print("Hello " + name)

# Same thing, but different:

name = None # We use NONE the same way as NULL (C) in Python. It means "NOTHING".

while not name:
    name = input("Enter your name: ")

print("Hello " + name)