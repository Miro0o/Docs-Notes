# QEMU Develop Guide

[TOC]



## Res
🏠 https://www.qemu.org/docs/master/specs/index.html



## Intro
This section of the manual documents various parts of the internals of QEMU. You only need to read it if you are interested in reading or modifying QEMU’s source code.

QEMU is a large and mature project with a number of complex subsystems that can be overwhelming to understand. The development documentation is not comprehensive but hopefully presents enough to get you started. If there are areas that are unclear please reach out either via the IRC channel or mailing list and hopefully we can improve the documentation for future developers.

All developers will want to familiarise themselves with [QEMU Community Processes](https://www.qemu.org/docs/master/devel/index-process.html#development-process) and how the community interacts. Please pay particular attention to the [QEMU Coding Style](https://www.qemu.org/docs/master/devel/style.html#coding-style) and [Submitting a Patch](https://www.qemu.org/docs/master/devel/submitting-a-patch.html#submitting-a-patch) sections to avoid common pitfalls.

If you wish to implement a new hardware model you will want to read through the [The QEMU Object Model (QOM)](https://www.qemu.org/docs/master/devel/qom.html#qom) documentation to understand how QEMU’s object model works.

Those wishing to enhance or add new CPU emulation capabilities will want to read our [TCG Emulation](https://www.qemu.org/docs/master/devel/index-tcg.html#tcg) documentation, especially the overview of the [Translator Internals](https://www.qemu.org/docs/master/devel/tcg.html#tcg-internals).
- [QEMU Community Processes](https://www.qemu.org/docs/master/devel/index-process.html)
- [QEMU Build and Test System](https://www.qemu.org/docs/master/devel/index-build.html)
- [Internal QEMU APIs](https://www.qemu.org/docs/master/devel/index-api.html)
- [Internal Subsystem Information](https://www.qemu.org/docs/master/devel/index-internals.html)
- [TCG Emulation](https://www.qemu.org/docs/master/devel/index-tcg.html)



## Ref

