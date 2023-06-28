# Compiling Process

[TOC]



## Res


## Intro
![](../../../../../../Assets/Pics/Screenshot%202023-05-22%20at%209.50.58%20PM.png)

Although the machine we presented is quite different from a real machine, the assembly process we described is not. Virtually every assembler in use today passes twice through the source code. The first pass assembles as much code as it can, while building a symbol table; the second pass completes the binary instructions using address values retrieved from the symbol table built during the first pass.

The final output of most assemblers is **a stream of relocatable binary instructions**. Binary code is relocatable when the addresses of the operands are relative to the location where the operating system has loaded the program in memory, and the operating system is free to load this code wherever it wants. 

### 1️⃣ Preprocess

### 2️⃣ Compiling


### 3️⃣ Assembling


### 4️⃣Address Binding
#### Compile-time Binding

#### Loadtime Binding

#### Runtime Binding


### 5️⃣ Linking
#### Dynamic Linking
##### Loadtime Dynamic Linking

##### Runtime Dynamic Linking

#### Static Linking


## Ref

