# Servlet

> 来自[廖雪峰](https://www.liaoxuefeng.com/wiki/1252599548343744/1255945497738400) ：java web dev.

普通的Java程序是通过启动JVM，然后执行`main()`方法开始运行。但是Web应用程序有所不同，我们无法直接运行`war`文件，必须先启动Web服务器，再由Web服务器加载我们编写的`HelloServlet`，这样就可以让`HelloServlet`处理浏览器发送的请求。

因此，我们首先要找一个支持Servlet API的Web服务器。常用的服务器有：

-   [Tomcat](https://tomcat.apache.org/)：由Apache开发的开源免费服务器；
-   [Jetty](https://www.eclipse.org/jetty/)：由Eclipse开发的开源免费服务器；
-   [GlassFish](https://javaee.github.io/glassfish/)：一个开源的全功能JavaEE服务器。

还有一些收费的商用服务器，如Oracle的[WebLogic](https://www.oracle.com/middleware/weblogic/)，IBM的[WebSphere](https://www.ibm.com/cloud/websphere-application-platform/).



