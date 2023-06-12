# Switched Local Area Networks

[TOC]



## Res
↗ [Switched Network Basics](../📌%20Switched%20Network%20Basics/Switched%20Network%20Basics.md)



## Intro
![](../../../../../../Assets/Pics/Screenshot%202023-05-31%20at%209.40.19%20AM.png)



## Link-Layer Switches
↗ [Link Layer (Tier-2) Switches](../📌%20Switched%20Network%20Basics/Link%20Layer%20Network%20Devices/Link%20Layer%20(Tier-2)%20Switches/Link%20Layer%20(Tier-2)%20Switches.md)



## Broadcast Channels on Switched LAN
### IEEE 802 Family
↗ [IEEE 802 Family](../Switched%20Network%20Channels/Broadcast%20Channels/IEEE%20802%20Family/IEEE%20802%20Family.md)


### Ethernet (802.3)
↗ [Ethernet (802.3)](../Switched%20Network%20Channels/Broadcast%20Channels/IEEE%20802%20Family/Ethernet%20(802.3)/Ethernet%20(802.3).md)


### WLAN & WiFi
↗ [WLAN & WiFi (802.11)](../Switched%20Network%20Channels/Broadcast%20Channels/IEEE%20802%20Family/WLAN%20&%20WiFi%20(802.11)/WLAN%20&%20WiFi%20(802.11).md)



## 🧐 Link Virtualization: A Network as a Link Layer
Because this chapter concerns link-layer protocols, and given that we’re now nearing the chapter’s end, let’s reflect on how our understanding of the term link has evolved. We began this chapter by viewing the link as a physical wire connecting two communicating hosts. In studying multiple access protocols, we saw that multiple hosts could be connected by a shared wire and that the “wire” connecting the hosts could be radio spectra or other media. This led us to consider the link a bit more abstractly as a **channel**, rather than as a **wire**. In our study of Ethernet LANs (Figure 6.15), we saw that the interconnecting media could actually be a rather complex switched infrastructure. Throughout this evolution, however, the hosts themselves maintained the view that the interconnecting medium was simply a link-layer channel connecting two or more hosts.

> We saw, for example, that an Ethernet host can be blissfully unaware of whether it is connected to other LAN hosts by a single short LAN segment (Figure 6.17) or by a geographically dispersed switched LAN (Figure 6.15) or by a VLAN (Figure 6.26).

In the case of a **dialup modem connection** between two hosts, the link connecting the two hosts is actually the telephone network -- a logically separate, global telecommunications network with its own switches, links, and protocol stacks for data transfer and signaling. From the Internet link-layer point of view, however, the dial-up connection through the telephone network is viewed as a simple “wire.” In this sense, the Internet virtualizes the telephone network, viewing the telephone network as a link-layer technology providing link-layer connectivity between two Internet hosts.

> You may recall from our discussion of overlay networks in Chapter 2 that an overlay network similarly views the Internet as a means for providing connectivity between overlay nodes, seeking to overlay the Internet in the same way that the Internet overlays the telephone network.

> Frame-relay and ATM networks can also be used to interconnect IP devices, though they represent a slightly older (but still deployed) technology and will not be covered here; see the very readable book [Goralski 1999] for details



## Link Layer Network Virtualization
### Drawbacks in Traditional Link Layer Networks
1. L**ack of traffic isolation**. Although the hierarchy localizes group traffic to within a single switch, broadcast traffic (e.g., frames carrying ARP and DHCP messages or frames whose destination has not yet been learned by a self-learning switch) must still traverse the entire institutional network. Limiting the scope of such broadcast traffic would improve LAN performance. Perhaps more importantly, it also may be desirable to limit LAN broadcast traffic for security/privacy reasons. For example, if one group contains the company’s executive management team and another group contains disgruntled employees running Wireshark packet sniffers, the network manager may well prefer that the executives’ traffic never even reaches employee hosts. This type of isolation could be provided by replacing the center switch in Figure 6.15 with a router. We’ll see shortly that this isolation also can be achieved via a switched (layer 2) solution.
2. **Inefficient use of switches**. If instead of three groups, the institution had 10 groups, then 10 first-level switches would be required. If each group were small, say less than 10 people, then a single 96-port switch would likely be large enough to accommodate everyone, but this single switch would not provide traffic isolation.
3. **Managing users**. If an employee moves between groups, the physical cabling must be changed to connect the employee to a different switch in Figure 6.15. Employees belonging to two groups make the problem even harder.


### VLAN
↗ [VLAN](../../../👰🏻‍♂️%20Network%20Virtualization/VLAN/VLAN.md)



## Ref

