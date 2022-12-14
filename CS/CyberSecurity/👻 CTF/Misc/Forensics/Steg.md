# ð«¥ Steg

[TOC]



## ð­ File Lookup

### File Type & File Head

#### `file` 

```yaml
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



Md5sum, sahsum,

### Hex-editor:

> [Top Hex Editors for Linux](https://www.tecmint.com/best-hex-editors-for-linux/)

Editor plugins: 

- nodepad++
- sublime text
- vscode
- ...

[hexyl](https://github.com/sharkdp/hexyl) 

[hexcurse](https://github.com/LonnyGomes/hexcurse) 

![Screenshot 2022-10-30 at 10.42.48 AM](../../../../../Assets/Pics/Screenshot 2022-10-30 at 10.42.48 AM.png)



### File breakup

[Binwalk](https://github.com/ReFirmLabs/binwalk)

foremost

dd

```yaml
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



### File converage

**Linux**: 

cat \<inputfile> > \<outputfile> 

md5sum, shasum,



**Win**:

copy

certutil -hashfile \<filename\> [md5]

 

## ð­ Pic Lookup

1. ç»å¾®çé¢è²å·®å«
2. gifå¾å¤å¸§éè
   1. é¢è²éééè
   2. ä¸åå¸§å¾ä¿¡æ¯éè
   3. ä¸åå¸§å¯¹æ¯éå
3. Exifä¿¡æ¯éè
4. å¾çä¿®å¤
   1. å¾çå¤´ä¿®å¤
   2. å¾çå°¾ä¿®å¤
   3. CRCæ ¡éªä¿®å¤
   4. é¿ï¼å®½ï¼é«åº¦ä¿®å¤
5. LSB
6. JPGå¾çå å¯
   1. Stegdetect
   2. outguess
   3. Jphide
   4. F5
7. äºç»´ç 



### Firework



### Exif



### Stegsolve



### LSB

#### [zsteg](https://github.com/zed-0xff/zsteg)



#### python



#### TweakPNG



#### Bftools (win)



## ð½  Compression

1. ä¼ªå å¯
   1. zip
   2. rar
2. æ´åç ´è§£
   1. Archpr (win)
   2. ziperello



1. 

