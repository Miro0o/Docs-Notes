# Python Third-party Libs

[TOC]



## Res
🏠 🔍 https://pypi.org


### Related Topics
↗ [The Python Standard Library](../../../../Interpreted%20Languages/Python/🌷%20The%20Python%20Standard%20Library/The%20Python%20Standard%20Library.md)
↗ [Python Based AI](../../../../../../Artificial%20Intelligence/🛫%20Frameworks%20&%20Implementations%20&%20SDKs/ML%20Programming%20&%20Frameworks/⭐️%20Python%20Based%20AI/Python%20Based%20AI.md)



## Intro



## PyPI
![img](../../../../../../../Assets/Pics/logo-large.9f732b5f.svg)


🏠 https://pypi.org

The Python Package Index (PyPI) is a repository of software for the Python programming language.

PyPI helps you find and install software developed and shared by the Python community. [Learn about installing packages](https://packaging.python.org/installing/).

Package authors use PyPI to distribute their software. [Learn how to package your Python code for PyPI](https://packaging.python.org/tutorials/packaging-projects/).



## Ref
[👍 Hunting for Malicious Packages on PyPI]: https://jordan-wright.com/blog/post/2020-11-12-hunting-for-malicious-packages-on-pypi/
About a year ago, the Python Software Foundation [opened a Request for Information (RFI)](https://discuss.python.org/t/what-methods-should-we-implement-to-detect-malicious-content/2240) to discuss how we could detect malicious packages being uploaded to PyPI. Whether it’s [taking over abandoned packages](https://blog.npmjs.org/post/141577284765/kik-left-pad-and-npm), [typosquatting on popular libraries](https://github.com/dateutil/dateutil/issues/984), or [hijacking packages using credential stuffing](https://github.com/ChALkeR/notes/blob/master/Gathering-weak-npm-credentials.md), it’s clear this is a real issue affecting nearly every package manager. 

The truth is that package managers like PyPI are critical infrastructure that almost every company relies on. I could write for days on this topic, but I’ll just let this xkcd suffice for now.

![](../../../../../../../Assets/Pics/Pasted%20image%2020240915011047.png)

[👍 Finding malicious PyPI packages through static code analysis: Meet GuardDog]: https://securitylabs.datadoghq.com/articles/guarddog-identify-malicious-pypi-packages/
