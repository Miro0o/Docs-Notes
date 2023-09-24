# DNS Reconnaissance

[TOC]



## Res
https://www.dnsleaktest.com



## Intro
> Note that DNS information may contain stale or incorrect entries. To minimize inaccurate information, query different source servers and use different tools to cross-validate results. Review results and manually verify any suspect findings.

Once a tester has identified the targets that have an online presence and contain items of interest, the next step is to identify the IP addresses and routes to the target.

DNS reconnaissance is concerned with identifying who owns a particular domain or series of IP addresses (the sort of information gained with whois although this has been completely changed with the General Data Protection Regulation (GDPR) enforcement across Europe from May 2018), the DNS information defining the actual domain names and IP addresses assigned to the target and the route between the penetration tester or the attacker and the final target.

This information gathering is semi-active—some of the information is available from freely available open sources such as DNSstuff.com, while other information is available from third parties such as DNS registrars. Although the registrar may collect IP addresses and data concerning requests made by the attacker, it is rarely provided to the end target. The information that could be directly monitored by the target, such as DNS server logs, is almost never reviewed or retained.

Because the information needed can be queried using a defined systematic and methodical approach, its collection can be automated.



## 👉 The whois command (Post GDPR)
The whois command used to be the first step in identifying an IP address for many years until GDPR was enforced. Formerly, the whois command was used to to query databases that store information on the registered users of an internet resource, such as a domain name or IP address. Depending on the database that is queried, the response to a whois request will provide names, physical addresses, phone numbers, and email addresses (useful in facilitating social engineering attacks), as well as IP addresses and DNS server names. After 25th May 2018, there are no registrant details provided; however, attackers can understand which whois server responds and it retrieves domain data that includes availability, ownership, creation, expiration details, and name servers.



## 👉 nslookup



## 👉 dig


## 👉 Sublist3r
↗ [OSINT/ 👉 Sublist3r](../../../OSINT/OSINT.md#👉%20Sublist3r)



## DNS & IPv4
| Application                  | Description                                                  |
| ---------------------------- | ------------------------------------------------------------ |
| dnsenum,dnsmap, and dnsrecon | These are comprehensive DNS scanners—DNS record enumeration (A, MX, TXT, SOA, wildcard, and so on), subdomain brute-force attacks, Google lookup, reverse lookup, zone transfer, and zone walking. dsnrecon is usually the first choice—it is highly reliable, results are well parsed, and data can be directly imported into the Metasploit framework. |
| dnstracer                    | This determines where a given DNS gets its information from, and follows the chain of DNS servers back to the servers that know the data. |
| dnswalk                      | This DNS debugger checks specified domains for internal consistency and accuracy. |
| fierce                       | This locates non-contiguous IP space and hostnames against specified domains by attempting zone transfers and then attempting brute-force attacks to gain DNS information. |



## DNS & IPv6
The increased size of the addressable address space presents some problems to penetration testers, particularly when using scanners that step through the available address space looking for live servers. However, some features of the IPv6 protocol have simplified discovery, especially the use of ICMPv6 to identify active link-local addresses.

It is important to consider IPv6 when conducting initial scans for the following reasons:
- There's uneven support for IPv6 functionality in testing tools, so the tester must ensure that each tool is validated to determine its performance and accuracy in IPv4, IPv6, and mixed networks.  
- Because IPv6 is a relatively new protocol, the target network may contain misconfigurations that leak important data; the tester must be prepared to recognize and use this information.
- Older network controls (firewalls, IDS, and IPS) may not detect IPv6. In such cases, penetration testers can use IPv6 tunnels to maintain covert communications with the network and exfiltrate the data undetected.

Kali includes several tools developed to take advantage of IPv6 (most comprehensive scanners, such as `nmap`, now support IPv6), some of which are as follows; tools that are particular to IPv6 were largely derived from the **THC-IPv6 Attack Toolkit**.

The following table provides the list of tools that are utilized for reconnaissance of IPv6:

| Application       | Description                                                  |
| ----------------- | ------------------------------------------------------------ |
| dnsdict6          | Enumerates sub-domains to obtain IPv4 and IPv6 addresses (if present) using a brute force search based on a supplied dictionary file or its own internal list. |
| dnsrevenum6       | Performs reverse DNS enumeration given an IPv6 address.      |
| `covert_send6 `   | Sends the content of a file covertly to the target.          |
| `covert_send6d `  | Writes covertly received content to file.                    |
| denial6           | Performs various denial of service attacks on a target.      |
| `detect-new-ip6 ` | Detects new IPv6 addresses joining the local network.        |
| detect_sniffer6   | Tests whether systems on the local LAN are sniffing          |
| Exploit6          | Performs exploits of various CVE-known IPv6 vulnerabilities on the destination |
| fake_dhcps6       | Fake DHCPv6 server                                           |


> 👉 Metasploit can also be utilized for IPv6 host discovery. The `auxiliary/scanner/discovery/ipv6_multicast_ping` module will discover all of the IPv6-enabled machines with the physical (MAC) address

> 👉 THC IPv6 suite `atk6-alive6` will discover alive addresses in the same segment.



## Ref

