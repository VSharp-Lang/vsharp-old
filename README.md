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
<br>`python3 vsharp.py <filename>`</br>
2. Windows
<br>`python vsharp.py <filename>`</br>
3. MacOS
<br>`python3 vsharp.py <filename>`</br>
Or if you have the exe you can follow do the following command:
<br>`vsharp.exe <filename>`</br>

# Building the language
This part is windows only.
<br>To build it into an exe file you need to download the source and run the build.bat file.</br>
The requierments are that you need to have Python3 installed and pyinstaller installed, you can install python on their <a href="https://www.python.org/">official website</a> and you can install pyinstaller by running this command: <br>`pip install pyinstaller`</br>
<br>Be patient and when its done you should have an exe file on the \dist\ directory where you extracted the language.</br>
You can run a file in the command prompt after like this!
<br>
![image](https://user-images.githubusercontent.com/68329886/182557690-05c89078-99fa-4640-9cc6-d3e405259ee7.png)
</br>

# Documentation

<br><strong>NOTE: The example.vs includes everything documented here.</strong></br>
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
<br>Here is how you can print to the console in vsharp.</br>
Keep in mind that to print `//` instad of it printing `#` you need to add a `-` before it
```
main {
  Console.Print("Hello, World!");
  Console.Print(20);
  Console.Print(13 + 50);
  Console.Print("You can print -// now!");
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
<br>You can also <strong>import</strong> libraries!</br>
For example you can import a default library called `random` which can generate random stuff!
<br>To import something you need to put `import` and the import module of the thing you want to import.</br>
```
import System.Random.Import;
```
<br>It's that easy! Let me show you how to use the <strong>random</strong> module.</br>
To generate a `integer` value you can run this command:
```
main {
  // We are importing the module
  import System.Random.Import;
  // We are generating a random number from 1 to 20
  Console.Print(System.Random.Int(1, 20));
}
```
<br>You must be confused! Let me show you what I mean by `intiger`. There are a lot of value types in V#</br>
1. `String` --> Typed in quotes ("") and stores characters from `a-Z` and numbers `0-9`
2. `Integer` --> Holds numbers from `-9223372036854775807` to `9223372036854775807`
3. `Float` --> Holds the same thing as an integer but it is a decimal number.
4. `Boolean` --> Holds only two (2) values, true or false
```
<br>Those are the basic data types, now you're probably not confused!</br>
<strong>NOTE: The random module has all the functions the python random module has so you can read up on that.</strong>
