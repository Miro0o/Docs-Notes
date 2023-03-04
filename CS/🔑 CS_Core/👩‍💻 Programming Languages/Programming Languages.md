# Programming Languages in a nut shell

[TOC]



## Res
[List Of Some Of The Software Development Trends That Have Dominated The Year 2020](https://www.cisin.com/coffee-break/trends/list-of-some-of-the-software-development-trends-that-have-dominated-the-year-2020.html)

🪜 [TIOBE](https://www.tiobe.com/tiobe-index/)

↗ [Compilation](../Compilation/Compilation.md)


## Intro
### History of programming languages 

> <https://zh.wikipedia.org/zh-cn/程式語言歷史>

+ Hyponymy & hyperymy

> https://en.wikipedia.org/wiki/Hyponymy_and_hypernymy 

![](../../🏠%20Assets/pics/600px-Hyponym_and_hypernym.png)

#### 1940～

#### 1950 ～ 1960
+ FORTRAN
+ LISP
+ COBOL

#### 1967 ～ 1978
+ C

#### 1980 ～
+ Ada
+ C++
+ Perl

#### 1990 ～
+ Python
+ Java
+ PHP
+ JS
+ VB

#### 2000 ～ 
+ .NET
+ swift
+ C#


## Types of Programming Languages 
### Plantform Specific
#### [.NET](https://zh.wikipedia.org/wiki/.NET%E6%A1%86%E6%9E%B6 ".NET框架")

-   [C#](https://zh.wikipedia.org/wiki/C%E2%99%AF "C♯") 
    -   [Visual C#](https://zh.wikipedia.org/wiki/Microsoft_Visual_C%E2%99%AF "Microsoft Visual C♯")
-   [C++/CLI](https://zh.wikipedia.org/wiki/C%2B%2B/CLI "C++/CLI") 
    -   [Visual C++](https://zh.wikipedia.org/wiki/Microsoft_Visual_C%2B%2B "Microsoft Visual C++")
-   [F#](https://zh.wikipedia.org/wiki/F%E2%99%AF "F♯")
-   [PowerShell](https://zh.wikipedia.org/wiki/PowerShell "PowerShell")
-   [IronPython](https://zh.wikipedia.org/wiki/IronPython "IronPython")
-   [IronScheme](https://zh.wikipedia.org/w/index.php?title=IronScheme&action=edit&redlink=1)
-   [VB.NET](https://zh.wikipedia.org/wiki/Visual_Basic_.NET "Visual Basic .NET")
-   [Small Basic](https://zh.wikipedia.org/wiki/Microsoft_Small_Basic "Microsoft Small Basic")


#### [JVM](https://zh.wikipedia.org/wiki/Java%E5%B9%B3%E8%87%BA "Java平臺")

-   [Java](https://zh.wikipedia.org/wiki/Java "Java") 
    -   [AspectJ](https://zh.wikipedia.org/w/index.php?title=AspectJ&action=edit&redlink=1)
    -   [JSP](https://zh.wikipedia.org/wiki/JSP "JSP")
-   [Scala](https://zh.wikipedia.org/wiki/Scala "Scala")
-   [Clojure](https://zh.wikipedia.org/wiki/Clojure "Clojure")
-   [JRuby](https://zh.wikipedia.org/wiki/JRuby "JRuby")
-   [Jython](https://zh.wikipedia.org/wiki/Jython "Jython")
-   [Kawa](https://zh.wikipedia.org/w/index.php?title=Kawa&action=edit&redlink=1)
-   [Groovy](https://zh.wikipedia.org/wiki/Groovy "Groovy")
-   [Kotlin](https://zh.wikipedia.org/wiki/Kotlin "Kotlin")


#### [Xcode](https://zh.wikipedia.org/wiki/Xcode "Xcode")

-   [Objective-C](https://zh.wikipedia.org/wiki/Objective-C "Objective-C")
-   [AppleScript](https://zh.wikipedia.org/wiki/AppleScript "AppleScript")
-   [Swift](https://zh.wikipedia.org/wiki/Swift_(%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80) "Swift (程式語言)")


### Programming Paradigm

> 🔗 https://www.geeksforgeeks.org/introduction-of-programming-paradigms/

**Paradigm** can also be termed as method to solve some problem or do some task. Programming paradigm is an approach to solve problem using some programming language or also we can say it is a method to solve a problem using tools and techniques that are available to us following some approach. There are lots for programming language that are known but all of them need to follow some strategy when they are implemented and this methodology/strategy is paradigms.

![img](../../../Assets/Pics/1-344.png)
<small>https://www.geeksforgeeks.org/introduction-of-programming-paradigms/</small>


#### Declarative Programming Paradigm

> 💡 [Reactive Programming](https://en.wikipedia.org/wiki/Reactive_programming) is a declarative programming paradigm concerned with data streams and the propagation of change. With this paradigm, it's possible to express static (e.g., arrays) or dynamic (e.g., event emitters) data streams with ease, and also communicate that an inferred dependency within the associated execution model exists, which facilitates the automatic propagation of the changed data flow.
> 
> My notes of Reactive Programing Paradigm can be found in 👉 [Software Engineering/Dev Pattern/RX](../../Software%20Engineering/👷🏻%20Dev%20Pattern/RX/RX.md)

It is divided as Logic, Functional, Database. In computer science the _declarative programming_ is **a style of building programs that expresses logic of computation without talking about its control flow**. It often considers programs as theories of some logic. It may simplify writing parallel programs. The focus is on what needs to be done rather how it should be done basically emphasize on what code is actually doing. It just declares the result we want rather how it has be produced. This is the only difference between imperative (how to do) and declarative (what to do) programming paradigms. Getting into deeper we would see logic, functional and database.

##### Logic Programming Paradigm
It can be termed as abstract model of computation. It would solve logical problems like puzzles, series etc. In logic programming we have a knowledge base which we know before and along with the question and knowledge base which is given to machine, it produces result. In normal programming languages, such concept of knowledge base is not available but while using the concept of artificial intelligence, machine learning we have some models like Perception model which is using the same mechanism.   
In logical programming the main emphasize is on knowledge base and the problem. The execution of the program is very much like proof of mathematical statement, e.g., Prolog.

##### Functional Programming
**JavaScript**: developed by Brendan Eich

👉 [Haskell](Compiled%20Languages/Haskell/Haskell.md): developed by Lennart Augustsson, Dave Barton

**Scala**: developed by Martin Odersky
**Erlang**: developed by Joe Armstrong, Robert Virding
**Lisp**: developed by John Mccarthy
**ML**: developed by Robin Milner
**Clojure**: developed by Rich Hickey

##### Database Processing Approach
```mysql
CREATE DATABASE databaseAddress;
CREATE TABLE Addr (
    PersonID int,
    LastName varchar(200),
    FirstName varchar(200),
    Address varchar(200),
    City varchar(200),
    State varchar(200)
);
```

#### Imperitive Programming Paradigm
It is one of the oldest programming paradigm. It features close relation to machine architecture. It is based on Von Neumann architecture. It works by changing the program state through assignment statements. It performs step by step task by changing state. The main focus is on how to achieve the goal. The paradigm consist of several statements and after execution of all the result is stored.

> Examples of **Imperative** programming paradigm:
> 
> **C**: developed by Dennis Ritchie and Ken Thompson
> **Fortran**: developed by John Backus for IBM
> **Basic**: developed by John G Kemeny and Thomas E Kurtz

##### Procedural Programming Paradigm
**C**: developed by Dennis Ritchie and Ken Thompson
**C++**: developed by Bjarne Stroustrup

👉 [C&CPP](Compiled%20Languages/C&CPP/C&CPP.md)

**Java**: developed by James Gosling at Sun Microsystems
**ColdFusion**: developed by J J Allaire
**Pascal**: developed by Niklaus Wirth

##### Object Oriented Programming, OOP
**Simula**: first OOP language

👉 [Java](Compiled%20Languages/Java/Java.md): developed by James Gosling at Sun Microsystems

**C++**: developed by Bjarne Stroustrup
**Objective-C**: designed by Brad Cox
**Visual Basic .NET**: developed by Microsoft
**Python**: developed by Guido van Rossum
**Ruby**: developed by Yukihiro Matsumoto 
**Smalltalk**: developed by Alan Kay, Dan Ingalls, Adele Goldberg

##### Parallel Processing Approach
Parallel processing is the processing of program instructions by dividing them among multiple processors. A parallel processing system posses many numbers of processor with the objective of running a program in less time by dividing them. This approach seems to be like divide and conquer. 

Examples are NESL (one of the oldest one) and C/C++ also supports because of some library function.



