# Text & File & Dir Management Basics

[TOC]



## Res
↗ [Awesome CLI /File Management](../../../../../🗺%20CS_Overview/🕶️%20Awesome%20List/📌%20Awesome%20General%20CLI%20Software%20List/Awesome%20File%20&%20Dir%20Management.md)



## File Type & File Head
### 👉 `file` 
```shell
file

Determine file type.
More information: <https://manned.org/file>.

- Give a description of the type of the specified file. Works fine for files with no file extension:
    file filename

- Look inside a zipped file and determine the file type(s) inside:
    file -z foo.zip

- Allow file to work with special or device files:
    file -s filename

- Don't stop at first file type match; keep going until the end of the file:
    file -k filename

- Determine the MIME encoding type of a file:
```



## Hex /Binary Dump/Editors
### Editor Plugins
#### 👉 nodepad++ & hex


#### 👉 Sublime Text & hex


#### 👉 vscode & hex


#### 👉 vim & hex
↗ [Vim Advance Usages /Hex View](../../../../👩‍💻%20Programming%20Methodology%20and%20Languages/🛠️%20Programming%20Tools%20Chain/Text%20Editors/Vim/Vim%20Usages/Vim%20Advance%20Usages.md#Hex%20View)


### 👉 010 editor
🏠 https://www.sweetscape.com/010editor/


### 👉 `hexdump` | `xdd` | `od`
od - dump files in octal and other formats


### 👉 `hexyl` | `hexcurse`
🚧 https://github.com/sharkdp/hexyl
🚧 https://github.com/LonnyGomes/hexcurse

![Screenshot 2022-10-30 at 10.42.48 AM](../../../../../../../Assets/Pics/Screenshot%202022-10-30%20at%2010.42.48%20AM.png)


[Top Hex Editors for Linux]: https://www.tecmint.com/best-hex-editors-for-linux/
[Linux下查看二进制文件]: https://blog.csdn.net/qq_19922839/article/details/115483499

[ ⭐ Radare2: The Libre Unix-Like Reverse Engineering Framework]: https://github.com/radareorg/radare2

[在 Linux 上分析二进制文件的 10 种方法]: https://linux.cn/article-12187-1.html
1. `file`
2. `idd`
3. `Itrace`
4. `hexdump`
5. `strings`
6. `readelf`
7. `objdump`
8. `strace`
9. `nm`
10. `gdb`


### 👉 `bless`
> This tool is from ↗ [SeedLab - Cryptography](../../../../../CyberSecurity/☠️%20Kill%20Chain/🎯%20Cyber%20Ranges%20&%20Labs/Labs/SEED%20Project/SeedLab%20-%20Cryptography.md##👉%20MD5%20Collision%20Attack%20Lab)



## File Breakup
### 👉 `binwalk` | `foremost` | `dd` | `iconv`
#### binwalk
↗ [binwalk](../../../../../CyberSecurity/☠️%20Kill%20Chain/Reverse%20Tools%20&%20Binary/⛰️%20Static%20Binary%20Analysis/binwalk.md)


#### dd

```shell
dd

Convert and copy a file.
More information: <https://ss64.com/osx/dd.html>.

- Make a bootable USB drive from an isohybrid file (such like `archlinux-xxx.iso`):
    dd if=file.iso of=/dev/usb_drive

- Clone a drive to another drive with 4 MB block and ignore error:
    dd if=/dev/source_drive of=/dev/dest_drive bs=4m conv=noerror

- Generate a file of 100 random bytes by using kernel random driver:
    dd if=/dev/urandom of=random_file bs=100 count=1

- Benchmark the write performance of a disk:
    dd if=/dev/zero of=file_1GB bs=1024 count=1000000
    
- Skip counts (total number of $count, but skip the first $skip):
	dd if=/input/file/path of=output/file/path count=100 skip=2
	
```


[Linux 创建指定大小的文件]: https://www.cnblogs.com/guanghe/p/8908814.html
[👍 https://manpages.debian.org/testing/coreutils/dd.1.en.html]: https://manpages.debian.org/testing/coreutils/dd.1.en.html


#### foremost
foremost - Recover files using their headers, footers, and data structures


#### iconv



### 👉 `zip2john` | `7z2john`



## File Checksum
### 👉 `md5` | `md5sum`


### 👉 `md5collgen`
> This tool is from ↗ [SeedLab - Cryptography](../../../../../CyberSecurity/☠️%20Kill%20Chain/🎯%20Cyber%20Ranges%20&%20Labs/Labs/SEED%20Project/SeedLab%20-%20Cryptography.md#👉%20MD5%20Collision%20Attack%20Lab)


### 👉 `shasum`


### 👉 `certutil`
certutil -hashfile \<filename\> [md5]



## Ref
