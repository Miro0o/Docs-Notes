# Kill Chain

[TOC]



## Res
### Related Topics
↗ [Pen-testing](../🥇%20Best%20Practice/💉%20Pen-testing/Pen-testing.md)
↗ [Reverse Engineering & System & Binary](../🥇%20Best%20Practice/🪆%20Reverse%20Engineering%20&%20System%20&%20Binary/Reverse%20Engineering%20&%20System%20&%20Binary.md)
↗ [Forensics](../🥇%20Best%20Practice/Forensics/Forensics.md)
↗ [OSINT](../🥇%20Best%20Practice/OSINT/OSINT.md)
↗ [Security Audit & Security Audit Trail](../🥇%20Best%20Practice/Security%20Audit%20&%20Security%20Audit%20Trail/Security%20Audit%20&%20Security%20Audit%20Trail.md)
↗ [Social Engineering & Physical Security](../🥇%20Best%20Practice/Social%20Engineering%20&%20Physical%20Security/Social%20Engineering%20&%20Physical%20Security.md)



## Intro
> 💡
> The conception of 'kill chain' was coined against scenarios in ↗ [Pen-testing](../🥇%20Best%20Practice/💉%20Pen-testing/Pen-testing.md). Here in this section of notes i extend it to a broader scope covering all tools used in security activities. 

In 2009, Mike Cloppert of Lockheed Martin CERT introduced the concept that is now known as the **attacker kill chain**. This includes the steps taken by an adversary when they are attacking a network. It does not always proceed in a linear flow as some steps may occur in parallel. Multiple attacks may be launched over time at the same target, and overlapping stages may occur at the same time.

A typical kill chain of an attacker can be described as follows:
- **Explore or reconnaissance phase**: The _adage, reconnaissance time_ is _never wasted time_, adopted by most military organizations, acknowledges that it is better to learn as much as possible about an enemy before engaging them. For the same reason, attackers will conduct extensive reconnaissance of a target before attacking. In fact, it is estimated that at least 70 percent of the work effort of a penetration test or an attack is spent conducting reconnaissance! Generally, they will employ two types of reconnaissance:
	- **Passive**: This does not directly interact with the target in a hostile manner. For example, the attacker will review the publicly available website(s), assess online media (especially social media sites), and attempt to determine the **attack surface** of the target. One particular task will be to generate a list of past and current employee names. These names will form the basis of attempts to brute force or guess passwords. They will also be used in social engineering attacks. **This type of reconnaissance is difficult, if not impossible, to distinguish from the behavior of regular users.**
	- **Active**: This can be detected by the target but it can be difficult to distinguish most online organizations' faces from the regular backgrounds. Activities occurring during active reconnaissance include physical visits to target premises, port scanning, and remote vulnerability scanning.

- **Delivery phase**: Delivery is the selection and development of the weapon that will be used to complete the exploit during the attack. The exact weapon chosen will depend on the attacker's intent as well as the route of delivery (for example, across the network, via wireless, or through a web- based service). The impact of the delivery phase will be examined in the second half of this book.

- **Exploit or compromise phase**: This is the point when a particular exploit is successfully applied, allowing attackers to reach their objective. The compromise may have occurred in a single phase (for example, a known operating system vulnerability was exploited using a buffer overflow), or it may have been a multiphase compromise (for example, an attacker physically accessed premises to steal a corporate phone book. The names were used to create lists for brute force attacks against a portal logon. In addition, emails were sent to all employees to click on an embedded link to download a crafted PDF file that compromised their computers). Multiphase attacks are the norm when a malicious attacker targets a specific enterprise.

- **Achieve phase – Action on the Objective**: This is frequently, and incorrectly, referred to as the exfiltration phase because there is a focus on perceiving attacks solely as a route to steal sensitive data (such as login information, personal information, and financial information); it is common for an attacker to have a different objective. For example, a business may wish to cause a denial of service in their competitor's network to drive customers to their own website. Therefore, this phase must focus on the many possible actions of an attacker. One of the most common exploit activity occurs when the attackers attempt to improve their access privileges to the highest possible level (**vertical escalation**) and to compromise as many accounts as possible (**horizontal escalation**).  

- **Achieve phase – Persistence**: If there is value in compromising a network or system, then that value can likely be increased if there is persistent access. This allows attackers to maintain communications with a compromised system. From a defender's point of view, this is the part of the kill chain that is usually the easiest to detect.



## Ref

