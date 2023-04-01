 + 考研
	+ 计算机网络
	+ 数据结构（？
	+ 操作系统

+ accessment
	+ homework (3~4)
	+ _no_ midterm exam
	+ pick-up (3~4)

+ course gists (6th)
	+ 1.1 ～ 1.3
	+ 1.4
	+  1.5 

+ quick notes
	+ ietf.org
	+ 网络编程

--- 

# 1.1 

+ transmission
	+ speed transmission
	+ quality transmission
+ electrical sign transmit speed: 2*10^8 m/s
+ tcp congestion control 
+ udp/tcp/
	+ tcp : 可靠的，有序的
	+ udp: 不可靠的，无序的，
+ bit/byte ???? 
+ 3G
	+ wcdma europe 联通
	+ cdma2000 高通 ?
	+ td-scdma 
+ protocol
	+ 
	+ control sending, receiving of msgs
	+ format+order+actions taken

		clint				|				svr
				→ handshake(megs)
				response ←
				data
				ack
		
		
+ internet standards
	+ **IETF** internet engineering task force
		+ **RFC** request for comments 


# 1.2
+ network edge
	+ hosts: c/s
	+ servers often in data centers
+ access networks: physical media
	+ wired,wireless
+ network core

+ connect end system to edge router
	+ residential access nets
	+ institutional access networks
	+ mobile access networks 
+ access net:
	+  home network
		+ to/from headend or central office 
		+ cable or DSL moderm
		+ power moderm
	+ enterprise access networks (**Ethernet**)
		+ companis. universitoes, etc,
		+ transmission rates: 10M bps, 100M bps, 1G bps, 10G bps


>                                    G				M				K
>     net						1Gb			10*3
>     file-system				1GB		    2*10


+ wireless acces networks
	+ LAN 802.11 b/g (WiFi)
	+ WAN 
		+ cellular 
		+ 3G,4G: LTE
	+ WLAN
		+ AP : access point 

+ transmission rate / link bandwidth / 
+ Physical media
	+ twisted pair (TP) 2*4
		+ STP/UTP
			+ shielded/unshielded
		+ category 5 ----- 100Mbp 
		+ category 6 ----- 10Gbp

	+ coaxial cable
	+ fiber optic cable
	+ radio 
		+ radio link types:
			+ **terrestrial radio**
				+ terrestrial micowave
					+ up to 45 Mbp
				+ LAN (WiFi)
				+ wide-area
			+ **satellite**

# 1.4
## four sources of packet delay
+ nodal processing delay
	+ check bit errors
		+ CRC
	+ determine output link
+ transmission delay
	+ delay in uploading data to the link
	+ depends on [bandwidth](https://baike.baidu.com/item/带宽/266879) ↓
	+ bandwidth = transmission rate
	+ = the rate of transforming **binary num (0/1)** to **electrical/ optic signa** 
+ propagation delay
	+ time takes on the physical link
		+ length of physical link 
		+ propagation speed in medium ($2*10^8$ m/s)
	+ **bandwidth-delay product**
		+ the total amount of bit on a full-loaded physical link
		+ $=R(b/s)*Dprop(s)=R*D$
		+ R: stransmission rate
		
+  "Real" Internet delays and routes
	+  [ping](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/ping)
	+  [**traceroute**](https://www.cnblogs.com/emilyyoucan/p/7478532.html)
		+ prequisite 
			+  dest IP/  port
			+  src: source IP/ port 
			+  TTL (time-to-live), drop, hop
+  throughput 
	+  practical rate between **systemes**
		+  compared with **bandwidth**, which is the theorical rate.  
	+  each connection path between host is referred as **flow**
	+  condisder an optimal distribution strategy:
		+  1, 2, 3, 4 ,5 (bpm) are required by each flow 
		+  strategy 1: evenly split 
		+  strategy 2: proportionally split
		+  strategy 3: fulfil as many as the system can, evenly split the rest 


> #### 5G
	> mMTC
	> surpport 1M end access in


# 1.5 Why layering? 
	> 	app			| bussiness / usr-space process |
	> 	transport	| reliable transport (TCP/UDP)	| kernel module
	> 	network		| routing, (IP -- Dijkstra )	| kernel module
	> 	link		| neighbour node				| NIC + driver 
	>	physical	| signal transform				|
	
	e.g. 
		transport
			the setting of the timer in TCP transport
		link layer:
			master-slave mode in bluetooth
			
