# Sonarqube

## π Guides

### π Resources

π [Try Out SonarQube -- official docs](https://docs.sonarqube.org/latest/)



### πͺIntro

![SonarQube Instance Components](../../../../../../Assets/Pics/dev-cycle.png)



**Sonarqube uses C/S architecture.** 

For Server side, install Sonarqube (community, professional)

For Client side, install Sonar-scanner, ant, maven or use IDE built-in plug-in. 



#### π¨ Quick-start

##### π¨ Installation

π [Prerequisites and Overview](https://docs.sonarqube.org/latest/requirements/requirements/)

brew, docker, dmg, zip ...

skip.

 

##### Config:

###### 1. Server side

> config file found under installation directory. 
>
> Mine is `/usr/local/Cellar/sonarqube/9.5.0.56709/libexec/conf`



1. JDK
2. Database (choose one of the three)
   1. [PostgreSQL](http://www.postgresql.org/)

      1. Set configuration. See specifics on  [PostgreSQL](../PostgreSQL/Intro.md) 
   2. [Microsoft SQL Server](http://www.microsoft.com/sqlserver/)
   3. [Oracle](http://www.oracle.com/database/)

      > β οΈ NOTE:
      >
      > If no exterior database specified, Sonarqube uses its own built-in databases, which reads/writes data to RAM and thus not sustainable. 
      >
      > There will be a banner π₯ at the bottom of the homepage warning data not persistent. Once connected to a persistent database system the banner goes off. 
3. Username/psword for server. 



```yaml
sonar.jdbc.username=testuser
sonar.jdbc.password=mypassword
sonar.jdbc.url=jdbc:postgresql://localhost:5432/sonarqube
```





###### 2. Client side

> config file found under installation directory. 
>
> Mine is `/usr/local/Cellar/sonar-scanner/4.7.0.2747/libexec/conf`



1. JDK
2. sonarqube server addr
3. etc. 

```properties
#Configure here general information about the environment, such as SonarQube server     connection details for example
#No information about specific project should appear here
#----- Default SonarQube server
sonar.host.url=http://localhost:9000
#----- Default source code encoding
sonar.sourceEncoding=UTF-8
```





##### π Scan

Depending on different clients, operation varies. 

Examples:

######  1οΈβ£ Sonar-scanner

```properties
# sonar-project.properties 

# ε?δΉ sonarqube ζε‘ε¨εθ‘¨ζΎη€Ίηι‘Ήη?εη§°
sonar.projectKey=devops-hello-service
 
# ε?δΉι‘Ήη?εη§°
sonar.projectName=My project
 
# ε?δΉι‘Ήη?ηηζ¬δΏ‘ζ―
sonar.projectVersion=1.0
 
# ζε?ζ«ζδ»£η ηη?ε½δ½η½?οΌε€δΈͺιε·ειοΌjavaι‘Ήη?ζΊδ»£η δΈθ¬ε¨srcη?ε½δΈι’οΌ
# ζ­€ε€δΈΊθ?Ύη½?δΈΊε½εη?ε½
sonar.sources=./
 
# ζ§θ‘ι‘Ήη?ηΌη 
sonar.sourceEncoding=UTF-8

# ζΊδ»£η ε¨ε­η?ε½
sonar.java.binaries=target
 
```



###### 2οΈβ£ Maven

Skip.



###### 3οΈβ£ Jenkins

Skip.



#### β Deploy Sonarqube on Kubernets

Tbd. 





#### π Refs

[SonarQube 03 SonarScannerηδ½Ώη¨ javaι‘Ήη?ζ«ζ]:https://blog.csdn.net/qq_34556414/article/details/117621335

