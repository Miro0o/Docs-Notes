# [Kali Linux](https://www.kali.org)

[TOC]



> ↗️  Kali is based on [Debian](../../🔑 CS_Core/🥷🏼 OS/Linux/Distros/Debian/Debian/Debian.md).



## 🛣 Guides

### Resources

📂 [Kali Docs]: https://www.kali.org/docs/

[Kali Tools]: https://www.kali.org/tools/

🎬 [奇安信联合出品网络安全Kali Linux精品全套教程完整版]: https://www.bilibili.com/video/BV15t4y1P7sU/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d



### Set-up

Setup kali vm and ssh it from local. 

1. Download corresponding version of kali based on plantforms. 

2. Implement kali (via emulator as qemu or vm manager like parallel, VMware or virt-manager)

3. Enable cli-mode only. ( Optional, 👀 see [Troubleshooting](Troubleshooting.md#Boot kali on text mode (CLI only)) for more).

   1. `sudo systemctl set-default multi-user.target` then reboot.

4. Configure network. (Kali disables DHCP as default)

   1. `ipconfig` look up NIC.
   2. `dhclient eth0` using DHCP allocate an ip number to `eth0`.
   3. or manually allocate IP number
      1. `inonconfig` 
      2. `/etc/network/interfaces`

5. Setup proxy (optional)

   1. `/root/etc/bash.bashrc`
   2. `/root/etc/apt.conf`
   3. 

6. Enable `ssh` connection. ( see ↗️ [SSH](../../🔑 CS_Core/🏎️ Networking/📌 Basics/0x02 Application Layer/Virtual Host Access/SSH/SSH.md) for details )
   1. `netstat -lnt` look up open ports.
   2. `vim /etc/ssh/sshd_config` edit sshd config. 
      1. `PubkeyAuthentication yes`
      2. `PermitRootLogin yes`  (optional)
      3. other customized settings. (optional)
   3. `service ssh start` start ssh service
   4. `service ssh status` look up ssh service status
   5. `update-rc.d ssh enable ` enable service boot start. 

7. Update Kali packages. (Kali use Debian packages system)

   ```shell
   # From CLI:
   echo deb http://http.kali.org/kali kali main contrib non-free >> /etc/apt/sources.list
   
   
   # or edit sources.list:
   ## kali
   deb http://http.kali.org/kali kali main contrib non-free
   ## kali-dev
   deb http://http.kali.org/kali kali-dev main contrib non-free
   ## kali security updates
   deb http://security.kali.org/kali-security kali/updates main contrib non-free
   ## Bleeding Edge repo, which is for non-official kali packages like aircrack-ng, dnsrecon, sqlmap, beef-xss ...
   deb http://repo.kali.org/kali kali kali-bleeding-edge main
   
   ```

8. Costumize Kali Linux

   1. Reset `root` password
      1. `passwd root`

   2. Add regular user
      1. `adduser <user_name>`

   3. Accelerate Kali 
      1. `preload`
      2. `bleachbit`
      3. `bum`
      4. `gnome-do`
   4. Share filefolder
   5. Encrypt filefolder

9. Manage third-party package

   1. use third-party package
      1. `apt-file` search for info of package in `apt`
      2. `gnome-tweak-tool`
      3. `instanbul` 
      4. `openoffice`
      5. `scrub`
      6. `shutter`
      7. `team viewer`
      8. `terminator`

   2. run third-party package as non-root user
      1. `ps aux | grep <process>` look up running process status
      2. `sux - <non_root_user> <process>` run process as a non-root user

10. Manage  pen testing results

    1. BT 5r3 underesocre the use of  `Draedis` and `MagicTree`.
    2. Kali provides `KeepNote` and `Zim desktop wiki`.
    3. 








`iptables` configuration required. See👀 [gnucli - iptables](../../GNU/GNU-CLI.md#iptables) for further info



## Intro

### [BackTrack (BT)](https://www.backtrack-linux.org)

BackTrack was a Linux distribution that focused on security, based on the Knoppix Linux distribution aimed at digital forensics and penetration testing use. In March 2013, the [Offensive Security](https://www.offensive-security.com/) team rebuilt BackTrack around the Debian distribution and released it under the name Kali Linux.

The last version of BackTrack is BT 5r3. 



> <img src="../../../Assets/Pics/Screenshot 2023-01-19 at 4.12.03 PM.png" alt="Screenshot 2023-01-19 at 4.12.03 PM" style="zoom:50%;" />
>
> Offensive Security is an American international company working in information security, penetration testing and digital forensics. Operating from around 2007, the company created open source projects, advanced security courses, the ExploitDB vulnerability database, and the Kali Linux distribution. The company was started by Mati Aharoni, and employs security professionals with experience in security penetration testing and system security evaluation. The company has provided security counseling and training to many technology companies.



### Kali

[Kali Linux](https://www.kali.org/) *(formerly known as [BackTrack Linux](https://www.backtrack-linux.org/))* is an [open-source](https://www.kali.org/docs/policy/kali-linux-open-source-policy/), [Debian-based Linux](https://www.kali.org/docs/policy/kali-linux-relationship-with-debian/) distribution aimed at advanced Penetration Testing and Security Auditing. It [does this by](https://www.kali.org/features/) providing common tools, configurations, and automations which allows the user to focus on the task that needs to be completed, not the surrounding activity.

Kali Linux contains industry specific modifications as well as [several hundred tools](https://www.kali.org/docs/policy/penetration-testing-tools-policy/) targeted towards various Information Security tasks, such as Penetration Testing, Security Research, Computer Forensics, Reverse Engineering, Vulnerability Management and Red Team Testing.

Kali Linux is a multi-platform solution, accessible and freely available to information security professionals and hobbyists.



#### [Kali Linux Features](https://www.kali.org/docs/introduction/what-is-kali-linux/#kali-linux-features)

- **More than [600](https://www.kali.org/docs/policy/penetration-testing-tools-policy/) penetration testing tools included:** After reviewing every tool that was included in BackTrack, we eliminated a great number of tools that either simply did not work or which duplicated other tools that provided the same or similar functionality. Details on what’s included are on the [Kali Tools](https://www.kali.org/tools) site.
- **Free (as in beer) and always will be:** Kali Linux, like BackTrack, is [completely free](https://www.kali.org/docs/policy/kali-linux-open-source-policy/) of charge and always will be. You will never, ever have to pay for Kali Linux.
- **Open source Git tree:** We are committed to the open source development model and our [development tree](https://gitlab.com/kalilinux) is available for all to see. All of the source code which goes into Kali Linux is available for anyone who wants to tweak or rebuild [packages](https://pkg.kali.org/) to suit their specific needs.
- **FHS compliant:** Kali adheres to the [Filesystem Hierarchy Standard](https://www.pathname.com/fhs/), allowing Linux users to easily locate binaries, support files, libraries, etc.
- **Wide-ranging wireless device support:** A regular sticking point with Linux distributions has been support for wireless interfaces. We have built Kali Linux to support as many wireless devices as we possibly can, allowing it to run properly on a wide variety of hardware and making it compatible with numerous USB and other wireless devices.
- **Custom kernel, patched for injection:** As penetration testers, the development team often needs to do wireless assessments, so our kernel has the latest injection patches included.
- **Developed in a secure environment:** The [Kali Linux team](https://www.kali.org/about-us/) is made up of a small group of individuals who are the only ones trusted to commit packages and interact with the repositories, all of which is done using multiple secure protocols.
- **GPG signed packages and repositories:** Every package in Kali Linux is signed by each individual developer who built and committed it, and the repositories subsequently sign the packages as well.
- **Multi-language support:** Although penetration tools tend to be written in English, we have ensured that Kali includes true multilingual support, allowing more users to operate in their native language and locate the tools they need for the job.
- **Completely customizable:** We thoroughly understand that not everyone will agree with our design decisions, so we have made it as easy as possible for our more adventurous users to [customize Kali Linux](https://www.kali.org/docs/development/live-build-a-custom-kali-iso/) to their liking, all the way down to the kernel.
- **ARMEL and ARMHF support:** Since ARM-based single-board systems like the [Raspberry Pi](https://www.kali.org/docs/arm/raspberry-pi/) and [BeagleBone Black](https://www.kali.org/docs/arm/beaglebone-black/), among others, are becoming more and more prevalent and inexpensive, we knew that [Kali’s ARM support](https://www.kali.org/docs/introduction/kali-on-arm-a-bit-of-history/) would need to be as robust as we could manage, with fully working installations for both [ARMEL and ARMHF](https://en.wikipedia.org/wiki/ARM_architecture) systems. Kali Linux is available on [a wide range of ARM devices ](https://www.kali.org/docs/arm/)and has ARM repositories integrated with the mainline distribution so tools for ARM are updated in conjunction with the rest of the distribution.



*For more features of Kali Linux, please see the following page: [Kali Linux Overview](https://www.kali.org/features/).*



## Ref
