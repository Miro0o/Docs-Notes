# SublimeText over SSH

[TOC]



## Res


## Intro



## Ref
[How to use Sublime over SSH]: https://stackoverflow.com/questions/15958056/how-to-use-sublime-over-ssh

[Locally edit remote directories/files via ssh tunneling]: https://forum.sublimetext.com/t/locally-edit-remote-directories-files-via-ssh-tunneling/62514)

That’s what we have.

ST heavily relies on filesystem notifications to update its internal representation of all folders and files. Hence it’s not playing well with filesystems, such as sshfs or the WSL2 which don’t support those.

There’s also no API for plugins such as sftp or rsub to built their own filesystem tries. The only thing a plugin can do is receiving a list of files and present them in a quick panel.

ST isn’t designed for remote workflows.