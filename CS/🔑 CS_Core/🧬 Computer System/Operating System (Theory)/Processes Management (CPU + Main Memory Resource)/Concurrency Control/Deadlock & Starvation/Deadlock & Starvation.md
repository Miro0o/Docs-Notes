# Deadlock & Starvation

[TOC]



## Res


## Intro
Deadlock can be defined as the **permanent blocking** of a set of processes that either compete for system resources or communicate with each other. A set of processes is deadlocked when each process in the set is blocked awaiting an event (typically the freeing up of some requested resource) that can only be triggered by another blocked process in the set. Deadlock is permanent because none of the events is ever triggered. Unlike other problems in concurrent process management, there is no efficient solution in the general case.

All deadlocks involve **conflicting needs for resources** by two or more processes.


### Joint Progress Diagram
> As shown, the joint progress diagram can be used to record the execution history of two processes that share resources. In cases where more than two processes may compete for the same resource, a higher-dimensional diagram would be required. The principles concerning fatal regions and deadlock would remain the same.



![|300](../../../../../../../Assets/Pics/Screenshot%202023-06-12%20at%2010.41.10%20AM.png)

![](../../../../../../../Assets/Pics/Screenshot%202023-06-12%20at%2010.38.07%20AM.png)

The figure shows six different execution paths. These can be summarized as follows:
1. Q acquires B then A, then releases B and A. When P resumes execution, it will be able to acquire both resources.
2. Q acquires B then A. P executes and blocks on a request for A. Q releases B and A. When P resumes execution, it will be able to acquire both resources.
3. Q acquires B then P acquires A. Deadlock is inevitable, because as execution proceeds, Q will block on A and P will block on B.
4. P acquires A then Q acquires B. Deadlock is inevitable, because as execution proceeds, Q will block on A and P will block on B.
5. P acquires A then B. Q executes and blocks on a request for B. P releases A and B. When Q resumes execution, it will be able to acquire both resources.
6. P acquires A then B, then releases A and B. When Q resumes execution, it will be able to acquire both resources.

The gray-shaded area of Figure 6.2, which can be referred to as a **fatal region**, applies to the commentary on paths 3 and 4. If an execution path enters this fatal region, then deadlock is inevitable. Note the existence of a fatal region depends on the logic of the two processes. However, deadlock is only inevitable if the joint progress of the two processes creates a path that enters the fatal region.

---
Whether or not deadlock occurs depends on both the dynamics of the execution and on the details of the application. For example, suppose P does not need both resources at the same time so the two processes have the following form:

![](../../../../../../../Assets/Pics/Screenshot%202023-06-12%20at%2010.41.42%20AM.png)



## Principles of Deadlock
### Resource Types leading to Deadlock
> All deadlocks involve **conflicting needs for resources** by two or more processes.

#### Reusable Resources
> 可重用资源造成死锁的原因：
> 1. 可重用资源数量有限 （e.g. 内存资源请求）
> 2. 可重用资源请求顺序不当 （e.g. 两个进程同时读写一个文件）

A reusable resource is one that can be safely used by only one process at a time and is not depleted by that use. Processes obtain resource units that they later release for reuse by other processes. 

Examples of reusable resources include processors, I/O channels, main and secondary memory, devices, and data structures (such as files, databases, and semaphores).


#### Consumable Resources
A consumable resource is one that can be created (produced) and destroyed (consumed). Typically, there is no limit on the number of consumable resources of a particular type. An unblocked producing process may create any number of such resources. When a resource is acquired by a consuming process, the resource ceases to exist.

Examples of consumable resources are interrupts, signals, messages, and information in I/O buffers.


### Resource Allocation Graphs
A useful tool in characterizing the allocation of resources to processes is the resource allocation graph, introduced by Holt [HOLT72].

![](../../../../../../../Assets/Pics/Screenshot%202023-06-12%20at%2010.51.44%20AM.png)


### 🍯 The Sufficient Conditions for Deadlock (死锁的充要条件)
1. **Mutual exclusion**: Only one process may use a resource at a time. No process may access a resource unit that has been allocated to another process.

2. **Hold and wait**: A process may hold allocated resources while awaiting assignment of other resources.

3. **No preemption**: No resource can be forcibly removed from a process holding it.

==If all previous 3 condition reached, **then** if following condition holds, deadlock **occurs**.== (There is a sequential significance of the previous 3 and the 4th conditions for deadlock occurs. Term "occurs" is what distinguishes "deadlock avoidance" policy and "deadlock prevention" policy)

> i.e. The first three conditions are **necessary**, but **not sufficient**, for a deadlock to exist. For deadlock to actually take place, a fourth condition is required:

4. **Circular wait**: A closed chain of processes exists, such that each process holds at least one resource needed by the next process in the chain.

![](../../../../../../../Assets/Pics/Screenshot%202023-06-12%20at%2010.52.58%20AM.png)


💡 To clarify this discussion, it is useful to return to the concept of the joint progress diagram. Recall that we defined a **fatal region** as one such that once the processes have progressed into that region, those processes will deadlock.

==A fatal region exists only if all of the first three conditions listed above are met==. If one or more of these conditions are not met, there is no fatal region and deadlock cannot occur. Thus, these are **necessary conditions** for deadlock.

For deadlock to occur, there must be not only a fatal region but also a sequence of resource requests that has led into the fatal region. If a circular wait condition occurs, then in fact the fatal region has been entered. Thus, all four conditions listed above are sufficient for deadlock



## 🚕 Approaches to Deadlock
There is no single effective strategy that can deal with all types of deadlock. Three approaches are common:
• **Deadlock prevention**: Disallow one of the three necessary conditions for deadlock occurrence, or prevent circular wait condition from happening.

• **Deadlock avoidance**: Do not grant a resource request if this allocation **might** lead to deadlock.

• **Deadlock detection & recovery**: Grant resource requests when possible, but periodically check for the presence of deadlock and take action to recover.

↗ [Approaches to Deadlock](Approaches%20to%20Deadlock.md)



## Ref

