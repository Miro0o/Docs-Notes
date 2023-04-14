# File Management Basics

[TOC]



## Res
↗ [Awesome CLI /File Management](../../../../../🗺%20CS_Overview/🕶️%20Awesome/Awesome%20CLI/File%20Management.md)



## Text Editors
↗ [👍 Vim](../../../../👩‍💻%20Languages%20Programming/🐛%20Programming%20Tools%20Chain/Text%20Editors/Vim/👍%20Vim.md)



## 🔭 File Lookup
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


### Hex-editor
> [Top Hex Editors for Linux](https://www.tecmint.com/best-hex-editors-for-linux/)

Editor plugins: 

- nodepad++
- sublime text
- vscode
- ...

[hexyl](https://github.com/sharkdp/hexyl) 

[hexcurse](https://github.com/LonnyGomes/hexcurse) 

![Screenshot 2022-10-30 at 10.42.48 AM](../../../../../../../Assets/Pics/Screenshot%202022-10-30%20at%2010.42.48%20AM.png)


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
**Linux**
cat \<inputfile> > \<outputfile> 

md5sum, shasum,



**Win**
copy

certutil -hashfile \<filename\> [md5]



## File Filter/Finder
### fd

