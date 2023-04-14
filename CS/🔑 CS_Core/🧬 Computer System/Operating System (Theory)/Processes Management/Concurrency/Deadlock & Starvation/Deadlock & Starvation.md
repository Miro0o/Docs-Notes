# Deadlock & Starvation

[TOC]



## Res


## Intro

## Principle of Deadlock
Deadlock can be defined as the permanent blocking of a set of processes that either compete for system resources or communicate with each other. A set of processes is deadlocked when each process in the set is blocked awaiting an event (typically the freeing up of some requested resource) that can only be triggered by another blocked process in the set. Deadlock is permanent because none of the events is ever trig- gered. Unlike other problems in concurrent process management, there is no efficient solution in the general case.

All deadlocks involve conflicting needs for resources by two or more processes.

### Reusable Resources

### Consumable Resources


### Resource Allocation Graphs


### 🍯 The Sufficient Conditions for Deadlock
1. **Mutual exclusion**: Only one process may use a resource at a time. No process may access a resource unit that has been allocated to another process.

2. **Hold and wait**: A process may hold allocated resources while awaiting assign- ment of other resources.

3. **No preemption**: No resource can be forcibly removed from a process holding it.

4. **Circular wait**: A closed chain of processes exists, such that each process holds at least one resource needed by the next process in the chain.



## 🚕 Approaches to Deadlock
↗ [Approaches to Deadlock](Approaches%20to%20Deadlock.md)



## Ref

