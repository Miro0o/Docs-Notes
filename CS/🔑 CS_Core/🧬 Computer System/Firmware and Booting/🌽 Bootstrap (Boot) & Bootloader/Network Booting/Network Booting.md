# Network Booting

[TOC]



## Res


## Intro
Most computers are also capable of booting over a [computer network](https://en.wikipedia.org/wiki/Computer_network "Computer network"). In this scenario, the operating system is stored on the disk of a [server](https://en.wikipedia.org/wiki/Server_(computing) "Server (computing)"), and certain parts of it are transferred to the client using a simple protocol such as the [Trivial File Transfer Protocol](https://en.wikipedia.org/wiki/Trivial_File_Transfer_Protocol "Trivial File Transfer Protocol") (TFTP). After these parts have been transferred, the operating system takes over the control of the booting process.

As with the second-stage boot loader, network booting begins by using **generic network access methods** provided by the **network interface's boot ROM**, which typically contains a **[Preboot Execution Environment](https://en.wikipedia.org/wiki/Preboot_Execution_Environment "Preboot Execution Environment") (PXE) image.** No drivers are required, but the system functionality is limited until the operating system kernel and drivers are transferred and started. As a result, once the ROM-based booting has completed it is entirely possible to network boot into an operating system that itself does not have the ability to use the network interface.



## Ref

