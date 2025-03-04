# Program Execution (Runtime)

[TOC]



## Res
### Related Topics
↗ [Operating System Kernel (Kernel Mode)](../../👷🏾‍♂️%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/😴%20Operating%20System%20Components%20&%20Runtime%20Libraries/Operating%20System%20Kernel%20(Kernel%20Mode).md)
↗ [Operating System Components & Runtime Libraries](../../👷🏾‍♂️%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/😴%20Operating%20System%20Components%20&%20Runtime%20Libraries/Operating%20System%20Components%20&%20Runtime%20Libraries.md)

↗ [ASM (Assembly Languages)](../../👩‍💻%20Computer%20Languages%20&%20Programming%20Methodology/ASM%20(Assembly%20Languages)/ASM%20(Assembly%20Languages).md)
- ↗ [8086 ASM (16 bit)](../../👩‍💻%20Computer%20Languages%20&%20Programming%20Methodology/ASM%20(Assembly%20Languages)/x86%20ISA%20Based%20ASM/8086%20ASM%20(16%20bit).md)
↗ [Instruction Set Architecture (ISA) & Processor Architecture](../../👷🏾‍♂️%20Computer%20System/Computer%20Architecture/Instruction%20Set%20Architecture%20(ISA)%20&%20Processor%20Architecture/Instruction%20Set%20Architecture%20(ISA)%20&%20Processor%20Architecture.md)
↗ [Instruction Basics](../../👷🏾‍♂️%20Computer%20System/Computer%20Architecture/Instruction%20Set%20Architecture%20(ISA)%20&%20Processor%20Architecture/📌%20ISA%20Basics/📌%20Instruction%20Basics/Instruction%20Basics.md)
↗ [Instruction Execution](Instruction%20Execution/Instruction%20Execution.md)

↗ [File Types & File Formats /Executable](../../👷🏾‍♂️%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/OS%20IO%20System/IO%20Generality%20(via%20Abstraction)/File%20&%20File%20System/File%20Types%20&%20File%20Formats.md)

↗ [OS Processes & Automata Management (CPU + Main Memory Resource)](../../👷🏾‍♂️%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/OS%20Processes%20&%20Automata%20Management%20(CPU%20+%20Main%20Memory%20Resource)/OS%20Processes%20&%20Automata%20Management%20(CPU%20+%20Main%20Memory%20Resource).md)
- ↗ [System Calls](../../👷🏾‍♂️%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/OS%20Processes%20&%20Automata%20Management%20(CPU%20+%20Main%20Memory%20Resource)/📌%20Processes%20Description%20&%20Control/System%20Calls/System%20Calls.md)
↗ [OS Memory Management (Main Memory + Secondary Memory Resource)](../../👷🏾‍♂️%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/OS%20Memory%20Management%20(Main%20Memory%20+%20Secondary%20Memory%20Resource)/OS%20Memory%20Management%20(Main%20Memory%20+%20Secondary%20Memory%20Resource).md)
- ↗ [Address Space & Memory Layout](../../👷🏾‍♂️%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/OS%20Memory%20Management%20(Main%20Memory%20+%20Secondary%20Memory%20Resource)/Address%20Space%20&%20Memory%20Layout.md)
- ↗ [Virtual Memory (OS Software Level)](../../👷🏾‍♂️%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/OS%20Memory%20Management%20(Main%20Memory%20+%20Secondary%20Memory%20Resource)/Virtual%20Memory%20(OS%20Software%20Level)/Virtual%20Memory%20(OS%20Software%20Level).md)

↗ [Primary Storage (Main Memory) Technologies & RAM](../../👷🏾‍♂️%20Computer%20System/Computer%20Architecture/Computer%20Microarchitectures%20(Computer%20Organization)%20&%20von%20Neumann%20Model/Computer%20Memory%20&%20Storage/Primary%20Storage%20(Main%20Memory)%20Technologies%20&%20RAM/Primary%20Storage%20(Main%20Memory)%20Technologies%20&%20RAM.md)
↗ [Virtual Memory (Hardware and Control Structure)](../../👷🏾‍♂️%20Computer%20System/Computer%20Architecture/Computer%20Microarchitectures%20(Computer%20Organization)%20&%20von%20Neumann%20Model/Computer%20Memory%20&%20Storage/Primary%20Storage%20(Main%20Memory)%20Technologies%20&%20RAM/Virtual%20Memory%20(Hardware%20and%20Control%20Structure)/Virtual%20Memory%20(Hardware%20and%20Control%20Structure).md)


