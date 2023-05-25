# Scheduling Algorithms

[TOC]



## Res


## Intro


## Scheduling Principles: Constraints & Objectives
Table 9.3 presents some summary information about the various scheduling policies that are examined in this subsection. The selection function determines which process, among ready processes, is selected next for execution. The function may be based on **priority**, **resource requirements**, or the **execution characteristics** of the process. In the latter case, three quantities are significant:
- w = time spent in system so far, waiting
- e = time spent in execution so far
- s = total service time required by the process, including e; 

generally, this quantity must be estimated or supplied by the user.
For example, the selection function max[w] indicates an FCFS discipline.

![](../../../../../../../Assets/Pics/Screenshot%202023-05-18%20at%203.13.48%20PM.png)


### 1️⃣ Decision Modes
The decision mode specifies the instants in time at which the selection function is exercised. There are two general categories.

#### Preemptive Scheduling
> **Preemptive**: The currently running process may be interrupted and moved to the Ready state by the OS. The decision to preempt may be performed when a new process arrives, when an interrupt occurs that places a blocked process in the Ready state, or periodically, based on a clock interrupt.



#### Non-preemptive Scheduling
> **Nonpreemptive**: In this case, once a process is in the Running state, it contin- ues to execute until (a) it terminates or (b) it blocks itself to wait for I/O or to request some OS service.



### 2️⃣ Performance Metrics
#### Single Job Perspective
##### Turnaround Time (TAT)

##### Response Time
##### Deadline (时限/截止时间)
- Hard DDL: time before which a job must conplete
- Soft DDL: time before which a job is preferred to complete (may come with penality for the timeover)


#### Batch Jobs Perspective
##### Throughput
Throughtput is measured as the number of completed jos/processes in a unit of time.
Average number of instructions per job affects throughput.


#### System Perspective
##### Resource Utilization
The time when the resource (processor or I/O) is busy in a unit of time. 


### 3️⃣ Fairness
#### Starvation
a process is admitted but never gets executed (and hence never terminates or completes)

Consequences: inefficiency and errors
- Unhappy users
- Wasted resoures
- Deadlock

#### Other Forms of Fairness
##### Proportional Fairness
resources allocated to a user/job/process is proportional to a weight value

##### Max-min Fairness
The minimal resource allocated to a user/job/process is maximized

##### Dominant Resource Fairness
fair sharing based on critical resources



## Scheduling Algorithms
### Scheduling Algorithms Overview
#### Characteristics of Various Scheduling Policies
![](../../../../../../../Assets/Pics/Screenshot%202023-05-18%20at%202.36.09%20PM.png)


#### Priority Scheduling
↗ [Priority Scheduling](Uniprocessor%20Scheduling/Priority%20Scheduling.md)


### 1️⃣ Non-preemptive Scheduling Algorithms
#### FCFS /FIFO
The simplest scheduling policy is first-come-first- served (FCFS), also known as first-in, first-out (FIFO) or a strict queueing scheme. As each process becomes ready, it joins the ready queue. When the currently running process ceases to execute, the process that has been in the ready queue the longest is selected for running.



#### SPN (Shortest Process Next) /SJF ()

##### EW


#### HRRN (Highest Response Ratio Next)
##### Response Ratio


### 2️⃣ Preemptive Scheduling Algorithms
#### RR (Round Robin), Time Slicing

> ⚠ Next job enter into cpu before the current job fully exit


With round robin, the principal design issue is the **length of the time quantum**, or **slice**, to be used. If the quantum is very short, then short processes will move through the system relatively quickly. On the other hand, there is processing over- head involved in handling the clock interrupt and performing the scheduling and dispatching function. Thus, very short time quanta should be avoided. One useful guide is that the time quantum should be slightly greater than the time required for a typical interaction or process function. If it is less, then most processes will require at least two time quanta. Figure 9.6 illustrates the effect this has on response time. Note in the limiting case of a time quantum that is longer than the longest-running process, round robin degenerates to FCFS.


![](../../../../../../../Assets/Pics/Screenshot%202023-05-18%20at%204.08.21%20PM.png)


![](../../../../../../../Assets/Pics/Screenshot%202023-05-18%20at%204.13.03%20PM.png)



#### SRT (Shortest Remaining Time)
> May be viewed as the preemptive verson of SPN



#### Multi-Level Feedback Queue, Feedback (MLFQ)
- no prior knowledge about the execution time of porcess
- adsf
- adsf

![](../../../../../../../Assets/Pics/Screenshot%202023-05-18%20at%204.13.47%20PM.png)


MLFQ is biased against long process
- approach 1
- approach 2




## Scheduling Algorithms Rverview
### A Comparison of Scheduling Policies
| Process | Arrival Time | Service Time |
| - | - | - |
| A | 0 | 3 |
| B | 2 | 6 |
| C | 4 | 4 |
| D | 6 | 5 |
| E | 8 | 2 |

![](../../../../../../../Assets/Pics/Screenshot%202023-05-18%20at%202.41.22%20PM.png)

![](../../../../../../../Assets/Pics/Screenshot%202023-05-18%20at%203.22.49%20PM.png)



## Ref

