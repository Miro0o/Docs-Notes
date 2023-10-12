# Network Emulation

[TOC]



## Res
📂 https://www.qemu.org/docs/master/system/devices/net.html



## Intro



## Ref
[Qemu虚拟机与宿主机之间文件传输]: http://pwn4.fun/2020/05/27/Qemu虚拟机与宿主机之间文件传输/
[Ubuntu下SSH登录Qemu虚拟机]: http://pwn4.fun/2019/05/31/Ubuntu下SSH登录Qemu虚拟机/

[Set up a Mac for Qemu with Bridged Network]: https://upstreamwithoutapaddle.com/home-lab/bare-metal-bootstrap/

[在 macos 创建 QEMU 桥接网络]: https://taoshu.in/unix/qemu-bridge-on-macos.html

[👍 kvm的4中网络模型（qemu-kvm）]: https://www.cnblogs.com/wyzhou/p/9630660.html

[QEMU网络操作相关说明及常用命令]: https://github.com/QthCN/opsguide_book/blob/master/QEMU网络操作相关说明及常用命令.md

[QEMU 网络配置一把梭]: https://wzt.ac.cn/2021/05/28/QEMU-networking/
[👍 QEMU虚拟机网络模拟]: https://www.owalle.com/2019/12/26/network-in-vm/

QEMU可以模拟多种网卡设备(例如PCI或者ISA设备)，同时可将这些虚拟网卡与host上的虚拟网络设备(或者虚拟的hub)连接起来。各种不同类型的网络设备既可以为虚拟机提供真实的网络访问(例如TAP、SLiRP user模式)，也可以是同一个host上面的不同虚拟机之间的访问(Socket)。  
常见的网络设备实现有4种：
1. User模式: `-net user` (如果没有指定`-net xx`这是默认配置)。
2. TAP(Terminal Access Point): 这是QEMU推荐的虚拟机联网的虚拟网络设备的后端实现。可以认为虚拟网卡直接与其相连。TAP接口的行为应该与真实的网络设备一样，一旦将TAP绑定到“网桥”(bridge)上之后，他们就可以网络通信了。
3. Hubs: hub实现将多个网络设备连接起来，比如QEMU的虚拟网卡(TAP设备)，将虚拟机中的多个网卡相连，或者host的网络设备通过参数`-netdev hubport`或者`-nic hubport`相连。
4. Socket: 通过参数`-netdev socket` (或`-nic socket`或`-net socket`) 可以实现多个虚拟机之间的互联。

[👍 QEMU 网络配置]: https://tomwei7.com/2021/10/09/qemu-network-config/

QEMU 的网络由两个部分组成:
- 提供给虚拟机的虚拟网卡（virtual network device）比如经典的 e1000,rtl8139 以及 virtio-net-pci 等，是虚拟机内部看到的设备
- 与虚拟网卡交互的后端（network backend）虚拟机往虚拟网卡写入的数据都会由 network backend 流出到真实的网络环境中