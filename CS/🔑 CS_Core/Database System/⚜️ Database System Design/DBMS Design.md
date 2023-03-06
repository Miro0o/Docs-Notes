# DBMS Design

[TOC]



## Components of A DBMS

![|500](../../../../Assets/Pics/Screenshot%202023-03-06%20at%203.32.35%20PM.png)
<small>Components of a DBMS</small>


![|500](../../../../Assets/Pics/Screenshot%202023-03-06%20at%203.32.51%20PM.png)
<small>Components of a Database Manager</small>


## DBMS Architectures
### Mainframe Architecture
![](../../../../Assets/Pics/Pasted%20image%2020230306154507.png)

| Advantages of Mainframe Architecture | Disadvantages of Mainframe Architecture |
| - | - |
| Large number of concurrent users | Does not take advantage of local computer processing power |
| Able to handle very large volume of transactions | Does not take advantage of local computer processing power |
| Suitable for slow network environments | Does not take advantage of local computer processing power |
| Central location of both application | Hardware is relatively expensive |
| Character-based interface | DBMS makes maintenance relatively simple |

### Desktop Architecture
![|500](../../../../Assets/Pics/Pasted%20image%2020230306155045.png)

| Advantages of Mainframe Architecture | Disadvantages of Mainframe Architecture |
| - | - |
| Inexpensive to acquire | Only available to a single user at a time |
| Easy to configure | Only available at a single computer|
| Requires few resources to operate | May impose limits on how data can be stored |


### File Server Architecture
![](../../../../Assets/Pics/Pasted%20image%2020230306155115.png)

| Advantages of Mainframe Architecture | Disadvantages of Mainframe Architecture |
| - | - |
| Inexpensive to acquire | Only viable for a limited number of users, perhaps 10 or fewer |
| Easy to configure | Query performance declines quickly as the amount of data increases |
| Low-cost option for multi-user concurrency | Multiple installation of both application software and DBMS can lead to version control issues for both |



### Client/Server Architecture (Traditional Two-Tier C/S)
![](../../../../Assets/Pics/Pasted%20image%2020230306155216.png)

| Advantages of Mainframe Architecture | Disadvantages of Mainframe Architecture |
| - | - |
| Makes good use of processing power of multiple computers | Application software is distributed, possibly leading to version control issues |
| Handles large amounts of both data and transactions | DBMS software is relatively expensive compared to the file-server approach |
| Can support thousands of concurrent users |  |



### Web Architecture (Three-Tier C/S)
![](../../../../Assets/Pics/Pasted%20image%2020230306155344.png)

| Advantages of Mainframe Architecture | Disadvantages of Mainframe Architecture |
| - | - |
| All advantages of the client/server architecture |  Adds another layer of complexity (web server) |
| Increased ease of application version control | Various software apps must keep synchronized with database software |
| Very good at handling intermittent use from large numbers of users (millions)| Upgrades in browsers may require changes to application |



## Ref
[Database Architectures]: https://app.myeducator.com/reader/web/617b/chapter01/gj149/

