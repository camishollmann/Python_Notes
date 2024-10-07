# Shortcuts for comments: Ctrl + K + C.
# Continue from 1:13:10 on Bro Code.

# We will now learn about nested loops in python.
# The "inner loop" will finish all of it's iterations before finishing one
# iteration of the "outer loop".

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns): # WILL print all columns before jumping to next row.
        print(symbol, end="") # The " end="" " argument avois the default column break.
    print() # Jumps to a new column.

# "Print()" breaks the column by default. The "end" argument is "/n" by deafult, so
# in this exercise we changed that to be able to print multiple times in a single
# line.