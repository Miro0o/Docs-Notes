overview:
3.5 connection-oriented transport: TCP
3.7 TCP congestion control

3.6 principles of TCP congestion

-----
# 3.1 transport services and protocols
transport service provide ==logical communication== between proccesses, while network service provide logical communication between hosts
+ ** TCP, transmission control protocol**
	+ reliable,==in-order delivery==
	> in-order: 有序
	> delivery: the action between transpor layer and app layer
	+ congestion control
	+ flow control
	+ connection setup 
+ **UDP, user datagram protocol   **
	+ unreliable, unordered delivery==(in computer networking, term **delivery** specificlly refers to the action taken between application layer and the layer  nearest to it (usually transport layer))==
	+ no-frills extension of “best-effort” IP
+ services not available:
	+ delay guarantees
	+ bandwidth guarantees


# 3.2 Multiplexing & Demultiplexing 
## Port
> **bind error ! **
> when port assignment (multiplexing ) conflicts bind error ocdcurs. 
+ full name --> transport port (port number is assigened by transport protocol )
+ (0, 1023] --> well-known port #
	+ 80, 21, 20, 25, 110,
+ [1024, 65535] --> ephemoeral port #

## Multiplexing
+ adsf 


## Demultiplexing
+ TCP demultiplexing rules:
	+ ==4-tuples==
		+ dst port
		+ dst IP
		+ src port
		+ src IP
	+ one process contains multiple entities (socket?) to receive msg. 
+ UDP demultiplexing rules:
	+ dst port
	+ one process contains singly entity to receive msgs.
	+ ⚠️ ⚠️ ⚠️ however, UDP guarrantee the intact of scr pakage. it uses the same algorithme as TCP to check bit error. 

# 3.3 UDP: User Datagram Protocol 

it's interesting to point out that, the market proportion of UDP is gainning. 

+ “no frills,” “bare bones” Internet transport protocol
+ “best effort” service, UDP segments may be:
	+ lost
	+ delivered out-of-order to app
+ connectionless:
	+ no handshaking between UDP sender, receiver
	+ each UDP segment handled independently of others

> UDP handles packages seperately, while TCP either handles multiple at a time or one at a multile times. 

  ##  ==**why is there a UDP?**==
+ no connection establishment (which can add RTT delay)
+ simple: no connection state at sender, receiver
+ small header size
+ no congestion control
+ UDP can blast away as fast as desired!
+ can function in the face of congestion

## UDP uses in:

