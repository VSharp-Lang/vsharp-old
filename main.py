import sys

arg = sys.argv

def parse(contents):
    args = contents.split()
    cont = contents.replace("; ", "\n")
    cont = cont.replace(";", "\n")
    cont = cont.replace("Console.Print", "print")
    cont = cont.replace("{", "")
    cont = cont.replace("}", "\n")
    cont = cont.replace("main", "")
    cont = cont.replace("-", "")
    cont = cont.replace("//", "#")
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

if len(arg) > 1:
    try:
        with open(arg[1], "r") as f:
            cont = f.read()
            content = parse(cont)
            exec(content)

    except FileExistsError:
        print("File doesn't exist.")
else:
    print("Command is: python main.py <filename>")
