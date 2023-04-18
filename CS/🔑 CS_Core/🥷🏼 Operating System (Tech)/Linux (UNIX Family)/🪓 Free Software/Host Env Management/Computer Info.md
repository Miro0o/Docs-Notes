# Computer Info

[TOC]



## Res


## Computer Hardware Info
### Architecture Info
#### lscpu

#### lshw /hwinfo

#### lnxi
Inxi is a 10K line mega bash script that fetches hardware details from multiple different sources and commands on the system, and generates a beautiful looking report that non technical users can read easily.

#### dmidecode
The dmidecode command is different from all other commands. It extracts hardware information by reading data from the [SMBOIS data structures](https://en.wikipedia.org/wiki/System_Management_BIOS) (also called DMI tables).


### Interfaces Info
#### lspci /lsscsi /lsusb


### Storage Info
#### du
The du command is a standard Linux/Unix command that **allows a user to gain disk usage information quickly**. It is best applied to specific directories and allows many variations for customizing the output to meet your needs. As with most commands, the user can take advantage of many options or flags.


#### lsblk /df / pydf

#### fdisk /mount /free

#### hdparm


### 👀 Looking up files under `/proc/`





## OS Info
### Host Info
#### uname

#### hostname /hostnamectl
Display the system's hostname using:
```shell
$ hostname
```

You can also use the `hostname` command to modify the system's name temporarily. Here's an example:
```shll
$ hostname demo.example.com
```

To persistently change the hostname, use the `hostnamectl` command, or directly modify the default configuration file `/etc/hostname`.
```shell
 hostnamectl set-hostname server1.example.com
```






## Ref
[16 Commands to Check Hardware Information on Linux]: https://www.binarytides.com/linux-commands-hardware-info/



