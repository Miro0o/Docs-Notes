# Principles of Reliable Data Transfer

[TOC]



## Res
↗ [Error Control](Error%20Control/Error%20Control.md)



## Basics
🔗 【深入浅出计算机网络 - 3.2.3 （1）可靠传输的相关基本概念】 https://www.bilibili.com/video/BV1mG41157Tb/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

==RDT exits on every layer of OIS!==

### Overview
![](../../../../../Assets/Pics/Screenshot%202023-04-15%20at%209.35.42%20AM.png)
![](../../../../../Assets/Pics/Screenshot%202023-04-15%20at%209.37.53%20AM.png)
![](../../../../../Assets/Pics/Screenshot%202023-04-15%20at%209.38.22%20AM.png)


### FSM
![](../../../../../Assets/Pics/Screenshot%202022-11-13%20at%2010.38.37%20AM.png)
<small>FSM is used for RDT demonstration</small>

![](../../../../../Assets/Pics/Screenshot%202023-04-14%20at%2011.49.52%20AM.png)
<small>FSM Legends</small>

🙈 See ↗ [Automaton (FSM)](../../../🧮%20Math%20for%20CS/🦾%20Operations%20Research/COP/Automaton%20(FSM)/Automaton%20(FSM).md) for detailed FSM info.


### 📌 ARQ (Automatic Repeat reQuest)
Control messages allowing the receiver to let the sender know what has been received correctly, and what has been received in error and thus requires repeating --- in a computer network setting, reliable data transfer protocols based on such retransmission are known as **ARQ (Automatic Repeat reQuest)** protocols.

Fundamentally, **three additional protocol capabilities are required in ARQ protocols** to handle the presence of bit errors:

1. **Error detection**. First, a mechanism is needed to allow the receiver to detect when bit errors have occurred. Recall from the previous section that UDP uses the Inter- net checksum field for exactly this purpose. In Chapter 6, we’ll examine error- detection and -correction techniques in greater detail; these techniques allow the receiver to detect and possibly correct packet bit errors. For now, we need only know that these techniques require that extra bits (beyond the bits of original data to be transferred) be sent from the sender to the receiver; these bits will be gath- ered into the packet checksum field of the rdt2.0 data packet.

2. **Receiver feedback**. Since the sender and receiver are typically executing on dif- ferent end systems, possibly separated by thousands of miles, the only way for the sender to learn of the receiver’s view of the world (in this case, whether or not a packet was received correctly) is for the receiver to provide explicit feedback to the sender. The positive (ACK) and negative (NAK) acknowledgment replies in the message-dictation scenario are examples of such feedback. Our rdt2.0 protocol will similarly send ACK and NAK packets back from the receiver to the sender. In principle, these packets need only be one bit long; for example, a 0 value could indicate a NAK and a value of 1 could indicate an ACK.
 
3. **Retransmission**. A packet that is received in error at the receiver will be retrans- mitted by the sender.


### Pipelined RDT (Pipelined Error Correction)

![](../../../../../Assets/Pics/Screenshot%202023-04-15%20at%2010.25.21%20AM.png)



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


![](../../../../../Assets/Pics/Screenshot%202023-04-15%20at%209.57.30%20AM.png)

### rdt 2.2: NAK-free
![](../../../../../Assets/Pics/Screenshot%202022-11-20%20at%2010.32.54%20AM.png)
<small>rdt 2.2 Sender, Receiver fragments</small>


### rdt 3.0: channel with errors and loss
![](../../../../../Assets/Pics/Screenshot%202022-11-20%20at%2010.33.57%20AM.png)
<small>rdt 3.0 Sender</small>


![](../../../../../Assets/Pics/Screenshot%202023-04-15%20at%209.57.41%20AM.png)
![](../../../../../Assets/Pics/Screenshot%202023-04-15%20at%209.58.00%20AM.png)![](../../../../../Assets/Pics/Screenshot%202023-04-15%20at%209.58.21%20AM.png)

![](../../../../../Assets/Pics/Screenshot%202023-04-15%20at%209.44.37%20AM.png)


### SW Utilization
![](../../../../../Assets/Pics/Screenshot%202023-04-15%20at%209.59.19%20AM.png)
![](../../../../../Assets/Pics/Screenshot%202023-04-15%20at%209.59.30%20AM.png)



## 🚴‍♀️ Go-back-N (GBN)
【深入浅出计算机网络 - 3.2.3 （3）可靠传输的实现机制 - 回退N帧协议】 https://www.bilibili.com/video/BV1Lt4y1J7uu/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

![](../../../../../Assets/Pics/Screenshot%202023-04-15%20at%2010.24.37%20AM.png)


![](../../../../../Assets/Pics/Screenshot%202023-04-15%20at%2010.26.51%20AM.png)

![](../../../../../Assets/Pics/Screenshot%202023-04-15%20at%2010.31.23%20AM.png)
![](../../../../../Assets/Pics/Screenshot%202023-04-15%20at%2010.31.03%20AM.png)
![](../../../../../Assets/Pics/Screenshot%202023-04-15%20at%2010.32.33%20AM.png)
![](../../../../../Assets/Pics/Screenshot%202023-04-15%20at%2010.41.36%20AM.png)



## 🚴‍♀️ Selective Repeat (SR)
【深入浅出计算机网络 - 3.2.3 （4）可靠传输的实现机制 - 选择重传协议】 https://www.bilibili.com/video/BV1aV4y1H7yc/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

![](../../../../../Assets/Pics/Screenshot%202023-04-15%20at%2010.45.04%20AM.png)

![](../../../../../Assets/Pics/Screenshot%202023-04-15%20at%2010.48.29%20AM.png)
![](../../../../../Assets/Pics/Screenshot%202023-04-15%20at%2010.49.49%20AM.png)



## Ref

