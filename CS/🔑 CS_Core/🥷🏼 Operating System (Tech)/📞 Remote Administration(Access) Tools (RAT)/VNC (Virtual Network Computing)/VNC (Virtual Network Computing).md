# VNC (Virtual Network Computing)

[TOC]



## Res


## Intro
> 🔗 https://en.wikipedia.org/wiki/Virtual_Network_Computing


Virtual Network Computing (VNC) is a graphical desktop-sharing system that uses the [Remote Frame Buffer protocol (RFB)](https://en.wikipedia.org/wiki/RFB_protocol) to **remotely control another computer**. It transmits the keyboard and mouse input from one computer to another, relaying the graphical-screen updates, over a network.

> VNC and RFB are [registered trademarks](https://en.wikipedia.org/wiki/Registered_trademark "Registered trademark") of [RealVNC](https://en.wikipedia.org/wiki/RealVNC "RealVNC") Ltd. in the US and some other countries.



### Operations
- The VNC [server](https://en.wikipedia.org/wiki/Server_(computing) "Server (computing)") is the program on the machine that shares some screen (and may not be related to a physical display – the server can be ["headless"](https://en.wikipedia.org/wiki/Headless_system "Headless system")), and allows the client to share control of it.
- The VNC [client](https://en.wikipedia.org/wiki/Client_(computing) "Client (computing)") (or viewer) is the program that represents the screen data originating from the server, receives updates from it, and presumably controls it by informing the server of collected local input.
- The VNC [protocol](https://en.wikipedia.org/wiki/Communications_protocol "Communications protocol") ([RFB protocol](https://en.wikipedia.org/wiki/RFB_protocol "RFB protocol")) is very simple, based on transmitting one graphic primitive from server to client ("Put a rectangle of [pixel](https://en.wikipedia.org/wiki/Pixel "Pixel") data at the specified X,Y position") and [event messages](https://en.wikipedia.org/wiki/Event-driven_programming "Event-driven programming") from client to server.


### Security
VNC may be tunneled over an [SSH](https://en.wikipedia.org/wiki/Secure_Shell "Secure Shell") or [VPN](https://en.wikipedia.org/wiki/Virtual_private_network "Virtual private network") connection which would add an extra security layer with stronger encryption. SSH clients are available for most platforms; SSH tunnels can be created from UNIX clients, Microsoft Windows clients, Mac clients (including Mac OS X and [System 7](https://en.wikipedia.org/wiki/System_7 "System 7") and up) – and many others. There are also freeware applications that create instant VPN tunnels between computers.



## Ref

