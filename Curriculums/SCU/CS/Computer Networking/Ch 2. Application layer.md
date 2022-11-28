+ outline
	+ 2.2 Web and HTTP
	+ 2.5 DNS

---

# 2.1  Application architectures
+ possible structure of application:
	+ client-server
	+ peer-to-peer (P2P)
		+ server module
		+ client module
+ process communicating
	+ IPC, inter-process communication
		+ SHM, shared memory 	
			+ 
		+ F-S
		+ Socket
+ tributes required:
	+ date integrity
		+ 100 %
		+ not so demanding
+ Securing TCP
	+ SSL
	+ hash
		+ md5
		+ SHA
		
# 2.2 Web and HTTP
# 2.3 FTP
+ connecting 2 channels , one for instruction (21 ), one for file trasfer (20)
+  
# 2.4 electronic mail (SMTP <-->  POP3/ IMAP/HTTP)
		
# 2.5 DNS
> [Domain name](https://www.cnblogs.com/blockcipher/p/3355532.html) : case insensitive     
> 
Domain Name System (DNS):
§ distributed database implemented in hierarchy of many name servers
§ application-layer protocol: hosts, DNS servers communicate to resolve names (address/name translation)
• note: core Internet function, implemented as application-layer protocol
• complexity at network’s “edge”

+ **architecherue** 
	+ root server (13)
		+ DNSSEC – provides security (authentication, message integrity)
		+ ICANN (Internet Corporation for Assigned Names and Numbers) manages root DNS domain
	+  TLD server (~ 1500)
		+   authoritative servers (4~5 hunderd million)
	+ 👉 local DNS server 
		+ 🤔 balancer
			+ round-robin 
			+ serve as a cache server. it contains a cached lists. whenever an request is demand, local DNS server will first check its cache: if the requried IP is up-to-date, it return this IP instead of require root DNS server. 
+  **DNS name resolution:**
	+  recursive query (out of date)
	+  iterated query
+ ** DNS records**
	> DNS: distributed database storing** Resource Records (RR)**

	+ types:
		+ A
			+ hostname <--> IP add
		+ CNAME
			+ alias hostname <--> 'canonical' hostname
		+ NS
			+ domain <--> authoritative hostname
		+ MX
			+ value is name of SMTP mail server associated with name

+ **DNS security **
	+ DDoS
		+ hacker capitalizes zillions of 'zombie node ' to send scrIP-rigged packages to server saimutaineously, server send back the package to the target host. 
		+ requst package is significantly small campared to the return package. 
	+ Sproofing

# 2.6 P2P applications
+ basics
> http://ipr.mofcom.gov.cn/article/gjxw/gfgd/202011/1956770.html
+ Gen 1
	+ e.g. 海盗湾
	+ bbs torrnet
	+ centralized  BT tracker
	+ ![[IMG_0379.heic]]
+ Gen 2


# 2.7 socket programming with UCP/TCP