   # JDBC+Servlet+Ajax实现用户增删改查

### JDBC:Java数据库连接

### Servlet:服务器端小程序

### Ajax:JS异步请求对象，访问Ｓｅｒｖｌｅｔ



## 一、数据库设计

用户表User

![img](https://img2018.cnblogs.com/blog/1173963/201905/1173963-20190503114101457-924735296.png)

用户数据:

![img](https://img2018.cnblogs.com/blog/1173963/201905/1173963-20190503114140217-1673347042.png)

sql脚本

~~~sql
CREATE DATABASE scu;

USE scu;

CREATE TABLE users
(
  id INT PRIMARY KEY,
  account VARCHAR(20) NOT NULL,
  `password` VARCHAR(20) NOT NULL,
  `name` VARCHAR(20) NOT NULL,
  info VARCHAR(20),
  create_time DATETIME,
  modify_time DATETIME
);
INSERT INTO users VALUES
(1,'zhao','123','赵','用户赵的个人信息','2021-7-24',NULL),
(2,'qian','123','钱','用户钱的个人信息','2021-7-24',NULL),
(3,'sun','123','孙','用户孙的个人信息','2021-7-24',NULL),
(4,'li','123','李','用户李的个人信息','2021-7-24',NULL);
 
~~~



## 二、示例效果

* 用户列表

![img](https://img2018.cnblogs.com/blog/1173963/201905/1173963-20190503132930443-1751317952.png)

* 添加用户:

  ![img](https://img2018.cnblogs.com/blog/1173963/201905/1173963-20190503135435092-730653586.gif)

  * 删除用户

  ![img](https://img2018.cnblogs.com/blog/1173963/201905/1173963-20190503135806378-812512066.gif)

  * 修改用户

    ![img](https://img2018.cnblogs.com/blog/1173963/201905/1173963-20190503135732391-1422118903.gif)

    

## **三、环境配置 **

使用的环境为：JDK1.8+Servlet3.0+Tomcat8.0

开发工具：idea２０１７



## 四、创建项目

在Idea中创建Java Enterprise 项目，配置JDK和tomcat,并复制以下依赖包和js

![image-20210724211915261](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210724211915261.png)

修改index.jsp文件，测试项目。

说明：

1.创建Java Enterprise项目

2.配置JDK和Tomcat

3.勾选Java Web Model

4.给项目命名

5.修改index.jsp文件

6.启动Tomcat测试 



## 五、原理图

![image-20210724225006172](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210724225006172.png)

## 六、实现步骤

### 1.用户列表

​    1。网页使用Ajax连接Servlet,

     ~~~
     <html>
       <head>
         <meta charset="utf-8"/>
         <title>测试</title>
         <!--引入Jquery 才能使用Ajax-->
         <script src="js/jquery-3.3.1.min.js"></script>
       </head>
       <body>
       <h2>用户列表</h2>
       <button onclick="getUsers()">联通servlet</button>
     
       <script>
         //点击联通servlet按钮执行的函数
         function getUsers(){
             // alert("OK")
             //使用ajax连接userServlet
             $.ajax({
                 type:'get',
                 url:'userServlet'
             });
         }
       </script>
     
       </body>
     </html>
     ~~~



​    2.服务器端设计Servlet

~~~
@WebServlet("/userServlet")  //ajax访问路径
public class UserServlet extends HttpServlet {


    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        System.out.println("联通了");
    }
}

~~~





3.servlet返回数据给网页

~~~
@WebServlet("/userServlet")  //ajax访问路径
public class UserServlet extends HttpServlet {


    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        System.out.println("联通了");
        //response响应对象：返回数据
        //设置返回数据的编码
        response.setCharacterEncoding("utf-8");
        //获得响应的输出（传输）对象out
        PrintWriter out=response.getWriter();
        //返回数据到网页
        out.print("Servlet接通了");
        //关闭
        out.flush();
        out.close();
    }
}

~~~



4.网页接收返回数据

~~~
<html>
  <head>
    <meta charset="utf-8"/>
    <title>测试</title>
    <!--引入Jquery 才能使用Ajax-->
    <script src="js/jquery-3.3.1.min.js"></script>
  </head>
  <body>
  <h2>用户列表</h2>
  <button onclick="getUsers()">联通servlet</button>

  <script>
    //点击联通servlet按钮执行的函数
    function getUsers(){
        // alert("OK")
        //使用ajax连接userServlet
        $.ajax({
            type:'get',
            url:'userServlet',
            //接收Servlet返回数据resp
            success:function(resp){
                alert(resp);
            }
        });
    }
  </script>

  </body>
</html>
~~~





5.DAO访问数据库

1)加载驱动：加载MySQL的驱动

2）打开数据库连接：Java和数据建立的通道

3）执行SQL语句：

4）得到结果：结果集

结果集ResultSet就是一个二维表

有一个记录指针，移动记录指针可以访问每行数据

next():移动记录指针

5）关闭数据库连接

UserDAO数据访问类

~~~java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class UserDAO {

    //获得全部用户数据
    public void getAllUsers(){
        try{
            //加载驱动
            Class.forName("com.mysql.jdbc.Driver");
            //获得数据库的连接
            //连接的数据库地址
            String url="jdbc:mysql://localhost:3306/scu";
            //登录账户:超级管理员root
            String user="root";
            //登录密码
            String pwd="123";
            //获得数据库的连接
            Connection con= DriverManager.getConnection(url,user,pwd);
            System.out.println("连通数据库");
            String sql="SELECT * FROM users";
            //创建Statement对象
            Statement st=con.createStatement();
            //执行SQL语句:查询executeQuery
            //并得到查询结果ResultSet
            ResultSet rs=st.executeQuery(sql);
//            //移动记录指针到第一行
//            rs.next();
//            //访问改行的字段
//            //第一个字段int类型
//            int id=rs.getInt(1);
//            //第二个字段varchar型
//            String ac=rs.getString(2);
//            System.out.println(id+","+ac);
//            rs.next();//移动到第二行
//            .....
            //全部读取结果集
            while(rs.next()){ //从头到尾逐行移动指针
                int id=rs.getInt(1);
                String ac=rs.getString(2);
                System.out.println(id+","+ac);
            }
            //关闭连接
            con.close();

        }catch (Exception e){
            e.printStackTrace();
        }


    }
    //主方法测试
    public static void main(String[] args) {
        //实例化UserDAO
        UserDAO dao=new UserDAO();
        //调用getAllUsers方法
        dao.getAllUsers();
    }
}

~~~



6.DAO返回数据

~~~java
public class UserDAO {

    //获得全部用户数据
    public String getAllUsers(){
        String result="";//查询结果
        try{
            //加载驱动
            Class.forName("com.mysql.jdbc.Driver");
            //获得数据库的连接
            //连接的数据库地址
            String url="jdbc:mysql://localhost:3306/scu";
            //登录账户:超级管理员root
            String user="root";
            //登录密码
            String pwd="123";
            //获得数据库的连接
            Connection con= DriverManager.getConnection(url,user,pwd);
            System.out.println("连通数据库");
            String sql="SELECT * FROM users";
            //创建Statement对象
            Statement st=con.createStatement();
            //执行SQL语句:查询executeQuery
            //并得到查询结果ResultSet
            ResultSet rs=st.executeQuery(sql);
            //全部读取结果集
            while(rs.next()){ //从头到尾逐行移动指针
                int id=rs.getInt(1);
                String ac=rs.getString(2);
                result+=id+","+ac+";";
            }
            //关闭连接
            con.close();

        }catch (Exception e){
            e.printStackTrace();
        }
        return result;//返回查询结果

    }
 
}
~~~



7.Servlet调用DAO,得到返回数据

~~~java
@WebServlet("/userServlet")  //ajax访问路径
public class UserServlet extends HttpServlet {


    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        System.out.println("联通了");
        //response响应对象：返回数据

        //调用DAO返回数据库数据
        UserDAO dao=new UserDAO();//实例化
        //调用getAllUser是方法,得到数据
        String res=dao.getAllUsers();

        //设置返回数据的编码
        response.setCharacterEncoding("utf-8");
        //获得响应的输出（传输）对象out
        PrintWriter out=response.getWriter();
        //返回数据到网页
        out.print(res);
        //关闭
        out.flush();
        out.close();
    }
}
~~~



7.数据封装:表==》实体对象

实体类对应一张表，表的字段在实体都有对相应

~~~java
//实体类：对应users表
//CREATE TABLE users
//        (
//        id INT PRIMARY KEY,
//        account VARCHAR(20) NOT NULL,
//        `password` VARCHAR(20) NOT NULL,
//        `name` VARCHAR(20) NOT NULL,
//        info VARCHAR(20),
//        create_time DATETIME,
//        modify_time DATETIME
//        );
public class User {
    private int id;
    private String account;
    private String pawword;
    private String name;
    private String info;
    private Date createTime;
    private Date modifyTime;

    //规范1.必须有一个无参数构造器
    public User(){}
    //规范2:每个字段必须有getter/setter


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getAccount() {
        return account;
    }

    public void setAccount(String account) {
        this.account = account;
    }

    public String getPawword() {
        return pawword;
    }

    public void setPawword(String pawword) {
        this.pawword = pawword;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getInfo() {
        return info;
    }

    public void setInfo(String info) {
        this.info = info;
    }

    public Date getCreateTime() {
        return createTime;
    }

    public void setCreateTime(Date createTime) {
        this.createTime = createTime;
    }

    public Date getModifyTime() {
        return modifyTime;
    }

    public void setModifyTime(Date modifyTime) {
        this.modifyTime = modifyTime;
    }
    //测试方便：toString（）


    @Override
    public String toString() {
        return "User{" +
                "id=" + id +
                ", account='" + account + '\'' +
                ", pawword='" + pawword + '\'' +
                ", name='" + name + '\'' +
                ", info='" + info + '\'' +
                ", createTime=" + createTime +
                ", modifyTime=" + modifyTime +
                '}';
    }
}

~~~



8.改造ＤＡＯ，封装数据到实体对象

使用集合存放多个对象

ArrayList

~~~java
public class UserDAO {

    //获得全部用户数据
    public ArrayList<User> getAllUsers(){
//        String result="";//查询结果
        //创建返回的集合
        ArrayList<User> users=new ArrayList<>();
        try{
            //加载驱动
            Class.forName("com.mysql.jdbc.Driver");
            //获得数据库的连接
            //连接的数据库地址
            String url="jdbc:mysql://localhost:3306/scu";
            //登录账户:超级管理员root
            String user="root";
            //登录密码
            String pwd="123";
            //获得数据库的连接
            Connection con= DriverManager.getConnection(url,user,pwd);
            System.out.println("连通数据库");
            String sql="SELECT * FROM users";
            //创建Statement对象
            Statement st=con.createStatement();
            //执行SQL语句:查询executeQuery
            //并得到查询结果ResultSet
            ResultSet rs=st.executeQuery(sql);
            //全部读取结果集
            while(rs.next()){ //从头到尾逐行移动指针
                //没查询一行，封装为一个User对象
                User usr=new User();
                //封装数据:从表中转换为对象
                usr.setId(rs.getInt(1));
                usr.setAccount(rs.getString(2));
                usr.setPawword(rs.getString(3));
                usr.setName(rs.getString(4));
                usr.setInfo(rs.getString(5));
                usr.setCreateTime(rs.getDate(6));
                usr.setModifyTime(rs.getDate(7));

                //添加到集合
                users.add(usr);
            }
            //关闭连接
            con.close();

        }catch (Exception e){
            e.printStackTrace();
        }
        return users;//返回查询结果

    }
    //主方法测试
    public static void main(String[] args) {
        //实例化UserDAO
        UserDAO dao=new UserDAO();
        //调用getAllUsers方法
        ArrayList<User> users=dao.getAllUsers();
        //迭代集合
        for(User u: users){
            System.out.println(u);
        }
    }
}
~~~



9、服务器网页之间的数据交换格式（JSON）(XML)

格式样式:名值对

~~~
一条数据
{
   "name":"张三",
   "gender":"男",
   "age":"18"
}
多条数据
[
  {
   "name":"张三",
   "gender":"男",
   "age":"18"  
  },
   {
   "name":"李四",
   "gender":"男",
   "age":"18"  
  },
  {
   "name":"王五",
   "gender":"男",
   "age":"18"  
  },

]
~~~

Java对象或者集合转换为JSON

转换工具:gson/jackson/...

gson.toJson(user)

~~~
转换一个对象
		User user=new User(1,"ada","123","张三");
        //对象转换JSON
        JSONObject json=new JSONObject();
        json.put("user",user);
        System.out.println(json.toString());
        执行结果
        {"user":		{"account":"ada","createTime":null,"id":1,"info":"","modifyTime":null,"name":"张三","password":"123"}}	
        
转换集合:
      //实例化UserDAO
        UserDAO dao=new UserDAO();
        //调用getAllUsers方法
        ArrayList<User> users=dao.getAllUsers();
        JSONObject json = new JSONObject();
        json.put("users", users);
        System.out.println(json);
        
结果 ：

{"users":[
   {"account":"zhao","createTime":null,"id":1,"info":"用户赵的个人信息","modifyTime":null,"name":"赵","password":"123"},
   {"account":"qian","createTime":null,"id":2,"info":"用户钱的个人信息","modifyTime":null,"name":"钱","password":"123"},
   {"account":"sun","createTime":null,"id":3,"info":"用户孙的个人信息","modifyTime":null,"name":"孙","password":"123"},
   {"account":"li","createTime":null,"id":4,"info":"用户李的个人信息","modifyTime":null,"name":"李","password":"123"}
   ]
}

~~~

改造Servlet

~~~
@WebServlet("/userServlet")  //ajax访问路径
public class UserServlet extends HttpServlet {


    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        System.out.println("联通了");
        //response响应对象：返回数据

        //调用DAO返回数据库数据
        UserDAO dao=new UserDAO();//实例化
        //调用getAllUser是方法,得到数据
        ArrayList<User> users=dao.getAllUsers();
        //将users转换为ＪＳＯＮ
        JSONObject json=new JSONObject();
        json.put("users",users);
        //设置返回数据的编码
        response.setCharacterEncoding("utf-8");
        //获得响应的输出（传输）对象out
        PrintWriter out=response.getWriter();
        //返回数据到网页
        out.print(json.toString());
        //关闭
        out.flush();
        out.close();
    }
}
~~~



10、网页数据渲染

~~~
<h2>用户列表</h2>
  <button onclick="getUsers()">全部用户信息</button>
  <table id="userlist" border="1">
    <tr>
      <th>ID</th>
      <th>账号</th>
      <th>昵称</th>
      <th>用户信息</th>
    </tr>
  </table>
  <script>
    //点击联通servlet按钮执行的函数
    function getUsers(){
        // alert("OK")
        //使用ajax连接userServlet
        $.ajax({
            type:'get',
            url:'userServlet',
            //指定返回数据类型为json
            dataType:'json',
            //接收Servlet返回数据
            success:function(data){
                // console.log(data);
                // // alert(data.users);
                for(var i=0;i<data.users.length;i++){
                    var user=data.users[i];//得到第i个元素
                    var str="<tr><td>"+user.id+"</td><td>"+user.account+"</td><td>"
                        +user.name+"</td><td>"+user.info+"</td></tr>";
                    //$("#userlist")找到ID为userist的元素
                    //append添加行
                    $("#userlist").append(str);
                }
            }
        });
    }
  </script>
~~~



11.Web流程总结

1)网页使用ajax 访问服务器servlet

2)servlet调用DAO

