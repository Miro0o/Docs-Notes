# ACL

[TOC]



## Intro

A network access control list (ACL) is made up of rules that either allow access to a computer environment or deny it. In a way, an ACL is like a guest list at an exclusive club. Only those on the list are allowed in the doors. This enables administrators to ensure that, unless the proper credentials are presented by the device, it cannot gain access. 

There are two basic kinds of ACLs:

1. **Filesystem ACLs**: These work as filters, managing access to directories or files. A filesystem ACL gives the operating system instructions as to the users that are allowed to access the system, as well as the privileges they are entitled to once they are inside.
2. **Networking ACLs**: Networking ACLs manage access to a network. To do this, they provide instructions to switches and routers as to the kinds of traffic that are allowed to interface with the network. They also dictate what each user or device can do once they are inside.

When ACLs were first conceived, they worked like [firewalls](https://www.fortinet.com/resources/cyberglossary/how-does-a-firewall-work), blocking access to unwanted entities. While many firewalls have network access control functions, some organizations still use ACLs with technologies such as [virtual private networks (VPNs)](https://www.fortinet.com/resources/cyberglossary/what-is-a-vpn). In this way, an administrator can dictate which kinds of traffic get encrypted and then sent through the secure tunnel of the VPN.



## Res

【ACL技术-1-访问控制列表（基本原理）】 https://www.bilibili.com/video/BV1zy4y1t7Fj/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

【ACL技术-2-基本ACL实验（配合telnet）】 https://www.bilibili.com/video/BV1cB4y1N7kL/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

【ACL技术-3-高级ACL实验（配合telnet）】 https://www.bilibili.com/video/BV1DV411n7WH/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d



## Ref

[What Is a Network Access Control List?]: https://www.fortinet.com/resources/cyberglossary/network-access-control-list
