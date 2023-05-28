# Systems on a Chip (SOCs)

[TOC]



## Res


## Intro
Systems on a chip (SOCs) are distinguished from microcontrollers by their complexity and increased on-chip resources.

- Microcontrollers often require supporting circuits such as signal processors, decoders, and signal converters, to name only a few.

A system on a chip is **a single piece of silicon** that contains all circuits required to deliver a set of functions. A system on a chip can even **consist of more than one processor**. These loosely coupled processors do not necessarily share the same clock or memory space. The individual processor functions can be specialized to the extent that they are provided with ISAs designed specifically for efficient programming in a particular application domain. 

> For example, an Internet router may have several RISC processors that handle communications traffic and a CISC processor for configuration and management of the router itself.

Although microcontroller memory is usually measured in kilobytes, SOCs can include memory on the order of megabytes. With their larger memories, SOCs accommodate full-featured **real-time operating systems**. The great advantage of SOCs is that they are faster, smaller, and more reliable, and they consume less power than the several chips they replace.


### off-the-self SOCs 🆚 Costumization of SOCs
Although there are many **off-the-shelf SOCs** available, **customization** is sometimes required to support a particular application.

Rather than absorb the cost of designing an SOC from scratch, a **semicustom chip** may be assembled from **intellectual property (IP) circuits** licensed from companies that specialize in creating and testing circuit designs. Licensed IP module designs are combined with customized circuits to produce a **circuit mask**. The completed mask is subsequently sent to a circuit fabrication facility (a fab) to be etched in silicon. This process is very expensive. Mask costs are now approaching $1 million (US). The economic benefits of this approach must therefore be considered carefully. If a standard SOC provides the same functionality -- even with lesser performance -- the $1 million expenditure is not justifiable. We return to this idea in a later section.


## Ref

