# Troubleshooting

[TOC]



## 👉 `conda update conda error`
#conda 

Turn out to be the channel site's error. I deleted all other channels but default and conda-forge. Then it worked.



["conda update conda" error #10333]:https://github.com/conda/conda/issues/10333



## 👉 `Solving environment: failed with initial frozen solve. Retrying with flexible solve`
#conda 

I highly doubted that this has something to do with my inconsistency envrionment error report. 

I found these solusions but none of them worked for me:

- create a new conda env
- downgrade conda version
- conda config --set priority :false
- conda config  --set priority: flexible 



[Solving environment: failed with initial frozen solve. Retrying with flexible solve.#9367]: https://github.com/conda/conda/issues/9367
[Conda install and update do not work also solving environment get errors]: https://stackoverflow.com/questions/57518050/conda-install-and-update-do-not-work-also-solving-environment-get-errors



## 👉 The environment is inconsistent, please check the package plan carefully
#conda 

**Description**

After error occured when downloading anything package from repo, i realized it might be the repo itself went slip. So i deleted every other repo but `default` and `conda-forge` . Then `conda install` again. Since the previous packages are all from situ mirror site, the new "conda" mirror site packages are, as reported, inconsistent.

**Solusion**

Still no solusion to this. 

I desperately tried following shell:

```shell
# all under base env
conda update conda
conda install anaconda
# i run this for several times because i found each time i try it it promptes new updates. There was a time i doubt it can never end...
conda update --all
```

I have no idea how things going.

However after i desperately run above code for several times i can somehow `pip` the package sucessfully like a charm!

But i still cannot `conda install`. Instead i make with `pip`.

🥹🥹🥹🥹



[The environment is inconsistent, please check the package plan carefully #8490]: https://github.com/conda/conda/issues/8490
[How to resolve inconsistent package warnings in conda?]:https://stackoverflow.com/questions/56072846/how-to-resolve-inconsistent-package-warnings-in-conda



## 👉  Why Conda cannot call correct Python version after activating the environment?
#conda 


TLDR;

```shell
# deactivate Conda environment
# (until even base environment is deactivated)
conda deactivate
# activate your environment
conda activate your_env_name_goes_here
```

This happened after `conda update --all`. Shut the terminal down and restart. 



[Why Conda cannot call correct Python version after activating the environment?]: https://stackoverflow.com/questions/36733179/why-conda-cannot-call-correct-python-version-after-activating-the-environment



## 👉 pip: no module named \_internal
#pip

This did it for me:
```python
python -m pip install --upgrade pip
```

Environment: OSX && Python installed via [brew](https://docs.brew.sh/Homebrew-and-Python)


[pip: no module named _internal]: https://stackoverflow.com/questions/49940813/pip-no-module-named-internal