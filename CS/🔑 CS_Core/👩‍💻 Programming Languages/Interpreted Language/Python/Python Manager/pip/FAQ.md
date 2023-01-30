# FAQ

[TOC]



## 👉 [What's the difference between --find-links and --index-url pip flags?](https://stackoverflow.com/questions/46651454/whats-the-difference-between-find-links-and-index-url-pip-flags)

`index-url` can be considered a page with nothing but packages on it. You're telling pip to find what you want to install on that page; and that page is in a predictable format as per PEP 503. The index will only list packages it has available.

`find-links` is an array of locations to look for certain packages. You can pass it file paths, individual URLs to TAR or WHEEL files, HTML files, git repositories and more.

You can combine the two, for example, if you wanted to use some packages from your local system and others from a repository online.

You can see all the different ways pip will parse "links to packages" in the [`pip/test_index.pyp`](https://github.com/pypa/pip/blob/a9d56c7734fd465d01437d61f632749a293e7805/tests/unit/test_index.py)unit tests.

