# Development(History) of Operating Systems

[TOC]



## Res



## Ease of Evolution of an OS
A major OS will evolve over time for a number of reasons:
1. **Hardware upgrades plus new types of hardware :** For example, early versions of UNIX and the Macintosh OS did not employ a paging mechanism because they were run on processors without paging hardware. Subsequent versions of these operating systems were modified to exploit paging capabilities. Also, the use of graphics terminals and page-mode terminals instead of line-at-a-time scroll mode terminals affects OS design. For example, a graphics terminal typically allows the user to view several applications at the same time through “windows” on the screen. This requires more sophisticated support in the OS.
2. **New services:** In response to user demand or inresponse to the needs of system managers, the OS expands to offer new services. For example, if it is found to be difficult to maintain good performance for users with existing tools, new measurement and control tools may be added to the OS.
3. **Fixes:** Any OS has faults. The seared is covered over the course of time and fixes are made. Of course, the fix may introduce new faults.



## The Evolution of Operating Systems
### 🦄 Uniprocessors Operating Systems
#### Serial Processing


#### Simple Batch Systems
##### Resident Monitor
**Monitors were the precursors of modern-day operating systems.** Their role was straightforward. The monitor started the job and gave control of the computer to the job, and when the job was done, the monitor resumed control of the machine. The work originally done by people was being done by the computer, thus increasing efficiency and utilization.


#### Multiprogrammed Batch Systems
##### Simultaneous Peripheral Operations On-Line (SPOOLing)


#### Time-sharing Operating Systems

| S.No. | TIME SHARING | MULTIPROGRAMMING |
|-|-|-|
| 01. | Time Sharing is the logical extension of multiprogramming, in this time sharing Operating system many users/processes are allocated with computer resources in respective time slots. | Multiprogramming operating system allows to execute multiple processes by monitoring their process states and switching in between processes. |
|02.|Processors time is shared with multiple users that’s why it is called as time sharing operating system.|Processor and memory underutilization problem is resolved and multiple programs runs on CPU that’s why it is called multiprogramming.|
|03.|In this process, two or more users can use a processor in their terminal.|In this, the process can be executed by a single processor.|
|04.|Time sharing OS has fixed time slice.|Multi-programming OS has no fixed time slice.|
|05.|In time sharing OS system, execution power is taken off before finishing of execution.|In multi-programming OS system before finishing a task the execution power is not taken off.|
|06.|Here the system works for the same or less time on each processes.|Here the system does not take same time to work on different processes.|
|07.|In time sharing OS system depends on time to switch between different processes.|In Multiprogramming OS, system depends on devices to switch between tasks such I/O interrupts etc.|
|08.|System model of time sharing system is multiple programs and multiple users.|System model of multiprogramming system is multiple programs.|
|09.|Time sharing system minimizes response time.|Multiprogramming system maximizes processor use.|
|10.|Example: Windows NT.|Example: Mac OS.|



### 🎏 Multi-processor Operating Systems
#### Loosely Coupled Multiprocessors


#### Tightly Coupled Multiprocessors



### Real-time Operating Systems
↗ [RTOS (Real-Time Operating System)](../../../../Internet%20of%20Things/Embedded%20Computer%20Systems/Embedded%20Operating%20Systems/🐎%20RTOS%20(Real-Time%20Operating%20System)/RTOS%20(Real-Time%20Operating%20System).md)


### Distributed Operating Systems
↗ [Distributed Operating System](../../../../Software%20Engineering/🧠%20System%20Architecture%20Design/♟️%20Distributed%20Systems/Distributed%20Operating%20System/Distributed%20Operating%20System.md)


### Personal Computers & OS
↗ [Windows](../../../🥷🏼%20Operating%20System%20(Tech)/Windows/Windows.md)
↗ [Linux](../../../🥷🏼%20Operating%20System%20(Tech)/Linux%20(UNIX%20Family)/Linux.md)
↗ [MacOS](../../../🥷🏼%20Operating%20System%20(Tech)/Apple/MacOS%20(UNIX%20Family)/MacOS.md)



## ⭐️ Major Achievements
[DENN80a] proposes that there have been four major theoretical advances in the development of operating systems:

- Processes
- Memory management
- Information protection and security
- Scheduling and resource management

Each advance is characterized by principles, or abstractions, developed to meet difficult practical problems. Taken together, these four areas span many of the key design and implementation issues of modern operating systems.



## Modern OS Designs ...
↗ [Operating System Design](Operating%20System%20Design.md)



## Ref
[操作系统原理——第2章 操作系统概述]: https://blog.csdn.net/tangkcc/article/details/114852154
[单道批处理系统]: https://blog.csdn.net/TakahashiRyosuke/article/details/108230334
[操作系统的批处理和多道概念]: https://my.oschina.net/openK/blog/87193

[Difference between Time Sharing OS and Multiprogramming OS | GeeksfroGeeks]: https://www.geeksforgeeks.org/difference-between-time-sharing-os-and-multiprogramming-os/

[操作系统的发展历史 - Drew的文章 - 知乎]: https://zhuanlan.zhihu.com/p/367996835
