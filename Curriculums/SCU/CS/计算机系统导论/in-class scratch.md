[TOC]



# 16/9

[二进制小数表示/精度表示](https://www.cnblogs.com/jillzhang/archive/2007/06/24/793901.html)

+ > float遵从IEEE R32.24，而double 遵从R64.53。
+ > 补充资料：浮点数表示https://blog.csdn.net/shuzfan/article/details/53814424
+ 使用类似于科学计数法的表示方法。每个数字可以表示为$1.xxxxx \times 2^{xxxxx}$ 所以需要储存的只有式子中xxxxx的部分。
  >  ⚠️ 
  >
  > ==二进制中，小数点前的每一位基数是2，小数点后的每一位基数是1/2.== 其他进制同理。考试的时候竟然忘记了😓
+ 符号位 + 阶码 + 尾码。
+ float (32bits / 4 Bytes) ----> 1 + 8 + 23
	+ 其中8位阶码最高位为表正负的符号位。实际中阶码要额外+ 127 （$2^7-1$），即8位初始全为1的基础上再加实际的阶码。
	+ ![单精度数120.5的存储方式](https://www.cnblogs.com/images/cnblogs_com/jillzhang/WindowsLiveWriter/float_A919/clip_image002_12.gif)
	+ ⬆️ 图为十进制数120.5在计算机中的单精度储存方式。
+ double (64bits / 8 Bytes) - ---> 1 + 11 + 52
	+ double 和 floate 在储存上没有其他不同，位数多了一些。下图第一个是float，第二个是double。
	+ ![](https://www.cnblogs.com/images/cnblogs_com/jillzhang/WindowsLiveWriter/float_A919/clip_image001_1.gif)
	+ ![文本框: 0     100 0000 0101    1101 1010 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000](https://www.cnblogs.com/images/cnblogs_com/jillzhang/WindowsLiveWriter/float_A919/clip_image001_2.gif)

+ 


[补码/反码/原码](https://www.cnblogs.com/zhangziqiu/archive/2011/03/30/computercode.html)  ^bf45e9
>  [[../../../../CS/🔑 CS_Core/🦄 Algorithm & Data Structure/📌 Algo Basics/0x00 基本算法#^f11c14|graphic explanation]]
+ 利用同余 实现  *利用单向运算表示双向运算* 
+ 取反 时就是取 以限定步长为除数的膜 
	 + $a+(b)MOD(M)=a+(M-b)MOD(M)$
+ 补码+1 是给这个限定步长 即 除数 +1 
	+ $a+(b)MOD(M+1)=a+(M-b)MOD(M+1)$



[十六进制意义](https://blog.csdn.net/u012861978/article/details/46606223)
[无线电波&微波](https://www.shuxuele.com/physics/waves-radio-microwave.html) (**radio & microwave**)
> 无线电波(radio)与微波(microwave)都是在 [电磁频谱](https://www.shuxuele.com/physics/electromagnetic-spectrum.html)里的**长波长**的一端
> `radio` has wavelength $≥ 1 m$
> `microwave` has wavelength 1m~ 1nm



---
# 26/9

+ 采样率
> [奈奎斯特采样定理](https://www.cnblogs.com/zoneofmine/p/10853096.html)
>  [奈奎斯特和香农](https://blog.csdn.net/Dallin0408/article/details/59510405?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link)
>  绝大多数信号都是能够进行傅里叶变换的，就意味着，不管一个信号多么复杂，总可以分解为若干个正（余）弦信号的和，对应了信号的频率分量。因此，Nyquist采样定理只需找到信号最大的频率分量，再用2倍于最大频率分量的采样频率对信号进行采样，从理论上解决了，离散信号能够重建出连续信号的问题。

+ 
	+ Tele --> 8 Khz
	+ CD --> 44.1 Khz 
+ 量化/精度/（深度？）
+ 码率：单位时间记录的bit
	+ $=$ 采样率 $\times$ 深度
+ 立体声


## 编码
+ 压缩算法
+ 储存
	+ 储存格式
		+ MIDI
	+ 储存介质/方式
		 + CD	
		+ VCD
		+ DVD



[桌面系统环境](https://www.linuxidc.com/Linux/2014-06/103426p9.htm)

数据总线
+ 本地总线/内部总线
	+ CPU -[ RAM](https://www.crucial.com/articles/about-memory/support-what-does-computer-memory-do)
+ 扩展总线
	+ 用来实现[各种扩展端口](https://www.yinxiang.com/everhub/note/4828ea4f-240b-44bd-8cfd-20ecd7cd1657)与内部的数据交换 

显示设备
+ led 背光技术
+ lcd 液晶屏

图像质量
+ 显示器尺寸
+ 相应速率
+ 点距 dot position, dp
+ 分辨率

触摸屏
+ 电阻式
+ 点容式


像素
+ 单通道
+ 双通道
+ 三通道 
	+ RGB
+ 四通道
	+ CMYK

[DPI](http://www.rideau-info.com/photos/whatisdpi.html)
> **DPI** stands for **Dots Per Inch** which technically means **printer dots per inch**. Today it is a term often misused, usually to mean **PPI**, which stands for **Pixels Per Inch**. So when someone says they want a photo that is 300 dpi they really mean that they want 300 ppi.
> 
> *generally speaking, dot refers in a wirder arange, like the printer's ink dot, the sample dot, the physcical dot on screen... etc. whereas pixel only refers to the basic unit of digital image.  *
+ Common high-quality image formats: (in photography/ profasional field)
	+  **RAW**
	+ **TIFF**
	+ ** JPEG 94**
	+ etc...
+ other common-used image formats:
+ **JPEG** (0 ~ 100)
	+ usually, JPEG 75, JPEG 94, 
	+ adobe JPEG(0~12)
+ **GIF**
+ **PNG**


[EXIF](https://photographylife.com/what-is-exif-data) ( Exchangeable Image File Format )

3D 打印
+ aka 增材制造，addictive manufacturing
+ 细丝沉淀模型，FDM
	+ ABS
	+ PS

图像（位图） -->光栅化-> 图形（矢量图）
视频  			-->			 动画 

[RIFF](https://en.wikipedia.org/wiki/Resource_Interchange_File_Format) (Resource Interchange File Format)
> see here about the [structure of RIFF & .WAV](https://www.cnblogs.com/wangguchangqing/p/5957531.html)
> RIFF is a [container format](https://en.wikipedia.org/wiki/Container_format_(computing)) developed by Microsoft. see what's container format. 
> + RIFF file is [little-endian](http://liyanblog.cn/articles/2012/09/17/1347868763685.html)
> 
+ identifier (4 bit)
+ length (4 bit)
	+ length section only record the length of content, not including itself and the length of identifier, which adds up another 8 bits.
+ content (given length)
	+ [AVI](https://en.wikipedia.org/wiki/Audio_Video_Interleave)
	+ [WAV](https://en.wikipedia.org/wiki/WAV)
	+ [ANI](https://en.wikipedia.org/wiki/ANI_(animation_file_format))
	+ etc...
+ a pad byte (given length was obmitted)
 ![[Screen Shot 2021-09-27 at 11.20.31.png]]
 + see diff about [container format & code format](https://www.jianshu.com/p/7ceaa94d7fd7) and [here](http://www.manoner.com/post/音视频基础/常见编码格式和容器格式/)

 

 [美国出口管制条例](https://zh.wikipedia.org/zh-cn/美国出口管制条例)
 [超威半导体]()


----
# 29/9
+ [BlackBerry OS](https://en.wikipedia.org/wiki/BlackBerry_OS) (see more at [techopedia](https://www.techopedia.com/definition/25196/blackberry-os#:~:text=BlackBerry%20OS%20is%20a%20proprietary%20mobile%20operating%20system,the%20BlackBerry%20Bold%2C%20Curve%2C%20Pearl%20and%20Storm%20series.))
	+ **RIM**, Research In Motion
	+ **BES**, BlackBerry Enterprise Server
	+ **Java ME**, Java Micro Edition
	+ akin iOS, BlackBerryOS only run on BlackBerry devices
	>  BlackBerry OS was discontinued after the release of [BlackBerry 10](https://en.wikipedia.org/wiki/BlackBerry_10 "BlackBerry 10") in January 2013; however, support for the older OS continued until the end of 2013.
+ 3 essential components
	+ Motherboard
		> Interl, ARM <--> Acorn, [AMD](https://zh.wikipedia.org/wiki/超威半导体) ,[ASUS](https://en.wikipedia.org/wiki/Asus), [GIGABYTE](https://en.wikipedia.org/wiki/Gigabyte_Technology),  
		+ ATX, Adcanced Technology eXtended
		
			>  ATX is a motherboard form factor specification developed by Intel in 1995
			>  BTX: in 2003, Intel announced the BTX standard
			>  + [ATX 电源](https://sites.google.com/site/fenghuangsite/dian-nao/ying-jian/atx-dian-yuan-ban-ben-ji-fa-zhan-li-cheng-jie-xi)
					> + [接头](https://www.basemu.com/atx-power-supply-20pin-connector-pinout.html)
					>   ![ATX电源接口定义](https://www.basemu.com/wp-content/uploads/2016/10/ATX-power-supply-all.gif)
			+ Micro ATX
			+ Mini ATX, aka ITX
			+ [SATA](https://zh.wikipedia.org/zh-cn/SATA), aka Serial ATA, Serial Advanced Technology Attachment. disk interface. 
			+ > [并发，并行，串行，同步，异步](https://blog.csdn.net/qq_26442553/article/details/78729793): 并发是对事件的描述，并行串行是一种传输方式，同步异步是对通讯方式对描述
			+ PIN 
		+ ![[Screen Shot 2021-09-29 at 14.47.15.png]]
			+ Northbridge
				+ now often integrated into CPU
				+ CPU, RAM, video card
			+ Southbridge
				+ peripherials
			+ **BIOS** (/ˈbaɪɒs, -oʊs/, BY-oss, -⁠ohss; an acronym for** Basic Input/Output System **and also known as the System BIOS, ROM BIOS, BIOS ROM or PC BIOS) is firmware used to perform hardware initialization during the booting process (power-on startup), and to provide runtime services for operating systems and programs.
			+ **[PCI](https://blog.csdn.net/BjarneCpp/article/details/81096619)**, Peripheral Component Interconnect is a **local computer bus** for attaching hardware devices in a computer and is part of the PCI Local Bus standard.
		+ **BUS**
			+ contral bus
			+ address bus
			+ data bus
				+ front side bus, (FSB), connecting CPU and northbridge.
			+ 
	+ CPU
	
		> + Intel:  
		> Atom, Pentium, Core, Xeon, Itanium
		> + ADM:  
			> Fusion, A4/A6/A8/A10
		> + 兆芯
		> + 飞腾，国防科技大学 DSP 
		> + 海光 AMD + 中科曙光 X86
		> + 麒麟 kylin，鲲鹏，
		+ CPU <=> Control unit + ALU (arithmetic logic unit)
		+ Fetch-Execute Cycle
			+ ![[Screen Shot 2021-09-29 at 15.09.35.png]]
			+ fetches
			+ interprets
			+ executes
			+ stores
		+ Interface
			+ Slots
			+ Sockets
				+  distinct from [Sockets](https://www.tutorialspoint.com/unix_sockets/what_is_socket.htm) in web programming.
		+ encapsulation
			+  [DIP](https://baike.baidu.com/item/DIP/443840)
			+ [LGA/Land Grid Array](https://baike.baidu.com/item/LGA封装技术/7138677)：
		+ [CPU frequency ](https://zhuanlan.zhihu.com/p/53477952)(内频（主频），外频，超频，睿频)
			+ **Internal Clock**, --> CPU
			>  Internal system clock sends pulses at a fixed rate to synchronize all computer operations
			>  stands for CPU clock frequency
			+ 
				+ Clock Rate
				+ Clock cycle
			+ **FSB**, CPU <--> northbridge
			+ **External Clock**, northbridge <--> northbridge
				> equals to mainboard's frequency $times$ CPU multipiler(aka CPU Clock Ratio)
			+ overclocked
			+ [intel turbo clock](https://g.co/kgs/XxJ3kj) & AMD TurboCore
		+ Moore's law
		+ Heat dissipation
		+ Enhance CPU performance
			+ multiple COREs
				+ Internal clock frequency has reached to ceilling (as least for the time being), so add up the number of core is an option. 
			+ Hyper-Threading, (HT)
				+ a single Cores run multiple threads at a time
		+ CPU Cache/ multi-layer Cache
			> a spesical high-speed memory that stores most recently used data in orer to speed up the process of instruction execution
			> [Monolithic kernel & micro kernel](https://zhuanlan.zhihu.com/p/53612117)
			> [Cache vs RAM](https://www.cnblogs.com/jokerjason/p/9584402.html)
			+ L1, L2, L3
				+ L1>L2>L3>RAM
		+ word length
			+ bit digits CPU processes at a time
			+ 数据位宽/总线宽度
		+ [CPU architecture](https://www.quora.com/What-is-the-actual-difference-between-x86-ARM-and-MIPS-architectures)
			> CISC
			> + IA-32 : intel arch 32-bit
			> IA-64 Intel arch 64-bit
			> + X86
			> 	X86_64
			> 	
			> 	> AMD64,  VIA Nano
			>
			>  RISC
			> + Power
			> [MIPS](http://finance.sina.com.cn/tech/csj/2021-03-10/doc-ikkntiak7306876.shtml)
			> ARM
		+ + CISC: Complex Instruction Set Computer
				+ Intel/AMD 
			+ RISC: reduced Instruction Set Computer
				+ ARM / MISP
			+ [RISC-V](https://wiki.riscv.org/display/TECH/Tech+Home)
		+ IA-64: EPIC (Explicitly Parallel Instruction Computers)
		+ [IPS](https://baike.baidu.com/item/IPS屏幕/7048984)
	
	+ Memory
	+ > [ROM, RAM, FLAH](https://zhuanlan.zhihu.com/p/38339306) : ROM (read only memory), RAM (randem access memory) flash ([USB flash disk](https://www.flypeng.com/dnzs/1318.html), u盘)
	+ + RAM 
			+ RAM DRAM, RAM SRAM
			+ high speed, volatile memory, 
		+ Memory capacity
		+ Memory clock/ Cycle time
		+ Data rate
		+ 内存规范
			+ DRAM
			+ SRAM
			+ SDRAM
				+ SDR, DDR
		+ [fool-profing](https://cdc.tencent.com/2013/10/10/别让用户发呆-设计中的防呆策略/)
		+ connecting finger
	+ ROM
	+ Benchmark
	
+ Hypervisor
A **hypervisor**,aka a **virtual machine monitor** or** VMM**, is software that creates and runs virtual machines (VMs). A hypervisor allows one host computer to support multiple guest VMs by virtually sharing its resources, such as memory and processing.
>  Red hat
>  VMware
>  Cierix
>   Hyper-V
>   Huawai
>   浪潮
>   Xen, KOM 

[UPS](https://zanzan.tw/archives/13364)
- 电脑规格UPS
- 路由器规格UPS
- 光纤规格UPS

# 13/10
## Storage 
>  data path / bus ??
>  https://www.geeksforgeeks.org/introduction-of-alu-and-data-path/
>  + The CPU can be divided into two sections: **the data section **and** the control section**. The DATA section is also known as the data path.BUS: In early computers “BUS” were parallel electrical wires with multiple hardware connections. Therefore a bus is a communication system that transfers data between components inside a computer, or between computers. It includes hardware components like wires, optical fibers, etc and software, including communication protocols. The Registers, ALU, and the interconnecting BUS are collectively referred to as data paths.
+ 
+ Disk interface
	+ IDE (Iintegrated Drive Electronics)
		+ variant of IDE --- **ATA** ()
		+ 2 IDE ports --- primary prot & secondary port
		+ each port support 2 disk
	+ SATA
	+ SCSI
	+ SAS (series attached scis)
+ Mass storage
	+ **Optical Media** (==sperial circle track, NOT concentric circle track==)
		+ Pits / Lands represents 1s / 0s in binary.
	
		> 回形针📎
		+ CD (Compact Disk)
			+ [CD-ROM](https://baike.baidu.com/item/CD-ROM/513612) 
			+ CD-R (Recordable)
			+ CD-RW (ReWritable)
			+ VCD
		+ DVD (Digital Versatile DIsk)
			> http://en.wikipedia.org/wiki/Optical_disk
			+ DVD-DL (double layer)
			+ DVD-DS (double sided)
			+ DVD+ / DVD-
		+ BD/HD
			+ [Blue-ray disk](https://www.baike.com/wiki/蓝光?view_id=4yc3nh8cyta5mo)
				+ https://www.eet-china.com/mp/a25670.html
				+ 📖 [WiKi](https://zh.wikipedia.org/zh-cn/藍光光碟)
				+ [CBHD](https://zh.wikipedia.org/wiki/CBHD)
		+ S3 
	+ **Magnetic Media**
	
		1. [Floppy Disk](https://www.computerhope.com/jargon/f/floppydi.htm) (Floppy disk drice required)
			+ aka diskette
				+ build-in
				+ external
			+ Zip disk 
		2. [Hard Disk Driver](https://www.computerhope.com/jargon/h/harddriv.htm) (HD, HDD, 机械硬盘)
			> RAMAC   (Random Access Method of Accounting and Control)
			> + [3 types of hard disk](https://blog.csdn.net/xiaofei0859/article/details/50456930): HHD (hybrid hard disk), SSD (solid state dsik), HDD (hard disk driver)
			+ formatting ()
			+ layout
				+ track
				+ cylinder
				+ sector
				+ platter
				+ read/write head
			+ machanism
				+ TBD..
			+ head crush
			+ specs: 
			  ![[Screen Shot 2021-10-13 at 15.17.10.png]]
			+ **locating a block of data**
				+ seek time (main time cost)
				+ latency
				+ transfer time
				+ total time to access a disk block 
			+ external hard disk
			+ removable hard disk
			+ network hard disk
			+ 
		3. Magnetic Tape Data Storage
	
	+  **Circuit**
		+  solid state storage
			+  A nonvolatile storage medium that employs integrated circuits rather than magnetic or optical media
	+  **Flash memory**
	+   USB Flash Drive
	+   Memory card
	+   Secure digital card
	+   Microfilm & Microfiche


## I/O sys

> [what is UEFI, and how is it different from BIOS?](https://www.howtogeek.com/56958/htg-explains-how-uefi-will-replace-the-bios/)
> both UEFI and BIOS are low-level software that starts when you boot your PC before booting your operating system, but UEFI is a more modern solution, supporting larger hard drives, faster boot times, more security features, and—conveniently—graphics and mouse cursors.
> The BIOS will soon be dead: Intel has announced [plans to completely replace it with UEFI](https://www.anandtech.com/show/12068/intel-to-remove-bios-support-from-uefi-by-2020) on all their [chipsets](https://www.pugetsystems.com/labs/articles/Z97-vs-H97---What-is-the-Difference-562/) by 2020.
+ ![[Screen Shot 2021-10-13 at 15.52.16.png]]
+	Extension slot
	+ An expansion slot is a slit-like socket on the motherboard into which a circuit board can be inserted.
	+ interface standerd
		+ ISA
		+ PCI
			+ PCI-Express
			+ 
		+ AGP
+  Extension Card
	+  the circuit board is called extension card
+ ![[Screen Shot 2021-10-13 at 15.53.49.png]]
	+ internal 
		+ Soud card / PCI
		+ Modem card / PCMCIA
		+ Network card / BNC+RJ45/ PCI
		+ Digiral TV card / PCI
		![[Screen Shot 2021-10-13 at 16.00.08.png]]
		+ Digiral TV card / PCIE1x
	+ external
	+ > [video interface](https://zhuanlan.zhihu.com/p/133994348)
		+  VGA, Video Graphics Array
			+ IBM, 1987, monolog 
		+ DVI, Digital Visual Interface
		+ HDMI, High Definition Multimedia Interface
		+ DP, Display port
			+ https://baike.baidu.com/item/DisplayPort接口/10713038
+ Extension Port

	![[Screen Shot 2021-10-13 at 16.06.22.png]]
	![[Screen Shot 2021-10-13 at 16.07.35.png]]
	+ serial port
		+ one bit of data at a time
	+ parallel port
		+ transfer more than one bit at a time
	+ USB, universal serial bus port
		+ USB 1.0
		+ USB 2.0
			+ Micro USB
		+ USB 3.0
			+ USB 3.1 Gen 1
			+ USB 3.1 Gen 2
			+ etc...
		> see up-to-date port types at [here](https://www.yinxiang.com/everhub/note/4828ea4f-240b-44bd-8cfd-20ecd7cd1657)
		> ![[600px-ports_type.jpeg]]
	+ FireWire
	+ Special-purpose port
		+ MIDI
		+ SCSI
		+ IrDA
		+ Bluetooth
+ PnP (Plug and Play) & Hot Plug
+ Pointing devices
	+ Mechenical mouse
	+ optical mouse
	+ trackball
	+ touchpad
	+ pointing track
	+ joystick
	+ wheel
	+ pedal
	+ Kinect
+ Optical reader
	+ OCR
	+ OMR
+ bar code
+ two-demensional code
	+ data metric
	+ [QR code](https://www.cnblogs.com/sddai/p/5675041.html#:~:text=QR码%28Quick%20Response%20Code%29%20是二维码的一种，在正方形二位矩阵内通过黑白标识编码二进制位从而编码数据，最早发明用于日本汽车制造业追踪零部件%E3%80%82,QR码现有40个标准版本，4个微型版本%E3%80%82%20QR码的数据编码方式有四种：%20数字（Numeric）：0-9%20大写字母和数字（alphanumeric）：0-9，A-Z，空格，%24，%25，%2A，%2B，-，.，%2F，%3A)
		+ https://cloud.tencent.com/developer/news/520947
+ RFID


+ [PCB](https://www.bilibili.com/read/cv9989006)
PCB, Printed Circuit Board / PCBA, printed circuit board + assembly.


# 20/10/21
## Software
software types:
+ System Software
	+ Operating Systems
	+ Device Drivers
	+ Utilities
+ application 

Development Software:
+ Programming Languqages
+ Scripting Languages
+ Quality Assurance Tools


[web apps](https://en.wikipedia.org/wiki/Web_application)

# Network
Shannon - Weaver Model of Communication: 
![Shannon - Weaver Model of Communication|500](https://wiki.mbalib.com/w/images/thumb/a/a8/%E9%A6%99%E5%86%9C-%E9%9F%A6%E5%BC%97%E6%A8%A1%E5%BC%8F2.jpg/700px-%E9%A6%99%E5%86%9C-%E9%9F%A6%E5%BC%97%E6%A8%A1%E5%BC%8F2.jpg)

## network types:
+ pan, personal area network
+ lan, local area network
+ man, metropolitan area network
+ wan, wide area network

## communication channel (media)
+ [wireless channel](https://zhuanlan.zhihu.com/p/137391589)
	+ radio, rf signals
		+ bluetooth
		+ wifi
		+ etc
	+ microwave
		+ oriented. 微波可以指向一个方向，不能穿过金属物体，适用于视线传播
		+ cecullar data
		+ 广域无线设备之间传输塔台
	+ open to pubic : 2.4 GHz / 5 GHz
+ wired channel 

**Federal Communications Commission**

+ bandwidth
	+ digital signal: bps
	+ analog signal: Hz
+ broad band: > 25Mbps
+ narrow band < 25Mbps

## topology
point-to-point, star, mesh, bus

DTE: data terminal equipment
DCE: data communication equipment 

router/modem

![[Screen Shot 2021-11-10 at 2.43.11 PM.png]]
![[Screen Shot 2021-11-10 at 2.44.28 PM.png]]

## communication protocol

+ communication protocol:
	+ phisical rotocol
	+ transmission protocol
	+ arrival protocol 

handshaking
protocol stack
error correction

## Internet
adcanced reserch projects agency, ARPA --> arpanet --> internet --> Internet

comcast, AT&T, NTT

ICANN, internet corporation for assigned names and numbers

### internet infrastructure

internet backbone
AT&T, CenturyLink, Verizon,NTT, 
mesh topology, high capacity, fast route, fiber communication

ISP, internet service provider
IXP, internet eXchange Point
+ IXP, where different ISP exchange content 


**charge on Internet: **
![[Screen Shot 2021-11-17 at 2.11.36 PM.png]]
### packet
+ [**network switching**](https://zhuanlan.zhihu.com/p/372344282)

circuit switching
+ PSTN, public Switching Telephone Network
packet switching

UDP/TCP, core network protocol, transmission layer
+ creat package

communication port

### internet address

**IP**, internet address manage. it defines to types of ip address:** IPv4, IPv6**


static IP address.
+ permenant, 
+ stabel

dyanmic IP address
+ temporaryt
+ DHCP, dynamic host configuration protocol
	+ private IP address, free from ICANN
		+ un-routed, no access to Internet, using within private network
		+ .edu network
			+ 10, 172, 192, FD, Fc00


NAT, network address translation


### domain name

[Internet kill switch](https://techshielder.com/zh/什么是kill-switch？)

DNS
+ DNS spoofing

lab:
WHOIS, 190.181.132.250

### Internet access

connection access
+ speedtest.com

bandwidth cap
bandwidth throttling

asymmetric connection
symmetric connection

Ping
Latency /  ms
+ i.e. time taken on a-->b + b-->a
packet loss
jitter

Traceroute
Akamai : Realtime Web Monitor 
downrightnow.com

#### 有线电视因特网服务
cable internet service

#### 电话网络因特网服务

**dial-up**
+ upload speed: < 56 Kbps. narrow band

**ISDN**, integrated services digital network

**DSL**, digital subscriber line
+ ASDL
+ SDSL
+ HDSL
+ VDSL

**FTTH**, fiber-to-the-home

####  卫星因特网服务
satellite internet service

#### 移动宽带服务 
mobile broadband service
+ types
	+ voice 
	+ data
+ 3G
	+ CDMA
	+ GSM EDGE
+ 4G
	+ WiMAX
	+ LTE


## LAN
classified by the protocol used, there are various types of LAN, and  [Ethernet](https://zh.wikipedia.org/zh-cn/以太网) & WiFi are the two of them that are used widest. 
LAN uses 2.5 GHz and 5 GHz, so it's authorization-free.

Network Interface Controller, aka [NIC](https://zhuanlan.zhihu.com/p/371399045) （[what is NIC?](https://en.wikipedia.org/wiki/Network_interface_controller)）, allows devices to access LAN. 
> [网卡，网关，路由器](https://blog.csdn.net/bytxl/article/details/41897599)
+ containning a [MAC address( media access control address)](https://en.wikipedia.org/wiki/MAC_address) see notes about [[SCU/CS/Computer Networking/terms#^6f6664|MAC]] 
+ both built-in or plug-in.

### [Ethernet](https://zh.wikipedia.org/zh-cn/以太网)
IEEE 802.3
wired connection, (100Mbps ~ 100Gbps)

star topology
built-in switch circuit
![[Screen Shot 2021-11-10 at 4.01.52 PM.png]]

Ethernet pros:
+ simple
+ safe
+ cheap
+ fexible
+ compatible

to impliment an Ethernet ...
+ built-in Ethernet port
+ ... or an external Ethernet adapter, 以太网适配器/以太网卡 


### Wi-Fi
IEEE 802.11
+ 802.11n  --- 600 Mbps --- 50~100 Mbps
+ 802.11ac --- 7Gbps --- 400 ~ 800 Mbps
+ 802.11ad
+ （standard to use depend on the supportability of the device ）

wireless connection, (50 Mbps ~ 800 Mbps)
[commonly used wireless connection](https://zhuanlan.zhihu.com/p/137391589) 
1. long-distance communication
	1. GPRS/CDMA (2.5G)
	2. 数传电台
	3. 扩频微波
	4. 无线网桥及卫星通信
	5. 短波通信技术
2. short-distance communication
	1. Zig-Bee
	2. 蓝牙(Bluetooth)
	3. 无线宽带(Wi-Fi)
	4. 超宽带(UWB)和近场通信(NFC)。

two config mode:
+ mesh topology (无线网状拓扑结构)
	+ no router, each host communicates with each other.
	+ akin to personal hotspot
+ star topology 
	+ 存在一个集中式广播设备（access point）协调网络设备间通讯
	+ 各终端节点通过该广播设备（路由器）通讯

Wi-Fi adapter

![[Screen Shot 2021-11-10 at 4.07.35 PM.png]]

SSID, service set identifier

wireless encryption
+ WEP, wired equivalent privacy
+ WPA, Wi-Fi Protected Access
+ PSK
wireless encryption key

guest network


## IoT
RFID, radio-frequency identification
NFC, near-field comunication
Bluetooth Smart
ZigBee
Z-Wave


[集线器、网桥、交换机、路由器、网关大解析](https://blog.csdn.net/frankarmstrong/article/details/77969699)
[无线通讯](https://zhuanlan.zhihu.com/p/137391589)


## file sharing

### file sharing on local area network :
network discovery
### file sharing on Internet: 
#### FTP
file transfer protocol, allowing file sharing through any TCP/IP network. 

+ dropbox

#### Torrent
origin: napster

BitTorrent, file sharing protocol


# World Wide Web
## basics of www
### Web overview
Web (short for world wide web) is one of the techonology communcating information under the Internet. web is a sub-network of Internet. 

Web is the set of HTML, imeages,videos, audios (and any other media?). it's accessable through HTTP on Internet. 

borwser is a software designed to access Web with easy. 
Microsoft Edge, Mozilla Firefox, Google Chrome, Apple safari

### Web history


1990, Time Berners-Lee
URL, HTML, HTTP, 
Nexus
Mosaic
Netscape

short URL
checkshorturl.com
getlinkinfo.com

### Web site
Web server
Web page

### hypertext link
unidirectional link
bidirectioinal link

### URL, uniform resource locator
```html
https://	www.cnn.com/	showbiz/	movies.htm
protocol	Web servername	directory	filename
```
short URL

### Browser
==plugin==
==extension==

## HTML 
### hypertext markup language
creat HTML file
+ html 转换程序。如ms word
+ 在线编辑器。如WordPress
+ 本地安装的编辑器。如Adobe Dreamweaver

HTML structure: 

![[Screen Shot 2021-11-17 at 3.26.45 PM.png]]

### CSS, cascading style sheets
set style rule for web

3 types of CSS: 
+ inline CSS
+ internal CSS
+ external CSS (recommand)

CSS 样式规则 包含 选择器和声明块。选择器指定应用样式规则的HTML元素，声明块指定样式。

![[Screen Shot 2021-11-24 at 3.02.35 PM.png]]

### script
script language:  js, php, python

client-side script
server-side script

### web hosting service
GoDaddy, AWS, HostGator

## HTTP 
> HTTP is on app lary; TCP/UDP is on transmission lary; IP is on network lary.

HTTP session
stateless protocol
HTTP status code

### [cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)
session cookie.
+ freed once window closed.

persistent cookie
+ stored at local host

first-party cookie
+ original web provide

third-party cookie
+ other web provide (spon)

###  HTTPs
HTTP + [[SCU/CS/Computer Networking/terms#^e87136|SSL/TLS]]

## Web search engine
search engine vs. search web

搜索引擎组件: 
+ 爬网程序 （Web crawler）
+ 索引器 (search engine indexer)
	+ 查询处理器 （query processor）
	+ 链接流行度 （link popularity）
	+ 搜索引擎优化 （search engine optimization, SEO）
	+ 赞助商链接 （sponsored links）
+ 数据库
+ 查询处理器 (query processor)


search item
search operator (google for instance)
+ AND
+ OR
+ NOT
+ ""
+ **
+ .. 

filter
advanced search

## private seaerch

AOL

search history
+ server log

## use raw material from www

Ref:
MLA, APA, Chicago

[fair use doctrine](https://www.copyright.gov/fair-use/more-info.html)


---
BSD 
GPL

pirated software

multi-tasking
multi-threading

.exe
.dll


木马 独立程序
蠕虫/病毒 传播

nat 和 防火墙


# social network

## social media
####  classification 
orientation-based
+ linkedin ---  facebook, google+

conten-based
+ blogger -- wordpress

#### social media honeycomb
![[Screen Shot 2021-12-01 at 2.29.58 PM.png]]

### social network basics 
online identity
social media profile

### geosocial networking
yelp, [foursquare](https://foursquare.com), [banjo](https://banjo.com), google maps

**crowdsourcing**
amazon, zappos, 

localization 

![[Screen Shot 2021-12-01 at 2.42.47 PM.png]]
geocoding
geotagging


sociogram, 社会关系图
binary adjacency matrix 二进制邻接矩阵

## content community

Bulletin Board System, BBS
project Gutenberg
Wikipedia
Webshots, Flicker, Photobucket
YouTube
Slide Share
Pinterest
Instagram

### media content community

metadata tag

formal tagging
Dublin Core Schema

### Intellectual Property
IP:
1. Patent
2. Trademark
3. Copyright
	1. public domain
	2. licence
4. commercial secrete

### [Creative Commons](https://creativecommons.org)
Creative Commons license

> create your own license on [CC.com](https://creativecommons.org/choose/)!! 
> 
> <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

fair use

derivative work


#### other licenes:
https://choosealicense.com
https://zhuanlan.zhihu.com/p/20641764


## Blog
Blogger, wordPress, Medium
Mashable, Gizmodo

[RSS](https://rss.com/blog/popular-rss-feeds/)
+ [RSS quick intro](https://sspai.com/post/56391)
+ [cainiao.com](https://www.runoob.com/rss/rss-reference.html)
+ [zhihu.com/ build own RSS](https://www.zhihu.com/question/384290217)

RSS reader
blog aggregator
Alltop

### microblogging service

### Wiki
NPOV, NOR, V


## online communication
### communication matrix
![[Screen Shot 2021-12-01 at 3.46.03 PM.png]]
### E-mail
email system
email server


message header


webmail
store-and-forward

SMTP(port: 25 / 578) --> POP3/IMAP (port: 110)

### Instant Messaging, IM
VoIP, voice over internet protocol
+ PSTN

![[Screen Shot 2021-12-01 at 3.58.31 PM.png]]

some of VoIP is open source  ...
while others are exclusive;
+ Skype, google hangouts, snapchat, facetime, Vonage
+ GoToMeeting, WebEx


## social media value
### identity
sockpuppet
generic profile image
tagline
+ headline, intro

### reputation
defamation
cyberbullying
impersonation
doppelganger

 ### privacy
 Personally Identifiable Information, PII

 # hack
 1. evil tween 
 2. 地址欺骗
	 1. DNS
 3. 勒索软件


# Database
operational database
analytical database

data mining
- 数据捕捞
- 数据钓鱼


predictive analytics
online analytical processing, OLAP

## Database model
unstructured file
- no unifield standard to organise these files

strctured file
- use a unifiled standard to organize 

### field
field name
variable-length field
fixed-length field

### record
-- a set of related fields

record type
record occurrence

### relationship
cardinality

entity-relationship diagram (erd / er)
[ERD 图及其画法](https://blog.csdn.net/WHEgqing/article/details/108998283)

1. hierarchical database
	- windows 
		- registry data

2. graph database
3. relational database
	- table
4. multidimensional database
5. object database
6. document-oriented databse


XML, eXtensible Markup Language

## database tools (DBMS)
ASCII, amerian standard code for information interchange

data dependence
data independence

CRM, ERP, SCM

single-level sort
multi-level sort

DBMS, database management system

for small-scale enterprises: 
FileMaker Pro
Microsoft Access

for larger scale enterprises:
IBM, Oracle, SAS, SAP

SQLite, MySQL

primary key

field validation rule
lookpup routine

### data type
real
integer
date
text
memo
logical
BLOB, Binary Large Object
Hyperlink

### normalization
data redundancy


### joining table

## bigdata

volume
velocity
variety
veracity
value

- low-density data
- high-density data

### NoSQL

MongoDB, Cassandra HBase, Hive, Presto, Google BigTable, Spark, Voldemort

# digital security

## security basics
### encryption
encryption, decryption
plaintext, cleartext

cryptographic key

AES, advanced ecryption standard

==### authentication==

user authetication
two-factor authentification

### password
strong password

brute-force attack
dictionary attack

### password manager
strength meter

## malware
malware exploit, 恶意软件攻击 / 有效载荷

code injection
side-loading
rootkit

### worm
self-reproduce, self-dirstribute
indie app

computer worm:
- mass-mailing worm
- Internet worm
- file-sharing worm

### trojan
dropper

stuxnet

### antivirus software
诺顿，卡巴斯基，F-Secure，windows defender, Avast

virus signature
heuristic analysis
false positive

## online intrusion
remote access trojan, RAT
locky, dridex, cryptolocker

### botnet
DDoS, distributed denial of service

### 0-day attack

on-access scan
on-demand scan
matwarebytes

### NETSTAT
port scan

### firewall
NAT, network address translatiion

## interception
spyware
adware
keylogger
man-in-the-middle, MITM, MIM
- evil twin
- addres spoofing
- 数字证书破解, TLS
- IMSI 捕获 (international mobile subscriber identity)
	- DEF CON
	- Ignite
	- LTE 4G技术


## social engineering (SE)
SMS, IRC
phishing
- spear phishing

pharming

### rogue antivirus
### PUA
PUP, potentially unwanted program, == PUA, potentially unwanted application








# final 
数字安全
![[C1E7A5910064CA13CCA2C36C470456A5.jpg]]

信息系统

数据库：
描述图片尽可能详尽
ER图
SQL语法


数据库设计， power designer
- 规范化



# Inforamtion system
Transaction processing system, TPS

