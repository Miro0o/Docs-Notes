# Social Engineering & Physical Security

[TOC]



## Res
↗ [Social Engineering Tools](../../☠️%20Kill%20Chain/Social%20Engineering%20Tools/Social%20Engineering%20Tools.md)
↗ [Physical Security](../../Physical%20Security/Physical%20Security.md)

🔗 [social-engineer.org](https://www.social-engineer.org)

This is an online resource for security professionals, adversarial simulators (pentesters), as well as enthusiasts. However, you may be asking, “What is Social Engineering?” It’s a blend of science, psychology and art. And, while it is amazing and complex, it is also very simple.

We define social engineering as,  “*Any act that influences a person to take an action that may or may not be in their best interest*” (Christopher Hadnagy, *Social Engineering: The Science of Human Hacking*. 2nd ed. Hoboken, NJ: Wiley Publishing, 2018). We define it in very broad and general terms because we feel that social engineering is not always negative. It can also encompass how we communicate with our parents, therapists, children, spouses, and others.



## Intro
Social engineering is the art of extracting information from humans. It is a type of attack that has made great progress in recent years by exploiting behavior, and by finding the weaknesses in given circumstances and conditions. This attack can be effective when a human is tricked into providing physical access to their system. It is the single most successful attack vector used during red teaming exercises, penetration testing, or an actual attack. The success of a social engineering attacks relies on two key factors:
- The knowledge that is gained during the reconnaissance phase. The attacker must know the names and usernames associated with the target; more importantly, the attacker must understand the concerns of the users on the network.

- Understanding how to apply this knowledge to convince potential targets to activate the attack by impersonating, talking to them over the phone, inquiring about them, clicking on a link, or executing a program. 

To support SET's social engineering attacks, the following general implementation practices will be described:
- Hiding malicious executables and obfuscating the attacker's URL
- Escalating an attack using DNS redirection  
- Gaining access to the system and network through USB


## Methodology & Attack Methods
### 1️⃣ Technology-based
- Email phishing: Attacks that utilize the email medium to harvest information or exploit a known software vulnerability in the victim's system are referred to as email phishing.

- Baiting: This is a technique that's used to embed a known vulnerability and create a backdoor, to achieve the objective by utilizing USB sticks and compact disks. Baiting focuses more on exploiting the human curiosity factor through the use of physical media. Attackers can create a Trojan that will provide backdoor access to the system either by utilizing the autorun feature, or when a user clicks to open the files inside the drive.

- Wi-Fi phishing: Penetration testers can utilize this technique to harvest usernames and passwords by setting up a fake Wi-Fi network, similar to the targeted company. For example, the attackers could target XYZ company by setting the SSID in their Wi-Fi exactly the same as or similar to the company's and then allow the users to connect without any password to the fake wireless router.

- SMSishing: Attackers perform phishing using Short Message Service (SMS) by sending links to click or drafting a message that makes the user reply to the text. Penetration testers can also utilize publicly offered services such as https://www.spoofmytextmessage.com/free.

- Quick Response Code (QR code): During a red team exercise, QR codes are also the most effective way to deliver a payload to an isolated area. Similar to spamming, QR codes can be printed and posted in places where most people visit, for example cafeterias, smoking zones, toilets, and other relevant areas.


#### Microcomputer or USB-based attack agents
##### 👉 The Raspberry Pi
↗ [Raspberry Pi](../../../Embedded%20&%20Internet%20of%20Things/🚟%20Embedded%20Computer%20Systems/🛌%20Single-Board%20Computer%20(SBC)/Raspberry%20Pi/Raspberry%20Pi.md)


##### 👉 The MalDuino – the BadUSB
↗ [MalDuino (BadUSB)](../../☠️%20Kill%20Chain/🤔%20Pen-testing%20Tools/Delivery%20Tools/MalDuino%20(BadUSB).md)


### 2️⃣ Human-based
Physical attacks typically involve the physical existence of an attacker, who then performs a social engineering attack. The following are the two types of physical attack that are engaged during RTE or penetration testing:

- Impersonation: This involves the testers creating a script and impersonating an important person in order to harvest information from a targeted set of staff. We recently performed a social engineering attack with the goal of identifying the username and password of a domain user through a physical social engineering exercise. The scenario involves an attacker talking to the victim and impersonating the internal IT helpdesk, "Dear Xman, I am Doctor X from the internal IT department. It has been noted that your system has been disconnected from the network for a period of 20 days. It is recommended to install the latest system updates due to the latest ransomware attack. Do you mind providing the laptop along with your username and password?" That resulted in the user providing the login details and as bonus passing on the laptop to the attacker. Now, the attacker's next move is to plant a backdoor into the system to maintain persistent access.  

- Attacks at the console: These involve all attacks that involve physical access to the system, such as changing the password of an administrator user, planting a keylogger, extracting stored browser passwords, or the installation of backdoor.

- Vishing. Vishing is the art of utilizing a recorded voice message or an individual calling the victim to extract information from a targeted victim or group of victims. Typically, Vishing involves a trustable script, for example, if company X announces a new joint venture with company Y, the staff will be curious about the future of both companies. This allows the attackers to call the victim directly with a pre-defined script as follows: "Hello, I am XX calling from Company Y, we have now been announced as a joint venture, so technically we are all the same team. Having said that, can you please let me know where your data centers are located and do provide me with list of mission-critical servers. If you are not the right person, can you point me to the right one. Many thanks, XX".


##### 👉 The Social Engineering Toolkit (SET)
↗ [SET (Social Engineering Toolkits)](../../☠️%20Kill%20Chain/Social%20Engineering%20Tools/SET%20(Social%20Engineering%20Toolkits).md)


##### 👉 Gophish
↗ [Gophish](../../☠️%20Kill%20Chain/Social%20Engineering%20Tools/Gophish.md)



## Ref