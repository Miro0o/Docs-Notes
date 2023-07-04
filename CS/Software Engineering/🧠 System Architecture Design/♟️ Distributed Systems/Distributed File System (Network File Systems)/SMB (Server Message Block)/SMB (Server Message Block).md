# SMB (Server Message Block)

[TOC]



## Res


## Intro
**Server Message Block** (**SMB**) is a communication protocol originally developed in 1983 by Barry A. 
- Feigenbaum at IBM and intended to provide [shared access](https://en.wikipedia.org/wiki/Shared_access "Shared access") to [files](https://en.wikipedia.org/wiki/Computer_file "Computer file") and [printers](https://en.wikipedia.org/wiki/Printer_(computing) "Printer (computing)") across [nodes](https://en.wikipedia.org/wiki/Node_(networking) "Node (networking)") on a network of systems running IBM's [OS/2](https://en.wikipedia.org/wiki/OS/2 "OS/2"). It also provides an authenticated [inter-process communication](https://en.wikipedia.org/wiki/Inter-process_communication "Inter-process communication") (IPC) mechanism. 
- In 1987, [Microsoft](https://en.wikipedia.org/wiki/Microsoft "Microsoft") and [3Com](https://en.wikipedia.org/wiki/3Com "3Com") implemented SMB in [LAN Manager](https://en.wikipedia.org/wiki/LAN_Manager "LAN Manager") for OS/2, at which time SMB used the [NetBIOS](https://en.wikipedia.org/wiki/NetBIOS "NetBIOS") service atop the [NetBIOS Frames](https://en.wikipedia.org/wiki/NetBIOS_Frames "NetBIOS Frames") protocol as its underlying transport. 
- Later, Microsoft implemented SMB in [Windows NT 3.1](https://en.wikipedia.org/wiki/Windows_NT_3.1 "Windows NT 3.1") and has been updating it ever since, adapting it to work with newer underlying transports: [TCP/IP](https://en.wikipedia.org/wiki/TCP/IP "TCP/IP") and [NetBT](https://en.wikipedia.org/wiki/NetBIOS_over_TCP/IP "NetBIOS over TCP/IP"). 
- In 1996, Microsoft published a version of SMB 1.0 with minor modifications under the **Common Internet File System** (**CIFS**[/sɪfs/](https://en.wikipedia.org/wiki/Help:IPA/English "Help:IPA/English")) moniker. CIFS was compatible with even the earliest incarnation of SMB, including [LAN Manager](https://en.wikipedia.org/wiki/LAN_Manager "LAN Manager")'s. It supports symbolic links, hard links, and larger file size, but none of the features of SMB 2.0 and later. Microsoft's proposal, however, remained an [Internet Draft](https://en.wikipedia.org/wiki/Internet_Draft "Internet Draft") and never achieved standard status. Microsoft has since discontinued use of the CIFS moniker but continues developing SMB and making subsequent specifications publicly available
- SMB over [QUIC](https://en.wikipedia.org/wiki/QUIC "QUIC") was introduced in Windows Server 2022. 

SMB implementation consists of two vaguely named [Windows services](https://en.wikipedia.org/wiki/Windows_service "Windows service"): "Server" (ID: `LanmanServer`) and "Workstation" (ID: `LanmanWorkstation`). It uses [NTLM](https://en.wikipedia.org/wiki/NT_LAN_Manager "NT LAN Manager") or [Kerberos](https://en.wikipedia.org/wiki/Kerberos_(protocol) "Kerberos (protocol)") protocols for user authentication.



## Ref
[Server Message Block | Wikipedia]: https://en.wikipedia.org/wiki/Server_Message_Block


