# Network layer overview: 
## data plane
local, per-router function
forwarding data form `input port` to `output port`
## control plane
network-wide logic
routing date from `src host` to `dst host`
- ___traditional routing algorithms___: implemented in routers
- ___software-defined networking (SDN)___: implemented in (remote) servers


## interplay between routing and forwarding 

+ forwarding table
+ routing table
	+ IP addrs
	+ MAC addrs

## network-layer service model

![[Screen Shot 2021-12-06 at 8.36.05 PM.png]]


# What's inside a router:

![[Screen Shot 2021-12-06 at 8.39.04 PM.png]]

## Input function
![[Screen Shot 2021-12-06 at 8.42.14 PM.png]]

### destination-based forwarding
Longest prefix matching

## Switching fabric
Switching rate
3 major types of switching fabrics: 
1. memory
2. bus
3. interconnection network
	1. 

![[Screen Shot 2021-12-06 at 8.56.06 PM.png]]

## Queuing

input queuing
output queuing

### buffer management

## packet scheduling
- FCFS
- priority
- round robin
- weighted fair queuing (WFQ)

---

## Network Neutrality

2015 US FCC Order on Protecting and Promoting an Open Internet: three “clear, bright line” rules:

§no blocking … “shall not block lawful content, applications, services, or non-harmful devices, subject to reasonable network management.”

§no throttling … “shall not impair or degrade lawful Internet traffic on the basis of Internet content, application, or service, or use of a non-harmful device, subject to reasonable network management.”

§no paid prioritization. … “shall not engage in paid prioritization”

   

US Telecommunication Act of 1934 and 1996:

•Title II: imposes “common carrier duties” on telecommunications services: reasonable rates, non-discrimination and requires regulation

•Title I: applies to information services:

•no common carrier duties (not regulated)

•but grants FCC authority “… as may be necessary in the execution of its functions”4

---

### Virtual Circuits: signaling protocols

VC: signal packages.


# IP: the Internet Protocol

