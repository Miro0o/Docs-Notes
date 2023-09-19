# Port Scan & Port Discovery

[TOC]



## Res



## Intro
Port scanning is the process of connecting to TCP and UDP ports to determine what services and applications are running on the target device. There are 65,535 ports each for both TCP and UDP on each system. Some ports are known to be associated with particular services (for instance, TCP 20 and 21 are the usual ports for the File Transfer Protocol (FTP) service). The first 1,024 are the well- known ports, and most defined services run over ports in this range; accepted services and ports are maintained by 🔗 [IANA](http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml).

![](../../../../../../../Assets/Pics/Screenshot%202023-04-01%20at%205.00.58%20PM.png)
![](../../../../../../../Assets/Pics/Screenshot%202023-04-01%20at%205.01.34%20PM.png)

> Although there are accepted ports for particular services, such as port 80 for web-based traffic, services can be directed to use any port. This option is frequently used to hide particular services, particularly if the service is known to be vulnerable to attack. However, if attackers complete a port scan and do not find an expected service or find it using an unusual port, they will be prompted to investigate further.

The universal port mapping tool, nmap, relies on active stack fingerprinting. Specially crafted packets are sent to the target system, and the response of the OS to those packets allows nmap to identify the OS. In order for nmap to work, at least one listening port must be open, and the operating system must be known and fingerprinted, with a copy of that fingerprint in the local database.

Using nmap for port discovery is very noisy—it will be detected and logged by network security devices. Some points to remember are as follows:

- Attackers and penetration testers focused on stealth will test only the ports that impact the kill chain they are following to their specific target. If they are launching an attack that exploits vulnerabilities in a web server, they will search for targets with port 80 or port 8080 accessible.

- Most port scanners have default lists of ports that are scanned—ensure that you know what is on that list and what has been omitted. Consider both TCP and UDP ports.

- Successful scanning requires a deep knowledge of TCP/IP and related protocols, networking, and how particular tools work. For example, SCTP is an increasingly common protocol on networks, but it is rarely tested on corporate networks.

- Port scanning, even when done slowly, can impact a network. Some older network equipment and equipment from specific vendors will lock when receiving or transmitting a port scan, hence turning a scan into a denial of service attack.

- Tools used to scan a port, particularly nmap, are being extended with regards to functionalities. They can also be used to detect vulnerabilities and exploit simple security holes.



## 👉 nmap



## 👉 netcat

While attackers utilize the proxying application and Tor network, it is also possible to write their own custom network port scanner. The following one-line command can be utilized during penetration testing to identify the list of open ports just by using netcat: `while read r; do nc -v -z $r 1-65535; done < iplist`



## Ref

