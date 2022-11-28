# [Ruby](https://www.ruby-lang.org/en/)

>  💎 Ruby is...
>
> A dynamic, open source programming language with a focus on simplicity and productivity. It has an elegant syntax that is natural to read and easy to write !



## Intro

### 🏗 Installation

to get the latest ruby: 
```shell
brew install ruby
```

Succeed!
```shell
==> Caveats
==> ruby
By default, binaries installed by gem will be placed into:
  /usr/local/lib/ruby/gems/3.1.0/bin

You may want to add this to your PATH.

ruby is keg-only, which means it was not symlinked into /usr/local,
because macOS already provides this software and installing another version in
parallel can cause all kinds of trouble.

If you need to have ruby first in your PATH, run:
  echo 'export PATH="/usr/local/opt/ruby/bin:$PATH"' >> ~/.zshrc

For compilers to find ruby you may need to set:
  export LDFLAGS="-L/usr/local/opt/ruby/lib"
  export CPPFLAGS="-I/usr/local/opt/ruby/include"
```



### 🏋🏿‍♂️ How it works

Ruby use `gem` as a package manager. However, when running a project a suggested way to manage dependencies is using dependence config file `Gemfile`. And to execute `Gemfile` run `Bundle install` .



1️⃣ `Ruby` is installed by default at `/usr/local/opt/ruby/bin/ruby`

2️⃣ Packages maneged by `gem` is installed by default at `/usr/local/lib/ruby/gems/3.1.0`



More info, run `gem environment` to check out: 

```shell
gem environment
RubyGems Environment:
  - RUBYGEMS VERSION: 3.3.11
  - RUBY VERSION: 3.1.2 (2022-04-12 patchlevel 20) [x86_64-darwin21]
  - INSTALLATION DIRECTORY: /usr/local/lib/ruby/gems/3.1.0
  - USER INSTALLATION DIRECTORY: /Users/mir0/.gem/ruby/3.1.0
  - RUBY EXECUTABLE: /usr/local/opt/ruby/bin/ruby
  - GIT EXECUTABLE: /usr/bin/git
  - EXECUTABLE DIRECTORY: /usr/local/lib/ruby/gems/3.1.0/bin
  - SPEC CACHE DIRECTORY: /Users/mir0/.gem/specs
  - SYSTEM CONFIGURATION DIRECTORY: /usr/local/Cellar/ruby/3.1.2_1/etc
  - RUBYGEMS PLATFORMS:
     - ruby
     - x86_64-darwin-21
  - GEM PATHS:
     - /usr/local/lib/ruby/gems/3.1.0
     - /Users/mir0/.gem/ruby/3.1.0
     - /usr/local/Cellar/ruby/3.1.2_1/lib/ruby/gems/3.1.0
  - GEM CONFIGURATION:
     - :update_sources => true
     - :verbose => true
     - :backtrace => false
     - :bulk_threshold => 1000
  - REMOTE SOURCES:
     - https://rubygems.org/
```



### To learn more ...

📂 [Ruby Docs](https://www.ruby-lang.org/en/documentation/)



### 🖇 Refs:

[How to find where gem files are installed]:https://stackoverflow.com/questions/19072070/how-to-find-where-gem-files-are-installed
[Don't use Ruby pre-built on macOS by default]:https://www.freecodecamp.org/news/do-not-use-mac-system-ruby-do-this-instead/
[install Ruby on Rails / macOS]:https://mac.install.guide/rubyonrails/index.html
[install Ruby on your mac -- everything you need to know]:https://stackify.com/install-ruby-on-your-mac-everything-you-need-to-get-going/



