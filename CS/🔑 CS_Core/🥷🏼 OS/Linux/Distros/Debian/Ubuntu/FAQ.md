# FAQ



#### 👉 Diff between `apt` & `apt-get`

> [What is the difference between apt and apt-get?](https://askubuntu.com/a/934449/1636059)

**Sum-up:** `apt` = most common used command options from `apt-get`, `apt-cache` and `apt-config`.

here are various tools that interact with [Advanced Packaging Tool (APT)](https://help.ubuntu.com/lts/serverguide/apt.html.en) and allow you to install, remove and manage packages in [Debian based Linux distributions](https://www.debian.org/derivatives/). `apt-get` is one such command-line tool which is widely popular. Another popular tool is [Aptitude](https://help.ubuntu.com/lts/serverguide/aptitude.html.en) with both GUI and command-line options.

If you have used `apt-get` commands, you might have come across a number of similar commands such as `apt-cache`, `apt-config` etc. And this is where the problem arises.

You see, these commands are way too low level and they have so many functionalities which are perhaps never used by an average Linux user. On the other hand, the most commonly used package management commands are scattered across `apt-get`, `apt-cache` and `apt-config`.

The `apt` commands have been introduced to solve this problem. `apt` consists some of the most widely used features from `apt-get`, `apt-cache` and `apt-config` leaving aside obscure and seldom used features.

With `apt`, you don’t have to fiddle your way from `apt-get` to `apt-cache` to `apt-config`. `apt` is more structured and provides you with necessary options needed to manage packages.

I have written in detail on the [difference between apt and apt-get](https://itsfoss.com/apt-vs-apt-get-difference/).