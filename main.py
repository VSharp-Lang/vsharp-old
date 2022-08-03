# main.py

# imports needed
import sys, time
from interpreter import parse

# to get the filename
arg = sys.argv

# checks if you input the filename
if len(arg) > 1:
    try:
        # open specified file
        with open(arg[1], "r") as f:
            cont = f.read()
            content = parse(cont)
            exec(content)
    # in case file doesnt exist
    except FileExistsError:
        print("File doesn't exist.")
else:
    print("Command is: python main.py <filename>")
