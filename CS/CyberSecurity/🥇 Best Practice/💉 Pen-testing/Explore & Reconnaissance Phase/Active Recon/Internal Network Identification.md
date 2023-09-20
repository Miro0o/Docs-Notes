# Internal Network Identification

[TOC]



## Locating network shares

### smbclient

One of the oldest attacks that penetration testers these days forget is the NETBIOS null session, which will allow them to enumerate all of the network shares: `smbclient -I TargetIP -L administrator -N -u`



### enum4linux