### Other Resources
https://textbook.cs161.org/memory-safety/x86.html
x86 Assembly and Call Stack | UCB CS161 Computer Security Textbook

📃 https://cpu.land
Putting the “You” in CPU
Curious exactly what happens when you run a program on your computer? Read this article to learn how multiprocessing works, what system calls really are, how computers manage memory with hardware interrupts, and how Linux loads executables.
- [Ch. 0 Intro](https://cpu.land/)
- [Ch. 1 Basics](https://cpu.land/the-basics)
- [Ch. 2 Multitasking](https://cpu.land/slice-dat-time)
- [Ch. 3 Exec](https://cpu.land/how-to-run-a-program)
- [Ch. 4 ELF](https://cpu.land/becoming-an-elf-lord)
- [Ch. 5 Paging](https://cpu.land/the-translator-in-your-computer)
- [Ch. 6 Fork-Exec](https://cpu.land/lets-talk-about-forks-and-cows)
- [Ch. 7 Epilogue](https://cpu.land/epilogue)



## Intro
![application_execution_and_computer_data_flow.excalidraw|800](../../../../Assets/Illustrations/Computer%20System/application_execution_and_computer_data_flow.excalidraw.md)


### Program = Automata
↗ [Program, Computer, and Automation](../../../🗺%20CS%20Overview/Program,%20Computer,%20and%20Automation.md)

- (computing resources) CPU
- (storage resources) Register + Address Space

>  Here either register or address space are all conceptual, they are the virtualization of the actual hardware. Register here refers to specific ISA defined registers, not those computer microarchitecture actually has; address space, by the same token, is the virtual memory layout visible to users, not the physical memory layout.

- (program) instructions + data


### Program Execution: Software Perspective
↗ [Procedure (Function) Call & Runtime Memory Layout](Procedure%20(Function)%20Call%20&%20Runtime%20Memory%20Layout.md)


### Program Execution: Hardware Perspective
↗ [Instruction Execution](Instruction%20Execution/Instruction%20Execution.md)



## 🤔 An Example: How C Program Executed on Linux? /C Program Startup Process
> 🔗 https://www.gnu.org/software/hurd/glibc/startup.html

**Statically-linked program**
- The ELF headers points program start at `_start`.
- `_start` (sysdeps/mach/hurd/i386/static-start.S) calls `_hurd_stack_setup`
- `_hurd_stack_setup` (sysdeps/mach/hurd/i386/init-first.c) calls `first_init` which calls `__mach_init` to initialize enough to run RPCs, then runs the `_hurd_preinit_hook` hooks, which initialize global variables of libc.
- `_hurd_stack_setup` (sysdeps/mach/hurd/i386/init-first.c) calls `_hurd_startup`.
- `_hurd_startup` (hurd/hurdstartup.c) gets hurdish information from servers and calls its `main` parameter.
- the `main` parameter was actually `doinit` (in sysdeps/mach/hurd/i386/init-first.c), which mangles the stack and calls `doinit1` which calls `init`.
- `init` sets threadvars, tries to initialize threads (and perhaps switches to the new stack) and gets to call `init1`.
- `init1` gets the Hurd block, calls `_hurd_init` on it
- `_hurd_init` (hurd/hurdinit.c) initializes initial ports, starts the signal thread, runs the `_hurd_subinit` hooks (`init_dtable` hurd/dtable.c notably initializes the FD table and the `_hurd_fd_subinit` hooks, which notably checks `std*`).
- We are back to `_start`, which jumps to `_start1` which is the normal libc startup which calls `__libc_start_main`
- `__libc_start_main` (actually called `LIBC_START_MAIN` in csu/libc-start.c) initializes libc, tls, libpthread, atexit
- `__libc_start_main` calls initialization function given as parameter `__libc_csu_init`,
- `__libc_csu_init` (csu/elf-init.c) calls `preinit_array_start` functions
- `__libc_csu_init` calls `_init`
- `_init` (sysdeps/i386/crti.S) calls `PREINIT_FUNCTION`, (actually libpthread on Linux, `__gmon_start__` on hurd)
- back to `__libc_csu_init` calls `init_array_start` functions
- back to `__libc_start_main`, it calls calls application's `main`, then `exit`.

![](../../../../Assets/Pics/Pasted%20image%2020240925195819.png)
<small>http://dbp-consulting.com/tutorials/debugging/linuxProgramStartup.html
</small>


**dynamically-linked program**
- dl.so ELF headers point its start at `_start`.
- `_start` (sysdeps/i386/dl-machine.h) calls `_dl_start`.
- `_dl_start` (elf/rtld.c) initializes `bootstrap_map`, calls `_dl_start_final`
- `_dl_start_final` calls `_dl_sysdep_start`.
- `_dl_sysdep_start` (sysdeps/mach/hurd/dl-sysdep.c) calls `__mach_init` to initialize enough to run RPCs, then calls `_hurd_startup`.
- `_hurd_startup` (hurd/hurdstartup.c) gets hurdish information from servers and calls its `main` parameter.
- the `main` parameter was actually `go` inside `_dl_sysdep_start`, which calls `dl_main`.
- `dl_main` (elf/rtld.c) interprets ld.so parameters, loads the binary and libraries, calls `_dl_allocate_tls_init`.
- we are back to `go`, which branches to `_dl_start_user`.
- `_dl_start_user` (./sysdeps/i386/dl-machine.h) runs `RTLD_START_SPECIAL_INIT` (sysdeps/mach/hurd/i386/dl-machine.h) which calls `_dl_init_first`.
- `_dl_init_first` (sysdeps/mach/hurd/i386/init-first.c) calls `first_init` which calls `__mach_init` to initialize enough to run RPCs, then runs the `_hurd_preinit_hook` hooks, which initialize global variables of libc.
- `_dl_init_first` calls `init`.
- `init` sets threadvars, tries to initialize threads (and perhaps switches to the new stack) and gets to call `init1`.
- `init1` gets the Hurd block, calls `_hurd_init` on it
- `_hurd_init` (hurd/hurdinit.c) initializes initial ports, starts the signal thread, runs the `_hurd_subinit` hooks (`init_dtable` hurd/dtable.c notably initializes the FD table and the `_hurd_fd_subinit`hooks, which notably checks `std*`).
- we are back to `_dl_start_user`, which calls `_dl_init` (elf/dl-init.c) which calls application initializers.
- `_dl_start_user` jumps to the application's entry point, `_start`
- `_start` (sysdeps/i386/start.S) calls `__libc_start_main`
- `__libc_start_main` (actually called `LIBC_START_MAIN` in csu/libc-start.c) initializes libc, atexit,
- `__libc_start_main` calls initialization function given as parameter `__libc_csu_init`,
- `__libc_csu_init` (csu/elf-init.c) calls `_init`
- `_init` (sysdeps/i386/crti.S) calls `PREINIT_FUNCTION`, (actually libpthread on Linux, `__gmon_start__` on hurd)
- back to `__libc_csu_init` calls `init_array_start` functions
- back to `__libc_start_main`, it calls application's `main`, then `exit`.

```c
#include <stdio.h>

__attribute__((constructor)) void hello() {
  printf("Hello, World\n");
}

// See also: atexit(3)
__attribute__((destructor)) void goodbye() {
  printf("Goodbye, Cruel OS World!\n");
}

int main() {
}
```



## Ref
[👍 How libc startup in a process works?]: https://www.gnu.org/software/hurd/glibc/startup.html

[👍 Linux x86 Program Start Up or - How the heck do we get to main()? by Patrick Horgan]: http://dbp-consulting.com/tutorials/debugging/linuxProgramStartup.html
