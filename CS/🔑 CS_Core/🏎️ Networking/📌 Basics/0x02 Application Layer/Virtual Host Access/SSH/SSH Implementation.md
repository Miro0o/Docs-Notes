

# SSH Client

[TOC]



An SSH client is a program that allows establishing secure and authenticated SSH connections to [SSH servers](https://www.ssh.com/ssh/server).

SSH client software is available for major enterprise environment operating systems, such as Unix variations, Microsoft Windows and IBM z/OS.



## Cyberduck - SFTP/FTP Client for Mac

Cyberduck is a fairly popular file transfer client for Apple Mac and Microsoft Windows. It supports FTP, SFTP, WebDAV, Amazon S3, OpenStack Swift, Backblaze B2, Microsoft Azure & OneDrive, Google Drive and Dropbox.

Cyberduck was built by David V. Kocher, Yves Langisch, and [iterate GmbH](https://iterate.ch/).

#### Security Alert

Cyberduck can use [public keys for authentication](https://ssh.com/ssh/public-key-authentication). Many organizations have been found to have massive numbers of unmanaged SSH keys. They pose a major security and compliance risk. [More information on SSH Key Management >](https://ssh.com/iam/ssh-key-management)

Opening SSH tunnels from the external Internet into organizations has also become a common way to circumvent security policies and open backdoors. [More information on SSH Tunneling >](https://ssh.com/ssh/tunneling/)



## Filezilla - SSH and FTP Client

> :warning: FTP has already been deprecated for major security concerns. 



The FileZilla project is an open source development initiative behind the “FileZilla Free FTP Solution”. The project made its first release in 2001. The software is still distributed free of charge under the terms of the GNU General Public License.

FileZilla is well-suited for small-scale file transfer requirements. There is no commercial support, so each user is on their own. The FileZilla community has web forums, Wiki, and bug tracking systems which provide assistance.



#### Alternatives for FileZilla

Modern SSH clients, such as [Tectia SSH](https://www.ssh.com/products/tectia-ssh) offer file transfers integrated with a terminal client. ==The [FTP](https://www.ssh.com/ssh/ftp) and [FTPS](https://www.ssh.com/ssh/ftp/ftps) protocols shouldn't really be used anymore, as they are quite insecure or aren't as robust as [SFTP](https://www.ssh.com/ssh/sftp).==

Please see the [SSH clients](https://www.ssh.com/ssh/client) page for a list of alternatives for various platforms.



## PuTTY

PuTTY is a versatile terminal program for Windows. It is the world's most popular free SSH client. It supports [SSH](https://www.ssh.com/ssh/protocol), [telnet](https://www.ssh.com/ssh/telnet), and raw socket connections with good terminal emulation. It supports [public key authentication](https://www.ssh.com/ssh/public-key-authentication) and Kerberos single-sign-on. It also includes command-line [SFTP](https://www.ssh.com/ssh/sftp) and [SCP](https://www.ssh.com/ssh/scp) implementations.

[Learn all about PuTTY here >](https://www.ssh.com/academy/ssh/putty)



## Tectia SSH Client

[Tectia is the original SSH Client (and Server) solution](https://www.ssh.com/products/tectia-ssh/) developed by the founder of SSH Tatu Ylönen.

Tectia is the backbone of the SSH Client technology with a more than 25-year-long history of securing SSH environments.



## Ref

