# Stealth scanning

[TOC]

## Overview

When employing stealth to support reconnaissance, a tester mimicking the actions of a hacker will do the following:

- Camouflage tool signatures to avoid detection and triggering an alarm Hide the attack within legitimate traffic
- Modify the attack to hide the source and type of traffic
- Make the attack invisible using nonstandard traffic types or encryption

Stealth scanning techniques can include some or all of the following:

- Adjusting source IP stack and tool identification settings
- Modifying packet parameters (`nmap`)
- Using proxies with anonymity networks (ProxyChains and the Tor network)



## Adjusting source IP stack and tool identification settings

Before the penetration tester (or the attacker) begins testing, we must ensure that all unnecessary services on Kali are disabled or turned off.

### DHCP

For example, if the local DHCP daemon is enabled and is not required, it is possible for the DHCP to interact with the target system, which could be logged and send alarms to the target's administrators.

### Identifying sequence

Some commercial and open source tools (for example, the Metasploit framework) tag their packets with an identifying sequence. This can trigger certain intrusion detection system.

to test tags:

- Use dummy VM. Compare system logs to identify tagging trace.
- Analyze traffic, like by using Wireshark. 

## Modifying packet parameters

When attempting to minimize detection, some stealth techniques to avoid detection and subsequent alarms include the following:

- Attackers approach the target with a goal in mind and send the minimum number of packets needed to determine the objective. For example, if you wish to confirm the presence of a web host, you first need to determine whether port 80, the default port for web-based services, is open.

- Avoid scans that may connect with the target system and leak data. Do not ping the target or use **synchronize** (**SYN**) and non-conventional packet scans, such as **acknowledge** (**ACK**), **finished** (**FIN**), and **reset** (**RST**) packets.

- Randomize or spoof packet settings, such as the source IP and port address, and the MAC address.
- Adjust the timing to slow the arrival of packets at the target site.
- Change the packet size by fragmenting packets or appending random data to confuse packet inspection devices.

### Nmap

↗️ [Nmap Proj](../../../../../🔑 CS_Core/🥷🏼 OS/Linux/🪓 Linux Softwares/🌐 Network Management/Nmap Proj/Nmap Proj.md) 



## Using proxies with anonymity networks

### Tor

Tor (www.torproject.org) is an open source implementation of the third-generation onion routing that provides free access to an anonymous proxy network. Onion routing enables online anonymity by encrypting user traffic and then transmitting it through a series of onion routers. 

↗️ [Tor](../../../../../🔑 CS_Core/🏎️ Networking/📌 Basics/0x02 Application Layer/Dark web/Tor/Tor.md) 



### Proxy

↗️ [Proxy](../../../../../🔑 CS_Core/🏎️ Networking/Proxy/Proxy.md) 

#### Privoxy

a noncaching web proxy.

#### proxy chain

edit file `/etc/proxychains.conf ` 

Proxy servers may be down, or they may be experiencing a heavy load (causing slow or latent connections); if this occurs, a defined or strict ProxyChain will fail because an expected link is missing. Therefore, disable the use of `strict_chain` and enable `dynamic_chain`, which ensures that the connection will be routed.

Open proxies can be easily found online (an example would be https://www.proxynova.com/proxy-server-list/) and added to the proxychains.conf file. Testers can take advantage of this to further obfuscate their identity.





