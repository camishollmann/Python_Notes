# Shortcuts for comments: Ctrl + K + C.
# Continue from 1:02:00 on Bro Code.

# We will now learn about logical operators.
# The are "and", "or" and "not", used to check if to or more conditional statements
# are true.

temp = int(input("What is the temperature outside?: ")) # In degrees CELSIUS.

if not(temp >= 0 and temp <= 30):
    print("The temperature is bad today!")
    print("Stay inside!")
elif not(temp < 0 or temp > 30):
    print("The temperature is good today!")
    print("Go outside!")

# The "not" logical operator takes ONE condition and flips it's logical value:
# If it's true, it will flip it to false, and if it's false, it will flip it to true.
# Use it to REVERSE the program!


