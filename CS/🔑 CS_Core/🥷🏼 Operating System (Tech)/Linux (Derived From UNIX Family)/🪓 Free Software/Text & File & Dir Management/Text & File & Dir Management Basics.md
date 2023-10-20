# Text & File & Dir Management Basics

[TOC]



## Res
↗ [Awesome CLI /File Management](../../../../../🗺%20CS_Overview/🕶️%20Awesome%20List/📌%20Awesome%20Open%20Source%20CLI%20Software/Awesome%20File%20&%20Dir%20Management.md)



## ELF File Info & Manipulation
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

### 👉 `size`


### 👉 `objdump` | `objcopy` | `xdd`


### 👉 `readelf`


### 👉 `nm`


### 👉 `strip`



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
> This tool is from ↗ [SeedLab - Cryptography](../../../../../CyberSecurity/☠️%20Kill%20Chain/🎯%20Cyber%20Ranges%20&%20Labs/🧪%20Labs/SEED%20Project/SeedLab%20-%20Cryptography.md#👉%20MD5%20Collision%20Attack%20Lab)


### 👉 `shasum`


### 👉 `certutil`
certutil -hashfile \<filename\> [md5]



## File Management
### 👉 `rm`



## Dir Management
### 👉 `ls`


### 👉 `tree`





## Ref
