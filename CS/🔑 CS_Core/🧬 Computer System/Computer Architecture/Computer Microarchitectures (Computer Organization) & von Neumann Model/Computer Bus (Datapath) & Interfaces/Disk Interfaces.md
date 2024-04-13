# Disk Interfaces

[TOC]


## Res


## Intro
 Disk interface
	+ IDE (Iintegrated Drive Electronics)
		+ variant of IDE --- **ATA** ()
		+ 2 IDE ports --- primary prot & secondary port
		+ each port support 2 disk
	+ SATA
	+ SCSI
	+ SAS (series attached scis)

SCSI (pronounced “scuzzy”) is one of the most important and enduring I/O interfaces. It has been around since 1981, when it set standards for connecting and transferring data between a computer and an I/O device. Although it is used most frequently for hard disk drives and older tape drives, it can be used with other I/O devices, such as scanners. SCSI is technically available in a variety of different interfaces, including parallel and serial attached. Serial-attached SCSI (SAS) is an evolution of parallel SCSI, in which the disk controllers are linked directly to the disk drives, which enables up to 128 different devices simultaneously. SCSI is fast, has a wide range of applications, has great scalability, is better for storing and moving large amounts of data, and is reliable. It is, however, more expensive than other interfaces, and because there are so many different types of SCSI interfaces, it can get confusing.


The ATA interface is based on IBM’s PC ISA bus. ATA is often used to connect hard disk drives, CD drives, and other similar peripherals and is the least expensive of the hard disk interfaces. The main disadvantages of the ATA interface are that only one device on the cable can read/write at a time and that a limited cable length is allowed for each device (typically 18 inches). However, the low price and ease of setup made this interface very popular. Parallel ATA (PATA) is actually the same as ATA; the term PATA was introduced to differentiate parallel ATA from serial ATA (SATA). ATA allowed for data to be sent 16 bits at a time through a single 16-bit connection that was used for data traveling in both directions.

Today, the majority of computers are switching from ATA and SCSI to SATA disk drives. Serial ATA is a bit-serial interface and the most common interface for all but enterprise hard disk drives. Bit-serial interfaces typically use one data/control cable to connect a device to a computer, meaning data are sent one bit at a time down a single connection in each direction; however, there is a separate connection for data going into and out of the device. Although it might seem faster to send 16 bits in parallel, SATA is faster than the older ATA, basically because of the transfer speeds each can reach: ATA transfers data up to 133 megabytes per second, whereas SATA interfaces can reach up to 600 megabytes per second, depending on the actual interface being used. Serial and parallel modes are discussed in the next section.



## Ref

