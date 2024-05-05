# FAQ

[TOC]



## 👉 How to change/ view Jupyter Notebook's python interpreter? (using `conda` to switch Jupyter Notebook's python env?)
As mentioned in the comments, conda support for jupyter notebooks is needed to switch kernels. Seems like this support is now available through conda itself (rather than relying on pip). [http://docs.continuum.io/anaconda/user-guide/tasks/use-jupyter-notebook-extensions/](http://docs.continuum.io/anaconda/user-guide/tasks/use-jupyter-notebook-extensions/)

`conda install nb_conda`

which brings three other handy extensions in addition to Notebook Conda Kernels.


---

> 💡 by default jupyter notebook uses the conda env it was started with. (This [sets the default environment](https://stackoverflow.com/q/38984238/3345375) for Jupyter Notebooks.) Otherwise, the **Root environment** is the default.



[👍 In which conda environment is jupyter executing? | Stackoverflow]: https://stackoverflow.com/q/37085665/16542494

[Change interpreter in jupyter notebook | Stackoverflow]: https://stackoverflow.com/q/58645807/16542494



## Ref

