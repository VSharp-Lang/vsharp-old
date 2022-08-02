# main.py

# import needed
import sys

# to get the filename
arg = sys.argv

# prase function that converts vs code to python code
def parse(contents):
    # removing unsupported python characters or changing code to python code
    args = contents.split()
    cont = contents.replace("; ", "\n")
    cont = cont.replace(";", "\n")
    cont = cont.replace("Console.Print", "print")
    cont = cont.replace("{", "")
    cont = cont.replace("}", "\n")
    cont = cont.replace("main", "")
    cont = cont.replace("-", "")
    cont = cont.replace("//", "#")
    cont = cont.replace("var ", "")
    # error messages
    if len(args) > 2:
        error = ""
        if args[0] != "main":
            error = error + "\nSyntaxError: Lacking main class"
        if args[1] != "{" or args[0] == "main{":
            error = error + "\nSyntaxError: Lacking '{' after main class"
        if args[len(args)-1] != "}":
            error = error + "\nSyntaxError: Lacking '}' at the end of main class"

        if error != "":
            return "print(\"\"\""+error+"\"\"\")"
        else:
            return cont
    else:
        return "print('SyntaxError: Lacking main class defenition')"

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
