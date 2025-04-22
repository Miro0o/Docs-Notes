# JDBC (Java DataBase Connectivity)

[TOC]



## Res
### Related Topics


### Other Resources
👉 [尚硅谷JDBC核心技术视频教程](https://www.bilibili.com/video/BV1eJ411c7rf?p=3&share_source=copy_web) ⭐️⭐️⭐️

[DAO tutorial --- official dev doc](https://balusc.omnifaces.org/2008/07/dao-tutorial-data-layer.html)



## Intro
```ascii
												┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐
┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐							   ┌───────────────┐
│  ┌───────────────┐  │							│  │   App.class   │  │
   │   Java App    │							   └───────────────┘
│  └───────────────┘  │							│          │          │
           │									           ▼
│          ▼          │							│  ┌───────────────┐  │
   ┌───────────────┐							   │  java.sql.*   │
│  │JDBC Interface │<─┼─── JDK					│  └───────────────┘  │
   └───────────────┘							           │
│          │          │							│          ▼          │
           ▼									   ┌───────────────┐     TCP    ┌───────────────┐   
│  ┌───────────────┐  │							│  │ mysql-xxx.jar │──┼────────>│ MySQL (mysqld)│   
   │  JDBC Driver  │<───── Vendor				   └───────────────┘            └───────────────┘
│  └───────────────┘  │							└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘									  
           │											  JVM
└ ─ ─ ─ ─ ─│─ ─ ─ ─ ─ ┘
           ▼
   ┌───────────────┐
   │   Database    │
   └───────────────┘
```



## Ref
[MySQL JDBC Attack , Java Web Security | p4d0rn]: https://p4d0rn.gitbook.io/java/jdbc-attack/mysql
JDBC（Java DataBase Connectivity）是SUN公司发布的一个java程序与数据库之间通信的接口（规范），各大数据库厂商去实现JDBC规范，并将实现类打包成jar包

![](../../../../../../../../Assets/Pics/Pasted%20image%2020250324211154.png)

进行数据库连接时指定了数据库的URL及连接配置 `Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test","root", "root");`

若JDBC连接的URL被攻击者控制，就可以让其指向恶意的MySQL服务器

JDBC连接MySQL服务端时，会有几个内置的SQL查询语句会执行，查询的结果集会在MySQL客户端被处理时会调用`ObjectInputStream#readObject`进行反序列化。

攻击者可以搭建恶意MySQL服务器，返回精心构造的查询结果集，进行客户端反序列化攻击。

可被利用的两条查询语句：
- SHOW SESSION STATUS
- SHOW COLLATION

恶意MySQL服务器搭建：
- https://github.com/fnmsd/MySQL_Fake_Server 📌
- https://github.com/rmb122/rogue_mysql_server
