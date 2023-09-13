# Troubleshooting

[TOC]



## Res


## 👉 ImportError: No module named Crypto.Cipher

### WARNING 😱: Don't use `crypto` or `pycrypto`anymore!

As you can read on [this page](https://blog.sqreen.com/stop-using-pycrypto-use-pycryptodome/), the usage of `pycrypto` is **not** safe anymore:

> `Pycrypto` is vulnerable to a heap-based buffer overflow in the ALGnew function in block_templace.c. It allows remote attackers to execute arbitrary code in the python application. It was assigned the [CVE-2013-7459](https://security-tracker.debian.org/tracker/CVE-2013-7459) number.
> 
> `Pycrypto` didn’t release any fix to that vulnerability and no commit was made to the project since Jun 20, 2014.


### Update 2021-01-18
The CVE is fixed now (thanks @SumitBadsara for pointing it out!). You can find the current status of the open security tickets for each package at the Debian security tracker:

- [`python-crypto`](https://security-tracker.debian.org/tracker/source-package/python-crypto)
- [`pycryptodome`](https://security-tracker.debian.org/tracker/source-package/pycryptodome)


### Use Python3's `pycryptodome` instead!
Make sure to uninstall all versions of `crypto` and `pycrypto` first, then install `pycryptodome`:
```python
pip3 uninstall crypto 
pip3 uninstall pycrypto 
pip3 install pycryptodome
```

All of these three packages get installed to the same folder, named `Crypto`. Installing different packages under the same folder name can be a common source for errors!

For more information, see [pycryptodome.org](https://www.pycryptodome.org/en/latest/src/introduction.html).


### Best practice: virtual environments
In order to avoid problems with pip packages in different versions or packages that install under the same folder (i.e. `pycrypto` and `pycryptodome`) you can make use of a so called _virtual environment_. There, the installed pip packages can be managed for every single project individually.

To install a virtual environment and setup everything, use the following commands:
```python
# install python3 and pip3
sudo apt update
sudo apt upgrade
sudo apt install python3
sudo apt install python3-pip

# install virtualenv
pip3 install virtualenv

# install and create a virtual environment in your target folder
mkdir target_folder
cd target_folder
python3 -m virtualenv .

# now activate your venv and install pycryptodome
source bin/activate
pip3 install pycryptodome

# check if everything worked: 
# start the interactive python console and import the Crypto module
# when there is no import error then it worked
python
>>> from Crypto.Cipher import AES
>>> exit()

# don't forget to deactivate your venv again
deactivate
```

For more information, see [docs.python-guide.org](https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv).



[ImportError: No module named Crypto.Cipher | Stackoverflow]: https://stackoverflow.com/questions/19623267/importerror-no-module-named-crypto-cipher


## Ref

