# CS162: Operating System

[TOC]



## Res
### 课程资源
- 课程网站：[https://cs162.org/](https://cs162.org/)
- 课程视频：[https://www.youtube.com/watch?v=YfHY0pvpRkk](https://www.youtube.com/watch?v=YfHY0pvpRkk)，每节课的链接参见课程网站
- 课程教材：[Operating Systems: Principles and Practice (2nd Edition)](http://ospp.cs.washington.edu/)
- 课程作业：[https://cs162.org/](https://cs162.org/)，6 个 Homework, 3 个 Project，具体要求参见课程网站


### 资源汇总
由于北大的操统实验班采用了该课程的 Project，为了防止代码抄袭，我的代码实现没有开源。



## 课程简介
- 所属大学：UC Berkeley
- 先修要求：CS61A, CS61B, CS61C
- 编程语言：C, x86汇编
- 课程难度：🌟🌟🌟🌟🌟🌟
- 预计学时：200 小时+，上不封顶

这门课让我记忆犹新的有两个部分：

首先是教材，这本书用的教材 _Operating Systems: Principles and Practice (2nd Edition)_ 一共四卷，写得非常深入浅出，很好地弥补了 MIT6.S081 在理论知识上的些许空白，非常建议大家阅读。相关资源会分享在本书的经典书籍推荐模块。

其次是这门课的 Project —— Pintos。Pintos 是由 Ben Pfaff 等人在 x86 平台上编写的教学用操作系统，Ben Pfaff 甚至专门发了篇 [paper](https://benpfaff.org/papers/pintos.pdf) 来阐述 Pintos 的设计思想。

和 MIT 的 xv6 小而精的 lab 设计理念不同，Pintos 更注重系统的 Design and Implementation。Pintos 本身仅一万行左右，只提供了操作系统最基本的功能。而 4 个Project，就是让你在这个极为精简的操作系统之上，分别为其增加线程调度机制 (Project1)，系统调用 (Project2)，虚拟内存 (Project3) 以及文件系统 (Project4)。所有的 Project 都给学生留有很大的设计空间，总代码量在 2000 行左右。根据 Stanford 学生[自己的反馈](https://www.quora.com/What-is-it-like-to-take-CS-140-Operating-Systems-at-Stanford)，在 3-4 人组队的情况下，后两个 Project 的人均耗时也在 40 个小时以上。

虽然难度很大，但 Stanford, Berkeley, JHU 等多所美国顶尖名校的操统课程均采用了 Pintos。如果你真的对操作系统很感兴趣，Pintos 会极大地提高你编写和 debug 底层系统代码的能力。在本科阶段，能自己设计、实现并 debug 一个大型系统，是一段非常珍贵的经历。

北大 2022 年春季学期的操作系统实验班也将会首次引入 Pintos 作为课程 Project。我和该课程的[另一位助教](https://github.com/AlfredThiel)整理并完善了 Pintos 的[实验文档](https://alfredthiel.gitbook.io/pintosbook/)，并利用 Docker 配置了跨平台的实验环境，想自学的同学可以按文档自行学习。在毕业前的最后一个学期，希望能用这样的尝试，让更多人爱上系统领域，为国内的系统研究添砖加瓦。
