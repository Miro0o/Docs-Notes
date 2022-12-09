# Github

[TOC]

## [如何使用 GitHub](https://csdiy.wiki/必学工具/GitHub/)

如果你还从未在 GitHub 上建立过自己的远程仓库，也没有克隆过别人的代码，那么我建议你从 [GitHub的官方教程](https://docs.github.com/cn/get-started)开始自己的开源之旅。

如果你想时刻关注 GitHub 上一些有趣的开源项目，那么我向你重磅推荐 [HelloGitHub](https://hellogithub.com/) 这个网站以及它的同名微信公众号。它会定期收录 GitHub 上近期开始流行的或者非常有趣的开源项目，让你有机会第一时间接触各类优质资源。

GitHub 之所以成功，我想是得益于“我为人人，人人为我”的开源精神，得益于知识分享的快乐。如果你也想成为下一个万人敬仰的开源大佬，或者下一个 star 破万的项目作者。那就把你在开发过程中灵感一现的 idea 化作代码，展示在 GitHub 上吧～

不过需要提醒的是，开源社区不是法外之地，很多开源软件并不是可以随意复制分发甚至贩卖的，了解各类[开源协议](https://www.runoob.com/w3cnote/open-source-license.html)并遵守，不仅是法律的要求，更是每个开源社区成员的责任。



## ⚱️ Resources

[github docs](https://docs.github.com/en)

[gh: Github CLI](https://cli.github.com/manual/gh)



## 🧸 Extensions

### GCM

>  More info TBD..

[Git Credential Manager](https://github.com/GitCredentialManager/git-credential-manager) (GCM) is a secure [Git credential helper](https://git-scm.com/docs/gitcredentials) built on [.NET](https://dotnet.microsoft.com/) that runs on Windows, macOS, and Linux. It aims to provide a consistent and secure authentication experience, including multi-factor auth, to every major source control hosting service and platform.

GCM supports (in alphabetical order) [Azure DevOps](https://dev.azure.com/), Azure DevOps Server (formerly Team Foundation Server), Bitbucket, GitHub, and GitLab. Compare to Git's [built-in credential helpers](https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage) (Windows: wincred, macOS: osxkeychain, Linux: gnome-keyring/libsecret), which provide single-factor authentication support for username/password only.

GCM replaces both the .NET Framework-based [Git Credential Manager for Windows](https://github.com/microsoft/Git-Credential-Manager-for-Windows) and the Java-based [Git Credential Manager for Mac and Linux](https://github.com/microsoft/Git-Credential-Manager-for-Mac-and-Linux).

#### Install

See the [installation instructions](https://github.com/GitCredentialManager/git-credential-manager/blob/release/docs/install.md) for the current version of GCM for install options for your operating system.

#### Current status

Git Credential Manager is currently available for Windows, macOS, and Linux*. GCM only works with HTTP(S) remotes; you can still use Git with SSH:

- [Azure DevOps SSH](https://docs.microsoft.com/en-us/azure/devops/repos/git/use-ssh-keys-to-authenticate?view=azure-devops)
- [GitHub SSH](https://help.github.com/en/articles/connecting-to-github-with-ssh)
- [Bitbucket SSH](https://confluence.atlassian.com/bitbucket/ssh-keys-935365775.html)

#### How to use

Once it's installed and configured, Git Credential Manager is called implicitly by Git. You don't have to do anything special, and GCM isn't intended to be called directly by the user. For example, when pushing (`git push`) to [Azure DevOps](https://dev.azure.com/), [Bitbucket](https://bitbucket.org/), or [GitHub](https://github.com/), a window will automatically open and walk you through the sign-in process. (This process will look slightly different for each Git host, and even in some cases, whether you've connected to an on-premises or cloud-hosted Git host.) Later Git commands in the same repository will re-use existing credentials or tokens that GCM has stored for as long as they're valid.

Read full command line usage [here](https://github.com/GitCredentialManager/git-credential-manager/blob/release/docs/usage.md).

#### Configuring a proxy

See detailed information [here](https://github.com/GitCredentialManager/git-credential-manager/blob/release/docs/netconfig.md#http-proxy).

#### Additional Resources

See the [documentation index](https://github.com/GitCredentialManager/git-credential-manager/blob/release/docs/README.md) for links to additional resources.

#### Experimental Features

- [Windows broker (experimental)](https://github.com/GitCredentialManager/git-credential-manager/blob/release/docs/windows-broker.md)



### [GitHubpage](https://pages.github.com)

#### [Blogging with Jekyll](https://help.github.com/articles/using-jekyll-with-pages)

Using [Jekyll](https://jekyllrb.com/), you can blog using beautiful Markdown syntax, and without having to deal with any databases. [Learn how to set up Jekyll](https://jekyllrb.com/docs/).

#### [Custom URLs](https://help.github.com/articles/setting-up-a-custom-domain-with-pages)

Want to use your own custom domain for a GitHub Pages site? Just create a file named CNAME and include your URL. [Read more](https://help.github.com/articles/setting-up-a-custom-domain-with-pages).

#### [Guides](https://help.github.com/categories/20/articles)

Learn how to create custom 404 pages, use submodules, and [learn more about GitHub Pages](https://help.github.com/categories/20/articles).



## ❓FAQ

1. [Creating GitHub CLI extensions](https://docs.github.com/en/github-cli/github-cli/creating-github-cli-extensions)



## Troubleshootings

### 👉 ssh clone git@githubs.com

```shell
git clone git@github.com:ssh-address
```

ref: 
https://www.seozen.top/ssh-github-keygen-2021.html
https://blog.csdn.net/Felicity294250051/article/details/53606158

