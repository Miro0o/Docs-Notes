## 8086CPU ASM

[TOC]



## Res
↗ [OS Programming](../../../Computer%20System/Operating%20System/📟%20OS%20Programming/OS%20Programming.md)



## 8086CPU Overview
#TODO 


## Memory Access
### Bus
![](../../../../../../Assets/Pics/Screenshot%202023-03-05%20at%2010.19.55%20AM.png)


### Physical Address Expression
#### Segment Address


#### Bias Address

![](../../../../../../../Assets/Pics/Screenshot%202023-03-05%20at%2011.20.42%20AM.png)

![](../../../../../../../Assets/Pics/Screenshot%202023-03-05%20at%2011.25.44%20AM.png)

> “段地址x16+偏移地址=物理地址” 的本质含义是:CPU 在访问内存时，用一个基础地址(段地址x10)和一个相对于基础地址的偏移地址相加，给出内存单元的物理地址。
> 更一般地说，8086CPU 的这种寻址功能是“基础地址+偏移地址=物理地址” 寻址模式的一种具体实现方案。8086CPU 中，段地址x16 可看作是基础地址。


## 🫙 Registers
16 bit register

14 total registers
AX、BX、CX、DX、SI、DI、SP、BP、IP、CS、SS、DS、ES、PSW

### General Register
AX, BX, CX, DX

![](../../../../../Assets/Pics/Screenshot%202023-03-05%20at%201.49.29%20PM.png)

#### AX and return (DOS system)
Following instuctions returns the program
```asm
mov ax, 4c00H
int 21H
```

#### [BX] and bias address
In the expression of [BX], bias address is stored in register BX.

#### CX and loop
```asm
mov cx, idata
s:
	code segment

	code ends
loop s
```

### Segment Register
CS /DS /SS /ES


> 为什么8086CPU不支持将数据直接送入段寄存器的操作? 这属于8086CPU 硬件设计的问题，我们只要知道这一点就行了

#### CS + IP /IR
Current instruction address.


#### DS + [address]
Current data addresss.

##### Data Segment


#### SS + SP
Current stack top address.

##### Stack
![](../../../../../../../Assets/Pics/Screenshot%202023-03-05%20at%201.15.14%20PM.png)

##### Stackoverflow
![](../../../../../Assets/Pics/Screenshot%202023-03-05%20at%201.44.33%20PM.png)



## Instructions
![](../../../../../Assets/Pics/Screenshot%202023-03-05%20at%2011.05.13%20AM.png)

### mov, add, sub


### push, pop


## Ref
