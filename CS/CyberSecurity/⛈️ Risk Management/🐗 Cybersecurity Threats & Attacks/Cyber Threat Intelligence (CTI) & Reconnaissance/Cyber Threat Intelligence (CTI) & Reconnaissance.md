# Cyber Threat Intelligence (CTI) & Reconnaissance

[TOC]



## Res
### Related Topics
↗ [Social Engineering & Physical Security](../../../⛈️%20Risk%20Management/🐗%20Cybersecurity%20Threats%20&%20Attacks/Social%20Engineering%20&%20Physical%20Security/Social%20Engineering%20&%20Physical%20Security.md)

↗ [Vulnerability Assessment（漏洞危害评估）](../../../🏰%20Cybersecurity%20Basics%20&%20InfoSec/🍦%20Software%20Security/Software%20Vulnerability/Vulnerability%20Assessment（漏洞危害评估）/Vulnerability%20Assessment（漏洞危害评估）.md)
↗ [Cyberspace Assets Mapping & Management](../../../⛈️%20Risk%20Management/🐄%20Cyberspace%20Assets/🧨%20Cyberspace%20Assets%20Mapping%20&%20Management/Cyberspace%20Assets%20Mapping%20&%20Management.md)


### Other Resource
👍 https://github.com/mitre/cti
This repository contains the MITRE ATT&CK® and CAPEC™ datasets expressed in STIX 2.0. See [USAGE](https://github.com/mitre/cti/blob/master/USAGE.md) or [USAGE-CAPEC](https://github.com/mitre/cti/blob/master/USAGE-CAPEC.md) for information on using this content with [python-stix2](https://github.com/oasis-open/cti-python-stix2).

If you are looking for ATT&CK represented in STIX 2.1, please see the [attack-stix-data](https://github.com/mitre-attack/attack-stix-data) GitHub repository. Both MITRE/CTI (this repository) and attack-stix-data will be maintained and updated with new ATT&CK releases for the foreseeable future, but the data model of attack-stix-data includes quality-of-life improvements not found on MITRE/CTI. Please see the [attack-stix-data USAGE document](https://github.com/mitre-attack/attack-stix-data) for more information on the improved data model of that repository.



## Intro: Reconnaissance
> Penetration

An attacker will typically dedicate up to 75% of the overall work effort for a penetration test to reconnaissance, as it is this phase that allows the target to be defined, mapped, and explored for the vulnerabilities that will eventually lead to exploitation.

There are two types of reconnaissance:
- Passive reconnaissance (direct and indirect) 
- Active reconnaissance

Generally, passive reconnaissance is concerned with analyzing information that is openly available, usually from the target itself or public sources online. On accessing this information, the tester or attacker does not interact with the target in an unusual manner—requests and activities will not be logged, or will not be traced directly to the tester. Therefore, passive reconnaissance is conducted first to minimize the direct contact that may signal an impending attack or to identify the attacker.

In this chapter, you will learn the principles and practices of passive reconnaissance, which include the following:
- Basic principles of reconnaissance  
- OSINT  
- Online resources and dark web search  
- Using scripts to automatically gather OSINT data Obtaining user information
- Profiling users for password lists
- Using social media to extract words





## Ref
[2020年SANS CTI调查结果解读：网空威胁情报 (CTI) 日益成熟]: https://www.secrss.com/articles/17525
1. 报告核心观点
2. 报告调查主要内容（节选）
	1. 如何衡量情报计划的有效性？
	2. 哪些流程和工具能有效支持CTI的协作工作
	3. CTI使用的核心场景和情报内容有哪些？？
	4. 组织有效使用CTI的阻力是什么？
3. 从报告中我们能看到什么？
	1. 网空威胁情报应用逐渐成熟
	2. 网空威胁情报内生趋势逐年上涨
	3. 网空威胁情报处理流程趋于半自动化
	4. 团队协作是情报有效使用的关键
4. 如何实现情报内生，聚合应变？
	1. 情报内生是什么
	2. 情报内生实践案例

[👍 信息收集总结]: http://uuzdaisuki.com/2021/05/31/信息收集总结/
