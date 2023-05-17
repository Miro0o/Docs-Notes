# ☄️ Troubleshootings

[TOC]



## 👉 Can't connect to MySql
[Warning about SSL connection when connecting to MySQL database](https://stackoverflow.com/questions/34189756/warning-about-ssl-connection-when-connecting-to-mysql-database)

[Cannot create PoolableConnectionFactory](https://stackoverflow.com/questions/5203696/cannot-create-poolableconnectionfactory)



## 👉 Tomcat and Spring framework incompatible.
[SEVERE: Error configuring class 【org.springframework.web.context.ContextLoaderListener】NoClassDefFoundError: javax/servlet/ServletContextListener](https://stackoverflow.com/questions/68995226/severe-error-configuring-class-org-springframework-web-context-contextloaderli)

[IDEA启动项目，日志输出文件输出地址](https://blog.csdn.net/David_jiahuan/article/details/102583873)



## 👉 Authentication plugin `caching_sha2_password` cannot be loaded
[Authentication plugin 'caching_sha2_password' cannot be loaded -- stackoverflow](https://stackoverflow.com/questions/49194719/authentication-plugin-caching-sha2-password-cannot-be-loaded)

[authentication plugin caching_sha2 - CSDN](https://blog.csdn.net/u012613251/article/details/80346665)



## 👉 _ERROR 1698 (28000): Access denied for user ‘root’@’localhost’_.



```sql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'insert_password';
```


[How to Solve MySQL Error: Access denied for user root@localhost]: https://phoenixnap.com/kb/access-denied-for-user-root-localhost



## 👉 Runing mysql on localhost /127.0.01



[Getting Error: connect ECONNREFUSED 127.0.0.1:3306 | Stackoverflow]: https://stackoverflow.com/questions/56374530/getting-error-connect-econnrefused-127-0-0-13306




## 👉 ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2 "No such file or directory")

From the error message, I can only assume you're using the `mysql` client from your host and trying to connect it to `localhost`. The `mysql` client has a special case where it converts a hostname of `localhost` to the default Unix socket path instead, hence the error you're seeing. Swap `localhost` for `127.0.0.1` and it'll probably work.

In the future, these sorts of questions/requests would be more appropriately posted to [the Docker Community Forums](https://forums.docker.com/), [the Docker Community Slack](https://blog.docker.com/2016/11/introducing-docker-community-directory-docker-community-slack/), or [Stack Overflow](https://stackoverflow.com/search?tab=newest&q=docker).



[ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2 "No such file or directory") #157 | Github Issues]: https://github.com/MariaDB/mariadb-docker/issues/157

