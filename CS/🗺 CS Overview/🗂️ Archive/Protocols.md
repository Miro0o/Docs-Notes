# Protocols



## HTTP

> https://en.wikipedia.org/wiki/HTTP/3
> diff from [HTML5](https://en.wikipedia.org/wiki/HTML5)

HTTP/1.1 HTTP/2 -->TCP
HTTP/3 --> QUIC



## [Socks5](https://www.ibm.com/docs/en/secure-proxy/6.0.2?topic=scenarios-socks5-configuration) #unsolved



## [SSH](https://en.wikipedia.org/wiki/Secure_Shell)

[SSH Academy](https://www.ssh.com/academy)



> [openSSH](https://en.wikibooks.org/wiki/OpenSSH/Client_Configuration_Files#/etc/ssh/ssh_known_hosts)

+ **Secure Shell** (**SSH**) is a [cryptographic](https://en.wikipedia.org/wiki/Cryptography "Cryptography") [network protocol](https://en.wikipedia.org/wiki/Network_protocol "Network protocol") for operating network services securely over an unsecured network.Typical applications include remote [command-line](https://en.wikipedia.org/wiki/Command-line_interface "Command-line interface"), [login](https://en.wikipedia.org/wiki/Login "Login"), and remote command execution, but any [network service](https://en.wikipedia.org/wiki/Network_service "Network service") can be secured with SSH.
	+ akin FTP, rcp, 
	+ [ssh VS ssl/stl](https://searchsecurity.techtarget.com/definition/Secure-Shell)

### [Creating an SSH Key Pair for User Authentication](https://www.ssh.com/academy/ssh/keygen)

private key / public key

```shell
ssh-keygen -t ed25519 -C "usrname@domainname" -f <filename>

-t : 
	rsa
	dsa
	ecdas
	ed25519
	
```

> ⚠️ SSH on Github:
> [Use Personal access token in place of password to login Github.](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
> 
> [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
> + To configure your account on GitHub.com to use your new (or existing) SSH key, you'll also need to add the key to your account.

+ SFTP



## [FTP]()

File Transfer Protocol (FTP) supports 2 transmitting pattern :
1. PORT
2. PASV

FTP supports 3 authentication method:
1. anonymous authentication
2. local user authentication
3. virtual user	authentication

### [implement FTP on server/client host](https://help.aliyun.com/document_detail/60152.html) (by vsftpd)

#### server end: vsftpd (very secure ftp deamon)

1. installation
2. configuration
3. firewall


###### vsftp配置文件及参数说明

/etc/vsftpd目录下文件说明如下： 
-   /etc/vsftpd/vsftpd.conf是vsftpd的核心配置文件。
-   /etc/vsftpd/ftpusers是黑名单文件，此文件中的用户不允许访问FTP服务器。
-   /etc/vsftpd/user_list是白名单文件，此文件中的用户允许访问FTP服务器。

配置文件vsftpd.conf参数说明如下： 

-   用户登录控制参数说明如下表所示。 

![[../../../Assets/Pics/Screen Shot 2022-01-03 at 11.04.18 AM.png]]


#### client end: FileZilla

