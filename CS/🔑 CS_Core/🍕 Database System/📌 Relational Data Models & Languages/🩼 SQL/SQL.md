# SQL

[TOC]



## Res
### Reference
↗ [MySQL Manual](../../👔%20DBMS/Relational%20Database/🌙%20MySQL/📌%20MySQL%20Manual/MySQL%20Manual.md)


### Learning SQL
To access seas of resources of Database learning 🤤 

👉 [C语言中文网](http://c.biancheng.net/mysql/10/)
​👉 [廖雪峰的sql教程](https://www.liaoxuefeng.com/wiki/1177760294764384/1179613436834240)
​👉 [极客学院](https://wiki.jikexueyuan.com/project/mysql/)


### Compatibility
ANSI: standard SQL

other providers/ communities: standard SQL + different tweaks & changes 
- Oracle : PL/SQL
- Microsoft: T-SQL



## Intro
> An international standard now exists for the SQL language making it both the formal and de facto standard language for defining and manipulating relational databases (ISO, 1992, 2011a).

An international standard now exists for the SQL language making it both the formal and de facto standard language for defining and manipulating relational databases (ISO, 1992, 2011a).

SQL is an example of a **transform-oriented language**, or a language designed to use relations to transform inputs into required outputs. As a language, the ISO SQL standard has two major components:
- a **Data Definition Language (DDL)** for defining the database structure and controlling access to the data;
- a **Data Manipulation Language (DML)** for retrieving and updating data.


### History of SQL
#TODO 


### Terminology
The **ISO SQL standard** does not use the formal terms of relations, attributes, and tuples, instead using the terms tables, columns, and rows. In our presentation of SQL we mostly use the ISO terminology.

It should also be noted that SQL does not adhere strictly to the definition of the relational model described before. For example, SQL allows the table produced as the result of the SELECT statement to contain duplicate rows, it imposes an ordering on the columns, and it allows the user to order the rows of a result table.


### SQL Statements & Syntex & Notations
1️⃣ An SQL statement consists of **reserved words** and **user-defined words.** 
- **Reserved words** are a fixed part of the SQL language and have a fixed meaning. They must be spelled exactly as required and cannot be split across lines.
- **User-defined words** are made up by the user (according to certain syntax rules) and represent the names of various database objects such as tables, columns, views, indexes, and so on.

2️⃣ The words in a statement are also built according to a set of syntax rules.

3️⃣ Although the standard does not require it, many dialects of SQL require the use of a **statement terminator** to mark the end of each SQL statement (usually the semicolon “;” is used).

4️⃣ Most components of an SQL statement are **case-insensitive**, which means that letters can be typed in either upper- or lowercase. 

> ❗ The one important exception to this rule is that literal character data must be typed exactly as it appears in the database. For example, if we store a person’s surname as “SMITH” and then search for it using the string “Smith,” the row will not be found.

5️⃣ Although SQL is **free-format**, an SQL statement or set of statements is more readable if **indentation** and **lineation** are used. For example:
- each clause in a statement should begin on a new line;
- the beginning of each clause should line up with the beginning of other clauses;
- if a clause has several parts, they should each appear on a separate line and be indented under the start of the clause to show the relationship.

6️⃣ Throughout this and the next three chapters, we use the following **extended form of the Backus Naur Form (BNF) notation** to define SQL statements:
- uppercase letters are used to represent reserved words and must be spelled exactly as shown;
- lowercase letters are used to represent user-defined words;
- a vertical bar ( | ) indicates a choice among alternatives; for example, a | b | c;
- curly braces indicate a required element; for example, {a};
- square brackets indicate an optional element; for example, [a];
- an ellipsis(...) is used to indicate optional repetition of an item zero or more times.
	- For example: {a|b} (, c . . .) means either a or b followed by zero or more repetitions of c separated by commas.


#### Importance of SQL



## Ref