+ streaming multimedia apps
+ DNS
+ [SNMP](https://support.huawei.com/enterprise/zh/doc/EDOC1100087025)
+ HTTP/3

> [QUIC](https://baike.baidu.com/item/QUIC/17341272) (Quick UDP Internet Connection) is an UDP-based liarbry developed by Google.

![[UDP_structure.png]]

**NOTISE** ☝️ that the 16 bit  _length_ contains the bytes of the whole segment,hence the length of the whole segment is 65536 bytes. the length of _payload_ is 65535 - 2*32/8 bytes.  
while in other layer, datagram for instance, the _length_ is also 16bits, which means the _length_ of the datagram is also 65535. but the header's length is different in datagam (say 20 bits), hence the length of palyload is different. 

**checksum:**
> review:
> + 奇偶校验
>  + EDC, error detection code 
> + spoiler alert: CRC

+ checksum = 0x00
+ 0x00 补齐尾码
![[Screen Shot 2021-10-25 at 10.35.10.png]]
![[Screen Shot 2021-10-25 at 10.35.39.png]]

# 3.4 Principles of reliable data transfer （rdt）

+ ==stop & wait==
	+  rdt 1.0 
	+  rdt 2.0
		+  rdt 2.1 
		+  redt 2.2
	+  rdt 3.0
+  ==pipeline==
	+  gbn
	+  sr

-----

## rdt interface:

![[Screen Shot 2021-11-01 at 08.36.03.png]]

+ rdt_send()
+ udt_send()
+ deliver_data()
+ rdt_rcv()

> ## FSM
>
> [Finite State Machine](https://www.jianshu.com/p/dc59262dc646), or FSA "finite state automaton"
>
> </br> <iframe src="https://player.bilibili.com/player.html?aid=540400506&bvid=BV1Yi4y1t7J3&cid=184509542&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>


## [rdt](https://blog.csdn.net/springtostring/article/details/80379841) (==stop and wait==)
###  rdt 1.0
+ **premise**: persuming all underling channels are perfectlt reliable.
+ **Separate** FSMs for sender & receiver
+ ![[Screen Shot 2021-11-01 at 08.44.29.png]]

### rdt 2.0
+ **error : ** flip bits
	+ checksum
+ **sollusion : ** ACKs & NAKs
	+ ACKs:    acknowledgements
	+ NAKs: negative acknowledgements
	+ > rdt2.0在rdt1.0的基础上解决了比特位翻转的问题，这里的比特位防撞发生在运输层下面的不可信信道中数据包中的1可能会变0，0可能会变成1。rdt2.0增加了3种新机制：1.错误检验 2.接收者反馈接受信息（ACK,NAK）3.重传机制。在运输层对应用层的数据进行打包处理时，新增checksum（校验和），从而接收端可以对其数据包进行检验，如果正确，返回ACK，发送者继续发送下一个数据包；如果不正确，返回NAK，发送者重传数据。


	### rdt 2.1
	+ **error : ** garbled ACKs & NAKs
	+ **solusion :** sequence 0, 1
	+ ![[Screen Shot 2021-11-01 at 09.20.56.png|500]]
	### rdt 2.2
	+ **improvement : ** (ack, 0) / (ack, 1) ---> NAK-free
	+ ![[Screen Shot 2021-11-01 at 09.22.02.png|500]]
### rdt 3.0
+ **loss : ** packages & data loss
+ **solusion : ** timer
+ ![[Screen Shot 2021-11-01 at 09.45.18.png]]
+ ![[Screen Shot 2021-11-01 at 09.45.36.png]]
+ **Performance of rdt3.0 :** stink!


### other protocals ==(pipeline)==
> ⚠️⚠️⚠️ IMPORTANT 
> windows 
	> + size: the maximal size the protocal allows to store/process. 
	> + position: the onset digit
+ gbn (Go-Back-N) 
>1. 发送者在流水线中最多有 N 个未确认的数据报。
>2. 接收者仅发送累计的确认 ，如果中间有数据报缺失，就不予以确认。
>3. 发送者对最久未确认的数据报进行计时，如果计时器到点, 重传所有未确认的数据报。
>4. 发送窗口大于1，接受窗口等于1（也就意味着如果某一个报文段出现错误，那么接受窗口会停留再次，之后收到的数据将会被丢弃）


+
	+ window size n : gbn allows up to n consecutive transmitted ==in-flight== un-ACKed packages on pipeline 
	+ drop out-of-order pkg
	+ sends cumulative ack 
		+  receiver send feedback for every received pkg, but only the pkg with highest seq # of the consecutivly received pkgs. ( once the highest seq # pkg is confirmed, all pkgs before it is correctly received).
+  sr (selective repeat) 

> 1. 发送者在流水线中最多有 N 个未确认的数据报。  
> 2. 接收者对单个数据报进行确认。
> 3. 发送者对每一个未确认的数据报进行计时，如果计时器到点, 仅重传该个未确认的数据报。
> 4. 发送窗口大于1，接受窗口大于1（意味着可以缓存出错位置之后的报文段），最好是两者相同，
+	+  drop out-of-order pkg
	+  sends individual ack



# 3.5 Connection oriented protocal: TCP
>  + window size
>  + window size changing rate

## TCP: overview
+ point-to-point:
	+ one sender, one receiver
+ reliable, in-order byte steam:
	+ no “message boundaries" in TCP's buffer
+ full duplex data:
	+ bi-directional data flow in same connection
+ ==MSS:==[ maximum segment size](https://en.wikipedia.org/wiki/Maximum_segment_size) (1500Bytes, segment, transmission layer ? )
	+ (==MTU:== [maximum transmission unit at link layer](https://en.wikipedia.org/wiki/Maximum_transmission_unit), body )
+ cumulative ACKs
+ pipelining:
	+ TCP congestion and flow control set window size
+ connection-oriented:
	+ handshaking (exchange of control messages) initializes sender, receiver state before data exchange
+ ==flow controlled:== (differ from pkg loss during router in network layer)
	+ sender will NOT overwhelm receiver. (in transport layer)

## TCP segment structure

![[Screen Shot 2021-11-08 at 10.32.21 AM.png]]
+ sequence number:
	+ $2^{32} bits = 4GB$
+ RST: reset
	+ error occured, stop current transmission
+ SYN: synchronize
	+ tri-hankshake?
+ FIN: final
	+ correctly stop
+ [Flow control](https://en.wikipedia.org/wiki/Transmission_Control_Protocol#Flow_control):
	+ from networklayer 
	+ to app layer
+ options
	+ MSS

[UML](https://www.codesee.io/?utm_source=google&utm_medium=cpc&obility_id=130909286767&utm_campaign=&utm_term=uml%20software&utm_content=546082320446&gclid=Cj0KCQjw8p2MBhCiARIsADDUFVGPXT82ywHwnQEdQJOn_8QdtzWDYnKREL6yHn9g3SBHxQlniCtRKRcaAv2nEALw_wcB)

## TCP sequence numbers, ACKs
## TCP round trip time (rtt), timeout
estimate rtt:
+ SampleRTT
+ EstimatedRTT

[EWMA](https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc324.htm)

+ EstimatedRTT = (1- a)*EstimatedRTT + a*SampleRTT
+ typical value: a = 0.125



mac: 8 re
win: 12 re


capacity
receive window

# TCP congestion control

📜 https://en.wikipedia.org/wiki/TCP_congestion_control

> Sender window		--		swnd
> Receive window		--		rwnd
> Congestion window		--		cwnd

## overview: 

![[Screen Shot 2021-11-22 at 9.44.13 AM.png]]



## AIMD
Additive Increase and Multiplicative Decrease
+ sawtooth behavior
+ grow one MSS at a RTT time, 
+ decrease by half when loss detected

AIMD
+ distributed, asynchronous algorithm
+ optimize congested flow rates network wide
+ have desirable stability properties

## TCP: from slow start to congestion control
Slow start:
+ cwnd add up by the number of ACKs received concecutivly. 
+ so at beginnning, cwnd grow expoentially. 
+ once loss occured, cwnd reduced to 1 length* at a time, and set the ssthresh (slow start threshold) of the half of the last highest length.


*丢包判定 ： 
+ RTO 超时 （网络拥塞较严重）
	+ TCP Reno 和 TCP Tahoe 都从 1 开始 slow start 模式的倍数增长。
+ 重复ACK （网络拥塞较轻）
	+ TCP Reno 从 ssthresh 开始线性增长，而TCP Tahoe 从1 开始slow start 模式下的倍数增长。

Sender window = Min ( rwnd , cwnd )
![[Screen Shot 2021-11-29 at 8.36.12 AM.png]]
![[Screen Shot 2021-11-29 at 8.36.36 AM.png]]

## TCP fairness
![[AIMD-+State+Transition+Trace.jpeg]]
AIMD garantee the fairness of bandwidth distribution
