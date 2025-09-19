# Software Analysis Basics

[TOC]



## Res
### Related Topics
↗ [Software Quality Assurance (SQA)](../../../../../Software%20Engineering/🎭%20Software%20Quality%20Assurance%20(SQA)/Software%20Quality%20Assurance%20(SQA).md)
↗ [ICT System Reliability (Correctness) & Verification](../../../../⛈️%20Risk%20Management/🦟%20Vulnerabilities/ICT%20System%20Reliability%20(Correctness)%20&%20Verification.md)

↗ [Computer Languages & Programming Methodology](../../../../../🔑%20CS%20Core/👩‍💻%20Computer%20Languages%20&%20Programming%20Methodology/Computer%20Languages%20&%20Programming%20Methodology.md)
- ↗ [Programming Language Theory (PLT)](../../../../../🔑%20CS%20Core/👩‍💻%20Computer%20Languages%20&%20Programming%20Methodology/🐢%20Programming%20Language%20Theory%20(PLT)/Programming%20Language%20Theory%20(PLT).md)
↗ [Program Language Translation & Compilation Theory (Compile-time)](../../../../../🔑%20CS%20Core/🛣️%20Program%20Compilation%20&%20Execution/🚮%20Program%20Language%20Translation%20&%20Compilation%20Theory%20(Compile-time)/Program%20Language%20Translation%20&%20Compilation%20Theory%20(Compile-time).md)
↗ [Compilation & Program Loading Tools](../../../../../🔑%20CS%20Core/👩‍💻%20Computer%20Languages%20&%20Programming%20Methodology/🛠️%20Programming%20Tool%20Chain/Compilation%20&%20Program%20Loading%20Tools/Compilation%20&%20Program%20Loading%20Tools.md)


