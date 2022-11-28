# [Maven](https://maven.apache.org)

## 🧑🏿‍🦯 Guides

###  🎁 Res

- [菜鸟](https://www.cnblogs.com/IcanFixIt/p/6994501.html)



## 🙋‍♀️ Q&A

##### 👉 Difference between `.jar` & `.war` ?

These files are simply zipped files using the java jar tool. These files are created for different purposes. Here is the description of these files:

- **.jar files:** The .jar files **contain libraries, resources and accessories files** like property files.
- **.war files:** The war file **contains the web application** that can be deployed on any servlet/jsp container. The .war file **contains jsp, html, javascript** and other files necessary for the development of web applications.

###### 🖇 Refs:

 [Difference between jar and war in Java](https://stackoverflow.com/questions/5871053/difference-between-jar-and-war-in-java) 

## 🏀 Troubleshootings

##### 👉 Use IDEA to export `.war` pkg

>  [Difference between jar and war in Java](https://stackoverflow.com/questions/5871053/difference-between-jar-and-war-in-java) 

Steps: 

1. config `pom.xml` in Project as follow (in my case JDK17)
   1. specify packing method: `war`
   2. specify build method: plugin name & version (i didn't do this the first time, and it pop out `error: Cannot access defaults field of properties`)

```xml
<packaging>war</packaging>

<build>
    <plugins>
        <- version here has to be compliant to JDK veresion->
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>3.8.1</version>
            <configuration>
                <source>17</source>
                <target>17</target>
            </configuration>
        </plugin>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-war-plugin</artifactId>
            <version>3.3.1</version>
        </plugin>
    </plugins>
</build>
```

2. in idea's `maven` tool view:
   1. clean
   2. Compile (if needed)
   3. package --> build
3. Done! 🍻

###### 🖇 Refs:

1. [maven 打jar包和war包](https://www.cnblogs.com/hzb462606/p/9395730.html)
2. [IDEA导出jar/war包（最简单的/maven projects导出）](https://blog.csdn.net/qq_42055933/article/details/104560620) 

2. [This is a reference for the Maven project descriptor used in Maven.](https://maven.apache.org/ref/2.2.1/maven-model/maven.html)
3. [Maven error Cannot access defaults field of Properties](https://stackoverflow.com/questions/67168999/maven-error-cannot-access-defaults-field-of-properties) 
4. [JDK17 & Maven version related](https://stackoverflow.com/a/69637290/16542494)
