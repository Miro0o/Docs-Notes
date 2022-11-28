# [Git](https://git-scm.com)



[TOC]




 > [git often-used commands](https://www.ruanyifeng.com/blog/2015/12/git-cheat-sheet.html)
 >
 > ⭐️ [VIsual Git Cheat Sheet](https://ndpsoftware.com/git-cheatsheet.html#loc=workspace;)  
 >
 > ⭐️ [Github Git Cheat Sheet](https://training.github.com)




## 🧭 [Quick - guide](https://git-scm.com/book/en/v2)

![gitworkflow](../../../../../Assets/Pics/gitworkflow.png)



Git is a [free and open source](https://git-scm.com/about/free-and-open-source) distributed version control system designed to handle everything from small to very large projects with speed and efficiency.
Git is [easy to learn](https://git-scm.com/doc) and has a [tiny footprint with lightning fast performance](https://git-scm.com/about/small-and-fast). ==It outclasses SCM tools like Subversion, CVS, Perforce, and ClearCase== with features like [cheap local branching](https://git-scm.com/about/branching-and-merging), convenient [staging areas](https://git-scm.com/about/staging-area), and [multiple workflows](https://git-scm.com/about/distributed).



### 🥅 Tutorials & Resources:

📂 ⭐️ [Git Official Docs](https://git-scm.com/doc)

📖 [廖雪峰的官方网站 liaoxuefeng.com](https://www.liaoxuefeng.com/wiki/896043488029600/898732864121440)

🤙🏾 [install Git](https://git-scm.com/book/it/v2/Per-Iniziare-Installing-Git)

🪠 And More ... (🔗 cited from<small> [🏫 Missing tutorial - MIT --- 6️⃣ Version Control (git)](../../../../🗺 CS_Overview/🏫 Missing tutorial - MIT.md#6️⃣ Version Control - git)  </small>)

- [Pro Git](https://git-scm.com/book/en/v2) is **highly recommended reading**. Going through Chapters 1–5 should teach you most of what you need to use Git proficiently, now that you understand the data model. The later chapters have some interesting, advanced material.
- [Oh Shit, Git!?!](https://ohshitgit.com/) is a short guide on how to recover from some common Git mistakes.
- [Git for Computer Scientists](https://eagain.net/articles/git-for-computer-scientists/) is a short explanation of Git’s data model, with less pseudocode and more fancy diagrams than these lecture notes.
- [Git from the Bottom Up](https://jwiegley.github.io/git-from-the-bottom-up/) is a detailed explanation of Git’s implementation details beyond just the data model, for the curious.
- [How to explain git in simple words](https://smusamashah.github.io/blog/2017/10/14/explain-git-in-simple-words)
- [Learn Git Branching](https://learngitbranching.js.org/) is a browser-based game that teaches you Git.
- [xkcd.com](https://xkcd.com/1597/)
- 



### 👼🏻 the origin of Git

Linus is the founder of Linux OS and it's community. By the year of 2002, Linus manage codes from voluteers worldwide all by his own to maintain the community for Linus dislike the way  SCM softwares work. but as the community enlarged, the amount of workload piled up expotentially and it's growingly hard to handle this seas of code manually. hence, Linus writed his own version control system, by himself again, by C within 2 weeks. thus came the birth of the Git we're using today.



### 🛠 implementation

    1. download
    2. create git repositery
    3. set identity

```shell
$ git config --global user.name "Your Name"
$ git config --global user.email "email@example.com"

# --global here set that use this identity on every git repositery on the current machine 
```



## ❓FAQ

### 👉 [Distributed vs centralized](https://www.liaoxuefeng.com/wiki/896043488029600/896202780297248#0)

CVS/SCN is centralized, while Git is distributed. 

> 你的理解是对的，比特币的区块链设计就类似git，人手一份全账本，只是用p2p全网同步，而git通常搞个中心化服务来同步
> svn像银行，完整账本只有银行有，作为终端节点可以向银行查询账本，但如果某一天银行没了，整个完整账本就没了
> 分布式的核心设计是同步，而不是主从


 ```markdown
   
1. 使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md  
2. Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)  
3. 你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目  
4. [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目  
5. Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)  
6. Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
 ```



### 👉 [git config](https://blog.csdn.net/joe_007/article/details/7276195)

` git config ` is a git built-in tool for management of git.

 ```shell
 /etc/gitconfig
 ~/.gitconfig
 .git/config
 ```



### 👉 [update remote git to local](https://www.cnblogs.com/sxy370921/p/11734612.html)

 + fetch --> merge
	+ fetch generate a new branch on locak host.
+ pull



### 👉 [ignore git local modification and refresh from remote git.](https://blog.csdn.net/haoaiqian/article/details/78284337)

+ restore
+ reset
+ stash



###  👉 [git branching](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell) #unsolved

 TBD. 
 sound understanding of git branching is essential to the command of whole git.  



## 🔗 Ref

1. [使用git stash命令保存和恢复进度](https://blog.csdn.net/daguanjia11/article/details/73810577)
2. [git merge 与 git rebase 的区别](https://blog.csdn.net/michaelshare/article/details/79108233)
   - 两者功能上都对文件进行合并。不过merge作为一个活动会体现在git commit记录时间线上，而rebase作为一个针对时间线的操作同时也会合并时间线。
3. 你真的会高效的在GitHub搜索开源项目吗? - chainho的文章 - 知乎 https://zhuanlan.zhihu.com/p/55294261







# Gitee

https://gitee.com/help

 