### Other Resources
↗ [NJU /软件分析](../../../../../🗺%20CS%20Overview/💋%20Intro%20to%20Computer%20Science/👩🏼‍🏫%20Courses%20of%20Universities/NJU%20南京大学/软件分析/软件分析.md)
- 《（静态）软件分析》课程网站（含课件、实验作业、实验文档）： https://tai-e.pascal-lab.net/lectures.html 
- 《（静态）软件分析》实验作业在线评测：https://oj.pascal-lab.net/
- [南京大学《软件分析》课程01（Introduction）](https://www.bilibili.com/video/BV1b7411K7P4?spm_id_from=333.788.comment.all.click) 
- [南京大学《软件分析》课程02（Intermediate Representation）](https://www.bilibili.com/video/BV1zE411s77Z?spm_id_from=333.788.comment.all.click) 
- [南京大学《软件分析》课程03（Data Flow Analysis I）](https://www.bilibili.com/video/BV1oE411K79d?spm_id_from=333.788.comment.all.click) 
- [南京大学《软件分析》课程04（Data Flow Analysis II）](https://www.bilibili.com/video/BV19741197zA?spm_id_from=333.788.comment.all.click) 
- [南京大学《软件分析》课程05（Data Flow Analysis - Foundations I）](https://www.bilibili.com/video/BV1A741117it?spm_id_from=333.788.comment.all.click) 
- [南京大学《软件分析》课程06（Data Flow Analysis - Foundations II）](https://www.bilibili.com/video/BV1964y1M7nL?spm_id_from=333.788.comment.all.click) 
- [南京大学《软件分析》课程07（Interprocedural Analysis）](https://www.bilibili.com/video/BV1GQ4y1T7zm?spm_id_from=333.788.comment.all.click) 
- [南京大学《软件分析》课程08（Pointer Analysis）](https://www.bilibili.com/video/BV1gg4y1z78p?spm_id_from=333.788.comment.all.click) 
- [南京大学《软件分析》课程09（Pointer Analysis - Foundations I）](https://www.bilibili.com/video/BV1NS4y1Q7UJ?spm_id_from=333.788.comment.all.click) 
- [南京大学《软件分析》课程10（Pointer Analysis - Foundations II）](https://www.bilibili.com/video/BV1fb4y1i7HY?spm_id_from=333.788.comment.all.click) 
- [南京大学《软件分析》课程11（Pointer Analysis - Context Sensitivity I）](https://www.bilibili.com/video/BV1wQ4y1v72e?spm_id_from=333.788.comment.all.click) 
- [南京大学《软件分析》课程12（Pointer Analysis - Context Sensitivity II）](https://www.bilibili.com/video/BV1aR4y1x7Zk?spm_id_from=333.788.comment.all.click) 
- [南京大学《软件分析》课程13（Static Analysis for Security）](https://www.bilibili.com/video/BV1Fq4y1B74m?spm_id_from=333.788.comment.all.click) 
- [南京大学《软件分析》课程14（Datalog-Based Program Analysis）](https://www.bilibili.com/video/BV1wa411k7Uv?spm_id_from=333.788.comment.all.click) 
- [南京大学《软件分析》课程15（CFL-Reachability and IFDS）](https://www.bilibili.com/video/BV1gL411j7vS?spm_id_from=333.788.comment.all.click) 
- [南京大学《软件分析》课程16（Soundness and Soundiness）](https://www.bilibili.com/video/BV1d3411s7tt?spm_id_from=333.788.comment.all.click)

https://www2.compute.dtu.dk/courses/02242/
https://courses.compute.dtu.dk/02242
02242: Program Analysis
Christian Gram Kalhauge | DTU

|No|Date|Topic|
|---|---|---|
|`01`|`2024-09-02`|[Introduction](https://courses.compute.dtu.dk/02242/topics/introduction.html)|
|`02`|`2024-09-09`|[Syntactic Analysis](https://courses.compute.dtu.dk/02242/topics/syntactic-analysis.html)|
|`03`|`2024-09-16`|[Semantics](https://courses.compute.dtu.dk/02242/topics/semantics.html)|
|`04`|`2024-09-23`|[Dynamic Analysis](https://courses.compute.dtu.dk/02242/topics/dynamic-analysis.html)|
|`05`|`2024-09-30`|[Bounded Static Analysis](https://courses.compute.dtu.dk/02242/topics/bounded-static-analysis.html)|
|`06`|`2024-10-07`|Recap / Project / QA|
|--|`2024-10-14`|Autumn holiday|
|`07`|`2024-10-21`|Self Study // Feedback From Proposals|
|`08`|`2024-10-28`|[Unbounded Static Analysis](https://courses.compute.dtu.dk/02242/topics/unbounded-static-analysis.html)|
|`09`|`2024-11-04`|[Concolic Execution](https://courses.compute.dtu.dk/02242/topics/concolic-execution.html)|
|`10`|`2024-11-11`|[How to write a good paper](https://courses.compute.dtu.dk/02242/topics/how-to-write-a-paper.html)|
|`11`|`2024-11-18`|Self Study // Peer Feedback On Papers|
|`12`|`2024-11-25`|[Context Sensitive Analysis](https://courses.compute.dtu.dk/02242/topics/context-sensitive-analysis.html)|
|`13`|`2024-12-02`|Q/A & How to-do a good presentation|
|--|`2024-12-10`|Exam|



## Intro: Software Analysis
![](../../../../../../Assets/Pics/Screenshot%202025-09-06%20at%2000.52.22.png)
<small>【南京大学《软件分析》课程01（Introduction）】 <a>https://www.bilibili.com/video/BV1b7411K7P4</a></small>

> 🎬 [Math's Fundamental Flaw - Veritasium](https://www.youtube.com/watch?v=HeQX2HjkcNo)


### Program and Program Analysis
> ↗ [The Essence of Computing - Program](../../../../../🗺%20CS%20Overview/The%20Essence%20of%20Computing%20-%20Program.md)

> 🔗 https://courses.compute.dtu.dk/02242/topics/introduction.html##sec:2

Back in the beginning of 20th century, a group of logician where obsessed with coming up with a system for proving all things in mathematics. The problem was that a [foundational crisis](https://en.wikipedia.org/wiki/Foundations_of_mathematics#Foundational_crisis) had emerged. Many mathematical theories had holes in them, or was able to prove theorems which are false [E.g ., Russell's paradox](https://en.wikipedia.org/wiki/Russell%27s_paradox).

To this end they came up with different systems for automatically proving things. David Hilbert came up with the [Hilbert's program](https://en.wikipedia.org/wiki/Hilbert%27s_program), and Alanzo Church came up with the [Lambda Calculus](https://en.wikipedia.org/wiki/Lambda_calculus). The underlying idea was, if we could come up with an automatic procedure for producing everything that is true, we can recursively enumerate all true things. This is known as recursively axiomatizable.

However, they quickly ran into a problem: how can we prove that these programs actually terminate? This is the fundamental program analysis question, and it strangely came before the program.

---
**What is a Program?**
To talk about program analysis, we first have to define what we mean when we say _program_. A program in the context of this course is going to be a **_structured object_** that exhibit some _behavior_ when executed.

> **Definition 1**: Program
> A program is structured object p∈L, from a language L, with a step function from state to state:
> - 𝚜𝚝𝚎𝚙: $𝐒𝐭𝐚𝐭𝐞 \to 𝐒𝐭𝐚𝐭𝐞$

==When executing a program, we often want to run it until it changes the state. This is called a **_fixpoint_**, or running the program to completion.==

---
**What is Program Analysis?** 
**_Program analysis_** is the art of extracting facts about the structure or the possible behavior from a program. These facts could be does the program eventually come to a halt, is the program well-formatted, or will my program exhibit a bug. 

In summary, program analysis is:
- Using automatic techniques to figure out facts about a computer program.

For simple languages, it is relatively easy to figure out what they do. For example, `1 + 2` will always execute to `3`. But, program analysis, in general, is extremely hard.

> 🔗 https://en.wikipedia.org/wiki/Decidability_(logic)
> 🔗 https://en.wikipedia.org/wiki/Program_analysis
> 
> In computer science, program analysis[1] is the process of analyzing the behavior of computer programs regarding a **property** such as correctness, robustness, safety and liveness. Program analysis focuses on two major areas: program optimization and program correctness. The first focuses on improving the program’s performance while reducing the resource usage while the latter focuses on ensuring that the program does what it is supposed to do.


### Scope of Program Analysis
#### Undecidability of Program Analysis
> ↗ [Church–Turing Thesis (Computability Thesis)](../../../../../🧮%20Mathematics/🤼‍♀️%20Mathematical%20Logic/😶‍🌫️%20Theory%20of%20Computation/Computability%20Theory%20-%20Turing%20Machine%20and%20R.E.%20Language/Church–Turing%20Thesis%20(Computability%20Thesis).md)

> 🔗 https://courses.compute.dtu.dk/02242/topics/introduction.html##sec:1.3

**A Turing-Complete Mess**
https://en.wikipedia.org/wiki/Turing_completeness

We are going to focus most our energy on programs from languages that are _Turing complete_. Turing complete languages are languages in which you can write any program executable on a machine. This class of programs is also what you are mostly familiar with. Java, C, Python, etc ., are all Turing complete languages. Even [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck) and [PowerPoint](https://www.youtube.com/watch?v=_3loq22TxSc) are Turing complete.

Using a Turing complete language is a double edge sword: while it is nice that it is powerful enough to do everything, it is also powerful enough to:
- fire the missiles,
- **not** fire the missiles,
- never terminate,
- kill grandma, and worst of all
- throw a null pointer exception!

So it would be nice be warned if any of these things might happen. However, that turns out to be very hard.

---
**The Halting problem**
https://en.wikipedia.org/wiki/Halting_problem

Consider the base of all analysis problems, the halting problem:

> **Definition 2**: The Halting Problem
> Given **any** program $p \in L$ from the language $L$, decide if it is going to terminate (halt) when executed on a state $s$.

This problem turns out to be impossible to solve correctly for all programs of a Turing complete language. It is in fact _undecidable_. While for some programs it is easy to say with confidence that it does terminate. We can't build an mechanical procedure which can do this for every program.

The argument goes a little like this. Consider you have a mechanical procedure for solving the halting problem, in that case we can encode it as a program:

```python
def does_halt(p : Program) -> bool:
    ...
```

Now we can use this program in another program:

```python
def main():
    while does_halt(main):
        print("Running")
```

This is a weird program: We can see that if `main` halts, it runs forever, and if it runs forever it will eventually halt. This is of course impossible, which strongly suggest that `does_halt` cannot exist.

---
**General Undecidability of Program Analysis**

We could hope that the problem that we can't figure out if a program terminates or not is special and does not affect any of the other things we would like to know about the program. But, sadly this is not the case. **Almost any interesting thing you would like to know about the behavior of the program can be _reduced_ to the halting problem.** This fact is called **_Rice's theorem_**.

> 🔗 [Rice's Theorem | wikipedia](https://en.wikipedia.org/wiki/Rice's_theorem)
> 
> In [computability theory](https://en.wikipedia.org/wiki/Computability_theory "Computability theory"), **Rice's theorem** states that all non-trivial semantic properties of programs are [undecidable](https://en.wikipedia.org/wiki/Undecidable_problem "Undecidable problem"). A _semantic_ property is one about the program's behavior (for instance, "does the program [terminate](https://en.wikipedia.org/wiki/Halting_problem "Halting problem") for all inputs?"), unlike a syntactic property (for instance, "does the program contain an [if-then-else](https://en.wikipedia.org/wiki/If-then-else "If-then-else") statement?"). A _non-trivial_ property is one which is neither true for every program, nor false for every program.
> 
> The theorem generalizes the undecidability of the [halting problem](https://en.wikipedia.org/wiki/Halting_problem "Halting problem"). It has far-reaching implications on the feasibility of [static analysis](https://en.wikipedia.org/wiki/Static_program_analysis "Static program analysis") of programs. It implies that it is impossible, for example, to implement a tool that checks whether any given program is [correct](https://en.wikipedia.org/wiki/Correctness_\(computer_science\) "Correctness (computer science)"), or even executes without error (it is possible to implement a tool that always overestimates or always underestimates, so in practice one has to decide what is less of a problem).
> 
> The theorem is named after [Henry Gordon Rice](https://en.wikipedia.org/wiki/Henry_Gordon_Rice "Henry Gordon Rice"), who proved it in his doctoral dissertation of 1951 at [Syracuse University](https://en.wikipedia.org/wiki/Syracuse_University "Syracuse University").

For example, since figuring out the halting problem is impossible, we can't say if the following problem actually fires the nukes:

```python
def main():
    something_that_might_go_forever()
    fire_the_nukes()
```

However, all hope is not lost! Although it's mathematically impossible to make a **perfect** program analysis, one can still make it a **useful** program analysis.
#### Soundness & Completeness
> ↗  [Mathematical Logic Basics (Formal Logic) /Soundness & Completeness](../../../../../🧮%20Mathematics/🤼‍♀️%20Mathematical%20Logic/📍%20Mathematical%20Logic%20Basics%20(Formal%20Logic)/Mathematical%20Logic%20Basics%20(Formal%20Logic).md#Soundness%20&%20Completeness)

> 🔗 https://courses.compute.dtu.dk/02242/topics/introduction.html##sec:1.6

In most cases, you either care that something _may_ happen, or that it _must_ happen. In the program from before, we can quite easily say that it **may** fire the nukes. If we do not want the nukes from not being fired, we can flag this as a bug. However, we might also build a missile luncher, in which case the nukes **must** be fired when press the red button.

These kinds of analyses allows us to error one of the sides. Here we steal some nomenclature from ↗ [Mathematical Logic](../../../../../🧮%20Mathematics/🤼‍♀️%20Mathematical%20Logic/Mathematical%20Logic.md). In logic **_soundness_** means that every provable statement is true, and **_completeness_** means that every true statement is provable.

> **Definition 3**: Soundness
> In a sound system, we can only prove true things.
> - if we can prove $\Phi$ given $\Sigma$
> 	- i.e. $(\Sigma \vdash \Phi)$ 
> - then $\Phi$ is **true** given $\Sigma$
> 	- i.e. $(\Sigma \models Φ)$
> - i.e. $\Sigma \vdash \Phi \implies \Sigma \models \Phi$

> **Definition 4**: Completeness
> In a complete system, we can prove all true things. 
> - if $\Phi$ is **true** given $\Sigma$
> 	- $(\Sigma \models \Phi)$
> - then $\phi$ is provable given $\Sigma$
> 	- $(\Sigma \vdash \Phi)$
> - i.e. $\Sigma \models \Phi \implies \Sigma \vdash \Phi$

Translated into program analysis jargon, we say an analysis is sound if when it produce a fact, then that is a real fact, and complete if it always can find a fact about the program if it is there. ==Because the problem we are talking about is **undecidable**, we CANNOT both be sound and complete.==

![|500](../../../../../../Assets/Pics/Screenshot%202025-09-08%20at%2023.56.20.png)
![](../../../../../../Assets/Pics/Pasted%20image%2020250908234809.png)
##### A Relaxed Goal: Approximative Answers
> 📖 Static Program Analysis | Anders Møller and Michael I. Schwartzbach

While it is impossible to build an analysis that would correctly decide a property for any analyzed program, it is often possible to build analysis tools that give useful answers for most realistic programs. As the ideal analyzer does not exist, there is always room for building more precise approximations (which is colloquially called the full employment theorem for static program analysis designers).

Approximative answers may be useful for finding bugs in programs, which may be viewed as a weak form of program verification. 

> 🔗 [In Defense of Soundness: A Manifesto](https://dl.acm.org/doi/pdf/10.1145/2644805)
> [...], virtually all published whole program analyses are unsound and omit conservative handling of common language features when applied to real programming languages.
#### FP,TN,FN vs TP
It is also useful to talk about how a program analysis has performed on individual programs or bugs. To do this we use nomenclature from [classification](https://en.wikipedia.org/wiki/Binary_classification).

An individual proposition Φ is either a true positive, true negative, false positive, or false negative, following the table below:

|                            | $(\Sigma \not\models \Phi)$ | $(\Sigma \models \Phi)$ |
| -------------------------- | --------------------------- | ----------------------- |
| $(\Sigma \not\vdash \Phi)$ | True Negative               | False Negative          |
| $(\Sigma \vdash \Phi)$     | False Positive              | True Positive           |

![](../../../../../../Assets/Pics/Pasted%20image%2020250908234329.png)

A sound analysis, therefore, has no false positives, and a complete analysis has no false negatives.


### Software Analysis Taxonomy
> 🔗 https://courses.compute.dtu.dk/02242/topics/introduction.html##sec:2

- Manual vs Automatic Analysis
	- The difference between manual and automatic analysis, is whether we have a well-defined procedure for analysing the code.
	- In many cases manual inspection is a crucial companion to automatic analysis. If taken to the extreme, we can actually require the user of the tool to prove to us that the code is correct. Now we only have to check the proof, which case we are entering the world of _Program Verification_.
- Syntactic vs Semantic Analysis
	- The difference between a syntactic and a semantic analysis is whether we focus on the **structure** of the program or on the **meaning** of the program.
	- The structure of the program or syntax is often represented as a tree of nodes as recognized by the parser.
	- In contrast the meaning of the program or semantics is represented as a set of all possible traces of a program. Here trace means a sequence of states and operations possible by the program.
- ↗ [SCA (Static Code Analysis) & SAST](👚%20SCA%20(Static%20Code%20Analysis)%20&%20SAST/SCA%20(Static%20Code%20Analysis)%20&%20SAST.md) 🆚 ↗ [DCA (Dynamic Code Analysis) & DAST](👙%20DCA%20(Dynamic%20Code%20Analysis)%20&%20DAST/DCA%20(Dynamic%20Code%20Analysis)%20&%20DAST.md)
	- Finally we can differentiate between dynamic and static analysis. A dynamic analysis interpolates the meaning of the program from a single trace, where a static analysis tries to predict all possible behaviors.
	- Dynamic analysis are often just executing the programs, and then reporting any behavior it exhibits. An dynamic analysis often have proof of the bad behavior. A dynamic analysis is **sound** if every behavior it finds is a real behavior, and **complete** if can find all behaviors.
	- Static analyses in contrast consider the entire programs, and then reports if the program is without bugs or problems. When a good static analysis says your program is good, it probably is, however, when it finds a potential bug, it can often not prove it to you. A static analysis is **sound** if every program it flags do exhibit some behavior, and **complete** if it flags all programs that contain the behavior.
	- It is sometimes a great idea to do a mix of a dynamic and static analysis, in which case we call it a **_hybrid_ analysis**.


**Interactive Application Security Testing (IAST)**
> 🔗 https://en.wikipedia.org/wiki/Interactive_application_security_testing

Interactive application security testing (abbreviated as IAST) is a security testing method that detects software vulnerabilities by interaction with the program coupled with observation and sensors. The tool was launched by several application security companies. It is distinct from static application security testing, which does not interact with the program, and dynamic application security testing, which considers the program as a black box. It may be considered a mix of both



## Ref
[Implies (⇒) vs. Entails (⊨) vs. Provable (⊢) | Mathematics]: https://math.stackexchange.com/a/286093/1230830
[Soundness and Completeness: Defined With Precision - By Bertrand Meyer | ACM]: https://cacm.acm.org/blogcacm/soundness-and-completeness-defined-with-precision/
