# Troubleshooting

[TOC]



## 👉 Error saving credentials: error storing credentials - err: exec: "docker-credential-desktop": executable file not found in $PATH
#docker 

### Problem

After a DockerForMac update i've realised, that that the `~/.docker/config.json` file is not refering to osxkeychain anymore. Its uses `docker-credential-desktop`.


### Solusion
Edit the file "**~/.docker/config.json**" and delete the following JSON key/value:
`"credsStore" : "desktop",`


[Error saving credentials: error storing credentials - err: exec: "docker-credential-desktop": executable file not found in $PATH]: https://github.com/docker/docker-credential-helpers/issues/149#issuecomment-566832756



## 👉 Docker pull "unexpected EOF"
#docker 

This was mainly because of weak network ( as I was using mobile hotspot )
configured the **docker daemon** to reduce the **tcp packets**
```shell
$ dockerd --max-concurrent-downloads <int>  
```
here **\<int\>** suggests the number of docker pull layers you want to download concurrently.  

**default is 3**

in mycase i had set to 2
```shell
dockerd --max-concurrent-downloads 2 &>/dev/null  
```

downside of doing this is sacrificing your precious time :)  
takes time like hell.


[Docker pull "unexpected EOF"]: https://stackoverflow.com/questions/53677592/docker-pull-unexpected-eof



## 👉 ERROR: permission denied while trying to connect to the Docker daemon socket

To create the docker group and add your user:

- Create the docker group.
```shell
sudo groupadd docker
```

- Add your user to the docker group.
```shell
sudo usermod -aG docker ${USER}
```

- You would need to loog out and log back in so that your group membership is re-evaluated or type the following command:
```shell
su -s ${USER}
```

- Verify that you can run docker commands without sudo.
```shell
docker run hello-world
```

- This command downloads a test image and runs it in a container. When the container runs, it prints an informational message and exits.
- If you initially ran Docker CLI commands using sudo before adding your user to the docker group, you may see the following error, which indicates that your `~/.docker/` directory was created with incorrect permissions due to the sudo commands.
```shell
WARNING: Error loading config file: /home/user/.docker/config.json -
stat /home/user/.docker/config.json: permission denied
```

- To fix this problem, either remove the `~/.docker/` directory (it is recreated automatically, but any custom settings are lost), or change its ownership and permissions using the following commands:

```shell
sudo chown "$USER":"$USER" /home/"$USER"/.docker -R
sudo chmod g+rwx "$HOME/.docker" -R
```


---
```shell
ubuntu@ip-172-31-21-106:/var/run$ ls -lrth docker.sock
srw-rw---- 1 root root 0 Oct 17 11:08 docker.sock
ubuntu@ip-172-31-21-106:/var/run$ sudo chmod 666 /var/run/docker.sock
ubuntu@ip-172-31-21-106:/var/run$ ls -lrth docker.sock
srw-rw-rw- 1 root root 0 Oct 17 11:08 docker.sock
```


[manage docker as a non root user | docker official docs]: https://docs.docker.com/install/linux/linux-postinstall/#manage-docker-as-a-non-root-user

[How to fix docker: Got permission denied while trying to connect to the Docker daemon socket]: https://www.digitalocean.com/community/questions/how-to-fix-docker-got-permission-denied-while-trying-to-connect-to-the-docker-daemon-socket

🎬 https://youtu.be/XfZvKLNXC9M

