# Troubleshootings

[TOC]



### 👉 Change default httpd on Mac to homebrewed httpd

Steps:

1. stop default apple httpd (if running)

2. disable auto-launch when booting 

   1. ` sudo launchctl unload -w /System/Library/LaunchDaemons/org.apache.httpd.plist `

      > ERROR:
      >
      > here i encountered this error: [launchctl unload say: Could not find specified service](https://superuser.com/questions/1364790/launchctl-unload-say-could-not-find-specified-service)

3. install httpd on homebrew

   1. `brew install httpd`

4. start homebrew httpd service

   1. `brew services start httpd`

> NOTICE:
>
>  old apple conf : `/etc/apache2/httpd.conf`
>
> whereas homebrew's is in `/usr/local/etc/httpd/httpd.conf`


[Changing default Apache version on Mac OS]: https://stackoverflow.com/questions/68111189/changing-default-apache-version-on-mac-os
[Mac重新安装PHP和Apache]: https://www.yulei1989.com/mac重新安装php和apache/



## Ref

