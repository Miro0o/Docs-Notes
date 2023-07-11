# aria2

[TOC]



## Res
🏠 https://aria2.github.io



## Intro
aria2 is a **lightweight** multi-protocol & multi-source command-line **download utility**. It supports **HTTP/HTTPS**, **FTP**, **SFTP**, **BitTorrent** and **Metalink**. aria2 can be manipulated via built-in **JSON-RPC** and **XML-RPC** interfaces.

### Features
- **Multi-Connection Download**. aria2 can download a file from multiple sources/protocols and tries to utilize your maximum download bandwidth. Really speeds up your download experience.
- **Lightweight**. aria2 doesn’t require much memory and CPU time. When disk cache is off, the physical memory usage is typically 4MiB (normal HTTP/FTP downloads) to 9MiB (BitTorrent downloads). CPU usage in BitTorrent with download speed of 2.8MiB/sec is around 6%.
- **Fully Featured BitTorrent Client**. All features you want in BitTorrent client are available: DHT, PEX, Encryption, Magnet URI, Web-Seeding, Selective Downloads, Local Peer Discovery and UDP tracker.
- **Metalink Enabled**. aria2 supports [The Metalink Download Description Format](http://tools.ietf.org/html/rfc5854) (aka Metalink v4), Metalink version 3 and [Metalink/HTTP](http://tools.ietf.org/html/rfc6249). Metalink offers the file verification, HTTP/FTP/SFTP/BitTorrent integration and the various configurations for language, location, OS, etc.
- **Remote Control**. aria2 supports RPC interface to control the aria2 process. The supported interfaces are JSON-RPC (over HTTP and WebSocket) and XML-RPC.



## Ref
