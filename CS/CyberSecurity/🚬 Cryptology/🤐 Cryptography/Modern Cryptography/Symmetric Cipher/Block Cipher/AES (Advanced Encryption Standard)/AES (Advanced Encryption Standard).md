# AES (Advanced Encryption Standard)

[TOC]



## Res


## Intro
### AES Background /History
![](../../../../../../../../Assets/Pics/Screenshot%202023-04-12%20at%204.44.50%20PM.png)
![](../../../../../../../../Assets/Pics/Screenshot%202023-04-12%20at%204.45.02%20PM.png)
![](../../../../../../../../Assets/Pics/Screenshot%202023-04-12%20at%204.45.10%20PM.png)
![](../../../../../../../../Assets/Pics/Screenshot%202023-04-12%20at%204.45.19%20PM.png)



## Math in AES


## AES Process
### AES Functions
#### Bytesub()
字节代替变换ByteSub(): 也称S盒变换, 是一个关于字节的非线性变换。 S盒变换是AES唯一的非线性变换，也是AES安全的关键。

与DES的S盒变换比较:
(1) AES使用16个相同的S盒，DES使用8个不相同的S盒
(2) AES的S盒有8位输入8位输出，是一种非线性替换。DES的S盒有6位输入4位输出，是一种非线性压缩。


#### ShiftRows()
行移位(ShiftRows)变换中，状态矩阵中的每一行将以字节为单位，循环右移不同的位移量。

#### MixColumns()
列混合变换对State中的每列进行独立的操作，它把每个列都看成GF(28)中的一个四项多项式s(x)，再 与GF(28)上的固定多项式 a(x)= {03}x3+{01}x2+{01}x+{02}进行模x4+1的乘法运算。



## AES Features
![](../../../../../../../../Assets/Pics/Screenshot%202023-04-19%20at%203.14.53%20PM.png)
![](../../../../../../../../Assets/Pics/Screenshot%202023-04-19%20at%203.15.03%20PM.png)



## Ref

