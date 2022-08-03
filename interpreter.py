# interpreter.py

# prase function that converts vs code to python code
def parse(contents):
    # removing unsupported python characters or changing code to python code
    args = contents.split()
    cont = contents.replace("; ", "\n")
    cont = cont.replace(";", "\n")
    cont = cont.replace("Console.Print", "print")
    cont = cont.replace("System.Execute", "exec")
    cont = cont.replace("funct", "def")
    cont = cont.replace("-def", "funct")
    if "System.Random.Import" in cont:
        import vs_random
        cont = vs_random.work(cont)
    else:
        cont = cont.replace("System.Random.Int", "")
        cont = cont.replace("System.Random.ReturnState", "")
        cont = cont.replace("System.Random.Seed", "")
        cont = cont.replace("System.Random.ReturnRandBits", "")
        cont = cont.replace("System.Random.Range", "")
        cont = cont.replace("System.Random.Choice", "")
        cont = cont.replace("System.Random.Choices", "")
        cont = cont.replace("System.Random.Shuffle", "")
        cont = cont.replace("System.Random.Sample", "")
        cont = cont.replace("System.Random.Default", "")
        cont = cont.replace("System.Random.Float", "")
        cont = cont.replace("System.Random.Triangular", "")
        cont = cont.replace("System.Random.Gammavariate", "")
        cont = cont.replace("System.Random.Gauss", "")
        cont = cont.replace("System.Random.Lognormvariate", "")
        cont = cont.replace("System.Random.Vonmisesvariate", "")
        cont = cont.replace("System.Random.Paretovariate", "")
        cont = cont.replace("System.Random.Weibullvariate", "")
        cont = cont.replace("System.Random.Normalvariate", "")
        cont = cont.replace("System.Random.Betavariate", "")
    cont = cont.replace("import System.Random.Import", "import random")
    cont = cont.replace(" -{", ":")
    cont = cont.replace("-{", ":")
    cont = cont.replace("}-", "")
    cont = cont.replace("System.ToInteger", "int")
    cont = cont.replace("System.ToString", "str")
    cont = cont.replace("System.ToFloat", "float")
    cont = cont.replace("System.ToBoolean", "bool")
    cont = cont.replace(": String", "")
    cont = cont.replace(": Integer", "")
    cont = cont.replace(": Float", "")
    cont = cont.replace(": Boolean", "")
    cont = cont.replace(":String", "")
    cont = cont.replace(":Integer", "")
    cont = cont.replace(":Float", "")
    cont = cont.replace(":Boolean", "")
    cont = cont.replace("{", "")
    cont = cont.replace("}", "\n")
    cont = cont.replace("main", "")
    cont = cont.replace("       ", "   ")
    cont = cont.replace("   ", "")
    cont = cont.replace("  ", "")
    cont = cont.replace("", "")
    cont = cont.replace("--", "   ")
    cont = cont.replace("//", "#")
    cont = cont.replace("-#", "//")
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
