# VSharp Interpreter

VSharp (V#) is a programming language made with the goal of having the smallest interpreter.
<br>How it works is that it takes the code of a file and turns it into python code.</br>
<br>This README.md file has a tutorial on how to use it.</br>

# Running a file
To run a file you need to have the main.py file in your computer, python3 installed and a file you can run.
<br>The recommended file extension is .vs but you can name it anything as this is a interpreted language.</br>
<br>These are the commands to run a file in different operating systems.</br>
1. Linux
<br>`python3 main.py <filename>`</br>
2. Windows
<br>`python main.py <filename>`</br>
3. MacOS
<br>`python3 main.py <filename>`</br>

# Documentation

To run code you first need to make a `main` class.
<br>Like this!</br>
```
main {

}
```
Comments can be marked using `//`
```
main {
// like this!
}
```
The reason why I didn't add a space is because it can cause errors, you need to put a `-` to make it easier to read but you can leave it blank if you want.
<br>Here is how you can print to the console in vsharp.</br>
```
main {
-Console.Print("Hello, World!");
}
```
<br>Make sure to put semicolons (;) at the end of a task to avoid errors</br>
