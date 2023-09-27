# FAQ

[TOC]



## 👉 Snap 🆚 Container ?
#snap #container 

(2020)

There is a document in the Snap repository that goes into a bit more depth on the underlying mechanisms used by Snap:

[https://github.com/snapcore/snapd/wiki/snap-confine-Overview](https://github.com/snapcore/snapd/wiki/snap-confine-Overview)

To give a quick overview here:
- Snap uses cgroups, as you surmised in your question
- There isn't really a "runtime"; cgroups are a feature of the Linux Kernel. The Kernel is the closest thing to a runtime used by Snap. Or, you could consider Snap itself to be the runtime.
- Snap is really only concerned with OS level isolation, eg libraries, binaries, etc.
- Snap doesn't really enforce device isolation or security.
- For security, Snap instead heavily relies on AppArmor and Seccomp.
- If you're on a distro that doesn't use AppArmor, Snaps have no security mechanisms.


[👍 Does snap packages run similar to containers (docker / rkt etc) or use different underlying technology? | Stackoverflow]: https://stackoverflow.com/a/63568874/16542494


---
(2022)

Snap installs apps on your local machine as self-contained packages. They include everything that is needed to run the software, so you don't have to install additional dependencies manually. In a sense it is a replacement for distribution specific package management. The app you install works like it normally would, so moving to a different machine works the same way. Do a new install and move the data as needed.

Docker runs services inside containers (think of it as a lightweight VM). These machines (or containers) have their own IPs, you can set up networking between them etc. Similar to Snap, a Docker image contains everything needed to run a particular service. You can run multiple containers from the same image (at the same time). It doesn't really do desktop apps, something which Snap can do. Docker is primarily targeted towards running services (e.g. a web server, database server, application server, …).

[https://askubuntu.com/a/868755](https://askubuntu.com/a/868755)

Similar to Snap, you don't really transfer Docker containers between instances. A container is supposed to be ephemeral (i.e. hold no state), so anything you want to keep (like database files) needs to be stored on the host. To transfer to a new machine, you'd transfer the data, then use that with a new container.

tl;dr: You can accomplish the same things, but the intended use case is slightly different. Snaps runs on your local machine, while Docker containers run inside a lightweight virtual environment, isolated from one another, unless you explicitly expose network ports or mount directories/files from the host.


[👍 Snap vs docker differences? | Linus tech tips]: https://linustechtips.com/topic/1415658-snap-vs-docker-differences/?do=findComment&comment=15287555

[what's the main difference between Docker and Snap?]: https://askubuntu.com/a/868755
