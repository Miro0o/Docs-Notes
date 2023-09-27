# Login Cracker

[TOC]



## Res



## Intro



## Ref
[👍 内网渗透：获取Windows内Hash密码方法总结 | 安全内参]: https://www.secrss.com/articles/24903
- **Windows下安全认证机制**
	- Windows下的安全认证机制总共有两种，一种是基于NTLM的认证方式，主要用在早期的Windows工作组环境中；另一种是基于Kerberos的认证方式，主要用在域环境中。
- **使用PwDump工具获取密码Hash**
	- PwDump7可以在CMD下提取出系统中的用户的密码hash，使用管理员权限直接运行该工具即可：获取到Hash后，我们可以用破解工具来破解得到明文密码，也可以进行哈希传递攻击来横向渗透。
- **使用Mimikatz工具抓取Windows密码**
	- Mimikatz的最大功能是可以直接读取Windows操作系统的明文密码，原理是lsass.exe是Windows系统的安全机制，主要用于本地安全和登陆策略，通常在我们登陆系统时输入密码后，密码便会存贮在lsass.exe内存中，经过wdigest和tspkg两个模块调用后，对其使用可逆的算法进行加密并存储在内存中，而Mimikatz正是通过对lsass.exe逆算获取到明文密码。
		- 需要注意的是当目标为win10或2012R2以上时，默认在内存中禁止保存明文密码，但是我们可以通过修改注册表的方式抓取明文，输入以下命令即可：
			- `Reg add HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest /vUseLogonCredential /t REG_DWORD /d 1 /f`
	- **1、直接读取**
	- **2、Procdump+Mimikatz离线读取lsass.dmp文件**
	- **3、通过SAM和System文件抓取密码和Hash**
- **Windows密码破解方法**
	- **1、ophcrack在线破解**
	- **2、ophcarck工具破解**
- **防范措施**
	- **1、更新补丁**
	- **2、关闭Wdigest Auth**

