# FAQs

[TOC]



## 👉 what does "TCP segment of a reassembled PDU" mean?

It means that Wireshark thinks the packet in question contains part of a packet (PDU - "Protocol Data Unit") for a protocol that runs on top of TCP.

If the reassembly is successful, the TCP segment containing the last part of the packet will show the packet.

The reassembly might fail if some TCP segments are missing.


[Wireshark-users: Re: 「Wireshark-users」 what does "TCP segment of a reassembled PDU" mean?]: https://www.wireshark.org/lists/wireshark-users/200805/msg00206.html

