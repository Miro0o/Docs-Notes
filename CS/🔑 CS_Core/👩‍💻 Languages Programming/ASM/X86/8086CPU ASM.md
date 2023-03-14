## 8086CPU ASM

[TOC]



## Res
↗ [OS Programming](../../../🧬%20Computer%20System/Operating%20System/📟%20OS%20Programming/OS%20Programming.md)



## 8086CPU Overview
#TODO 


## Memory Access
### Bus
![](../../../../../../Assets/Pics/Screenshot%202023-03-05%20at%2010.19.55%20AM.png)


### Physical Address Expression
#### Segment Address (段地址)


#### Offset Address（偏移地址）

![](../../../../../../../Assets/Pics/Screenshot%202023-03-05%20at%2011.20.42%20AM.png)

![](../../../../../../../Assets/Pics/Screenshot%202023-03-05%20at%2011.25.44%20AM.png)

> “段地址x16+偏移地址=物理地址” 的本质含义是:CPU 在访问内存时，用一个基础地址(段地址x10)和一个相对于基础地址的偏移地址相加，给出内存单元的物理地址。
> 更一般地说，8086CPU 的这种寻址功能是“基础地址+偏移地址=物理地址” 寻址模式的一种具体实现方案。8086CPU 中，段地址x16 可看作是基础地址。


## 🫙 Registers
16 bit register (2 byte, wordlength = 2B /16bits)

14 total registers
AX、BX、CX、DX、SI、DI、SP、BP、IP、CS、SS、DS、ES、PSW

### 1️⃣ General Register (Data Register)
AX = AH + AL
BX = BH + BL
CX = CH + CL
DX = DH + DL


![](../../../../../Assets/Pics/Screenshot%202023-03-05%20at%201.49.29%20PM.png)

#### AX and Return (DOS)
Following instuctions returns the program
```asm
mov ax, 4c00H
int 21H
```


#### [BX] and Offset Address
In the expression of [BX], offset is stored in register BX.


#### CX and loop
```asm
mov cx, idata
s:
	code segment

	code ends
loop s
```


### 2️⃣ Segment Register
CS /DS /SS /ES


> 💡 Abount Segment, go to ↗ [Data Representations in CS](../../../🧬%20Computer%20System/😤%20Number,%20Data%20and%20Math/Data%20Representations%20in%20CS.md)

> 为什么8086CPU不支持将数据直接送入段寄存器的操作? 这属于8086CPU 硬件设计的问题，我们只要知道这一点就行了


#### CS + IP /IR
Current instruction address.


#### DS + [address]
Current data addresss.

##### Data Segment


#### SS + SP
Current stack top address.

More about stack at ↗ [Data Representations in CS](../../../🧬%20Computer%20System/😤%20Number,%20Data%20and%20Math/Data%20Representations%20in%20CS.md)


### 3️⃣ Address Register
SI, DI, BP, SP

#### BX|BP + SI|DI + idata
```asm
DS: BX
[BX + SI]
[BX + DI]
[BX + SI|DI + idata]
idata[BX + SI|DI]
idata[BX][SI|DI]

SS: BP
[BP + SI]
[BP + DI]
[BP + SI|DI + idata]
idata[BP + SI|DI]
idata[BP][SI|DI]
```


#### SS + SP
Mentioned above.


### 4️⃣ Control Register
IP, FR

#### CS + IP
Mentioned above.

#### FR





## ASM Program
### Program Compilation


### Instructions
#### ASM Instructions
![](../../../../../Assets/Pics/Screenshot%202023-03-05%20at%2011.05.13%20AM.png)

##### mov, add, sub
##### div, mul

##### push, pop


##### and, or, xor


##### jmp, jcxz, loop

##### call, ret


#### Pseudocode
##### idata （immediate data）

##### Loop

##### Segment Prefix

##### db, dw, dd, dup
| meaing | byte length | word length |
|-|-|-|
| define byte | 1 byte | 0.5 word (8086) |
| define word | 2 byte | 1 word (8086) |
| define dword (double word) | 4 byte | 2 word (8086) |


##### X ptr (word ptr|byte ptr)



#### Other Notes


### Memory Allocation


### Memory Addressing
#### Data Location

#### Data Length




## Ref
[汇编中的栈帧理解]: https://blog.csdn.net/yhchinabest/article/details/103881857
[Stack-based memory allocation]: https://en.wikipedia.org/wiki/Stack-based_memory_allocation
