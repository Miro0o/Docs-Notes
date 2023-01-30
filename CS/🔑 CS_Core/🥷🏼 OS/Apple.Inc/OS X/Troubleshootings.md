# 🛠 Troubleshooting 

[TOC]



## 👉 [WindowServer taking up to much memory](https://macsecurity.net/view/393-windowserver-mac)

+ [to reduce windowserver memory&cpu](https://blog.mynook.info/post/macos-windowserver-calm-down/)
+ 

[sharing files](https://support.apple.com/zh-cn/guide/mac-help/mh17131/mac)

[check IPv6 on local host](https://www.cnblogs.com/cuihongyu3503319/p/7422877.html)

[compress file + .DS_Store](https://blog.csdn.net/doublebaidu/article/details/121417602)



## 👉 [to Quick-look/preview any source file on mac](https://paaatrick.com/2020-04-05-make-mac-quicklook-any-code-source-file/) #unsolved

+ brew 
  + qlcolorcode
    + support high-light code
  + qlstephen
    + support customized source-file preview

+ config
  + `~/Library/QuickLook/QLColorCode.qlgenerator/Contents/Info.plist`
  + `Document types > Item 0 > Document Content Type UTIs (CFBundleDocumentTypes > Item 0 > LSItemContentTypes`
  + use command line `mdls -name kMDItemContentType ./main.dart ` to check out a file's type name. example here look into the file './main.dart' and it returns as `kMDItemContentType = "com.apple.disk-image-dart"`. in real case change the file name to the real one. 



## 👉 [Garbled on macOS](https://www.jianshu.com/p/8b3de75f2658)  #unsolved

**第一种乱码类型**

在网络上查了一圈，找到三个相关答案：

1.  下载的文件名总是「乱码」？这里有各平台的解决方法 ：  
    [https://sspai.com/post/44360](https://links.jianshu.com/go?to=https%3A%2F%2Fsspai.com%2Fpost%2F44360)  
    Automator 流程:  
    [https://cl.ly/2v1E3n3f1q2M](https://links.jianshu.com/go?to=https%3A%2F%2Fcl.ly%2F2v1E3n3f1q2M)
2.  Mac OS X 下文件名乱码出现的原因和解决方法：  
    [https://zzi.io/?p=275](https://links.jianshu.com/go?to=https%3A%2F%2Fzzi.io%2F%3Fp%3D275)
3.  预组字符：  
    [https://zh.wikipedia.org/wiki/预组字符](https://links.jianshu.com/go?to=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E9%25A2%2584%25E7%25BB%2584%25E5%25AD%2597%25E7%25AC%25A6)



## 👉 macOS Mail

- [config mail](https://blog.csdn.net/houseq/article/details/39297111)

  

## 👉 [Mac 配置本地https 服务](https://www.jianshu.com/p/d22baeae50ea) #unsolved

1. built-in [apache http server](https://httpd.apache.org/#essentials)



## 👉 开机启动

https://www.jianshu.com/p/eee8a7de179c



## 👉 disable "Background item added" notification on macos Ventura

This seems to be a current bug due to migrating from a previous version of macOS and most people are forced to simply wait for an update that resolves the issue.

Consider reinstalling the offending applications. As an added precaution, once they are uninstalled visit these locations and delete the associated Google Launcher and Citrix Systems files:

`/Library/LaunchAgents`

`/Library/LaunchDaemons`

`/Users/[username]/Library/LaunchAgents`

  After carefully deleting those files reinstall the apps and see if that fixes their associations.



[how to disable "Background items Added" notification in mac os Ventura]:https://superuser.com/questions/1761503/how-to-disable-background-items-added-notification-in-mac-os-ventura
[Perpetual "Background Items Added"]: https://discussions.apple.com/thread/254341579





## 👉 [Mac上的欧路词典单词本迁移到有道词典 #node.js](https://www.cnblogs.com/howmacist/p/6240863.html)

TBD..



## 👉  [Git is not working after macOS Update (xcrun: error: invalid active developer path (/Library/Developer/CommandLineTools)](https://stackoverflow.com/questions/52522565/git-is-not-working-after-macos-update-xcrun-error-invalid-active-developer-pa)

In my case i entered following:

```shell
xcode-select --install
```

And follow the prompt. Everything Done!

**More info:**

[Install Xcode Command Line Tools]: https://mac.install.guide/commandlinetools/index.html



