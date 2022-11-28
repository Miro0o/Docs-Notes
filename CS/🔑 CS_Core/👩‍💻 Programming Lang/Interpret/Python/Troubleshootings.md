# Troubleshootings

###### 👉 [how to force stop a python process](https://stackoverflow.com/a/53211247/16542494)

**level 1:**
`CTRL + C `  to raise  `KeyboardInterrupt`

**level 2:**

1. approach #1
`CREL + Z` to suspend the process
`jobs` to check the current suspended process
`fg %n` to resume the suspended process, where `n` is the corresponding number of the process listed by `jobs`.
`kill %n` kills the listed `n` process

2.  approach #2
`ps aux | grep python` check the PID (Process ID) of the running process
`kill <PID>` to kill the process
> `kill` command send a `SIGTERM` signal to the system by default. 

**level 3:**

if `SIGTERM`dosen't work, then send `SIGKILL` signal.
use `kill -KILL <pid>` (or `kill -9 <pid>`) to achieve this. 



👉 [Fix Pip “Yanked Version” Warnings](https://adamj.eu/tech/2021/09/20/how-to-fix-pip-yanked-version-warnings/)

PyPI allows package maintainers to yank a given version. This is intended for removing versions with bad faults, such as security holes or broken installation.

The maintainer *could* delete the version, but this would break all installations pinned to that version, unleashing chaos. Yanking the version instead marks the version as unsafe, making it somewhat invisible while allowing pinned installs to succeed.

Conventionally, while yanking a pck the maintainer will also relesase a secure version. Generally if one doesn't specifically designate a version when piping pcks, pip will automaticallty choose the secure version.

When Yanked Version warnning occurred, to fix it we need to find an un-yanked version of the package that will work for us. This might mean upgrading, downgrading, or waiting for a new version. Upgrading is the most common course of action, since if a maintainer has yanked a version, they’ve likely released a fix shortly after.

1️⃣ check out the package’s page on [pypi.org](https://pypi.org/).

2️⃣  check available versions with the `pip index versions` command with the package name

