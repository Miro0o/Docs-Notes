# Internal Network Identification

[TOC]



## DHCP sniffing

The **Dynamic Host Configuration Protocol** (**DHCP**) is a service that dynamically assigns an IP address to the hosts on the network. 

This protocol operates at the MAC sub layer of the Data-Link layer of the TCP/IP protocol stack. 

Upon selection of auto-configuration, a broadcast query will be sent to the DHCP servers and when a response is received from the DHCP server, a broadcast query is sent by the client to the DHCP server requesting required information. The server will now assign an IP address to the system and other configuration parameters such as the **subnet mask**, **DNS**, and the **default gateway**.

We will now see traffic on **DNS**, **NBNS**, **BROWSER**, and other protocols that might potentially reveal hostnames, **VLAN** information, domains, and active subnets in the network.



## ifconfig

ifconfig returns DHCP configured information of the host. 

- `ine`t: The IP information obtained by the DHCP server should provide us with at least one active subnet which can be utilized to identify the list of live systems and services through different scanning techniques.
- `netmask`: This information can be utilized to calculate the subnet ranges. From the previous screenshot, we have `255.255.240.0`, which means CIDR is /20 and potentially we can expect `4094` hosts on the same subnet.
- **Default gateway**: The IP information of the gateway will provide the opportunity to ping other similar gateway IP's. For example, if your default gateway IP is `192.168.1.1` by using ping scans attackers may be able to enumerate other similar IPs such as `192.168.2.1`, `192.168.3.1`, and so on.
-  **Other IP address**: DNS information can be obtained by accessing the `/etc/resolv.conf` file. The IP addresses in this file are commonly addressed in all of the subnets and domain information will also be automatically available in the same file.



## ARP broadcasting

### nmap



### arp-scan



## SMB session exploitation (windows host)

### nmap

```shell
nmap --script smb-enum-users.nse -p445 <host>
```



### Metasploitable3



## Locating network shares

### smbclient

One of the oldest attacks that penetration testers these days forget is the NETBIOS null session, which will allow them to enumerate all of the network shares: `smbclient -I TargetIP -L administrator -N -u`



### enum4linux



## Reconnaissance of active directory domain servers

### rpcclient

