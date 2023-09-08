# Software Testing

[TOC]



## Res
[Prototype Testing Tutorial](https://www.softwaretestinghelp.com/prototype-testing-tutorial/)

[Pilot Testing – A Complete Guide](https://www.softwaretestinghelp.com/what-is-pilot-testing/) 


【2022最新软件测试自学教程 新手小白30天软件测试入门最强教程】 https://www.bilibili.com/video/BV1NM4y1K73T/?p=33&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d



## Intro
> 🔗 https://en.wikipedia.org/wiki/Software_testing

**Software testing** is the act of examining the artifacts and the behavior of the [software](https://en.wikipedia.org/wiki/Software) under test by validation and verification. Software testing can also provide an objective, independent view of the software to allow the business to appreciate and understand the risks of software implementation. Test techniques include, but not necessarily limited to:

- analyzing the product requirements for completeness and correctness in various contexts like industry perspective, business perspective, feasibility and viability of implementation, usability, performance, security, infrastructure considerations, etc.
- reviewing the product architecture and the overall design of the product
- working with product developers on improvement in coding techniques, design patterns, tests that can be written as part of code based on various techniques like boundary conditions, etc.
- executing a program or application with the intent of examining behavior
- reviewing the deployment infrastructure and associated scripts and automation
- take part in production activities by using monitoring and observability techniques


### Error, Faults and Failures
Software faults occur through the following process: A programmer makes an [error](https://en.wikipedia.org/wiki/Human_error) (mistake), which results in a [fault](https://en.wikipedia.org/wiki/Fault_(technology)) (defect, bug) in the software source code. If this fault is executed, in certain situations the system will produce wrong results, causing a [failure](https://en.wikipedia.org/wiki/Failure).

- Not all faults will necessarily result in failures. For example, faults in the [dead code](https://en.wikipedia.org/wiki/Dead_code) will never result in failures. 
  - A fault that did not reveal failures may result in a failure when the environment is changed. Examples of these changes in environment include the software being run on a new [computer hardware](https://en.wikipedia.org/wiki/Computer_hardware) platform, alterations in [source data](https://en.wikipedia.org/wiki/Source_data), or interacting with different software. A single fault may result in a wide range of failure symptoms.

- Not all software faults are caused by coding errors. One common source of expensive defects is requirement gaps, that is, unrecognized requirements that result in errors of omission by the program designer. Requirement gaps can often be [non-functional requirements](https://en.wikipedia.org/wiki/Non-functional_requirements) such as [testability](https://en.wikipedia.org/wiki/Software_testability), [scalability](https://en.wikipedia.org/wiki/Scalability), [maintainability](https://en.wikipedia.org/wiki/Maintainability), [performance](https://en.wikipedia.org/wiki/Computer_performance), and [security](https://en.wikipedia.org/wiki/Computer_security).


### Input combinations and preconditions
A fundamental problem with software testing is that testing under *all* combinations of inputs and preconditions (initial state) is not feasible, even with a simple product. This means that the number of [faults](https://en.wikipedia.org/wiki/Software_bug) in a software product can be very large and defects that occur infrequently are difficult to find in testing and debugging. More significantly, [non-functional](https://en.wikipedia.org/wiki/Non-functional_requirements) dimensions of quality (how it is supposed to *be* versus what it is supposed to *do*) — [usability](https://en.wikipedia.org/wiki/Usability), [scalability](https://en.wikipedia.org/wiki/Scalability), [performance](https://en.wikipedia.org/wiki/Computer_performance), [compatibility](https://en.wikipedia.org/wiki/Backward_compatibility), and [reliability](https://en.wikipedia.org/wiki/Reliability_(engineering)) — can be highly subjective; something that constitutes sufficient value to one person may be intolerable to another.

Software developers can't test everything, but they can use combinatorial test design to identify the minimum number of tests needed to get the coverage they want. Combinatorial test design enables users to get greater test coverage with fewer tests. Whether they are looking for speed or test depth, they can use combinatorial test design methods to build structured variation into their test cases.



## Measurement in software testing
Quality measures include such topics as [correctness](https://en.wikipedia.org/wiki/Correctness_(computer_science)), completeness, [security](https://en.wikipedia.org/wiki/Computer_security_audit) and [ISO/IEC 9126](https://en.wikipedia.org/wiki/ISO/IEC_9126) requirements such as capability, [reliability](https://en.wikipedia.org/wiki/Reliability_engineering), [efficiency](https://en.wikipedia.org/wiki/Algorithmic_efficiency), [portability](https://en.wikipedia.org/wiki/Porting), [maintainability](https://en.wikipedia.org/wiki/Maintainability), compatibility, and [usability](https://en.wikipedia.org/wiki/Usability).


### Hierarchy of testing difficulty
Here lists several [testability](https://en.wikipedia.org/wiki/Software_testability) classes:

- Class I: there exists a finite complete test suite.
- Class II: any partial distinguishing rate (i.e., any incomplete capability to distinguish correct systems from incorrect systems) can be reached with a finite test suite.
- Class III: there exists a countable complete test suite.
- Class IV: there exists a complete test suite.
- Class V: all cases.



## Testing Artifacts
### Test Plan


### Traceability matrix



### Test case



### Test script



### Test suite



### [Test fixture](https://en.wikipedia.org/wiki/Test_fixture) or test data



### Test harness



### Test run



## Testing Approach
### Static, Dynamic and Passive Testing



### Exploratory approach



### The "box" approach
#### White-box testing



#### Black-box testing



#### Visual testing



#### Grey-box testing



## 🪜 Testing Levels
↗️   [Testing Types](Testing%20Tyeps/Testing%20Types.md)

1. Unit testing
2. Integration testing
3. System testing
4. Acceptance testing



## 📡 Testing types, techniques, and tactics
> 🔗 https://en.wikipedia.org/wiki/Software_testing#Testing_types,_techniques_and_tactics



↗️   [Testing Types](Testing Types.md) 



## 🌊 Testing Process

↗️ [Testing Model](Testing Model.md) 



## 🤖 Automated Testing

↗️ [Automated Testing](🤖 Automated Testing/Automated Testing.md) 



## 🐛 Software Defect (Bug)

↗️  [Software Defect](Software Defect.md) 



## Recommended Reading
- [Best Software Testing Tools 2023 [QA Test Automation Tools\]](https://www.softwaretestinghelp.com/tools/)
- [Alpha Testing and Beta Testing (A Complete Guide)](https://www.softwaretestinghelp.com/what-is-alpha-testing-beta-testing/)
- [Software Testing QA Assistant Job](https://www.softwaretestinghelp.com/software-testing-qa-assistant-job/)
- [Software Testing Course: Which Software Testing Institute Should I join?](https://www.softwaretestinghelp.com/which-software-testing-institute-should-i-join/)
- [Choosing Software Testing as your Career](https://www.softwaretestinghelp.com/choosing-software-testing-as-your-career/)
- [Software Testing Technical Content Writer Freelancer Job](https://www.softwaretestinghelp.com/software-testing-technical-content-writer-freelancer-job/)
- [Types of Risks in Software Projects](https://www.softwaretestinghelp.com/types-of-risks-in-software-projects/)
- [Best QA Software Testing Services from SoftwareTestingHelp](https://www.softwaretestinghelp.com/best-qa-software-testing-service-provider-company/)