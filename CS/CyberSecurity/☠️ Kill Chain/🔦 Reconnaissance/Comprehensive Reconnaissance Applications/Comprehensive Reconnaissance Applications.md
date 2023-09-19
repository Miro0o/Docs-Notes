# Comprehensive Reconnaissance Applications

[TOC]





## 👉 Deep Magic Information Gathering Tool (DMitry)
DMitry could perform whois lookups, retrieve netcraft.com information, search for sub-domains and email addresses, and perform TCP scans. Unfortunately, it wasn't extensible beyond these functions.



## 👉 recon-ng
The recon-ng framework is an open source framework for conducting reconnaissance (passive and active). The framework is similar to **Metasploit** and **Social Engineer Toolkit** (**SET**); recon-ng uses a very modular framework. Each module is a customized command interpreter, preconfigured to perform a specific task.



## SPARTA
The following items are available in the configuration:
- tool: This is the unique identifier of the command-line tool, for example, `nmap`
- label: This is the text that appears on the context menu
- command: Normally this should be in non-interactive mode and the full command that you will run using a tool
- Services: These are the list of services that need to be run during the automatic run; for example, if you configure to run `nmap` and when port 80 is identified automatically run `nikto`
- Protocol: Either `TCP` or `UDP` are the services that the tool should run on



## Native MS Windows commands
### nslookup



### net



### arp



### route



### netstat



### nbtstat

### reg

### wmic

### for