3)DAO访问数据库

4)DAO将结果封装实体对象返回给servlet

5)servlet将实体对象结果结果转换为JSON返回网页

6)网页ajax接收JSON数据，渲染数据()



### 2.添加用户信息

1.添加表单

~~~HTML
<h2>添加用户</h2>
  <form>
    ID:<input type="text" id="id"/><br/>
    账号:<input type="text" id="accout" /><br/>
    昵称:<input type="text" id="name" /><br/>
    用户信息:<input type="text" id="info"/><br/>
    <button onclick="addUser()">添加</button>
  </form>
   <script>
     function addUser(){
        //获得用户输入数据
        var id=$('#id').val();
        var account=$('#account').val();
        var name=$('#name').val();
        var info=$('#info').val();
         //封装为json
        var data={
            id:id,
            account:account,
            name:name,
            info:info
        };
        $.ajax({
            type:'post',  //post方式添加数据
            url:'userServlet',
            data:data,  //上传数据
            success:function(resp){
                alert(resp);
            }
        })
    }
~~~

2.Userservlet增加doPost方法对应post方式请求,并测试连通性

~~~java
    //添加用户POST方式
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        System.out.println("联通了");
        
        //获得响应的输出（传输）对象out
        PrintWriter out=response.getWriter();
        //返回数据到网页
        out.print("添加servlet联通");
        //关闭
        out.flush();
        out.close();
    }
}
~~~

