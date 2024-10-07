# Shortcuts for comments: Ctrl + K + C.
# Continue from 1:53:30 on Bro Code.

# We will now learn about functions in python.
# A function is a block of code which is executed only when it is called.

# When you still don't know what to put inside your function, you can type
# "pass" inside and work on another part of your code. 

# When you send information to a function, you use "arguments".
# When you define your function, you define your parameters like this:
# "def function(parameters):".

def hello(first_name, last_name):
    print("Hello " + first_name + " " + last_name)
    print("Have a nice day!")

my_name = "YOU" 
your_name = "THERE"
# It's nice if you don't use the same name as your parameters for variables.

hello("Camilla", "Hollmann")
hello(my_name, your_name)
