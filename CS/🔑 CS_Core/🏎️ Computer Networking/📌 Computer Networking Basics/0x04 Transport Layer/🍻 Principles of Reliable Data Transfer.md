# Principles of Reliable Data Transfer

==RDT exits on every layer of OIS!==



[TOC]



🔗 【深入浅出计算机网络 - 3.2.3 （1）可靠传输的相关基本概念】 https://www.bilibili.com/video/BV1mG41157Tb/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d



## FSM
![](../../../../../Assets/Pics/Screenshot%202022-11-13%20at%2010.38.37%20AM.png)
<small>FSM is used for RDT demonstration</small>

🙈 See [Automaton.md](../../../🧮 Math/Operations Research/COP/Automaton/Automaton.md) for detailed FSM info.



## 🚴‍♀️ Stop-and-Wait (SW)

🔗【深入浅出计算机网络 - 3.2.3 （2）可靠传输的实现机制 - 停止-等待协议】 https://www.bilibili.com/video/BV1WG4y167Gr/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d



### rdt 1.0: reliable transfer over reliable channel
![](../../../../../Assets/Pics/Screenshot%202022-11-20%20at%2010.27.32%20AM.png)

### rdt 2.0: channel with bit errors
![](../../../../../Assets/Pics/Screenshot%202022-11-20%20at%2010.29.42%20AM.png)
<small>rdt 2.0 corrupted packet scenario</small>

### rdt 2.1: handling garbled ack/nak

![](../../../../../Assets/Pics/Screenshot%202022-11-20%20at%2010.30.10%20AM.png)
<small>rdt 2.1 Sender, handling garbled ACK/NAKs</small>

![](../../../../../Assets/Pics/Screenshot%202022-11-20%20at%2010.30.20%20AM.png)
<small>rdt 2.1 Reseiver, handling garbled ACK/NAKs</small>



### rdt 2.2: NAK-free

![](../../../../../Assets/Pics/Screenshot%202022-11-20%20at%2010.32.54%20AM.png)
<small>rdt 2.2 Sender, Receiver fragments</small>

### rdt 3.0: channel with errors and loss

![](../../../../../Assets/Pics/Screenshot%202022-11-20%20at%2010.33.57%20AM.png)
<small>rdt 3.0 Sender</small>



## 🚴‍♀️ Go-back-N (GBN)



## 🚴‍♀️ Selective Repeat (SR)