3.UserServlet接收上传数据

~~~java
    //添加用户POST方式
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        System.out.println("联通了");
        //设置上传数据编码，放置乱码
        request.setCharacterEncoding("utf-8");
        //按名接收数据:注意数据都是String类型
        String ids=request.getParameter("id");
        String account=request.getParameter("account");
        String name=request.getParameter("name");
        String info=request.getParameter("info");

        //测试数据
        System.out.println(ids+account+name+info);
        response.setCharacterEncoding("utf-8");
        PrintWriter out=response.getWriter();
        out.print(ids+account+name+info);
        out.flush();
        out.close();
    }
~~~

4.封装并保存数据

UserDAO

~~~java
public class UserDAO {
    //保存用户信息
    public int save(User user){
      int result=0;
        try{
            //加载驱动
            Class.forName("com.mysql.jdbc.Driver");
            //获得数据库的连接
            //连接的数据库地址
            String url="jdbc:mysql://localhost:3306/scu";
            //获得数据库的连接
            Connection con= DriverManager.getConnection(url,"root","123");
            //SQL语句
            String sql="insert into users(id,account,name,info,password) values(?,?,?,?,'123')";

            //创建预编译命令对象
            PreparedStatement pst=con.prepareStatement(sql);
            //设置？参数的值
            pst.setInt(1,user.getId());
            pst.setString(2,user.getAccount());
            pst.setString(3,user.getName());
            pst.setString(4,user.getInfo());

            //执行SQL语句:增删改
            result=pst.executeUpdate();

            //关闭连接
            con.close();

        }catch (Exception e){
            e.printStackTrace();
        }
        return result;
    }
~~~



UserServlet

~~~java
      //添加用户POST方式
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        System.out.println("联通了");
        //设置上传数据编码，放置乱码
        request.setCharacterEncoding("utf-8");
        //接收上传数据

