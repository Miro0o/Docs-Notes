# OS X CLI

[TOC]



> ↗ [Awesome macOS](../../../../🗺 CS_Overview/🕶️ Awesome/Awesome macOS.md) for awesome Mac software & tools! 



## Network Management
> 
> 🔗 [Mac Network Commands Cheat Sheet](https://gist.github.com/jjnilton/add1eeeb3a9616f53e4c)
> **Note**: Since this seems to be helpful to some people, I formatted it to improve readability of the [original](https://gist.githubusercontent.com/jjnilton/add1eeeb3a9616f53e4c/raw/d7561c2ad6ab2b15aa85dafb9613c3c338e7583e/mac%2520network%2520commands%2520terminal). Also, note that this is from 2016, many things may have changed, and I don't use macOS anymore, so I probably can't help in case of questions, but maybe someone else can.


### 👉 pfctl
control the packet filter (PF) and network address translation (NAT) device

The pfctl utility communicates with the packet filter device.  It allows ruleset and parameter configuration and retrieval of status information from the packet filter.


[mac下的iptables---pfctl]: https://www.jianshu.com/p/eefe3877650f


### 👉 scutil
Manage system configuration parameters

Invoked with no options, scutil provides a command line interface to the "dynamic store" data maintained by configd(8).  Interaction with this data (using the `SystemConfiguration.framework` SCDynamicStore APIs) is handled with a set of commands read from standard input.  A list of the available commands is available by entering the help directive.


### 👉 networksetup
onfiguration tool for network settings in System Preferences.


```shell
sudo networksetup -setdnsservers Wi-Fi 185.228.168.168 185.228.169.168
sudo networksetup -listallnetworkservices

networksetup -setdnsservers Wi-Fi
networksetup -getdnsservers Wi-Fi
```


[manpagez: man pages & more | man networksetup(8)]: http://manpagez.com/man/8/networksetup/
[Where does scutil store its information]: https://apple.stackexchange.com/a/395647
[Change DNS on a Mac using Terminal]: https://cleanbrowsing.org/help/docs/manually-change-dns-on-a-mac-terminal/



## User Management
### 👉 dscl
#### Group Management
```shell
$ dscl . 
> cd /Groups

### Create User Group 'yeah'; either way
> create /Groups/yeah PrimaryGroupID 6666
> create /Groups/yeah gid 6666

### Add User 'yeah' to Group 'yeah'; either way
> append /Groups/yeah GroupMembership yeah
> merge /Groups/yeah users yeah

### Delete User 'yeah' form User Group 'yeah'
> delete /Groups/yeah GroupMembership yeah
### Delete User Group 'yeah'
> delete /Groups/yeah

### Lookup Info
> read /Groups/yeah [PrimaryGroupID] [GroupMembership]
> list /Groups [PrimaryGroupID] [GroupMembership]
```


#### User Management
```shell
$ dscl . 
> cd /Users

### Create User 'yeah' & allocate uid ; either way
> create /User/yeah UniqueID 8888
> create /User/yeah uid 8888

### add user 'yeah' to groups 6666 
> create /User/yeah PrimaryGroupID 6666
> create /User/yeah gid 6666
## Add user to admin group
> merge /Groups/admin users yeah
## Add user 'yeah' to Group 'yeah'; either way
> append /Groups/yeah GroupMembership yeah
> merge /Groups/yeah users yeah
## Delete User 'yeah' form User Group 'yeah'
> delete /Groups/yeah GroupMembership yeah

### Allocate User 'yeah' a bash shell
> create /User/yeah Usershell /bin/bash
> create /User/yeah shell /bin/bash

### Set realname for User 'yeah'
> create /User/yeah realname "oh yeah b"

### Set password for User 'yeah' as null (\*)
> create /User/yeah passwd '*'

### Change password for user 'yeah'
$ sudo passwd yeah
$ Changing password for yeah.
$ New password: ********
$ Retype new password: ********

### Allocate user 'yeah' home directory
$ sudo mkdir /User/yeah
$ sudo chown -R yeah:yeah /User/yeah
$ dscl .
> create /Users/yeah NFSHomeDirectory /Users/yeah
> create /Users/yeah home /Users/yeah

### Delet user 'yeah'
> delete /User/yeah

### Lookup info
> read /User/yeah
```


#### 📝 Notes
Here i got stuck a while. 

> **TL;DR**
> `sudo dscl . create /Groups/newGroupName gid 8888`
> `sudo dscl . create /Users/newUserName uid 6666 gid 8888`
> `sudo mkdir /User/home_dir_for_new_user`
> `chown -R newUserName:newGroupName /path/to/home/dir`
> `sudo dscl . create /Users/newUserName home /path/to/home/dir`
> `sudo dscl . create /Users/newUserName passwd '*'`
> `sudo passwd newUserName`
> `su - newUserName`


First i didn't assign gid number to new user, instead i append it to `staff` group on mac, which seems to have errors. 

So i assigned a new gid number to the new user (a new group, not `staff`) and set the `PrimaryGroupID` as it. (It seems like that the new user must have its `PrimaryGroupID` as a new gid rather than `staff` ?? ) This step is important because otherwise the new user cannot use `chown`.

After above i create the new user's home directory with sudo and `chown` that directory to new user. `chown  -R user:usergroup /path/to/home/dir`
Then set the home dir as the new user's home `sudo dscl . create /User/username home /path/to/home/dir`

However at this point i cannot `su` to this new user. i then set the password for it as null `sudo dscl . create /User/username passwd '*'` but it didn't work. I tried setting it as not null but didn't work either. 
Then i tried `sudo passwd username`. This worked.


[【小技巧】macOS 下用 dscl 命令行管理用户 - tobrainto的文章 - 知乎]: https://zhuanlan.zhihu.com/p/380906865
[chown illegal group name]: https://stackoverflow.com/questions/15980675/chown-illegal-group-name-mac-os-x
[Why can't I use my newly created user with chown?]: https://superuser.com/questions/923524/why-cant-i-use-my-newly-created-user-with-chown


### 👉 launchctl
#TODO 




## 📝 Reading List
[常用汇编命令]:https://baijiahao.baidu.com/s?id=1607834244588924669&wfr=spider&for=pc
[查看网络状态]:https://www.cnblogs.com/Pagenny/p/9800123.html

