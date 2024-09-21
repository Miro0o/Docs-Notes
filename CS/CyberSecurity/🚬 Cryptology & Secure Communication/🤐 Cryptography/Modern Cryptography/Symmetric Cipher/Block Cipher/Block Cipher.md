# Block Cipher

[TOC]



## Res
### Related Topics
↗ [Block Cipher Cryptanalysis](../../../../🤮%20Cryptanalysis/Modern%20Cipher%20Cryptanalysis/Symmetric%20Cipher%20Cryptanalysis/Block%20Cipher%20Cryptanalysis/Block%20Cipher%20Cryptanalysis.md)


### Other Resources



## Intro
分组密码是每次只能处理特定长度的一块数据的算法，每块都是一个分组，分组的比特数就称为分组长度，但是当加密的内容超过分组密码的分组长度时，就要对分组密码算法进行迭代，迭代的方法称为分组密码的模式。


## 👩🏼‍🏫 Block Cipher Design Principles 
### Security Perspective
![](../../../../../../../Assets/Pics/Screenshot%202023-04-12%20at%202.40.51%20PM.png)
#### Diffusion
尽量将每一位明文和密钥的的影响尽可能迅速地分布到较多的输出密文位中，以便隐藏明文的统计特性。 扩散的目的是希望密文的任一位Ci都尽可能与明文和密钥相关联，或者说明文和密钥任一位上值的改变都会影响到Ci的值。

![](../../../../../../../Assets/Pics/Screenshot%202023-04-24%20at%203.39.30%20PM.png)
#### Confusion
使密文与明文、加密密钥之间的统计关系尽量复杂化，使破译者难以从密文的统计特性导出与密钥相关的信息。为此，可以使用与密钥和明文输入有关的很复杂的非线性算法。(实现时主要利用复杂的替换算法) 使用复杂的非线性代替变换可以达到比较好的混淆效果，而简单的线性代替变换得到的混淆效果则不理想。

> 扩散和混淆机制是现代分组密码的设计基础。
> 
> 乘积和迭代机制有助于实现扩散和混淆: 如通常选择某些较简单的受密钥控制的密码变换(替代-置换)，通过乘积和迭代可以取得比较好的扩散和混淆的效果


### Implementation Perspective
![](../../../../../../../Assets/Pics/Screenshot%202023-04-12%20at%202.41.21%20PM.png)



## ✈️ Block Cipher Modes
### 1️⃣ ECB (Electronic Code Book)
将每块明文加密成相应的密码块，若最后一块不足64bit， 则用一些任意二进制序列填充。这样相同的明文块总被加密成相同的密文块。

![](../../../../../../../../Assets/Pics/Screenshot%202023-04-25%20at%208.51.09%20PM.png)

特点：
(1) 一种最简易的工作方式; 由于没有任何形式的反馈，在相同的明文加密后将产生相同的密文。这样 在处理具有固定数据结构的明文数据时容易暴露明文数据的固有格式。
	例如，某些具有格式化的报文， 往往作业号、通信地址、发报时间、密级等数据都除了位置固定外，明文数据也非常地有规律，这些常 用的数据通常在加密后密文的同一个位置出现，密码分析者就可能得到许多明密文对，从而为分析、破译带来有利的线索。
(2) 相同密钥作用下，密文块与明文块一一对应，易于 暴露明文的固有格式;
(3) 各密文块间缺乏相关性，信息易于受到块替换攻击 。 算法本质上相当于一个“大的单字母替换”; 同时，由于 ECB 模式下每个报文分组之间是相互独立的，这样，如果敌手有能力对报文进行分组 的插入与删除，敌手可以进行主动攻击，带来安全危险。
(4) 另外，ECB 模式无法纠正传输中的同步差错， 如果在传输中增加或丢失一个或多个比特，将引起密文分组的对齐错误，这样，整个密文序列都将不能 正确地解密。


### 2️⃣ CBC (Cipher Block Chain)
加入反馈机制，当前明文块在加密之前要与前面的密文块进行异或。
设明文块为 $m_1，m_2，...， m_N$ 产生的密文块为 $c_1，c_2，..., c_N$ 加密密钥为K，初始随机向量为IV(Initialization Vector)，加密算法记为$E_K$，解密算法记为$D_K$。

