# ❓FAQ

[TOC]



## 👉 [Distributed vs centralized](https://www.liaoxuefeng.com/wiki/896043488029600/896202780297248#0)

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



## 👉 [git config](https://blog.csdn.net/joe_007/article/details/7276195)

` git config ` is a git built-in tool for management of git.

 ```shell
/etc/gitconfig
~/.gitconfig
.git/config
 ```



## 👉 [update remote git to local](https://www.cnblogs.com/sxy370921/p/11734612.html)

 + fetch --> merge
   + fetch generate a new branch on locak host.
+ pull



## 👉 [ignore git local modification and refresh from remote git.](https://blog.csdn.net/haoaiqian/article/details/78284337)

+ restore
+ reset
+ stash



##  👉 [git branching](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell) #unsolved

 TBD. 
 sound understanding of git branching is essential to the command of whole git.  



## 👉  [Git: Could not resolve host github.com error while cloning remote repository in git](https://stackoverflow.com/questions/20370294/git-could-not-resolve-host-github-com-error-while-cloning-remote-repository-in)

**Error: "fatal: unable to access 'https://domain.com' Could not resolve host: github.com"**

It seems to be the proxy problem. Somehow the `http_proxy` and `https_proxy` is directed to the wrong address / protocols / other things. Reconfig `~/.gitrc` .



## Ref

[使用git stash命令保存和恢复进度]: https://blog.csdn.net/daguanjia11/article/details/73810577git
[merge 与 git rebase 的区别]: https://blog.csdn.net/michaelshare/article/details/79108233

- 两者功能上都对文件进行合并。不过merge作为一个活动会体现在git commit记录时间线上，而rebase作为一个针对时间线的操作同时也会合并时间线。

[git 添加多个远程仓库]: https://segmentfault.com/q/1010000008366409

