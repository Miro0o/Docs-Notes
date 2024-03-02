# SQL Injection

[TOC]



## Res
↗ [SeedLab - Web Security /👉 SQL Injection Attack Lab](../../../../☠️%20Kill%20Chain/🎯%20Cyber%20Ranges%20&%20Labs/🧪%20Security%20Labs/SEED%20Project/SeedLab%20-%20Web%20Security.md#👉%20SQL%20Injection%20Attack%20Lab)



## Intro


## Ref
[👍 SQL注入之盲注简单总结]: https://www.cnblogs.com/zane-s/articles/12371820.html
1. 什么是盲注？  
    盲注就是在sql注入过程中，sql语句执行的选择后，选择的数据不能回显到前端页面。此时，我们需要利用一些方法进行判断或者尝试，这个过程称之为盲注。
2. SQL盲注与SQL普通注入的区别？  
    普通注入是可以根据报错提示，进行sql语句注入从而，直接爆出我们想要的信息，比如数据库版本、数据库名、用户名、操作系统版本等；而盲注只能通过多次猜测，从而猜解出有用信息。相对来说sql盲注更加考验安全人员的手注能力。
3. SQL盲注分类：  
    Sql盲注可以简单分为三类 ：布尔盲注、延时盲注和报错盲注

[👍 SQL注入之布尔盲注并使用burp进行自动化爆破]: https://www.haochen1204.com/2021/03/29/sql-zhu-ru-zhi-bu-er-mang-zhu-bing-shi-yong-burp-jin-xing-zi-dong-hua-bao-po/#toc-heading-1
