# Apache HTTP Server

Apache HTTP Server ~~aka 'httpd'~~ is a http server software under *Apache Software Foundation* and *Apache HTTP Server Project*. 

Apachectl is a client programme for operation httpd. For instance to start httpd server run `sudo apachectl start` on Terminal. 



## 🧭 Guides

### Resources

📂 [Apache HTTP Server Version 2.4 Documentation](https://httpd.apache.org/docs/current/)

📂 [Apache Http Server Project](https://httpd.apache.org)

📖 [Apache HTTP Server Wiki](https://cwiki.apache.org/confluence/display/HTTPD/Home)



### Intro

Default configuration file : `/usr/local/apache2/conf`

> in my case: `/etc/apache2/httpd.conf` (🍎 apple built-in httpd)
>
> in my case: `/usr/local/etc/httpd/httpd.conf` (🍺 homebrew httpd)



Configuration file specifies every detail here needs. 



Default [DocumentRoot](https://httpd.apache.org/docs/current/mod/core.html#documentroot): `/Library/WebServer/Documents`

> in my case: `/Users/mir0/Desktop/server`



## ⚙️ Config

[httpd配置文件详解及实例](https://www.cnblogs.com/yinzhengjie/p/7764392.html)



## 🏀 Troubleshootings

###### 👉 Change default httpd on Mac to homebrewed httpd

 [Changing default Apache version on Mac OS](https://stackoverflow.com/questions/68111189/changing-default-apache-version-on-mac-os) 

[Mac重新安装PHP和Apache](https://www.yulei1989.com/mac重新安装php和apache/)

Steps:

1. stop default apple httpd (if running)

2. disable auto-launch when booting 

   1. ` sudo launchctl unload -w /System/Library/LaunchDaemons/org.apache.httpd.plist `

      > ERROR:
      >
      > here i encountered this error: [launchctl unload say: Could not find specified service](https://superuser.com/questions/1364790/launchctl-unload-say-could-not-find-specified-service)
      >
      >   

3. install httpd on homebrew

   1. `brew install httpd`

4. start homebrew httpd service

   1. `brew services start httpd`

> NOTICE:
>
>  old apple conf : `/etc/apache2/httpd.conf`
>
> whereas homebrew's is in `/usr/local/etc/httpd/httpd.conf`



## 🔗 Refs:

1. [httpd配置文件详解及实例](https://www.cnblogs.com/yinzhengjie/p/7764392.html)
2. [mac 自带 apache 详解](https://www.yisu.com/zixun/164931.html)
   [mac 自带 php](https://www.jianshu.com/p/8408a20a7110)

>ps: PHP was deprecated in macOS 11 and removed from macOS 12

3. [vhost](https://httpd.apache.org/docs/current/vhosts/examples.html)
4. [sign homebrew php module for macOS](https://www.simplified.guide/macos/apache-php-homebrew-codesign)
5. [Apache Configuration Error AH00558: Could not reliably determine the server's fully qualified domain name](https://www.digitalocean.com/community/tutorials/apache-configuration-error-ah00558-could-not-reliably-determine-the-server-s-fully-qualified-domain-name#setting-a-global-servername-directive)
6. [macOS XAMMP VirtualHost](https://www.jianshu.com/p/ffab257889a8)
7. [mac setting up virtual hosts](https://daily-dev-tips.com/posts/mac-os-x-setting-up-virtual-hosts/)
8. [如何通过Homebrew程序在macOS上安装Apache](https://www.onitroad.com/jc/archive/install-apache-macos-homebrew.html)
9. ⭐️ [macOS 12.0 Monterey Apache Setup: Multiple PHP Versions](https://getgrav.org/blog/macos-monterey-apache-multiple-php-versions)
   - [PHP 8.0: Apache Handler: Module name and file path changes](https://php.watch/versions/8.0/mod_php-rename)
   - [Apache配置PHP](https://www.yulei1989.com/apache配置php/)
   - [Mac重新安装PHP和Apache](https://www.yulei1989.com/mac重新安装php和apache/)
   - [brew-php-switcher](https://github.com/philcook/brew-php-switcher)
10. Tbd...



[httpd配置文件详解及实例](https://www.cnblogs.com/yinzhengjie/p/7764392.html)
