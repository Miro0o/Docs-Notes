# Troubleshooting

[TOC]



## 👉 You don't have write permissions for the /Library/Ruby/Gems/2.3.0 directory. (mac user)

You are correct that macOS won't let you change anything with the Ruby version that comes installed with your Mac. However, it's possible to install gems like `bundler` using a separate version of Ruby that doesn't interfere with the one provided by Apple.

Using `sudo` to install gems, or changing permissions of system files and directories is strongly discouraged, even if you know what you are doing. Can we please stop providing this bad advice?

The solution involves two main steps:
1. Install a separate version of Ruby that does not interfere with the one that came with your Mac.
2. Update your `PATH` such that the location of the new Ruby version is first in the `PATH`. Some tools do this automatically for you. If you're not familiar with the `PATH` and how it works, it's one of the basics that you should learn, and you'll understand why you sometimes get "command not found" errors and how to fix them.

(more at below👇)

[👍 You don't have write permissions for the /Library/Ruby/Gems/2.3.0 directory. (mac user) | Stackoverflow]: https://stackoverflow.com/questions/51126403/you-dont-have-write-permissions-for-the-library-ruby-gems-2-3-0-directory-ma



## 👉 Insecure world writable dir /Users/username in PATH, mode 040777 when running Ruby commands
#PATH #ruby 

Your home folder should only be writable by you, not by anyone else. The reason gem is complaining about this is that you have folders in your PATH that are inside your (insecure) home folder, and that means that anyone who wants to could hack you by renaming/moving your .rvm folder and replacing it with an impostor.

To fix your home folder, run `chmod go-w /Users/kristoffer`. If there are any other insecure folders on the way to anything in your PATH, you should fix them similarly.

BTW, the reason that Disk Utility didn't repair this is that it only repairs files installed as part of the OS (see [Apple's KB article on the subject](http://support.apple.com/kb/ht1452)). There is an option to repair home folder permissions if you boot from the install DVD and run Password Reset from the Utilities menu, but I'm not sure if it resets the permissions themselves or just ownership.

[Insecure world writable dir /Users/username in PATH, mode 040777 when running Ruby commands | Stackoverflow]: https://stackoverflow.com/q/6192003

