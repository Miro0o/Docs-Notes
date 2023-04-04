## 8086CPU ASM

[TOC]



## Res
↗ [OS Programming](../../../🥷🏼%20Operating%20System%20(Tech)/📟%20OS%20Programming/OS%20Programming.md)



## 8086CPU Overview
#TODO 



## Data & Instructions
↗ [von Neumann-Based Architecture /Memory](../../../🧬%20Computer%20System/Computer%20Organization%20&%20Architecture/🧝🏻‍♀️%20von%20Neumann%20Based%20Microarchitecture/Memory/Memory.md)



## ⛸️ Data Access
### Bus
![](../../../../../../Assets/Pics/Screenshot%202023-03-05%20at%2010.19.55%20AM.png)

As in ↗ [von Neumann Based Architectures /Bus](../../../🧬%20Computer%20System/Computer%20Organization%20&%20Architecture/🧝🏻‍♀️%20von%20Neumann%20Based%20Microarchitecture/Bus/Bus.md)

### Memory & Memory Address Space
As is ↗ [von Neumann Based Architectures /Memory](../../../🧬%20Computer%20System/Computer%20Organization%20&%20Architecture/🧝🏻‍♀️%20von%20Neumann%20Based%20Microarchitecture/Memory/Memory.md)


### Physical Address Expression
#### Segment Address (段地址)


#### Offset Address（偏移地址）

![](../../../../../../../Assets/Pics/Screenshot%202023-03-05%20at%2011.20.42%20AM.png)

![](../../../../../../../Assets/Pics/Screenshot%202023-03-05%20at%2011.25.44%20AM.png)

> “段地址x16+偏移地址=物理地址” 的本质含义是:CPU 在访问内存时，用一个基础地址(段地址x10)和一个相对于基础地址的偏移地址相加，给出内存单元的物理地址。
> 更一般地说，8086CPU 的这种寻址功能是“基础地址+偏移地址=物理地址” 寻址模式的一种具体实现方案。8086CPU 中，段地址x16 可看作是基础地址。


### Data Location
CPU, memory, interfaces


### Data Length



## Instruction Executions
### Instruction Transferring




## 🫙 Registers

16 bits register (2 bytes, word length = 2B /16bits)

14 total registers: 
AX、BX、CX、DX、 (general registers)
SI、DI、SP、BP、 (address registers)
IP、FR(PSW).         (control registers)
CS、SS、DS、ES、 (segment registers)

### 1️⃣ General Register (Data Register)
AX = AH + AL
BX = BH + BL
CX = CH + CL
DX = DH + DL


![](../../../../../Assets/Pics/Screenshot%202023-03-05%20at%201.49.29%20PM.png)

#### AX 
##### AX and Return (DOS)
Following instructions returns the program
```asm
mov ax, 4c00H
int 21H
```

##### AX + div

##### AX + mul



#### BX
##### [BX] and Offset Address
In the expression of [BX], the offset is stored in register BX.


#### CX
##### CX + loop
```asm
mov cx, idata
s:
	code segment

	code ends
loop s
```

##### CX + jcxz



#### DX
##### DX + div

Dividend:
- AX - for 8 bits divisor
	- AH - remainders
	- AL - quotient
- DX + AX - for 16 bits divisor
	- DX - remainders
	- AX - quotient

Divisor: 
- 8 bits or 16 bits
- stored in a reg or memory unit

##### DX + mul



### 2️⃣ Segment Register
CS /DS /SS /ES


> 💡 Abount Segment, go to ↗ [Data Representations & Storage in CS](../../../🧬%20Computer%20System/😤%20Number,%20Data%20and%20Math%20in%20Digital%20Systems/Data%20Representations%20&%20Storage%20in%20CS.md)

> 为什么8086CPU不支持将数据直接送入段寄存器的操作? 这属于8086CPU 硬件设计的问题，我们只要知道这一点就行了


#### CS 
##### CS + IP /IR
Current instruction address.


#### DS
##### DS + [address]
Current data addresss.

##### Data Segment


#### SS + SP
Current stack top address.

More about stack at ↗ [Data Representations & Storage in CS](../../../🧬%20Computer%20System/😤%20Number,%20Data%20and%20Math%20in%20Digital%20Systems/Data%20Representations%20&%20Storage%20in%20CS.md)


### 3️⃣ Address Register
SI, DI, BP, SP

#### BX|BP + SI|DI + idata
DS: BX
```asm
DS: BX
[BX + SI]
[BX + DI]
[BX + SI|DI + idata]
idata[BX + SI|DI]
idata[BX][SI|DI]
```

SS: BP
```asm
SS: BP
[BP + SI]
[BP + DI]
[BP + SI|DI + idata]
idata[BP + SI|DI]
idata[BP][SI|DI]
```


#### SP
##### SS + SP
Mentioned above.


### 4️⃣ Control Register
IP, FR

#### IP
##### CS + IP
Mentioned above.


#### FR (PSW, Program Status Word) (Flag Register)

![](../../../../../Assets/Pics/Screenshot%202023-03-20%20at%208.48.05%20PM.png)




## ASM Program
### Program Compilation
#TODO 


### Instructions in ASM
#### ASM Instructions
![](../../../../../Assets/Pics/Screenshot%202023-03-05%20at%2011.05.13%20AM.png)

##### mov, add, sub

##### div, mul

##### push, pop


##### and, or, xor


##### jmp, jcxz, loop

##### call, ret

##### int


#### Pseudocode
##### idata （immediate data）

##### Loop

##### Segment Prefix

##### db, dw, dd, dup
| meaning | byte length | word length |
|-|-|-|
| define byte | 1 byte | 0.5 word (8086) |
| define word | 2 byte | 1 word (8086) |
| define dword (double word) | 4 byte | 2 word (8086) |


##### X ptr (word ptr|byte ptr)

##### offset

##### nops


#### Other Notes
#TODO 


### Memory Allocation
#TODO 


### Memory Addressing
![](../../../../../Assets/Pics/Screenshot%202023-03-20%20at%207.56.36%20PM.png)

#### Data Location


#### Data Length


#### Direct Addressing Table
#TODO 



## Ref
[汇编中的栈帧理解]: https://blog.csdn.net/yhchinabest/article/details/103881857
[Stack-based memory allocation]: https://en.wikipedia.org/wiki/Stack-based_memory_allocation
[8086标志寄存器（Flag Register）]: https://blog.csdn.net/weixin_42109012/article/details/100148721

