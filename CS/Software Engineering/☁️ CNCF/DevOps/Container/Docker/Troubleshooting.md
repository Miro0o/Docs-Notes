# Troubleshooting

##### 👉 [Error saving credentials: error storing credentials - err: exec: "docker-credential-desktop": executable file not found in $PATH](https://github.com/docker/docker-credential-helpers/issues/149#issuecomment-566832756)

###### Prob:

After a DockerForMac update i've realised, that that the `~/.docker/config.json` file is not refering to osxkeychain anymore. Its uses `docker-credential-desktop`.

###### Solu:

Edit the file "**~/.docker/config.json**" and delete the following JSON key/value:
`"credsStore" : "desktop",`



