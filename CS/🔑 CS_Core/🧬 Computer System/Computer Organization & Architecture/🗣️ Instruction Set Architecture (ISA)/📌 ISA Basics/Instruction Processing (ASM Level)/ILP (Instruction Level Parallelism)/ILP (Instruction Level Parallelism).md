# ILP (Instruction Level parallelism)

[TOC]



## Res
↗ [Parallel & Multiprocessor Architectures](../../../../../Computer%20Microarchitectures%20(Computer%20Organization)/Computer%20Processors/Multiprocessor%20and%20Multicore%20Organization/Parallel%20&%20Multiprocessor%20Architectures/Parallel%20&%20Multiprocessor%20Architectures.md)



## Intro


## Instruction Pipelining
As noted at ↗ [Instruction Piplining](Instruction%20Piplining.md)



## Superscalar
Superscalar architectures (as you may recall from Chapter 4) perform multiple operations at the same time by employing parallel pipelines. Examples of superscalar architectures include IBM’s PowerPC, Sun’s UltraSPARC, and DEC’s Alpha.

Superscalar and VLIW machines fetch and execute more than one instruction per cycle.
#TODO 



## Super-pipelining
Super-pipelining architectures combine superscalar concepts with pipelining by dividing the pipeline stages into smaller pieces



## VLIW
very long instruction word

The IA-64 architecture exhibits a VLIW architecture, which means that each instruction can specify multiple scalar operations (the compiler puts multiple operations into a single instruction). 

Superscalar and VLIW machines fetch and execute more than one instruction per cycle.

#TODO 


## EPIC
Explicitly Parallel Instruction Computers



## Ref

