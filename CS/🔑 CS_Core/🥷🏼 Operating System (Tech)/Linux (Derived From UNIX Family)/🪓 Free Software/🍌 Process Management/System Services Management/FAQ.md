# FAQ

[TOC]



## 👉 Diffence between `systemd-sysctl` and `sysctl`
[`sysctl`](https://manpages.debian.org/bullseye/procps/sysctl.8) is an administrative tool which provides access to values in the `/proc/sys` virtual file system (see also [How to set and understand fs.notify.max_user_watches](https://unix.stackexchange.com/q/444998/86440)). You can use it to see the current value of a setting:
```
sysctl fs.inotify.max_user_watches
```

and to change the value:
```
sysctl fs.inotify.max_user_watches=524288
```

[`systemd-sysctl`](https://manpages.debian.org/bullseye/systemd/systemd-sysctl.8) is a systemd service which loads `sysctl` settings from a number of files during boot. You shouldn’t ever need to invoke or manipulate it directly.

The two tools are complementary: `sysctl` allows you to try a setting temporarily (the changes it makes don’t persist over reboots), and once you’ve decided on an appropriate value, writing it to a file in `/etc/sysctl.d` will ensure that `systemd-sysctl` sets it during boot. Again, see [How to set and understand fs.notify.max_user_watches](https://unix.stackexchange.com/q/444998/86440).



[Diffence between `systemd-sysctl` and `sysctl`]: https://unix.stackexchange.com/questions/709586/diffence-between-systemd-sysctl-and-sysctl