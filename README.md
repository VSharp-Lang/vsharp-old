# VSharp Interpreter

VSharp (V#) is a programming language made with the goal of having the smallest interpreter.
<br>How it works is that it takes the code of a file and turns it into python code.</br>
Feel free to post any bugs as it is currently in development at the moment!
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
In the main method if you put less than 2 spaces it will give an error.
<br>Here is how you can print to the console in vsharp.</br>
```
main {
  Console.Print("Hello, World!");
  Console.Print(20);
  Console.Print(13 + 50);
}
```
<br>Make sure to put semicolons (;) at the end of a task to avoid errors</br>
You can also use variables!
<br>Make sure it starts with `var` and has a space before the name or else it might cause errors</br>
```
main {
  // this is a variable example!
  var hello = "Hello, from a variable!";
  var printing = 20;
  Console.Print(hello);
  Console.Print(printing);
}
```