        //方法1：按名接收数据:注意数据都是String类型
//        String ids=request.getParameter("id");
//        String account=request.getParameter("account");
//        String name=request.getParameter("name");
//        String info=request.getParameter("info");
//
//        //封装数据
//        User user=new User();
//        int id=Integer.parseInt(ids);//转换为整数
//        user.setId(id);
//        user.setAccount(account);
//        user.setInfo(info);
//        user.setName(name);

        //方法2:直接将上传数据封装为实体对象,要求上传JSON字段名和实体对象字段名匹配
        User user=new User();
        try {
            BeanUtils.populate(user, request.getParameterMap());
        }catch (Exception e){
            e.printStackTrace();
        }

        //调用DAO,保存数据
        UserDAO dao=new UserDAO();
        int result=dao.save(user);


        response.setCharacterEncoding("utf-8");
        PrintWriter out=response.getWriter();
        if(result>0){
            out.print("添加成功!");
        }else{
            out.print("添加失败！");
        }

        out.flush();
        out.close();
    }
~~~

### 3.删除用户

1.index.jsp

~~~
 <script>
    function delUser(id){
        if(!confirm("确定删除?")) return;
        $.ajax({
            type:'delete',
            url:'userServlet?id='+id,
            success:function (resp) {
                alert(resp);
            }
        });

    }
    //点击联通servlet按钮执行的函数
    function getUsers(){
        // alert("OK")
        //使用ajax连接userServlet
        $.ajax({
            type:'get',
            url:'userServlet',
            //指定返回数据类型为json
            dataType:'json',
            //接收Servlet返回数据
            success:function(data){
                // console.log(data);
                // // alert(data.users);
                for(var i=0;i<data.users.length;i++){
                    var user=data.users[i];//得到第i个元素
                    var str="<tr><td>"+user.id+"</td><td>"+user.account+"</td><td>"
                        +user.name+"</td><td>"+user.info+"</td>"
                        +"<td><button onclick='delUser("+user.id+")'>删除</button></td></tr>";
                    //$("#userlist")找到ID为userist的元素
                    //append添加行
                    $("#userlist").append(str);
                }
            }
        });
    }
