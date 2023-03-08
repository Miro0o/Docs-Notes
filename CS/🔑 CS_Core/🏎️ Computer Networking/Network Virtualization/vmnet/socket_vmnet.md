# socket_vmnet

[TOC]



🏠 https://github.com/lima-vm/socket_vmnet

## Overview
`socket_vmnet` provides [vmnet.framework](https://developer.apple.com/documentation/vmnet) support for QEMU.

`socket_vmnet` does not require QEMU to run as the root user.

(But `socket_vmnet` itself has to run as the root, in most cases.)

`socket_vmnet` was forked from [`vde_vmnet`](https://github.com/lima-vm/vde_vmnet) v0.6.0. Unlike `vde_vmnet`, `socket_vmnet` does not depend on VDE.

#TODO 