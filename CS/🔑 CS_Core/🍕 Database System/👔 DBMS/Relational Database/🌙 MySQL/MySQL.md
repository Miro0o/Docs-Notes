# MySQL

[TOC]


## Res
### Leraning Materials
📂 [MySQL Documentaion](https://dev.mysql.com/doc/)

[runoob 菜鸟](https://www.runoob.com/mysql/mysql-database-import.html)

[C语言中s文网](http://c.biancheng.net/view/vip_8317.html)

[廖雪峰](https://www.liaoxuefeng.com/wiki/1177760294764384/1246617774585536)


### Others..
↗ [SQL](../../../📌%20Relational%20Data%20Models%20&%20Languages/🩼%20SQL/SQL.md)



## 🧭 Guides
### 🧑🏿‍🏭Installation
Here i use brew to manage mysql.
```shell
brew install mysql
```

Do as it indicates.

==NOTICE: MySQL Client的可执行程序是mysql，MySQL Server的可执行程序是mysqld。==



[brew install mysql on macOS]: https://stackoverflow.com/questions/4359131/brew-install-mysql-on-macos
   - [see this anser](https://stackoverflow.com/a/6378429/16542494)

[部署数据库 -- 阿里云开发者文档]: https://www.alibabacloud.com/help/zh/elastic-compute-service/latest/database-overview


### 🧑🏼‍🔧 Config
###### On my Mac: 
root: 12345678

SQLi: Qwas1zx@

Config : `/usr/local/etc/my.cnf`



## 🤷🏽‍♂️ Q&A
### 👽 User Management
1. [MySQL用户权限总结【用户授权必会】](https://blog.csdn.net/yeahPeng11/article/details/121584343) 

2. [MySQL用户管理：添加用户、授权、删除用户](https://www.cnblogs.com/chanshuyi/p/mysql_user_mng.html) 

3. [MySQL之权限管理](https://www.cnblogs.com/Richardzhu/p/3318595.html) 

4. [ERROR: 'Your password does not satisfy the current policy requirements'](https://stackoverflow.com/questions/43094726/your-password-does-not-satisfy-the-current-policy-requirements)

   - [see *password validate configuration metrics* & configure it](https://stackoverflow.com/a/43094873/16542494)
   - [mysql official -- validate-password-options-variables](https://dev.mysql.com/doc/refman/8.0/en/validate-password-options-variables.html)

   - `SHOW VARIABLES LIKE 'validate_password%';`


### 🎀 Connection
1. [Connect Java to a MySQL database](https://stackoverflow.com/questions/2839321/connect-java-to-a-mysql-database)
   - [Here's a step by step explanation how to install MySQL and JDBC and how to use it:](https://stackoverflow.com/a/2840358/16542494)
2. [IntelliJ IDEA 使用Java连接MySQL的方法](http://www.codebaoku.com/it-mysql/it-mysql-198662.html)



## Ref




