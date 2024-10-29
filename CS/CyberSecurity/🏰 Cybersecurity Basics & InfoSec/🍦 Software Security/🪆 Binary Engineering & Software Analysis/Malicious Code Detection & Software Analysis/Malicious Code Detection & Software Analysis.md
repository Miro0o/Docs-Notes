# Malicious Code Detection & Software Analysis

[TOC]



## Res
### Related Topics
↗ [Software Analysis in VM & Sandbox](../📌%20DCA%20(Dynamic%20Code%20Analysis)/Software%20Analysis%20in%20VM%20&%20Sandbox/Software%20Analysis%20in%20VM%20&%20Sandbox.md)
↗ [Malicious Codes & Software Engineering](../../../../⛈️%20Risk%20Management/🐗%20Cybersecurity%20Threats%20&%20Attacks/Malicious%20Codes%20&%20Software%20Engineering/Malicious%20Codes%20&%20Software%20Engineering.md)

↗ [Vulnerability Disclosure（漏洞挖掘）](../../🐒%20Software%20Vulnerability%20&%20Weakness/Vulnerability%20Disclosure（漏洞挖掘）/Vulnerability%20Disclosure（漏洞挖掘）.md)
↗ [Vulnerability Discovery（漏洞检测）](../../🐒%20Software%20Vulnerability%20&%20Weakness/Vulnerability%20Discovery（漏洞检测）/Vulnerability%20Discovery（漏洞检测）.md)

↗ [LLM & Security](../../../../🤖%20AI%20x%20Security/LLM%20&%20Security/LLM%20&%20Security.md)


### Learning Resources
📖 Practical Malware Analysis
🧪 https://github.com/mikesiko/PracticalMalwareAnalysis-Labs



## Intro




## Ref
[从"新"开始学习恶意代码分析——静态分析]: https://www.anquanke.com/post/id/207594#h2-0

[👍 Hunting for Malicious Packages on PyPI]: https://jordan-wright.com/blog/post/2020-11-12-hunting-for-malicious-packages-on-pypi/
About a year ago, the Python Software Foundation [opened a Request for Information (RFI)](https://discuss.python.org/t/what-methods-should-we-implement-to-detect-malicious-content/2240) to discuss how we could detect malicious packages being uploaded to PyPI. Whether it’s [taking over abandoned packages](https://blog.npmjs.org/post/141577284765/kik-left-pad-and-npm), [typosquatting on popular libraries](https://github.com/dateutil/dateutil/issues/984), or [hijacking packages using credential stuffing](https://github.com/ChALkeR/notes/blob/master/Gathering-weak-npm-credentials.md), it’s clear this is a real issue affecting nearly every package manager. 

The truth is that package managers like PyPI are critical infrastructure that almost every company relies on. I could write for days on this topic, but I’ll just let this xkcd suffice for now.

![](../../../../../../../Assets/Pics/Pasted%20image%2020240915011047.png)

[👍 Finding malicious PyPI packages through static code analysis: Meet GuardDog]: https://securitylabs.datadoghq.com/articles/guarddog-identify-malicious-pypi-packages/
