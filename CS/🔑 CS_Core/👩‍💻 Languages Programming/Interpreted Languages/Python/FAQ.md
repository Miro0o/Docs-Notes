# FAQ

[TOC]




## How-To
### 👉 Start a http server using python module http.server
 [Python_使用python快速启用HTTP服务器](https://www.cnblogs.com/testlearn/p/16072669.html) 

```shell
python -m http.server [port] [-d server-dir]
```


### 👉 Generating `requirement.txt`
```shell
$ pip freeze > requirements.txt

$ pip install pipreqs
# 在当前目录生成 
$ pipreqs . --encoding=utf8--force

```

[github.com/bndr/pipreqs](https://github.com/bndr/pipreqs)
 
 [python生成requirements.txt的两种方法 | learnku]: https://learnku.com/articles/47470
[python 项目自动生成requirements.txt文件]: https://blog.csdn.net/Irving_zhang/article/details/79087569



## Syntax
### 👉 [Difference between 'cls' and 'self' in Python classes?](https://stackoverflow.com/questions/4613000/difference-between-cls-and-self-in-python-classes)

The distinction between `"self"` and `"cls"` is defined in [`PEP 8`](http://www.python.org/dev/peps/pep-0008/#function-and-method-arguments) . As Adrien said, this is not mandatory. It's a coding style. `PEP 8` says:

> *Function and method arguments*:
>
> Always use `self` for the first argument to instance methods.
>
> Always use `cls` for the first argument to class methods.


### 👉 Assert, isinstance
[python中assert、isinstance的用法]: https://blog.csdn.net/qiqicos/article/details/78993748
[Python assert isinstance() Vector]: https://stackoverflow.com/questions/47268107/python-assert-isinstance-vector


### 👉 Operator overloading
[浅析Python运算符重载](https://blog.csdn.net/goodlixueyong/article/details/52589979)


### 👉 命令行传参数
**1️⃣ sys.argv**

sys模块是很常用的模块， 它封装了与python解释器相关的数据，例如sys.modules里面有已经加载了的所有模块信息，sys.path里面是PYTHONPATH的内容，而sys.argv则封装了传入的参数数据。 
使用sys.argv接收上面第一个命令中包含的参数方式如下：

``` python
# -*- coding:utf-8 -*-
# @Date  : 2019/2/27
import sys
gpus = sys.argv[1]
#gpus = [int(gpus.split(','))]
batch_size = sys.argv[2]
print gpus
print batch_size](<# -*- coding:utf-8 -*-
# @Date  : 2019/2/27

import sys


def test_for_sys(year, name, body):
    print('the year is', year)
    print('the name is', name)
    print('the body is', body)


if __name__ == '__main__':
    try:
        year, name, body = sys.argv[1:4]
        test_for_sys(year, name, body)
    except Exception as e:
        print(sys.argv)
        print(e)>)
```

**2️⃣ argparse**
`argparse` 模块也是 Python 自带的一个命令行参数模块，这个模块才是真的为了命令行参数而生的模块，相较之下 `sys.argv` 只是碰巧可以用在命令行参数上面而已。
```python
# -*- coding:utf-8 -*-
# @Date  : 2019/2/27

import argparse


def test_for_sys(year, name, body):
    print('the year is', year)
    print('the name is', name)
    print('the body is', body)


parser = argparse.ArgumentParser(description='Test for argparse')
parser.add_argument('--name', '-n', help='name 属性，非必要参数')
parser.add_argument('--year', '-y', help='year 属性，非必要参数，但是有默认值', default=2017)
parser.add_argument('--body', '-b', help='body 属性，必要参数', required=True)
args = parser.parse_args()

if __name__ == '__main__':
    try:
        test_for_sys(args.year, args.name, args.body)
    except Exception as e:
        print(e)

```
在添加命令行参数的属性的时候，还可以有更多的设置，如下：

- name or flags：也就是在使用参数的时候使用的符号，`--foo` 或者 `-f`
- action：根据我的理解，这个属性可以选择参数在只提供符号而不输入实际的值的时候给予一个默认的值
- nargs：这个属性规定了参数可以输入的个数
- const：这属性跟 action 属性一起使用
- default：这属性就是给参数设置一个默认值
- type：这个属性规定了参数的数据类型
- choices：这个属性给参数限定了一个选择的迭代，参数只能在这个范围内选择参数的值，否则报错
- required：参数的值为必填

**3️⃣ getopt**
getopt 是 Python 中一个内置标准模块，可以结合 sys.argv 模块，直接解析脚本运行时参数。
使用格式：getopt(args,shortopts,longopts = [])。

```python
from getopt import getopt
import sys

# 获取参数
# sys.argv[1:]：获取除脚本文件名外的所有命令行参数
# opts：存有所有选项及其输入值的元组列表
# args：去除有用的输入以后剩余的部分
opts, args = getopt(sys.argv[1:], 'i:u:p:d:', ['ip=', 'user=', 'pwd=', 'db='])

# 获取参数值
# 短参数
# python3 4_getopt.py -i 127.0.0.1 -u root -p 123456 -d mysqldb
# 长参数
# python3 4_getopt.py --ip 127.0.0.1 -u root -p 123456 -d mysqldb
ip_pre = [item[1] for item in opts if item[0] in ('-i', '--ip')]
ip = ip_pre[0] if len(ip_pre) > 0 else None
print("参数ip：", ip)

user_pre = [item[1] for item in opts if item[0] in ('-u', '--user')]
user = user_pre[0] if len(user_pre) > 0 else None
print("参数user：", user)

pwd_pre = [item[1] for item in opts if item[0] in ('-p', '--pwd')]
pwd = pwd_pre[0] if len(pwd_pre) > 0 else None
print("参数pwd：", pwd)

db_pre = [item[1] for item in opts if item[0] in ('-d', '--db')]
db = db_pre[0] if len(db_pre) > 0 else None
print("参数db：", db)
```

**3️⃣ Click**
Click 是 Flask 的团队 pallets 开发的优秀开源项目，它为命令行工具的开发封装了大量方法，使开发者只需要专注于功能实现。这是一个第三方库，专门为了命令行而生的非常有名的 Python 命令行模块。
```python
# -*- coding:utf-8 -*-
# @Date  : 2019/2/27

import click

@click.command()
@click.option('--name',default='Leijun',help='name 参数，非必须，有默认值')
@click.option('--year',help='year 参数',type=int)
@click.option('--body',help='body 参数')
def test_for_sys(year, name, body):
    print('the year is', year)
    print('the name is', name)
    print('the body is', body)

if __name__ == '__main__':
    test_for_sys()

```
**4️⃣ tf.app.run**
tensorflow也提供了一种方便的解析方式。
```python
import tensorflow as tf
tf.app.flags.DEFINE_string('gpus', None, 'gpus to use')
tf.app.flags.DEFINE_integer('batch_size', 5, 'batch size')

FLAGS = tf.app.flags.FLAGS

def main(_):
    print FLAGS.gpus
    print FLAGS.batch_size

if __name__=="__main__":
    tf.app.run()
```
注意： 
1. tensorflow只提供以下几种方法： 
	1. tf.app.flags.DEFINE_string， 
	2. tf.app.flags.DEFINE_integer, 
	3. tf.app.flags.DEFINE_boolean, 
	4. tf.app.flags.DEFINE_float 四种方法，分别对应str, int,bool,float类型的参数。这里对bool的解析比较严格，传入1会被解析成True，其余任何值都会被解析成False。
2. 脚本中需要定义一个接收一个参数的main方法：def main(_):，这个传入的参数是脚本名，一般用不到， 所以用下划线接收。
3. 以batch_size参数为例，传入这个参数时使用的名称为--batch_size，也就是说，中划线不会像在argparse 中一样被解析成下划线。
4. tf.app.run()会寻找并执行入口脚本的main方法。也只有在执行了tf.app.run()之后才能从FLAGS中取出参数。从它的签名来看，它也是可以自己指定需要执行的方法的，不一定非得叫main：
```python
run( main=None, argv=None )
```
5. tf.app.flags只是对argpars的简单封装。代码见https://github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/python/platform/flags.py



[Python 命令行参数的3种传入方式]: https://tendcode.com/article/python-shell/
[命令行运行Python脚本时传入参数的三种方式 | CSDN]: https://blog.csdn.net/weixin_35653315/article/details/72886718

[argparse | python docs]: https://docs.python.org/3/library/argparse.html#choices


### 👉 pyhon is & ==
https://www.runoob.com/note/24872

is 判断两个变量是否是引用同一个内存地址。
**is** 判断两个对象是否为同一对象, 是通过 id 来判断的; 当两个基本类型数据(或元组)内容相同时, id 会相同, 但并不代表 a 会随 b 的改变而改变。

== 判断两个变量是否相等。
== 判断两个对象的内容是否相同, 是通过调用 __eq__() 来判断的。