# File Organization

[TOC]



## Res


## Intro
![](../../../../../../../../../Assets/Pics/Screenshot%202023-06-08%20at%2010.23.38%20AM.png)



## Pile File
↗ [Pile File](Pile%20File/Pile%20File.md)

## Sequential File
↗ [Sequential File](Sequential%20File/Sequential%20File.md)



### Indexed Sequential File
↗ [Indexed Sequential File](Sequential%20File/Indexed%20Sequential%20File/Indexed%20Sequential%20File.md)


## Indexed File (Index + Pile)
↗ [Indexed File (Index + Pile)](Indexed%20File%20(Index%20+%20Pile)/Indexed%20File%20(Index%20+%20Pile).md)


## Direct /Hash File
The direct, or hashed, file exploits the capability found on disks to access directly any block of a known address. As with sequential and indexed sequential files, a key field is required in each record. However, there is no concept of sequential ordering here.

The direct file makes use of hashing on the key value. This function is explained in Appendix F. Figure F.1b shows the type of hashing organization with an overflow file that is typically used in a hash file.

Direct files are often used where very rapid access is required, where fixed- length records are used, and where records are always accessed one at a time. Examples are directories, pricing tables, schedules, and name lists.

#TODO 



## Ref

