# FAQ

[TOC]



## 👉 brew cleanup doesn't clean `~/Library/Caches/Homebrew` folder
#homebrew


The `cleanup` section of `brew`’s `man` page (emphasis mine):

> For all installed or specific formulae, remove any older versions from the cellar. In addition, old downloads from the Homebrew download-cache are deleted.
>
> If --prune=days is specified, remove all cache files older than days.
>
> If --dry-run or -n is passed, show what would be removed, but do not actually remove anything.
>
> If -s is passed, scrub the cache, removing downloads for even the latest versions of formulae. **Note downloads for any installed formulae will still not be deleted. If you want to delete those too: rm -rf $(brew --cache)**

This `cleanup` command, however, remains the caches in `~/Library/Caches/Homebrew` by default.  If you want to remove *everything*, run the suggested `rm` command.


[brew cleanup doesn't clean ~/Library/Caches/Homebrew #3784]: https://github.com/Homebrew/brew/issues/3784



## 👉 update github tokens
#homebrew #github 

git-hub token homepage :https://github.com/settings/tokens
to update token: https://gist.github.com/willgarcia/7347306870779bfa664e
