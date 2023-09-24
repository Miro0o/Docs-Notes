# Pen-testing

[TOC]



## Res
📂 [Pentest wiki](https://github.com/nixawk/pentest-wiki)

↗ [Kill Chain](../../☠️%20Kill%20Chain/Kill%20Chain.md)



## Intro
### Kill-Chain
↗ [Kill Chain](../../☠️%20Kill%20Chain/Kill%20Chain.md)


### Misconceptions of vulnerability scanning (Vscan), penetration testing (Pentest), and red team exercises (RTE)
- **Vulnerability scanning (Vscan)**: It is a process of identifying vulnerabilities or security loopholes in a system or network. One of the misconceptions about Vscan is that it will let you know all of the known vulnerabilities; well, it's not true. Limitations with Vscan are only potential vulnerabilities and it purely depends on the type of scanner that one utilizes; it might also include lots of false positives and, to the business owner, there is no clear vision on whether they are relevant risks or not and which one will be utilized by the attackers first to gain access. 

- **Penetration testing (Pentest)**: It is a process of safely exploiting vulnerabilities without much impact to the existing network or business. There is a lower number of false positives since the testers will try and simulate the exploit. Limitations with the pentest are only currently known, publicly available exploits and mostly these are project-focused testing. We often hear from pentesters during an assessment, "Yay! Got Root"—but we never question: What's next? This could be due to various reasons, such as the project limits you to report the high-risk issues immediately to the client or the client is interested in only one segment of the network and wants you to test that.

- **Red Team Exercise (RTE)**: It is a process of evaluating the effectiveness of an organization to defend against cyber threats and improve its security by any possible means; during an RTE, we can notice multiple ways of achieving project objectives and goals, such as complete coverage of activities with the defined project goal, including phishing, wireless, disk drops (USB, CD, and SSD), and physical penetration testing. The limitations with RTEs are time-bound, pre-defined scenarios and an assumed rather than real environment. Often, the RTE is run with a fully monitored mode for every technique and tactics are executed according to the procedure, but this isn't the case when a real attacker wants to achieve an objective.

Often, all three different testing methodologies refer to the term **hack** or **compromise**. We will hack your network and show you where your weaknesses are; but wait, does the client or business owner understand the term hack or compromise? How do we measure it? What are the criteria? And when do we know that the hack or compromise is complete? All the questions point to only one thing: what's the primary goal?


### Objective-based Penetration Testing
The primary goal of a pentest/RTE is to determine the real risk, differentiating the risk rating from the scanner and giving a business risk value for each asset, along with the brand image of the organization. It's not about whether how much risk they have; rather, it's about how much they are exposed. A threat that has been found does not really constitute a risk and need not be demonstrated



## Ref
