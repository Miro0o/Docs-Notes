#  ⁉️ FAQ

[TOC]



+ [mac自带数据库？](https://segmentfault.com/q/1010000008968721) 

+ [Difference between ulimit, launchctl, sysctl?](https://serverfault.com/questions/502053/difference-between-ulimit-launchctl-sysctl)

+ [Mac下查看端口占用情况](http://jartto.wang/2016/09/28/check-the-system-port-of-mac/)
  + netstat
  + lsof
  + ps
  + kill   







## 👉 Customize folder icon

[macOSicons](https://macosicons.com/#/)  

[Icons](https://icons8.com/) 



[在 Mac 上更改文件或文件夹的图标]: https://support.apple.com/zh-cn/guide/mac-help/mchlp2313/mac
[在 Mac 上自定“访达”工具栏]: https://support.apple.com/zh-cn/guide/mac-help/mchlp3011/mac



## 👉👉 How to clear cache on MAC?

> :warning: Use tools like  [CleanMyMacX](../../../🧰 Tools/🚀 Productivity/Storage Manager/CleanMyMacX.md) and [Cleaner One Pro](../../../🧰 Tools/🚀 Productivity/Storage Manager/Cleaner One Pro.md) to automate the process.



### What are the main cache types?

> :link: https://macpaw.com/how-to/clear-cache-on-mac

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



:link:

[Is it safe to delete ~/Library/Caches?](https://apple.stackexchange.com/questions/118941/is-it-safe-to-delete-library-caches) 



#### homebrew

[从零开始，编写一个 HomeBrew 缓存清理脚本](https://sspai.com/post/65842)



#### telegram



#### wechat



#### qq



[How to clear cache on Mac? Here's our guide]: https://macpaw.com/how-to/clear-cache-on-mac

