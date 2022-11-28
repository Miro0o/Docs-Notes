# [Mininet](http://mininet.org)

## Intro

Mininet creates a **realistic virtual network**, running **real kernel, switch and application code**, on a single machine (VM, cloud or native), in seconds, with a single command:

![img](http://mininet.org/images/frontpage_diagram.png)

Because you can easily [interact with](http://mininet.org/sample-workflow/#interacting-with-a-network) your network using the Mininet [CLI](http://mininet.org/walkthrough/#interact-with-hosts-and-switches) (and [API](http://mininet.org/api/annotated.html)), [customize](http://mininet.org/sample-workflow/#customizing-a-network) it, [share](http://mininet.org/sample-workflow/#sharing-a-network) it with others, or[deploy](http://mininet.org/sample-workflow#running-on-hardware) it on real hardware, Mininet is useful for [development](http://mininet.org/sample-workflow), [teaching](http://mininet.org/teaching), and [research](http://reproducingnetworkresearch.wordpress.com/).

Mininet is also a great way to develop, share, and experiment with Software-Defined Networking (SDN) systems using [OpenFlow](https://opennetworking.org/software-defined-standards/specifications/) and [P4](http://p4.org/).

Mininet is actively developed and supported, and is released under a permissive BSD Open Source [license](https://github.com/mininet/mininet/blob/master/LICENSE). We encourage you to [contribute](http://mininet.org/contribute) code, bug reports/fixes, documentation, and anything else that can improve the system!



### Resources

📂 [Introduction to Mininet](https://github.com/mininet/mininet/wiki/Introduction-to-Mininet#creating)

[Github/Mininet](https://github.com/mininet/mininet)



### Get-started

#### [Setup](http://mininet.org/vm-setup-notes/)

1. Download the Mininet VM from https://github.com/mininet/mininet/wiki/Mininet-VM-Images .

2. Set up `qemu` vm instance:(on mac using `hvf` accellerator)

   ```shell
   qemu-system-x86_64 -m 2048 mininet-vm-disk1.vmdk -machine accel=hvf -net nic,model=virtio -net user,net=192.168.101.0/24,hostfwd=tcp::8022-:22
   ```

3. Log in to vm via ssh/passwd: (default: mininet/mininet)

   ```shell
   # user + psword
   mininet-vm login: mininet
   Password: mininet
   
   # ssh
   # If you’re running the VM under QEMU/KVM with -net user and the 
   # hostfwd option as recommended above, the VM IP address is 
   # irrelevant. Instead you tell SSH to connect to port 8022 on the host:
   ssh -Y -p 8022 mininet@localhost
   ```

4. Set up SSH auto-login (👩🏼‍🍳 optional). 

   1. Check [Mininet vm setup notes](http://mininet.org/vm-setup-notes/) for details. 



#### [Automating Controller Startup](http://mininet.org/blog/2013/06/03/automating-controller-startup/)