# Shortcuts for comments: Ctrl + K + C.
# Continue from 2:17:05 on Bro Code.

# We will now learn about **kwargs in Python.
# kwargs are parameters that will pack all aguments into a dictionary.
# They are useful becautse they allow a function to accept a varying amount
# of keyword arguments.

def hello(**kwargs):
    # print("Hello " + kwargs["first"] + " " + kwargs["last"])
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")

hello(title="Mr.", first="Bro", middle="Dude", last="Code")