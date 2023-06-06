# Troubleshooting

[TOC]



## Res

## 👉 Recover from an unsuccessful git rebase with the `git reflog` command

1. use `git reflog` listing the commit history
```shell
$ git reflog 222967b (HEAD -> main)
HEAD@{0}: rebase (finish): returning to refs/heads/main 222967b (HEAD -> main) 
HEAD@{1}: rebase (squash): My big rebase c388f0c 
HEAD@{2}: rebase (squash): # This is a combination of 20 commits 56ee04d 
HEAD@{3}: rebase (start): checkout HEAD~20 0a0f875 
HEAD@{4}: commit: An old good commit [...]
```

2. find the last good commit that you want to recover. For example HEAD{3} here.
3. Restore the commit
```shell
git checkout HEAD{3}
```

4. merge commits (optional)


[Recover from an unsuccessful git rebase with the git reflog command]: https://opensource.com/article/23/1/git-reflog



## 👉 Git: Merge a Remote branch locally
You can reference those remote tracking branches ~(listed with `git branch -r`) with the name of their remote.

You need to fetch the remote branch:
```
git fetch origin aRemoteBranch
```

If you want to merge one of those remote branches on your local branch:
```
git checkout aLocalBranch
git merge origin/aRemoteBranch
```

_Note 1:_ For a large repo with a long history, you will want to add the `--depth=1` option when you use `git fetch`.

_Note 2:_ These commands also work with other remote repos so you can setup an `origin` and an `upstream` if you are working on a fork.

_Note 3_: [user3265569](https://stackoverflow.com/users/3265569/user3265569) suggests the following alias [in the comments](https://stackoverflow.com/questions/21651185/git-merge-a-remote-branch-locally/21653559#comment116902338_21653559):

> From `aLocalBranch`, run `git combine remoteBranch`  
> Alias:
> 
> ```
> combine = !git fetch origin ${1} && git merge origin/${1}
> ```


[Git: Merge a Remote branch locally]: https://stackoverflow.com/questions/21651185/git-merge-a-remote-branch-locally

- Read [this very well written answer](https://stackoverflow.com/a/71774640/10625611) by [torek](https://stackoverflow.com/users/1256452/torek) to get a much clearer picture on what actually happens behind the scene and to understand which option is the most appropriate option for you.
    
- You may want to keep an eye on [VonC](https://stackoverflow.com/users/6309/vonc)'s answer [here](https://stackoverflow.com/a/64163084/10625611) for updates on changes made to this feature in future updates.



## 👉 How do I fix a Git detached head?
Detached head means you are no longer on a branch, you have checked out a single commit in the history (in this case the commit previous to HEAD, i.e. HEAD^).


**If you want to _delete_ your changes associated with the detached HEAD**
You only need to checkout the branch you were on, e.g.
``` shell
git checkout master
```
Next time you have changed a file and want to restore it to the state it is in the index, don't delete the file first, just do
``` shell
git checkout -- path/to/foo
```
This will restore the file foo to the state it is in the index.


**If you want to _keep_ your changes associated with the detached HEAD**
1. Run `git branch tmp` - this will save your changes in a new branch called `tmp`.
2. Run `git checkout master`
3. If you would like to incorporate the changes you made into `master`, run `git merge tmp`from the `master` branch. You should be on the `master` branch after running `git checkout master`.


[How do I fix a Git detached head?]: https://stackoverflow.com/questions/10228760/how-do-i-fix-a-git-detached-head



## 👉 How do I force "git pull" to overwrite local files?
> ⚠ Warning:
> 
> Any uncommitted local change to tracked files will be lost, **even if staged**.
> 
> But any local file that's _not_ tracked by Git will _not_ be affected.

---

First, update all `origin/<branch>` refs to latest:
```bash
git fetch --all
```
Backup your current branch (e.g. `master`):
``` shell
git branch backup-master
```
Jump to the latest commit on `origin/master` and checkout those files:
``` shell
git reset --hard origin/master
```

**Explanation**
`git fetch` downloads the latest from remote without trying to merge or rebase anything.

`git reset` resets the master branch to what you just fetched. The `--hard` option changes all the files in your working tree to match the files in `origin/master`.


**Maintain current local commits**
⚠ It's worth noting that it is possible to maintain current local commits by creating a branch from `master` before resetting:
```bash
git checkout master
git branch new-branch-to-save-current-commits
git fetch --all
git reset --hard origin/master
```

After this, all of the old commits will be kept in `new-branch-to-save-current-commits`.


**Uncommitte changes**
Uncommitted changes, even if staged (with `git add`), will be lost. Make sure to `stash` or commit anything you need. For example, run the following:
``` shell
git stash
```

And later (after `git reset`), reapply these uncommitted changes:
``` shell
git stash pop
```

> Which may create merge conflicts.


[How do I force "git pull" to overwrite local files?]: https://stackoverflow.com/questions/1125968/how-do-i-force-git-pull-to-overwrite-local-files