![](../../../../../../../../Assets/Pics/Screenshot%202023-04-25%20at%208.06.06%20PM.png)

关于CBC初始向量IV的说明:
(1) 加密时，用于第一个明文块以产生第一个密文块; 解密时，用于对第一个密文块的解密输出进行异或，以产生第一个明文块;

(2) IV安全，否则第一个明文块易受攻击(假冒攻击) 

$$\begin{cases}
m_1 = D_K(C_1) ⊕ IV \\
C_1 = E_K(m_1 ⊕ IV)\\
\end{cases}
$$

若攻击者能够预测性地改变IV的比特，这也可以改变接收方m1的响应比特值。

![](../../../../../../../../Assets/Pics/Screenshot%202023-04-25%20at%208.50.17%20PM.png)


![](../../../../../../../../Assets/Pics/Screenshot%202023-06-14%20at%206.35.51%20PM.png)
#### Blocking Patterns
![](../../../../../../../../Assets/Pics/Screenshot%202023-04-12%20at%203.17.35%20PM.png)
#### CBC Features
(1) 加入反馈机制, 隐蔽明文的数据模式, 同一明文块会产生不同的密文块;算法不再是一个 “大的单字母替换”
(2) 有误码扩散，同时又有自同步特性; 若Ci在传送过程中出错，则解密时会造成mi和mi+1两个明文块都出错，但后面的密文块仍然能自动正确恢复。人们把这种错误传播形式称为“有限传播”
(3) 同时，在一定程度上，它能够有效地抵抗密文传输过程中对数据的篡改，诸如分组的重放、 插入和删除等。
(4) 只有当所有64比特块到达后才能开始编解码，不能直接用于交互式终端，否则传输带宽浪费严重


### 3️⃣ CFB (Cipher FeedBack)
可克服CBC方式的第(3)个问题。
CFB 模式(Cipher Feedback Mode)引入一个整数参数 s，1<=s<=b 。 需要注意的是，明文不是按 b 进行分组，而是按 s 分组，且明文的长度必须是 s 的倍数。CFB数据是按比分组小得多的单位进行加密的，密文依赖于前面所有的明文。

![](../../../../../../../../Assets/Pics/Screenshot%202023-04-25%20at%208.19.12%20PM.png)
![](../../../../../../../../Assets/Pics/Screenshot%202023-04-25%20at%208.19.21%20PM.png)

![](../../../../../../../../Assets/Pics/Screenshot%202023-06-14%20at%206.39.10%20PM.png)

特点：
CFB 模式由于采用的是密文反馈，故若某个密文分组在传输中出现一位或多位的错误，将会引起当前分组和后续部分分组的解密错误。因为只有当错误的密文比特从寄存器中移出后，解密才会恢复正常，故一个密文分组的出错会影响后面最多 $\lceil \frac b s \rceil$ 个分组的解密($\lceil X \rceil$ 表大于等于 x 的最小整数)。
(1) 移位寄存器的的内容与明文整个以前的历史有关， 同样需要一个初始向量(寄存器初值);
(2) 将分组密码转换为流密码(序列密码)，实现即时加密;
(3) 与ECB和CBC 模式项目相比，加密效率如何?


### 4️⃣ OFB (Output FeedBack)
在 OFB 模式中，先产生一个密钥流，然后将其与明文相异或。 因此，OFB 模式实际上就是一个同步流密码，通过反复加密一个初始向量 IV 来得到密钥流。这种方法有时也 叫“内部反馈”，因为反馈机制独立于明文和密文而存在的。

![](../../../../../../../../Assets/Pics/Screenshot%202023-04-25%20at%208.29.07%20PM.png)

![](../../../../../../../../Assets/Pics/Screenshot%202023-06-14%20at%206.40.33%20PM.png)

