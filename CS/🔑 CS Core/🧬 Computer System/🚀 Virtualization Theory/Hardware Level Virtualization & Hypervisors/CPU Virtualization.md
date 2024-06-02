# CPU Virtualization

[TOC]



## Res
🏠 
🚧 


### Related Topics
↗ [Instruction Set Architecture (ISA) & Processor Architecture](../../Computer%20Architecture/Instruction%20Set%20Architecture%20(ISA)%20&%20Processor%20Architecture/Instruction%20Set%20Architecture%20(ISA)%20&%20Processor%20Architecture.md)
↗ [x86 Architecture Family (80x86, 8086 family)](../../Computer%20Architecture/Instruction%20Set%20Architecture%20(ISA)%20&%20Processor%20Architecture/CISC%20(Complex%20Instruction%20Set%20Computer)/x86%20Architecture%20Family%20(80x86,%208086%20family)/x86%20Architecture%20Family%20(80x86,%208086%20family).md)
↗ [x86 Virtualization](📌%20Hardware-assisted%20Virtualization/CPU-assisted%20Virtualization/x86%20Virtualization/x86%20Virtualization.md)



## Intro
### ISA/CPU Privilege Design
↗ [Privilege Level & Protection Ring](../../Computer%20Architecture/Instruction%20Set%20Architecture%20(ISA)%20&%20Processor%20Architecture/📌%20ISA%20Basics/Privilege%20Level%20&%20Protection%20Ring.md)

![](../../../../../../../Assets/Pics/Pasted%20image%2020240217173550.png)
<small>Protection ring on an x86 CPU. Usually ring 0 is kernel space, ring 3 is user space.</small>


### 1️⃣ Full Virtualization
![](../../../../../Assets/Pics/Pasted%20image%2020230308111602.png)
<small>Full Vertualization under X86 Architcture</small>

> 比较著名的全虚拟化 VMM 有 Microsoft Virtual PC、VMware Workstation、Sun Virtual Box、Parallels Desktop for Mac 和 QEMU。QEMU 在今年（2019）对外宣称可以模拟所有设备。天啊，这简直是个奇迹般的伟大软件。
#### Hardware-Assistant Full Virtualization
![](../../../../../Assets/Pics/Pasted%20image%2020230308125433.png)

↗ [Hardware-assisted Virtualization](📌%20Hardware-assisted%20Virtualization/Hardware-assisted%20Virtualization.md)


### 2️⃣ Para-virtualization
![](../../../../../Assets/Pics/Pasted%20image%2020230308111614.png)
<small>Para-vertualization under X86 Architcture</small>



## Ref
[虚拟化技术原理（CPU、内存、IO） | cnblog]: https://www.cnblogs.com/bj-mr-li/p/11407927.html

[理解全虚拟、半虚拟以及硬件辅助的虚拟化 | cnblog]: https://www.cnblogs.com/woshiweige/p/4518430.html

