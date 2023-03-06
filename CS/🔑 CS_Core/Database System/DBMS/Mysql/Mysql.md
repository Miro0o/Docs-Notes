# Mysql

## 🧭 Guides

### ⛏ Resources

📂 [MySQL Documentaion](https://dev.mysql.com/doc/)

 [runoob 菜鸟](https://www.runoob.com/mysql/mysql-database-import.html)

 [C语言中s文网](http://c.biancheng.net/view/vip_8317.html)

 [廖雪峰](https://www.liaoxuefeng.com/wiki/1177760294764384/1246617774585536)



### 🧑🏿‍🏭Installation

Here i use brew to manage mysql.

```shell
brew install mysql
```

Do as it indicates.

==NOTICE: MySQL Client的可执行程序是mysql，MySQL Server的可执行程序是mysqld。==

###### Refs:

1. [brew install mysql on macOS](https://stackoverflow.com/questions/4359131/brew-install-mysql-on-macos)
   - [see this anser](https://stackoverflow.com/a/6378429/16542494)


2. [部署数据库 -- 阿里云开发者文档](https://www.alibabacloud.com/help/zh/elastic-compute-service/latest/database-overview)



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



## ☄️ Troubleshootings

###### 👉 Can't connect to MySql

[Warning about SSL connection when connecting to MySQL database](https://stackoverflow.com/questions/34189756/warning-about-ssl-connection-when-connecting-to-mysql-database)

[Cannot create PoolableConnectionFactory](https://stackoverflow.com/questions/5203696/cannot-create-poolableconnectionfactory)



###### 👉 Tomcat and Spring framework incompatible.

[SEVERE: Error configuring class 【org.springframework.web.context.ContextLoaderListener】NoClassDefFoundError: javax/servlet/ServletContextListener](https://stackoverflow.com/questions/68995226/severe-error-configuring-class-org-springframework-web-context-contextloaderli)

[IDEA启动项目，日志输出文件输出地址](https://blog.csdn.net/David_jiahuan/article/details/102583873)



###### 👉 Authentication plugin `caching_sha2_password` cannot be loaded:

[Authentication plugin 'caching_sha2_password' cannot be loaded -- stackoverflow](https://stackoverflow.com/questions/49194719/authentication-plugin-caching-sha2-password-cannot-be-loaded)

[authentication plugin caching_sha2 - CSDN](https://blog.csdn.net/u012613251/article/details/80346665)



