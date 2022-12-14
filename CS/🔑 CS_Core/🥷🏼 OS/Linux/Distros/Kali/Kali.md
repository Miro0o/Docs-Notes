# [Kali](https://www.kali.org)

[TOC]



## 🛣 Guides

### Resources

📂 [Kali Docs]: https://www.kali.org/docs/

[Kali Tools]: https://www.kali.org/tools/

🎬 [奇安信联合出品网络安全Kali Linux精品全套教程完整版]: https://www.bilibili.com/video/BV15t4y1P7sU/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d



### Set-up

Setup kali vm and ssh it from local. 

1. Download corresponding version of kali based on plantforms. 
2. Implement kali (via VM manager such as QEMU /Parallel /virtualbox).
3. Enable cli-mode only. ( See👀 [Troubleshooting](Troubleshooting.md#Boot kali on text mode (CLI only)) )
4. Enable ssh connection. (`iptables` configuration required. See👀 [gnucli - iptables](../../GNU/GNU-CLI.md#iptables) for further info. )
   1. `netstat -lnt` look up open ports.
   2. `vim /etc/ssh/sshd_config` edit sshd config. 
      1. `PubkeyAuthentication yes`
      2. `PermitRootLogin yes`  (optional)
      3. other customized settings. (optional)
   3. `service ssh start` start ssh service
   4. `service ssh status` look up ssh service status
   5. `update-rc.d ssh enable ` enable service boot start. 



