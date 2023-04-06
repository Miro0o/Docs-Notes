# Instruction Pipelining

[TOC]



> Instruction pipelining is one method used to exploit **instruction-level parallelism (ILP)**. (Other methods include superscalar and VLIW.) We include it in this chapter because ==the ISA of a machine affects how successful instruction pipelining can be.==
> 
> ↗ [ILP (Instruction Level Parallelism)](../../🧝🏻‍♀️%20von%20Neumann%20Based%20Microarchitecture/Processor/Instruction%20Processing/ILP%20(Instruction%20Level%20Parallelism).md)



## Res



## Intro
### Speedup S
Let’s calculate the speedup we gain using a pipeline. Without a pipeline, the time required is ntn cycles, where $t_n = k × t_p$. Therefore, the speedup (time without a pipeline divided by the time using a pipeline) is:
$$Speedup \ S = \frac{n \times t_n}{(k+n-1) \times t_p}$$
If we take the limit of this as n approaches infinity, we see that $(k + n − 1)$ approaches $n$, which results in a theoretical speedup of:
$$Speedup \ S = \frac{k \times t_p}{t_p} = k$$

From our preceding discussion of speedup, it might appear that the more stages that exist in the pipeline, the faster everything will run. This is true to a point. 
- There is a fixed overhead involved in moving data from memory to registers. 
- The amount of control logic for the pipeline also increases in size proportional to the number of stages, thus slowing down total execution. 
- In addition, there are several conditions that result in “pipeline conflicts,” which keep us from reaching the goal of executing one instruction per clock cycle.


### Pipeline Conflicts
#### Resource Conflicts  

#### Data Dependencies 

#### Conditional Branch Statements


### Predicated Instructions




#TODO 


## Ref

