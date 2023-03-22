# IPsec (Internet Protocol Security)

[TOC]



> 💡 IPsec is mostly replaced by [TLS](../../0x04%20Transport%20Layer/SSL%20&%20TLS/TLS/TLS.md) 
## Res


## Intro
> 🔗 https://www.techtarget.com/searchsecurity/definition/IPsec-Internet-Protocol-Security

### What is IPsec (Internet Protocol Security)?
**IPsec (Internet Protocol Security)** is a suite of protocols and algorithms for securing data transmitted over the internet or any public network. The Internet Engineering Task Force, or IETF, developed the IPsec protocols in the mid-1990s to provide security at the IP layer through authentication and encryption of IP [network packets](https://www.techtarget.com/searchnetworking/definition/packet).

IPsec originally defined two protocols for securing IP packets:
1. **Authentication Header (AH)**, provides data integrity and [anti-replay services](https://www.techtarget.com/searchnetworking/definition/anti-replay-protocol)
2. **Encapsulating Security Payload (ESP)**, encrypts and authenticates data

The IPsec suite also includes **Internet Key Exchange ([IKE](https://www.techtarget.com/searchsecurity/definition/Internet-Key-Exchange))**, which is used to generate shared security keys to establish a **security association (SA)**. SAs are needed for the encryption and decryption processes to negotiate a security level between two entities. A special router or firewall that sits between two networks usually handles the SA negotiation process.


### Key IPsec Protocols
- **IP AH.** AH is specified in RFC 4302. It provides data integrity and transport protection services. AH was designed to be inserted into an IP packet to add authentication data and protect the contents from modification.

- **IP ESP.** Specified in RFC 4303, ESP provides authentication, integrity and confidentiality through encryption of IP packets.

- **IKE.** Defined in RFC 7296, IKE is a protocol that enables two systems or devices to establish a secure communication channel over an untrusted network. The protocol uses a series of key exchanges to create a secure tunnel between a client and a server through which they can send encrypted traffic. The security of the tunnel is based on the Diffie-Hellman key exchange.

- **Internet Security Association and Key Management Protocol (ISAKMP).** ISAKMP is specified as part of the IKE protocol and RFC 7296. It is a framework for key establishment, authentication and negotiation of an SA for a secure exchange of packets at the IP layer. In other words, ISAKMP defines the security parameters for how two systems, or hosts, communicate with each other. Each SA defines a connection in one direction, from one host to another. The SA includes all attributes of the connection, including the cryptographic algorithm, the IPsec mode, the encryption key and any other parameters related to data transmission over the connection.

IPsec uses, or is used by, many other protocols, such as [digital signature](https://www.techtarget.com/searchsecurity/definition/digital-signature) algorithms and most protocols outlined in the IPsec and IKE Document Roadmap, or RFC 6071.


### A next step: Comparing IPsec VPN vs. SSL VPN
A Secure Socket Layer ([SSL](https://www.techtarget.com/searchsecurity/definition/Secure-Sockets-Layer-SSL)) VPN is another approach to securing a public network connection. The two can be used together or individually depending on the circumstances and security requirements.

With an IPsec VPN, IP packets are protected as they travel to and from the IPsec gateway at the edge of a private network and remote hosts and networks. An SSL VPN protects traffic as it moves between remote users and an SSL gateway. IPsec VPNs support all IP-based applications, while SSL VPNs only support browser-based applications, though they can support other applications with custom development.

_Learn more about [how IPsec VPNs and SSL VPNs differ](https://www.techtarget.com/searchsecurity/feature/Tunnel-vision-Choosing-a-VPN-SSL-VPN-vs-IPSec-VPN)_ _in terms of authentication and access control, defending against attacks and client security. See what is best for your organization and where one type works best over the other._


## How Does IPsec Works?
#TODO 



## Ref
[IPsec (Internet Protocol Security)]: https://www.techtarget.com/searchsecurity/definition/IPsec-Internet-Protocol-Security

