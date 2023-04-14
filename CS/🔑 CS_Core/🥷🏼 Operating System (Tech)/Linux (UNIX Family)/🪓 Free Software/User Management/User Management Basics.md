# User Management Basics

[TOC]



## Res

## Intro
### `su` | `login` | `sudo`

The _su_ (short for _substitute user_) [command](http://www.linfo.org/command.html) makes it possible to change a [login](http://www.linfo.org/login_def.html) session's _owner_ (i.e., the user who originally created that session by logging on to the system) without the owner having to first log out of that session. 

Although su can be used to change the ownership of a session to any user, it is most commonly employed to change the ownership from an ordinary user to the [_root_](http://www.linfo.org/root.html) (i.e., administrative) user, thereby providing access to all parts of and all commands on the computer or system. For this reason, it is often referred to (although somewhat inaccurately) as the _superuser_ command. It is also sometimes called the _switch user_ command.

[The su Command]: http://www.linfo.org/su.html



## Ref
[Linux 用户和用户组管理]: https://www.runoob.com/linux/linux-user-manage.html