~~~

2.UserDAO

~~~java
public class UserDAO {

    //按id删除用户
    public int del(int id){
        int result=0;
        try{
            //加载驱动
            Class.forName("com.mysql.jdbc.Driver");
            //获得数据库的连接
            //连接的数据库地址
            String url="jdbc:mysql://localhost:3306/scu";
            //获得数据库的连接
            Connection con= DriverManager.getConnection(url,"root","123");
            //SQL语句
            String sql="delete from users where id=?";

            //创建预编译命令对象
            PreparedStatement pst=con.prepareStatement(sql);
            //设置？参数的值
            pst.setInt(1,id);

            //执行SQL语句:增删改
            result=pst.executeUpdate();//返回整数>0表示成功,=0表示语句执行失败

            //关闭连接
            con.close();

        }catch (Exception e){
            e.printStackTrace();
        }
        return result;
    }

~~~

3.UserServlet

~~~java
 protected void doDelete(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        System.out.println("联通了");

        int id=Integer.parseInt(request.getParameter("id"));

        UserDAO dao=new UserDAO();
        int result=dao.del(id);

        response.setCharacterEncoding("utf-8");
        PrintWriter out=response.getWriter();
        if(result>0){
            out.print("删除成功!");
        }else{
            out.print("删除失败！");
        }

        out.flush();
        out.close();
    }
~~~



4.数据库工具化

DBUtil

~~~
package scu.util;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

/**
 * 数据库工具类
 */
public class DBUtil {
    //加载驱动
    static {
        try{
            Class.forName("com.mysql.jdbc.Driver");
        }catch (Exception e){
            e.printStackTrace();
        }
    }

