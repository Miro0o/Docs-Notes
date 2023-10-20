# Linux Directory System

[TOC]



## Res


## Intro
Figure below gives an overall idea of what the basic file system tree looks like (the image is kindly supplied under a CC By-SA license by Paul Gardner) and [Wikipedia has a break down with a summary of what each directory is used for](https://en.wikipedia.org/wiki/Unix_filesystem#Conventional_directory_layout).

![](../../../../../../../Assets/Pics/Pasted%20image%2020231019195646.png)



## Overview
### _/bin_
_/bin_ is the directory that contains _bin_aries, that is, some of the applications and programs you can run. You will find the _ls_ program mentioned above in this directory, as well as other basic tools for making and removing files and directories, moving them around, and so on. There are more _bin_ directories in other parts of the file system tree, but we’ll be talking about those in a minute.

### _/boot_
The _/boot_ directory contains files required for starting your system. Do I have to say this? Okay, I’ll say it: **DO NOT TOUCH!**. If you mess up one of the files in here, you may not be able to run your Linux and it is a pain to repair. On the other hand, don’t worry too much about destroying your system by accident: you have to have superuser privileges to do that.

### _/dev_
_/dev_ contains _dev_ice files. Many of these are generated at boot time or even on the fly. For example, if you plug in a new webcam or a USB pendrive into your machine, a new device entry will automagically pop up here.

### _/etc_
_/etc_ is the directory where names start to get confusing. _/etc_ gets its name from the earliest Unixes and it was literally “et cetera” because it was the dumping ground for system files administrators were not sure where else to put.

Nowadays, it would be more appropriate to say that _etc_ stands for “Everything to configure,” as it contains most, if not all system-wide configuration files. For example, the files that contain the name of your system, the users and their passwords, the names of machines on your network and when and where the partitions on your hard disks should be mounted are all in here. Again, if you are new to Linux, it may be best if you don’t touch too much in here until you have a better understanding of how things work.

### _/home_
_/home_ is where you will find your users’ personal directories. In my case, under _/home_ there are two directories: _/home/paul_, which contains all my stuff; and _/home/guest_, in case anybody needs to borrow my computer.

### _/lib_
_/lib_ is where _lib_raries live. Libraries are files containing code that your applications can use. They contain snippets of code that applications use to draw windows on your desktop, control peripherals, or send files to your hard disk.

There are more _lib_ directories scattered around the file system, but this one, the one hanging directly off of _/_ is special in that, among other things, it contains the all-important kernel modules. The kernel modules are drivers that make things like your video card, sound card, WiFi, printer, and so on, work.

### _/media_
The _/media_ directory is where external storage will be automatically mounted when you plug it in and try to access it. As opposed to most of the other items on this list, _/media_ does not hail back to 1970s, mainly because inserting and detecting storage (pendrives, USB hard disks, SD cards, external SSDs, etc) on the fly, while a computer is running, is a relatively new thing.

### _/mnt_
The _/mnt_ directory, however, is a bit of remnant from days gone by. This is where you would manually mount storage devices or partitions. It is not used very often nowadays.

### _/opt_
The _/opt_ directory is often where software you compile (that is, you build yourself from source code and do not install from your distribution repositories) sometimes lands. Applications will end up in the _/opt/bin_ directory and libraries in the _/opt/lib_ directory.

A slight digression: another place where applications and libraries end up in is _/usr/local_, When software gets installed here, there will also be _/usr/local/bin_ and _/usr/local/lib_ directories. What determines which software goes where is how the developers have configured the files that control the compilation and installation process.

### _/proc_
_/proc_, like _/dev_ is a virtual directory. It contains information about your computer, such as information about your CPU and the kernel your Linux system is running. As with _/dev_, the files and directories are generated when your computer starts, or on the fly, as your system is running and things change.

### _/root_
_/root_ is the home directory of the superuser (also known as the “Administrator”) of the system. It is separate from the rest of the users’ home directories BECAUSE YOU ARE NOT MEANT TO TOUCH IT. Keep your own stuff in your own directories, people.

### _/run_
_/run_ is another new directory. System processes use it to store temporary data for their own nefarious reasons. This is another one of those DO NOT TOUCH folders.

### _/sbin_
_/sbin_ is similar to _/bin_, but it contains applications that only the superuser (hence the initial _s_) will need. You can use these applications with the `sudo` command that temporarily concedes you superuser powers on many distributions. _/sbin_ typically contains tools that can install stuff, delete stuff and format stuff. As you can imagine, some of these instructions are lethal if you use them improperly, so handle with care.

### _/usr_
The _/usr_ directory was where users’ home directories were originally kept back in the early days of UNIX. However, now _/home_ is where users kept their stuff as we saw above. These days, _/usr_ contains a mish-mash of directories which in turn contain applications, libraries, documentation, wallpapers, icons and a long list of other stuff that need to be shared by applications and services.

You will also find _bin_, _sbin_ and _lib_ directories in _/usr_. What is the difference with their root-hanging cousins? Not much nowadays. Originally, the _/bin_ directory (hanging off of root) would contain very basic commands, like `ls`, `mv` and `rm`; the kind of commands that would come pre-installed in all UNIX/Linux installations, the bare minimum to run and maintain a system. _/usr/bin_ on the other hand would contain stuff the users would install and run to use the system as a work station, things like word processors, web browsers, and other apps.

But many modern Linux distributions just put everything into _/usr/bin_ and have _/bin_ point to _/usr/bin_ just in case erasing it completely would break something. So, while Debian, Ubuntu and Mint still keep _/bin_ and _/usr/bin_ (and _/sbin_ and _/usr/sbin_) separate; others, like Arch and its derivatives just have one “real” directory for binaries, _/usr/bin_, and the rest or _*bin_s are “fake” directories that point to _/usr/bin_.

### _/srv_
The _/srv_ directory contains data for servers. If you are running a web server from your Linux box, your HTML files for your sites would go into _/srv/http_ (or _/srv/www_). If you were running an FTP server, your files would go into _/srv/ftp_.

### _/sys_
_/sys_ is another virtual directory like _/proc_ and _/dev_ and also contains information from devices connected to your computer.

In some cases you can also manipulate those devices. I can, for example, change the brightness of the screen of my laptop by modifying the value stored in the _/sys/devices/pci0000:00/0000:00:02.0/drm/card1/card1-eDP-1/intel_backlight/brightness_ file (on your machine you will probably have a different file). But to do that you have to become superuser. The reason for that is, as with so many other virtual directories, messing with the contents and files in _/sys_ can be dangerous and you can trash your system. DO NOT TOUCH until you are sure you know what you are doing.

### _/tmp_
_/tmp_ contains temporary files, usually placed there by applications that you are running. The files and directories often (not always) contain data that an application doesn’t need right now, but may need later on.

You can also use _/tmp_ to store your own temporary files — _/tmp_ is one of the few directories hanging off / that you can actually interact with without becoming superuser.

### _/var_
_/var_ was originally given its name because its contents was deemed _variable_, in that it changed frequently. Today it is a bit of a misnomer because there are many other directories that also contain data that changes frequently, especially the virtual directories we saw above.

Be that as it may, _/var_ contains things like logs in the _/var/log_ subdirectories. Logs are files that register events that happen on the system. If something fails in the kernel, it will be logged in a file in _/var/log_; if someone tries to break into your computer from outside, your firewall will also log the attempt here. It also contains _spools_ for tasks. These “tasks” can be the jobs you send to a shared printer when you have to wait because another user is printing a long document, or mail that is waiting to be delivered to users on the system.

Your system may have some more directories we haven’t mentioned above. In the screenshot, for example, there is a _/snap_ directory. That’s because the shot was captured on an Ubuntu system. Ubuntu has recently incorporated [snap](https://www.ubuntu.com/desktop/snappy) packages as a way of distributing software. The _/snap_ directory contains all the files and the software installed from snaps.



## Ref
[👍 Classic SysAdmin: The Linux Filesystem Explained]: https://www.linuxfoundation.org/blog/blog/classic-sysadmin-the-linux-filesystem-explained

_This is a classic article written by Paul Brown_ _from the [Linux.com](http://linux.com/) archives. For more great SysAdmin tips and techniques check out our free [intro to Linux course](https://www.edx.org/course/introduction-to-linux?utm_medium=partner-marketing&utm_source=affiliate&utm_campaign=linuxfoundation&utm_content=blog-lfs101)_.

