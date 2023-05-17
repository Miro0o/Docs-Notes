# Disk Technology

[TOC]



## Res


## Intro



## Disk Interfaces
↗ [Disk Interfaces](../../../../Microcomputer%20Principles%20&%20Interfaces/Computer%20Interfaces/Disk%20Interfaces.md)



## Disk Structure
### Magnetic Disk


### Solid State Disk


### Optical Disks



## Disk Drives
### Rigid Disk Drives (HDD, Hard Disk Drive)

#### Performance Metrics
##### Access Time: Seek Time + Rotational Delay

**Seek time**:

**Rotational delay** 

##### Mean Time To Failure (MTTF)

#### Characteristics
- Low cost is the major advantage of hard disks
- But their limitations include:
	- Very slow compared to main memory
	- Fragility
	- Moving parats wear out



### Solid State Drives (SSD)

#### Enterprise SSDs


#### Performance Metrics
##### Unrecoverable Bit Error Ratio (UBER)
UBER is a measure of disk reliability 
UBER is calculated bu dividing the number of data errors by the number of bits read, using a simulated lifetime workload.


##### Terabytese Written (TBW)
TBW is a measure of disk endurance (service life)
TBW is the number of terabytes that can be written to the disk before the disk fails to meet specifications for speed and error rates.



## RAID (Redundant Array of Independent Disks)
### RAID Schemes
#### RAID Level 0 (RAID-0)


#### RAID Level 1 (RAID-1)


#### RAID Level 2 (RAID-2)
#### RAID Level 3 (RAID-3)
#### RAID Level 4 (RAID-4)
#### RAID Level 5 (RAID-5)
#### RAID Level 6 (RAID-6)

#### RAID DP
##### RAID DP & Naming Methods
A relatively new RAID technique employs a pair of parity blocks that protect overlapping sets of data blocks. This method goes by different names depending on the drive manufacturer (there are slight differences among the implementations). 

The most popular name at this writing seems to be double parity RAID (RAID DP). Others that crop up in the literature include 
1. EVENODD
2. diagonal parity RAID (also RAID DP)
3. RAID 5DP
4. advanced data guarding RAID (RAID ADG)
5. and—erroneously!—RAID-6.


### Hybrid RAID Schemes


### (Berkeley) RAID Nomenclature
After reading the foregoing sections, it should be clear to you that ==higher-numbered RAID levels are not necessarily “better” RAID systems.== Nevertheless, many people have a natural tendency to think that a higher number of something is always better than a lower number of something. For this reason, various attempts have been made to reorganize and rename the RAID systems that we have just presented.

We have chosen to retain the **“Berkeley” nomenclature** in this text because it is still the most widely recognized.


### RAID Schemes Summary & Comparison
![](../../../../../../../Assets/Pics/Screenshot%202023-05-16%20at%203.10.11%20PM.png)


![](../../../../../../../Assets/Pics/Screenshot%202023-05-16%20at%204.10.40%20PM.png)
![](../../../../../../../Assets/Pics/Screenshot%202023-05-16%20at%204.10.51%20PM.png)



## Ref

