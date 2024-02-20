# Hardware Level Virtualization (Hypervisors)

[TOC]



## Res
📂 [VMS System Managers Manual](https://wiki.preterhuman.net/VMS_System_Managers_Manual)
This Manual provides the basic concepts and procedures for VMS system
management; it is especially inteded for managers of small clusters and
systems.



## Intro
> There are differences between "hardware level virtualization" (which virtualize machine from hardware level) and "hardware-assisted virtualization" (which implementation virtualization services on hardware, usually the CPU)



## Hypervisor Architectures
> 🔗 According to [Formal requirements for virtualizable third generation architectures](http://doi.acm.org/10.1145/361011.361073) (1974), Hypervisors (VMMs) are divided into two categories: **native** and **hosted**.
> ![](../../../../../Assets/Pics/Pasted%20image%2020230308103644.png)


### 1️⃣ Native Hypervisor
![](../../../../../Assets/Pics/Pasted%20image%2020230308103729.png)

↗ [Native Hypervisor](Hypervisors%20Implementation/Native%20Hypervisor/Native%20Hypervisor.md)


### 2️⃣ Hosted Hypervisor
![](../../../../../Assets/Pics/Pasted%20image%2020230308103806.png)

↗ [Hosted Hypervisor](Hypervisors%20Implementation/Hosted%20Hypervisor/Hosted%20Hypervisor.md)



## 🎯 Hypervisor Technologies (CPU)
![](../../../../../Assets/Pics/Screenshot%202023-03-08%20at%201.16.52%20PM.png)


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



## 🎯 GPU Virtualization
↗ [GPU Virtualization](GPU%20Virtualization.md)



## Ref