特点：
(1) 可加密任意长度的数据(即不需要进行分组填充) 
(2) 没有误码扩散，适用于传输信息长度变化较大的数据，如语音、图像等;  
(3) 比CFB更易受对消息流的篡改;攻击者有可能通过对消息数据部分和校验部分的篡改，而以检错码不能检测的方式篡改密文。
(4) 链接相关性，密文与前面的明文无关。  
(5) 应用时要求一次一密方式(OTP，One-Time Pad)，即每次使用不同的IV，否则消息的机密性就得不到保证。

OFB与CFB的比较:
OFB是以过去的子密钥 $b_i-1$ 为基础来产生下一个子密钥， OTP密钥可钥预先生成;
CFB是以过去的密文块 $C_i-1$ 作为产生下一个子密钥的基础， 不可预先生成;


### 5️⃣ CTR (CounTeR)
![](../../../../../../../../Assets/Pics/Screenshot%202023-04-25%20at%208.33.18%20PM.png)

（1） 具有随机访问特性，可随机对任意一个密文分组进行 解密处理，对该密文分组的处理与其他密文无关;
（2）处理效率高，可进行并行处理，提高数据吞吐量;
（3）同一明文块会产生不同的密文块
（4）可提前进行预处理;  
（5）CTR 模式还可以处理任意长度的数据，而且加解密过程仅涉及加密运算，不涉及解密运算， 因此不用实现解密算法。


### 6️⃣ CSM (Ciphertext Stealing Mode)

![](../../../../../../../../Assets/Pics/Screenshot%202023-06-14%20at%206.41.42%20PM.png)


### ❓ Block Cipher Modes: How to choose
![](../../../../../../../../Assets/Pics/Screenshot%202023-04-12%20at%203.48.17%20PM.png)
![](../../../../../../../../Assets/Pics/Screenshot%202023-04-12%20at%203.51.54%20PM.png)



## Block Cipher Crypto-systems
### Product Cipher + Iterative Cipher (乘积密码体制与迭代密码体制)
当今绝大多数的分组密码都是乘积密码。所谓乘积密码，就是以某种方式连续执行两个或多个密码，以使得所得到的最后结果或乘积比其任意一个组成密码都更强。乘积密码通常伴随一系列置换与代换操作，常见的乘积密码是迭代密码，即对同一种密码进行迭代使用。

![](../../../../../../../Assets/Pics/Screenshot%202023-04-12%20at%202.41.40%20PM.png)

![](../../../../../../../Assets/Pics/Screenshot%202023-04-12%20at%202.41.50%20PM.png)



### ⭐️ Block Cipher Design Models

![](../../../../../../../../Assets/Pics/Screenshot%202023-04-12%20at%202.45.37%20PM.png)
#### 1️⃣ SPN (Substitution & Permutation Network)
#### 2️⃣ Feistel
特点：
（1）加解密结构相同，所使用的子密钥的顺序正好相反
（2）每一轮都只是对一半的明文进行加密
（3）分组大小越大，安全性越高
（4）密钥长度越大，安全性越高
（5）循环次数越多，安全性越高

![](../../../../../../../../Assets/Pics/Screenshot%202023-04-12%20at%202.55.23%20PM.png)
![](../../../../../../../../Assets/Pics/Screenshot%202023-04-12%20at%202.55.37%20PM.png)
![](../../../../../../../../Assets/Pics/Screenshot%202023-04-12%20at%202.55.49%20PM.png)


### Block Cipher Implementations
↗ [DES (Data Encryption Standard)](DES%20(Data%20Encryption%20Standard)/DES%20(Data%20Encryption%20Standard).md)
↗ [AES (Advanced Encryption Standard)](AES%20(Advanced%20Encryption%20Standard)/AES%20(Advanced%20Encryption%20Standard).md)
↗ [IDEA (International Data Encryption Algorithm)](IDEA(International%20Data%20Encryption%20Algorithm)/IDEA%20(International%20Data%20Encryption%20Algorithm).md)
↗ [RC2](RC/RC2.md) /[RC5](RC/RC5.md) /[RC6](RC/RC6.md)



## Ref
[密码学 分组密码模式]: https://www.secpulse.com/archives/173833.html
[👍 Feistel密码结构]: https://zengrx.github.io/2019/05/13/Feistel-cryptography-architecture/
