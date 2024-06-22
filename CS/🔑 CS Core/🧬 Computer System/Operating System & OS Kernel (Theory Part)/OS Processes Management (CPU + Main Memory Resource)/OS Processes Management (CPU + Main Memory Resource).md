# OS Processes Management (CPU + Main Memory Resource)

[TOC]



## Res
### Related Topics
↗ [C&CPP /OS Level Programming /Process Management](../../../🥷🏼%20Operating%20System%20(Engineering%20Part)/📟%20System%20Level%20Programming/OS%20Level%20Programming%20in%20Different%20Languages/OS%20Level%20Programming%20with%20C%20&%20CPP/Process%20Management/Process%20Management.md)

↗ [Distributed Process Management](../../../../System%20Architecture%20Design/🌌%20Distributed%20Systems/☯️%20Distributed%20Systems%20Design/Distributed%20Process%20Management/Distributed%20Process%20Management.md)
↗ [Operating System Kernel (Kernel Mode)](../../../🥷🏼%20Operating%20System%20(Engineering%20Part)/📟%20System%20Level%20Programming/😴%20Operating%20System%20Components%20&%20Runtime%20Libraries/🫀%20Operating%20System%20Kernel%20(Kernel%20Mode)/Operating%20System%20Kernel%20(Kernel%20Mode).md)

↗ [Instruction Execution](../../../🛣️%20Program%20Execution%20&%20Compilation%20System/🧙🏿‍♀️%20Program%20Execution%20(Runtime)/Instruction%20Execution/Instruction%20Execution.md)



## Intro
A process is an operating system abstraction that groups together multiple resources:
- An ↗ [Address Space](../OS%20Memory%20Management%20(Main%20Memory%20+%20Secondary%20Memory%20Resource)/Address%20Space.md)
- One or more ↗ [Threads & Coroutine](Threads%20&%20Coroutine/Threads%20&%20Coroutine.md)
- Opened files
- ↗ [Sockets](IPC%20(Inter%20Process%20Communication)/🧦%20Sockets/Sockets.md)
- ↗ [Semaphore](Concurrency%20Control/⭐️%20System%20Level%20Concurrency%20Control%20Mechanism/Concurrency%20Control%20Methods%20Abstraction/Semaphore/Semaphore.md)
- Shared memory regions
- Timers
- Signal handlers
- Many other resources and status information

All this information is grouped in the **Process Control Group (PCB)**. In Linux this is `struct task_struct`.

↗ [Processes Description & Control](📌%20Processes%20Description%20&%20Control/Processes%20Description%20&%20Control.md)
↗ (Linux) [Task Management & Scheduling (Process & Threads)](../../../🥷🏼%20Operating%20System%20(Engineering%20Part)/Linux%20(Derived%20From%20UNIX%20Family)/🔩%20Linux%20Kernel/⭕️%20Task%20Management%20&%20Scheduling%20(Process%20&%20Threads)/Task%20Management%20&%20Scheduling%20(Process%20&%20Threads).md)


### Context Switch
> ↗ [Interrupts (Software & Hardware)](../../../🛣️%20Program%20Execution%20&%20Compilation%20System/🧙🏿‍♀️%20Program%20Execution%20(Runtime)/Instruction%20Execution/Interrupts%20(Software%20&%20Hardware).md)
> ↗ [System Calls](📌%20Processes%20Description%20&%20Control/System%20Calls/System%20Calls.md)

At any point in time, a uniprocessor system can only execute the code for a single process. When the operating system decides to transfer control from the current process to some new process, it performs a context switch by saving the context of the current process, restoring the context of the new process, and hen passing control to the new process. The new process picks up exactly where it left off.

![](../../../../../../Assets/Pics/Screenshot%202023-10-13%20at%208.41.52PM.png)

As figure above indicates, the transition from one process to another is managed by the operating system kernel. The kernel is the portion of the operating system code that is always resident in memory. When an application program requires some action by the operating system, such as to read or write a file, it executes a special system call instruction, transferring control to the kernel. The kernel then performs the requested operation and returns back to the application program. Note that the kernel is not a separate process. Instead, it is a collection of code and data structures that the system uses to manage all the processes.



## Ref
