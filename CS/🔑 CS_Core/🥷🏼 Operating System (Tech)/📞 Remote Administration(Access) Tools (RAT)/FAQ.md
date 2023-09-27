# FAQ

[TOC]



## 👉 VNC Server Setup
### Setup RealVNC for kali on raspberry pi
#realvnc #kali 




[Kali 下安装VNC Server]: https://zhuanlan.zhihu.com/p/395121267




### Setup x11vnc for kali on raspberry pi
#kali #RaspberryPi #x11vnc 

Apparently, [Kali Linux 0.6 Raspberry Pi 3 w/ Nexmon](https://build.nethunter.com/rpi3-nexmon/) contains older packages. Once issuing the command `apt-get update && apt-get -y upgrade && apt-get -y dist-upgrade``tightvncserver` gets replaced by `tigervncserver`. Thus, `TightVNC` isn't part of this image of Kali Linux. `TigerVNC` is a fork that is supported by the standard Kali Linux repositories.

I managed to figure out a pretty good alternative to `TightVNC` and `TigerVNC`. Below is my expanded solution.


Solution:
I would recommend using `x11vnc` as it provides the actual desktop experience rather than a virtual one. 

To install `x11vnc` enter the following command:

`apt-get update && apt-get install -y x11vnc`

If you experience that the `framebuffer` size is too small, then to change it by doing the following:

1. Locate `/boot/config.txt` and open it using `nano` or `vim`

(**Note**: If the file `/boot/config.txt` does not exist, safely power-off the Pi using the command, `poweroff` and take the Micro-SD card out and plug it into a laptop or desktop computer. When the Micro-SD card mounts, open it. The `config.txt` file should be on the root of the mounted Micro-SD card).

2. uncomment the following text in `config.txt`: 

_Before_:

`#framebuffer_width=1280`

`#framebuffer_height=720`

_After_:

`framebuffer_width=1280`

`framebuffer_height=720`

3. Save and exit the file. Then, reboot the Pi and start `x11vnc` by using the following command to push it into a background process: `x11vnc -usepw -reopen -bg -forever &`

---

If you would like to start `x11vnc` at boot, add the following to a file called `x11vnc.desktop` in `~/.config/autostart`:

```
[Desktop Entry]
Type=Application
Name=x11vnc
Exec=x11vnc -usepw -reopen -bg -forever &
Comment=Starts an x11vnc server on port kali:5900
```

(**Note**: If `~/.config/autostart` does not exist, create the `autostart` directory by issuing the following command: `mkdir ~/.config/autostart`). 

See [how-to-execute-shell-script-on-kali-linux-startup](https://unix.stackexchange.com/questions/276463/how-to-execute-shell-script-on-kali-linux-startup) for more information on application autostart on Kali Linux.


[👍 tightvncserver - Displaying Grey Screen on Kali-Linux upon VNC Connection]: https://raspberrypi.stackexchange.com/questions/60874/tightvncserver-displaying-grey-screen-on-kali-linux-upon-vnc-connection



### Setup TightVNC for kali on raspberry pi
#tightvnc #RaspberryPi #kali 


[Kali 安装vnc | CSDN]: https://blog.csdn.net/blueicex2017/article/details/107225876




### Setup TightVNC for Rasp OS on Raspberry Pi
#tightvnc #RaspberryPi 



[树莓派开机连接桌面的两种方式]: https://blog.csdn.net/huying7664/article/details/124839349

