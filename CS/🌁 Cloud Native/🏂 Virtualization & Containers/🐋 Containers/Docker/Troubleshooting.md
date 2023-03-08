# Troubleshooting

[TOC]



## 👉 [Error saving credentials: error storing credentials - err: exec: "docker-credential-desktop": executable file not found in $PATH](https://github.com/docker/docker-credential-helpers/issues/149#issuecomment-566832756)

### Problem

After a DockerForMac update i've realised, that that the `~/.docker/config.json` file is not refering to osxkeychain anymore. Its uses `docker-credential-desktop`.


### Solusion

Edit the file "**~/.docker/config.json**" and delete the following JSON key/value:
`"credsStore" : "desktop",`



## 👉 [Docker pull "unexpected EOF"](https://stackoverflow.com/questions/53677592/docker-pull-unexpected-eof)
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