    /**
     * 获得连接
     * @return
     * @throws Exception
     */
    public static Connection getCon() throws Exception{
        String url="jdbc:mysql://localhost:3306/scu";
        Connection con= DriverManager.getConnection(url,"root","123");
        return con;
    }

    /**
     * 执行增删改
     * @param sql
     * @param args
     * @throws Exception
     */
    public static int update(String sql,Object... args) throws Exception{
        Connection con=getCon();
        PreparedStatement pst=con.prepareStatement(sql);
        for(int i=0;i<args.length;i++){
            pst.setObject(i+1,args[i]);
        }
        int r=pst.executeUpdate();
        con.close();
        return r;
    }

    /**
     * 执行查询
     * @param con
     * @param sql
     * @param args
     * @return
     * @throws Exception
     */
    public static ResultSet query(Connection con, String sql, Object... args) throws Exception{
        PreparedStatement pst=con.prepareStatement(sql);
        for(int i=0;i<args.length;i++){
            pst.setObject(i+1,args[i]);
        }
        ResultSet rs=pst.executeQuery();
        return rs;
    }
}
~~~

DAO改造

~~~
package scu.dao;

import scu.domain.User;
import scu.util.DBUtil;

import java.sql.*;
import java.util.ArrayList;

public class UserDAO {

    //按id删除用户
    public int del(int id){
        int result=0;
        try{
            //SQL语句
            String sql="delete from users where id=?";
            DBUtil.update(sql,id);
        }catch (Exception e){
            e.printStackTrace();
        }
        return result;
    }
    //保存用户信息
    public int save(User user){
      int result=0;
        try{
            //加载驱动
            String sql="insert into users(id,account,name,info,password) values(?,?,?,?,'123')";
            result=DBUtil.update(sql,user.getId(),user.getAccount(),user.getName(),user.getInfo());
        }catch (Exception e){
            e.printStackTrace();
        }
        return result;
    }
    //获得全部用户数据
    public ArrayList<User> getAllUsers(){
        //创建返回的集合
        ArrayList<User> users=new ArrayList<>();
        try{

            String sql="SELECT * FROM users";
            Connection con=DBUtil.getCon();
            ResultSet rs=DBUtil.query(con,sql);
            //全部读取结果集
            while(rs.next()){ //从头到尾逐行移动指针
                //没查询一行，封装为一个User对象
                User usr=new User();
                //封装数据:从表中转换为对象
                usr.setId(rs.getInt(1));
                usr.setAccount(rs.getString(2));
                usr.setPassword(rs.getString(3));
                usr.setName(rs.getString(4));
                usr.setInfo(rs.getString(5));
                //添加到集合
                users.add(usr);
            }
            //关闭连接
            con.close();

        }catch (Exception e){
            e.printStackTrace();
        }
        return users;//返回查询结果

    }



}

~~~



### 4.连接池

阿里的Druid连接池

C3P0连接池



## 任务

- 代码任务
  - 基本任务：查询所有、删除、增加的实现
  - 扩展任务：查看详情、编辑、搜索的实现
- 项目任务
  - 完成项目的功能模块的分析：xmind
  - 完成项目的数据库设计：PD
  - 提交两个文档：转成图片提交

# 项目分析

- 1.两金申报——项目申报
- 2.资源管理系统——项目管理
- 3.电商系统

## 需求分析

- 明确做什么：功能结构图来体现，流程图
- 用户需求——软件需求的过程
- 构建一个能够应用的项目需求

## 数据库设计

- 根据项目功能分析，确定需要哪些表来存储数据
- E-R图
  - 实体
  - 关系
- 数据库分析的过程
  - 找主要实体（名词），依赖实体
  - 找实体之间的关系：
    - 一对一：人和身份证
    - 一对多：老师和学生
    - 多对一：影片和影片类型
    - 多对多：影片和用户
  - 确定实体的属性

## PD

