# DPDK (Data Plane Development Kits)

[TOC]



## Res
🏠 https://www.dpdk.org
🚧 https://github.com/DPDK/dpdk

📂 http://core.dpdk.org
📂 http://doc.dpdk.org/guides/linux_gsg/

Please check the doc directory for release notes,
API documentation, and sample application information.

For questions and usage discussions, subscribe to: users@dpdk.org
Report bugs and issues to the development mailing list: dev@dpdk.org


### Related Topics
↗ [The Linux Foundation](../../../🥷🏼%20Operating%20System%20(Engineering%20Part)/Linux%20(Derived%20From%20UNIX%20Family)/The%20Linux%20Foundation.md)



## Intro
DPDK is a set of libraries and drivers for fast packet processing.
It supports many processor architectures and both FreeBSD and Linux.

The DPDK uses the Open Source BSD-3-Clause license for the core libraries and drivers. The kernel components are GPL-2.0 licensed.


### DPDK 对传统基于OS内核的数据传输的突破
> 📎 https://ctimbai.github.io/2018/04/10/tech/net/dpdk/DPDK_入门最佳指南/

相对传统的基于内核的网络数据处理，DPDK 对从内核层到用户层的网络数据流程进行了重大突破:
1. **传统 Linux 内核网络数据流程**
	1. 硬件中断--->取包分发至内核线程--->软件中断--->内核线程在协议栈中处理包--->处理完毕通知用户层
	2. 用户层收包-->网络层--->逻辑层--->业务层
2. **dpdk 网络数据流程**
	1. 硬件中断--->放弃中断流程
	2. 用户层通过设备映射取包--->进入用户层协议栈--->逻辑层--->业务层

具体地，DPDK在如下方面有重大突破：
- **UIO（用户空间的 I/O 技术）的加持**
	- DPDK 能够绕过内核协议栈，本质上是得益于 UIO 技术，通过 UIO 能够拦截中断，并重设中断回调行为，从而绕过内核协议栈后续的处理流程。
	- UIO 设备的实现机制其实是对用户空间暴露文件接口，比如当注册一个 UIO 设备 uioX，就会出现文件 /dev/uioX，对该文件的读写就是对设备内存的读写。除此之外，对设备的控制还可以通过 /sys/class/uio 下的各个文件的读写来完成。
	- ![](../../../../../Assets/Pics/Pasted%20image%2020240602165740.png)
- **内存池技术**
	- DPDK 在用户空间实现了一套精巧的内存池技术，内核空间和用户空间的内存交互不进行拷贝，只做控制权转移。这样，当收发数据包时，就减少了内存拷贝的开销。
- **大页内存管理**
	- DPDK 实现了一组大页内存分配、使用和释放的 API，上层应用可以很方便使用 API 申请使用大页内存，同时也兼容普通的内存申请。
- **无锁环形队列**
	- DPDK 基于 Linux 内核的无锁环形缓冲 kfifo 实现了自己的一套无锁机制。支持单生产者入列/单消费者出列和多生产者入列/多消费者出列操作，在数据传输的时候，降低性能的同时还能保证数据的同步。
- **poll-mode 网卡驱动**
	- DPDK 网卡驱动完全抛弃中断模式，基于轮询方式收包，避免了中断开销。
- **NUMA**
	- DPDK 内存分配上通过 proc 提供的内存信息，使 CPU 核心尽量使用靠近其所在节点的内存，避免了跨 NUMA 节点远程访问内存的性能问题。
- **CPU 亲和性**
	- DPDK 利用 CPU 的亲和性将一个线程或多个线程绑定到一个或多个 CPU 上，这样在线程执行过程中，就不会被随意调度，一方面减少了线程间的频繁切换带来的开销，另一方面避免了 CPU 缓存的局部失效性，增加了 CPU 缓存的命中率。
- **多核调度框架**
	- DPDK 基于多核架构，一般会有主从核之分，主核负责完成各个模块的初始化，从核负责具体的业务处理。

除了上述之外，DPDK 还有很多的技术突破，可以用下面这张图来概之。
![](../../../../../Assets/Pics/Pasted%20image%2020240602165622.png)



## Ref
[👍 What is DPDK?]: https://www.packetcoders.io/what-is-dpdk/

[👍 DPDK 入门最佳指南]: https://ctimbai.github.io/2018/04/10/tech/net/dpdk/DPDK_入门最佳指南/

[DPDK : 用 TestPMD 测试 DPDK 性能和功能 | CSDN]: https://blog.csdn.net/hhd1988/article/details/123009368
[DPDK测试testpmd]: https://www.cnblogs.com/hjxiamen/p/17947295