## Network layer overview: 
1. [[Ch 4. network layer#IP the Internet Protocol|IP Protocol]]
2. [[Ch 4. network layer#hierarchical addressing|ICMP]]
3. [[Ch 4. network layer#Routing algorithms Routing in the Internet|Path selection algorithms]]

![[Screen Shot 2021-12-06 at 7.53.12 PM.png]]

## IP Datagram format

![[Screen Shot 2021-11-29 at 8.55.31 AM.png]]
id : 16bits
flag: 3 bit 
+ ( 001 )b  --> MF(more frag)
	+ ( 000 ) b --> MF(more frag) = 0, i.e. the last frag of the datagram
	+ ( 001 ) b --> MF(more frag) ≠ 0, i.e. not the last frag of the datagram
+ (010)b --> DF (donot frag)
	+ (000)b --> DF = 0
	+ (010)b --> DF = 1
+ (100)b --> 
	+ 

fragment offset (13 bit): < length (16 bits)
+ fragment ONLY times of 8 
+ fragment offest is the begin sequence number divided by 8


## IP addressing

### IP addressing introduction

**1. IP address**: 32-bit identifier (IPv4 )associated with each host or router interface ( A.B.C.D )
> while MAC address (48 bits) has noe hierarchy

- ** dotted-dcimal IP address notation:** (221.1.1.1) --> 11011111.0000001.0000001.00000001

+ Subnet IP/ Subnet ID (A.B.C.x)
+ host IP/ host ID (x.x.x.D)
+ 

**2. interface: ** connection between host/router / physical link
> Ethernet switches
> WiFi base station
+ router typically have multiple interfaces
+ host typically have one or two interfaces; wired ethernet & wireless 802.11

**3. NIC**: network interface fcard  <--> netwrok adapter

### Subnets

**Subnets:**    device interfaces that can physically reach each other ==without passing through an intervening router==
+ flodding storm
	+ broadcasting pkgs in switcher loop

IP address have structure: 
1. Subnet part: the common high order bits
2. host part: the remaining part


**CIDR**
CIDR: Classless InterDomain Routing (pronounced “cider”)
subnet portion of address of arbitrary length
address format: a.b.c.d/x, where x is # bits in subnet portion of address


```shell

192.168.0.  |	0000 0000	--> netIP ()		*	| 	/ 24		
			|	0000 0001							|
			|	0000 0002							|	
			|	...									|
			|	1111 1111	--> broad-cast IP	*	|
uni-cast
multi-cast
broad-cast

* usually the '*' marked two host numbers are preserved for special use in network.
```

### Subnet mask
> https://www.huaweicloud.com/zhishi/ask009.html
> https://www.cnblogs.com/HDK2016/p/14343596.html


192.168.0.1/24
255.255.255.0

### how to get IP?
how does a ___subnet___ gets its own IP AND how does a___ host under that subnet___ gets its own IP?

for host getting IP: 
1. hard-cored by sysadmin in config file (e.g.   /etc/rc.config in UNIX)
2.    [[SCU/CS/Computer Networking/terms#DHCP|DHCP]],  Dynamic Host Configuration Protocol: dynamically get address from as server
		- plug-and-play

### DHCP
DHCP server usually collocated with the router. 
![[Screen Shot 2021-12-06 at 9.35.07 AM.png]]

DHCP running in the network example: (IMPORTANT!! better go check the PowerPoint)

![[Screen Shot 2021-12-06 at 8.14.33 PM.png]]

DHCP offer msg body (partially):
1. yiaddr
2. address of first-hop router for client
3. name and IP address of DNS sever
4. network mask (indicating network versus host portion of address)
5. gateway IP

### hierarchical addressing
#### 1.route aggregation
 using route aggregation, IP stored in routers can be reduced by a great scale. (400 Billion -> 0.5 Million)
 #### 2.more spesific IP ... 


[ICMP](https://www.cloudflare.com/learning/ddos/glossary/internet-control-message-protocol-icmp/): internet control message protocol
- allocates IP addresses, through 5 regional registries (RRs) (who may then allocate to local registries)
- manages DNS root zone, including delegation of individual TLD (.com, .edu , …) management

## Network addressing translation(NAT)

NAT maps `<ip1>:<port1>` on host in the local network to `<ip2>:<port2>` to the one router has. 

>⚠️ NOTICE that `port2` here allocated by the router is to distinguish different hosts on the subnet, and because the number that the router can attribute is limited to $2^{64} = 65535$ , so once the number of pkgs concurrently sent to NAT outnumber $2^{64} = 65535$, there is no alternative but drop the overflowed pkgs. 
>NO solid solution is given to this problem. 

![[Screen Shot 2021-12-06 at 10.07.34 AM.png]]

## IPv6
### tunneling and encapsulation

## QnA
Q. how does an ISP get block of address?
A. ICANN: Internet Corporation for Assigned Names and Numbers http://www.icann.org/
1. allocate IPs through 5 regional registries (RRs)
2. manages DNS root zones


# Routing algorithms & Routing in the Internet
## 👀 overview: 

```sell
algorithms: 								protocols:

link state (dijkstra)			--->		OSPF	
distance vector	(belman-ford)	--->		RIP (Routing Information protocol)
hierarchical routing			--->		BGP
```

#### Graph abstraction:
G = (N, E)
N = set of routers
E = set of links 

cost : 
1. distance
2. delay
3. payload/ thoughput
4. manually allocate
---
## 1. [[0x60 图论#1 Dijkstra| LS (Dijkstra)]] ---> OSPF 

> !! ==every other time intervel==nodes boradcast its table information in order to notice other node of the topology of the network. 
> BUT low efficience for large netwrok, because boradcasting comsuming huge resource of the broadwidth. 

## 2. [[0x60 图论#2 Bellman-Ford|DV (Bellman-Ford)]] ---> RIP
DV advertisement

### DV: link lost chages

link lost changes:
+ node detects local link cost change
+ bad news travels slow

poisoned reverse: 
for each neibour updates, distance value change to infinity before sending to tis src host. 
👉 but this solustion only solved naibour link lost. 

> !!  ==every other 30s== neibouring nodes exchange dv table in order to update the topology of the netwrok. 


### RIP (Routing Information Protocol)
enbeded in BSD-UNIX

up to 16 updates


## 3.  Hierarchical routing ---> BGP
1. aggregate routers into regions --> autonomous system (AS).
2. under same AS same protocol is implemented, quoted as intra-AS protocol (e.g., LS & DV) ; between diff AS there might be diff protocol implementation. 
3. gateway router: as edge of each AS.

iBGP
eBGP

