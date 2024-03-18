# FAQ

[TOC]



+ [mac自带数据库？](https://segmentfault.com/q/1010000008968721) 

+ [Difference between ulimit, launchctl, sysctl?](https://serverfault.com/questions/502053/difference-between-ulimit-launchctl-sysctl)

+ [Mac下查看端口占用情况](http://jartto.wang/2016/09/28/check-the-system-port-of-mac/)
  + netstat
  + lsof
  + ps
  + kill   


## 👉 Customize folder icon
#macos #customization

[macOSicons](https://macosicons.com/#/)  

[Icons](https://icons8.com/) 



[在 Mac 上更改文件或文件夹的图标]: https://support.apple.com/zh-cn/guide/mac-help/mchlp2313/mac
[在 Mac 上自定“访达”工具栏]: https://support.apple.com/zh-cn/guide/mac-help/mchlp3011/mac



## 👉👉 How to clear cache on MAC?
#macos #cache

> ⚠ Use tools like  [CleanMyMacX](../../../🧰 Tools/🚀 Productivity/Storage Manager/CleanMyMacX.md) and [Cleaner One Pro](../../../🧰 Tools/🚀 Productivity/Storage Manager/Cleaner One Pro.md) to automate the process.

### What are the main cache types?
> 🔗 https://macpaw.com/how-to/clear-cache-on-mac

There are roughly three main types of caches on your Mac:

#### System cache
Mac's system cache is a memory bank that connects the main memory and the processor. This allows the CPU, or central processing unit, to retrieve data that your device uses to execute instructions quickly and without the need to load it bit by bit.

#### Browser cache
No matter what web browser you use, they all have their own cache. Those caches store files and their elements like HTML, CSS, JavaScript, cookies, or images that your browser uses to display websites. For instance, product page images, login information, shopping cart content, etc. 

#### User cache (including app cache)
Just like a web browser, the app maintains cache of its own. It helps quickly reload images, search history, videos, and other needed information to speed up and improve the performance and efficiency of the apps.

Keep on reading to find out how to get rid of cache files — either automatically or manually.



### Large space comsuming locations
#### `/System/Library/Caches`
Seems to be important. Don't touch this location for the time being.


#### `~/Library/Caches`
It's generally safe, though a little dangerous depending, to do it but often not worth the effort.

The caches in `/System/Library/Caches` are generally small and useful, the ones in `/Library/Caches` are less system caches and much more readily cleared.

If you have a look in `~/Library/Caches` you will find a bunch of applications have a cache in there, none of them particularly large though dropbox sometimes has a fair sized cache. This folder can run quite large just because so many apps cache something in there.

If the cache `/Library/Caches` folder is over 3Gb then you have something that is caching quite a lot. On the three machines I just checked none had a `/Library/Caches` folder over .75 Gb so I'd go right ahead and remove some of it.

Don't worry about age, I'd worry about size.

In the terminal run the following to sort all of the files in that directory by size (ascending):

```sh
du -sh /Library/Caches/* | sort -h
```

Of course the best way to clear the caches is to install [AppleJack](http://applejack.sourceforge.net/) and do it with that in single user mode. Doing it with the System fully up can be a little dangerous. If you do it then I'd reboot immediately afterwards.

🔗 [Is it safe to delete ~/Library/Caches?](https://apple.stackexchange.com/questions/118941/is-it-safe-to-delete-library-caches) 


#### homebrew

[从零开始，编写一个 HomeBrew 缓存清理脚本](https://sspai.com/post/65842)

#### telegram

#### wechat

#### qq

[How to clear cache on Mac? Here's our guide]: https://macpaw.com/how-to/clear-cache-on-mac



## 👉 Swap memory usage too high
#macos #memory

> 🔗 https://apple.stackexchange.com/a/413259

So long as memory pressure looks OK, there's nothing to worry about.

macOS keeps things cached in RAM as long as that RAM is not needed by anything else - that gives it a tendency overall to look like it fills up & never empties.

The same can be said of swap. It fills, the contents may change, but the swap figure displayed is always a "high tide" figure. You never see it go down until you reboot.

It doesn't serve you or the OS well at all if it were to periodically flush unused RAM or swap just to "look tidier". Its purpose is best served by it just hanging onto it all in case it's needed again

> 🔗 https://apple.stackexchange.com/a/413352

There are two major misconceptions that are often seen in relation to memory management:

-   Full RAM is bad.
-   Full swap is bad.

Both are wrong.

...



## 👉 Turn off finder sounds
#macos #finder

This is annoying because whenever i'm palying music on my airpods from my phone, this finder sound effect from my mac kept came up and interrupt the music and force the sound player switch to the mac. 😠 F*

System Settings >> Sound >> Sound Effects >> Play user interface sound effects [uncheck]



## 👉 What Is Patext Mac
#macos #patext

Patext Mac is the name of an ad-supported program, whose primary purpose of activity is to enter your Mac while seeming like a helpful application, but in reality may cause multiple different advertisements to begin appearing on your computer, such as pop-ups and redirects. These ads are purely shown for profit and seeing them may lead to different types of risky websites in some cases. This is the main reason why it is strongly advisable to focus on removing this risky software from your Mac as soon as you can.

[What Is Patext Mac]: https://sensorstechforum.com/patext-mac-removal/



## 👉 What is Cryptexes?
#macos #cryptexes

> Where is it coming from?  
> Is it safe to keep?  
> Is it okay to remove from PATH?

`/System/Cryptexes` is part of [macOS security](https://eclecticlight.co/2022/11/16/cryptex-how-a-custom-iphone-is-changing-macos-updates/). Mostly Safari and a few other features use it.

So it came from Apple, it is safe to keep, and if you don't use anything in there it is likley safe to remove.



[What is this weird directory in my PATH on my Mac, (running latest macOS Ventura)? | StackExchange]: https://unix.stackexchange.com/q/725215



## 👉 [to Quick-look/preview any source file on mac](https://paaatrick.com/2020-04-05-make-mac-quicklook-any-code-source-file/) 
#unsolved

+ brew 
  + qlcolorcode
    + support high-light code
  + qlstephen
    + support customized source-file preview

+ config
  + `~/Library/QuickLook/QLColorCode.qlgenerator/Contents/Info.plist`
  + `Document types > Item 0 > Document Content Type UTIs (CFBundleDocumentTypes > Item 0 > LSItemContentTypes`
  + use command line `mdls -name kMDItemContentType ./main.dart ` to check out a file's type name. example here look into the file './main.dart' and it returns as `kMDItemContentType = "com.apple.disk-image-dart"`. in real case change the file name to the real one. 



## 👉 [Mac上的欧路词典单词本迁移到有道词典 #node.js](https://www.cnblogs.com/howmacist/p/6240863.html)

TBD..





## 👉 Configure macOS Mail

- [config mail](https://blog.csdn.net/houseq/article/details/39297111)

  

## 👉 [Mac 配置本地https 服务](https://www.jianshu.com/p/d22baeae50ea) 
#unsolved 

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



