main {
   import System.Random.Import;
   // these two statements print something, run it to see!
   Console.Print("Hello, World!");
   Console.Print("Hello lol");
   // making a variable
   var hello = "This was printed from a variable lol";
   Console.Print(hello);
   Console.Print(20);
   Console.Print("the -// is something");
   var number = 130;
   Console.Print(number);
   Console.Print(2021 + 1);
   Console.Print(System.Random.Int(1, 20));
   funct helloworld() -{
      --Console.Print("Hello, this is a -function.");
   }-
   helloworld();
   funct helloname(name : String) -{
      --Console.Print("Hello, "+name+".");
   }-
   helloname("John");
   helloname("Dave");
   // getting input!
   Console.Print("-"");
   var userInput = System.GetInput("Enter your name: ");
   helloname(userInput);
}
