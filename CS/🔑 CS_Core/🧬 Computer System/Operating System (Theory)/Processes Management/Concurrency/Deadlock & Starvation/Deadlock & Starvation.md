# Deadlock & Starvation

[TOC]



## Res


## Intro

## Principles of Deadlock
Deadlock can be defined as the permanent blocking of a set of processes that either compete for system resources or communicate with each other. A set of processes is deadlocked when each process in the set is blocked awaiting an event (typically the freeing up of some requested resource) that can only be triggered by another blocked process in the set. Deadlock is permanent because none of the events is ever triggered. Unlike other problems in concurrent process management, there is no efficient solution in the general case.

All deadlocks involve conflicting needs for resources by two or more processes.


### Reusable Resources
> 1. 资源数量有限
> 2. 资源请求顺序不当

A reusable resource is one that can be safely used by only one process at a time and is not depleted by that use. Processes obtain resource units that they later release for reuse by other processes. Examples of reusable resources include processors, I/O channels, main and secondary memory, devices, and data structures (such as files, databases, and semaphores).


### Consumable Resources
A consumable resource is one that can be created (produced) and destroyed (con- sumed). Typically, there is no limit on the number of consumable resources of a particular type. An unblocked producing process may create any number of such resources. When a resource is acquired by a consuming process, the resource ceases to exist. Examples of consumable resources are interrupts, signals, messages, and information in I/O buffers.


### Resource Allocation Graphs


### 🍯 The Sufficient Conditions for Deadlock (死锁的充要条件)
1. **Mutual exclusion**: Only one process may use a resource at a time. No process may access a resource unit that has been allocated to another process.

2. **Hold and wait**: A process may hold allocated resources while awaiting assignment of other resources.

3. **No preemption**: No resource can be forcibly removed from a process holding it.

4. **Circular wait**: A closed chain of processes exists, such that each process holds at least one resource needed by the next process in the chain.



## 🚕 Approaches to Deadlock
↗ [Approaches to Deadlock](Approaches%20to%20Deadlock.md)



## Ref

