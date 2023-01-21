# [Debian](https://www.debian.org)

[TOC]



## Res

📂 [Debian Documentation ](https://www.debian.org/doc/)

[Debian wiki](https://wiki.debian.org/FrontPage)

[Debian Reference](https://www.debian.org/doc/manuals/debian-reference/)



## Intro

Debian, also known as Debian GNU/Linux, is a Linux distribution composed of free and open-source software, developed by the community-supported **Debian Project**, which was established by Ian Murdock on August 16, 1993. The first version of Debian was released on September 15, 1993, and its first stable version was released on June 17, 1996. The Debian Stable branch is the most popular edition for personal computers and servers. Debian is also the basis for many other distributions, most notably Ubuntu.





## Debian Repository

> :link: https://wiki.debian.org/DebianRepository

A Debian repository is a set of Debian binary or source packages organized in a special directory tree and with various infrastructure files - checksums, indices, signatures, descriptions translations.

Client computers can connect to the repository to download and install the packages using an [Apt](https://wiki.debian.org/Apt)-based [PackageManagement](https://wiki.debian.org/PackageManagement) tool.

### The Debian package management tools

> :link: https://www.debian.org/doc/manuals/debian-faq/pkgtools.en.html

There are multiple tools that are used to manage Debian packages, from graphic or text-based interfaces to the low level tools used to install packages. All the available tools rely on the lower level tools to properly work and are presented here in decreasing complexity level.

:heavy_exclamation_mark: It is important to understand that the higher level package management tools such as **aptitude** or **synaptic** rely on **apt** which, itself, relies on **dpkg** to manage the packages in the system.

#### dpkg

This is the main package management program.

#### 🙌🏻 APT package management system

Much of why Debian is a strong Linux distribution comes from its [package management](https://en.wikipedia.org/wiki/Package_manager). Everything in Debian – every application, every component – everything – is built into a package. 

There are many [software packages](https://wiki.debian.org/Software) available for Debian – everything from the Linux kernel to games. And their number has been growing with every release. 

The [Apt](https://wiki.debian.org/Apt) (*Advanced Package Tool*) package management system is a set of tools to download, install, remove, upgrade, configure and manage Debian packages, and therefore all software installed on a Debian system.

> :vs:  **apt, apt-get**
>
> `apt` = **most common used command options** from `apt-get`, `apt-cache` and `apt-config`, which means that `apt` does not include every options form above tools like `apt-get`.
>
> ↗️ More on  [FAQ](FAQ.md#👉 Diff between `apt` & `apt-get`).

#### aptitude

**aptitude** is a package manager for Debian GNU/Linux systems that provides a frontend to the apt package management infrastructure.**aptitude** is a text-based interface using the curses library. Actions may be performed from a visual interface or from the command-line.

**aptitude** can be used to perform management tasks in a fast and easy way. It allows the user to view the list of packages and to perform package management tasks such as installing, upgrading, and removing packages.

**aptitude** provides the functionality of **apt-get**, as well as many additional features.



### Configuration

- [SourcesList](https://wiki.debian.org/SourcesList) - Edit packages sources (repositories) 
- [PackageInstallTips](https://wiki.debian.org/PackageInstallTips) - Package management tips 
- [AptConfiguration](https://wiki.debian.org/AptConfiguration) - Apt configuration and *pinning*
- [UnattendedUpgrades](https://wiki.debian.org/UnattendedUpgrades) - Automatically install latest security (and other) upgrades 
- [PackageManagement/Preseed](https://wiki.debian.org/PackageManagement/Preseed) - Preconfigure Debian packages before installation 
- [PackageManagement/Searching](https://wiki.debian.org/PackageManagement/Searching) - Searching for packages 
- [Backports](https://wiki.debian.org/Backports) - Newer versions of packages compatible with [DebianStable](https://wiki.debian.org/DebianStable)
- [DebianPackageManagement](https://wiki.debian.org/DebianPackageManagement) - Advanced topics on Debian package management 
- [SecureApt](https://wiki.debian.org/SecureApt) - Authenticate packages against cryptographic signatures

### Debian package documentation

- Every Debian package installs its documentation under `/usr/share/doc/<package_name>`. Check this directory for more information on a specific package. 
- All programs provided by Debian packages come with their own [ManPage](https://wiki.debian.org/ManPage).

### Package lists

To browse the list of Debian packages grouped by category, you can look at the [stable](https://packages.debian.org/stable/), [testing](https://packages.debian.org/testing/), [unstable](https://packages.debian.org/unstable/) and various other lists, or search on the  [packages homepage](https://packages.debian.org/).

### Repository management

- [DebianRepository/Setup](https://wiki.debian.org/DebianRepository/Setup) - summarizes the process of setting up a Debian package repository 
- [DebianRepository](https://wiki.debian.org/DebianRepository) - Debian package repository 
- [DebianRepository/Format](https://wiki.debian.org/DebianRepository/Format) - Debian package repository format 
- [DebianRepository/UseThirdParty](https://wiki.debian.org/DebianRepository/UseThirdParty) - Instructions to connect to a third-party repository

### Mirrors

The official Debian package repository is mirrored all over the world. 

- The Debian website has an [official list of Debian mirrors](https://www.debian.org/mirror/list)
- There also is a list of [unofficial repositories](https://wiki.debian.org/DebianRepository/Unofficial) containing various additional software 
- There is a [team in charge of mirrors](https://wiki.debian.org/Teams/Mirrors).

https://packages.debian.org/)

### Using a repository

Using a repository is fairly simple: for the official Debian repository open `/etc/apt/sources.list`, insert the line

```shell
deb http://ftp.debian.org/debian stable main contrib non-free
```

then run 

```shell
apt update
```

(As the root user or using sudo of course). You might also consider to use a URL like: 

- `http://ftp.<CC>.debian.org/debian` to use a location closer to you, network-wise. 
- `http://deb.debian.org/debian` to let a CDN choose the closest mirror to you (more [here](http://deb.debian.org/)) 

For the official Debian repositories this simple procedure is sufficient. The [[SourcesList](https://wiki.debian.org/SourcesList)] article contains further information about sources.list entries. For other third party repositories, you might want to follow [this excellent guide](https://wiki.debian.org/DebianRepository/UseThirdParty) to reduce the risk of hosing your system from a carelessly maintained repository. 



## Ref

[The 11 Best Debian-based Linux Distributions]: https://www.tecmint.com/debian-based-linux-distributions/

