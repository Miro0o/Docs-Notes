5.2 ARC
5.3 CSMACD

---

# EDC
EDC, error detection and correction

parity check
internet checksum

## CRC, Cyclic Redundancy Check.
![[Screen Shot 2021-12-13 at 9.32.42 AM.png]]

# multiple access protocols
TWE types of links:
1. point-to-point
	1. p2p link between ethernet switch, host (fiber link)
	2. ppp dial-up 
2. broadcast (shared medium)
	1. old-fashioned Ethernet
	2. upstream HFC in cable-based access network
	3. 802.11 wireless LAN, 4G/4G. satellite

> in bus transportation, muster/slave architecture, 

### MAC protocols: taxonomy

THREE broad classes:
1. channel partitioning
	1. time slots
		1. TDMA, time division multiple access
	2. frequency
		1. FDMA, frequency division multiple access
	3. code
2. randem access
	1. slotted ALOHA
	2. pure ALOHA
	3. [CSMA](https://blog.csdn.net/lucyxiaomeng/article/details/79707842)carrier sense multiple access
		1. simple CSMA: listen before transmit
		2. [CSMA/CD](https://blog.csdn.net/zyj66666/article/details/73732217), collision detection 
			1. [aother blog](https://blog.csdn.net/lucyxiaomeng/article/details/80563845)
			2. Ethernet CSMA/CD algorithm
				1. ==binary exponential backoff==
		3. CSMA/CA, 
		4. [diff between CAMA/CD & CSMA/CA](https://blog.csdn.net/yuzhongchun/article/details/8678749?spm=1001.2101.3001.6650.3&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-3.essearch_pc_relevant&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-3.essearch_pc_relevant)
			1. https://blog.csdn.net/weixin_42859280/article/details/86530097?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-1.essearch_pc_relevant&spm=1001.2101.3001.4242.2
3. taking turns

#### CSMA (carrier sense multiple access)

# LANs 
MAC address: used “locally” to get frame from one interface to another physically-connected interface (same subnet, in IP-addressing sense).
administered by IEEE. 
## addressing, ARP
### ARP, address resolution protocol
## Ethernet
## switches
> 一种攻击方法是，向交换机发送大量垃圾消息，利用交换机自学的机制使其表内充满垃圾地址至垃圾地址溢出。当真实的目标主机发送信息帧时，交换机因为查不到表会进行广播发送信息帧，此时监听机就可以收到想要的信息了。



