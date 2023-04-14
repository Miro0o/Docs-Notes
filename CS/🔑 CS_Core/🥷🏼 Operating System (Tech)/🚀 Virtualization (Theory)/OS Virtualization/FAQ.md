# FAQ

[TOC]



## 👉 Difference between linux namespace & Cgroup?
The proper links for those two notions have been fixed in [PR 14307](https://github.com/docker/docker/pull/14307/files):

> Under the hood, Docker is built on the following components:
> 
> The **[cgroups](https://www.kernel.org/doc/Documentation/cgroups/cgroups.txt)** and [namespaces](http://man7.org/linux/man-pages/man7/namespaces.7.html) capabilities of the Linux kernel

With:
- **cgroup**: Control Groups provide a mechanism for aggregating/partitioning sets of tasks, and all their future children, into hierarchical groups with specialized behaviour.
- **namespace**: wraps a global system resource in an abstraction that makes it appear to the processes within the namespace that they have their own isolated instance of the global resource.

In short:
- **Cgroups** = limits how much you can use;
- **namespaces** = limits what you can see (and therefore use)

See more at "[Anatomy of a Container: Namespaces, cgroups & Some Filesystem Magic](http://fr.slideshare.net/jpetazzo/anatomy-of-a-container-namespaces-cgroups-some-filesystem-magic-linuxcon)" by [Jérôme Petazzoni](http://fr.slideshare.net/jpetazzo).

Cgroups involve resource metering and limiting:
- memory
- CPU
- block I/O
- network

Namespaces provide processes with their own view of the system
Multiple namespaces:
- pid
- net
- mnt
- uts
- ipc
- user: **userns** it is [graduating from experimental in docker 1.10](https://github.com/docker/docker/pull/19187)  

> (per-daemon-instance remapping of container root to an unprivileged user is in progress: [PR 12648](https://github.com/docker/docker/pull/12648): see its [design](https://github.com/docker/docker/pull/11253))



[Difference between linux namespace & Cgroup?]: https://stackoverflow.com/a/34825184/16542494