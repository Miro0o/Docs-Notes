# Windows Architecture

[TOC]



## Windows Architecture Overview
![](../../../../../Assets/Pics/Screenshot%202023-03-02%20at%208.35.31%20PM.png)
<small>Windows Internals Architecture</small>

### Operating System Orgnization
#### Kernel Mode Processes
#TODO 

#### User Mode Processes
Windows supports four basic types of user-mode processes:
1. **Special system processes**: User-mode services needed to manage the system, such as the session manager, the authentication subsystem, the service manager, and the logon process.

2. **Service processes**: Theprinterspooler,theeventlogger,user-modecomponents that cooperate with device drivers, various network services, and many others. Services are used by both Microsoft and external software developers to extend system functionality, as they are the only way to run background user-mode activity on a Windows system. 

3. **Environment subsystems**: Provide different OS personalities (environments). The supported subsystems are Win32 and POSIX. Each environment subsystem includes a subsystem process shared among all applications using the subsystem and dynamic link libraries (DLLs) that convert the user appli- cation calls to ALPC calls on the subsystem process, and/or native Windows calls. 

4. **User applications**: Executables (EXEs) and DLLs that provide the functional- ity users run to make use of the system. EXEs and DLLs are generally targeted at a specific environment subsystem; although some of the programs that are provided as part of the OS use the native system interfaces (NT API). There is also support for running 32-bit programs on 64-bit systems.

### C/S Model

### Threads and SMP


### ☮️ Windoes Objects
#TODO 



## Ref
