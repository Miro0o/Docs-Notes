# FAQ

[TOC]



## Res


## 👉 gem/gemspec, RubyGems, rake/Rakefile, bundler/bundle and Gemfile/Gemfile.lock
#gem #ruby #bundle #bundler #gemfile #rake #Rakefile #gemspec #RubyGems

- `Ruby`是红宝石的意思，是编程语言的名字。`Ruby`语言的logo就是一颗红宝石。
	- `Ruby`是一门开源的动态编程语言，注重简洁和效率。其句法优雅，读起来自然，写起来舒适。
	- `Ruby`语言源文件的后缀是`.rb`。
- `rake`是`Ruby`语言的类`make`程序。可以在其中定义任务和源码依赖
	- rake = r(uby’s m)ake
	- 就像`make`有`Makefile`文件一样，`rake`有对应的`Rakefile`。
	- 它们都属于构建工具的范畴。
- `gem`是宝石的意思。能够很容易想到跟`Ruby`红宝石同处一系。
	- `gem`是`Ruby`的包管理系统，命令是`gem`，包名后缀也是`.gem`，类似于redhat 系的`rpm`。不过`rpm`只能安装本地包，不能联网下载。联网下载需使用`yum`或`dnf`。
	- 同样的，Debian系，包管理系统是`dpkg`，不能联网下载。联网下载需使用`apt`。
	- gemspec文件，是gem的描述文件，包含gem相关的信息，如包名、版本、简介、描述、作者、主页等。
	- 类似的，dpkg打包需要spec文件，deb打包需要control文件。
	- 这里要注意，gem对应的文件是gemspec。Gemfile和gem无关，它其实是bundler的配置文件名称。
- `bundler`是Ruby应用的外部依赖管理工具。
	- `bundle`是另一个gem，是用来解决”把bundler误拼写称bundle”的问题，唯一功能就是安装bundler，使两者同意而不报错。
	- `Gemfile`文件描述执行相关Ruby应用需要的外部依赖gem，包含源、gem名称、gem版本等信息。
	- 执行`bundler install`时，`bundler`会读取`Gemfile`文件并一次性安装所有依赖gem。


[一文搞清rake、Rakefile、gem、gemspec、bundler、bundle、Gemfile的关系]: https://cloud.tencent.com/developer/article/1596045
[👍 Ruby：版本管理 RVM、Gem 与 Bundler]: https://hoffmanzheng.github.io/2021/ruby-bundler/


