Python3 手册，整理一些知识点。

- [pip](#pip)
  - [pip 配置](#pip-配置)
  - [pip 包管理](#pip-包管理)
  - [pip 缓存管理](#pip-缓存管理)
- [实用函数](#实用函数)
  - [OS 相关](#os-相关)
  - [字符串](#字符串)
  - [文件目录](#文件目录)
  - [其它](#其它)

# pip
pip 是 Python 包管理工具，该工具提供了对 Python 包的查找、下载、安装、卸载的功能。

Python 安装包自带 pip 包管理工具，安装后位于 Python 安装目录的 Scripts 目录中。

pip 和 pip3 版本不同，Python2 使用 pip，Python3 使用 pip3。若系统中只有 Python3 则 pip 和 pip3 等价。

## pip 配置
#### 显示版本和路径
```sh
pip --version
# 或
pip -V
```

#### 获取帮助
```sh
pip --help
```

#### 升级 pip
```sh
# pip3 无法升级：No module named pip3
# Linux | macOS
pip install -U pip

# windows
python -m pip3 install -U pip
```

#### pip 开源软件镜像配置
```sh
# 临时使用清华镜像安装 opencv-python
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python

# 设置全局镜像，首先将 pip 升级到最新版本
pip install pip -U
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 若 pip 默认源网络连接较差，临时使用清华大学镜像站升级 pip
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U
```

## pip 包管理
#### 安装包
```sh
pip install SomePackage              # 最新版本
pip install SomePackage==1.0.4       # 指定版本
pip install 'SomePackage>=1.0.4'     # 最小版本

# 若 Python2 或 Python3 同时有 pip
python2 -m pip install xxx
python3 -m pip install xxx
```

#### 升级包
```sh
# 升级指定的包，通过使用==, >=, <=, >, < 来指定一个版本号。
pip install --upgrade SomePackage
```

#### 卸载包
```sh
pip uninstall SomePackage
```

#### 搜索包
```sh
pip search SomePackage
```

#### 显示安装包信息
```sh
pip show 

# 查看指定包的详细信息
pip show -f SomePackage
```

#### 列出已安装包
```sh
pip list
```

#### 查看可升级的包
```sh
pip list -o
```

## pip 缓存管理
pip 安装时，会将下载的文件进行缓存，以后再次安装次包时，不必再下载。

```sh
# pip 缓存目录
pip cache dir

# 列出当前缓存的安装包
pip cache list

# 显示缓存占用磁盘大小信息
pip cache info

# 删除缓存中的 gym 开头的包
pip cache remove gym*

# 删除全部缓存的包
pip cache purge
```

# 实用函数
## OS 相关
#### 计算机用户名称
```python
import os
print("登录电脑的用户名称：" + os.getlogin())
```

#### 获取用户家目录
```python
if sys.platform == 'win32':
    homedir = os.environ['USERPROFILE']
elif sys.platform == 'linux' or sys.platform == 'darwin':
    homedir = os.environ['HOME']
```

## 字符串
#### strip()
内置函数，返回删除前导和尾随空格的字符串副本。

```python
str = " 1,2,3,4 "

# 当 strip() 无参数时，删除前导和后缀的空格
print(str.strip())  # >1,2,3,4

# 当参数为 ' ' 时，同上
print(str.strip(' '))

# 当参数为 ',' 时，删除前导和后缀 ,
str = ",1,2,3,4,"
print(str.strip(','))   # >1,2,3,4
```

#### rstrip()
去除空白与换行字符。

#### repr()
内置函数，将对象转化为供解释器读取的形式。返回值是一个字符串。

```python
# 个人理解：此函数可以将对象按照定义转换为表达式字符串输出
str = "物品\t单价\t数量\n包子\t1\t2"

# 结果:
# 物品    单价    数量
# 包子    1       2   
print(str)

# 结果:
# '物品\t单价\t数量\n包子\t1\t2'
print(repr(str))
```

#### 输出格式化
1. 传统输出
```python
# 输出结果: 输出项1=1 输出项2=2 输出项3=3 输出项4=4
output_string = "输出项1=%s 输出项2=%s 输出项3=%s 输出项4=%s" % (1,2,3,4)
print(output_string)
```

2. 使用 "{}.format()"
```python
# 输出结果: 输出项1=1 输出项2=2 输出项3=3 输出项4=4
output_string  = "输出项1={} 输出项2={} 输出项3={} 输出项4={}".format(1,2,3,4)
print(output_string)

# 输出结果: 输出内容：4 输出内容：2 输出内容：3 输出内容：1
output_string = "输出内容：{3}  输出内容：{1} 输出内容：{2} 输出内容：{0}".format(1,2,3,4)
print(output_string)

# 获取文件路径 dir_name 下所有以当前文件扩展名 file_type 结尾的文件
files = glob(os.path.join(dir_name, "*{}".format(file_type)))
print(files)
```

3. print(f'字符串')
```python
# 字符串前面加 f 表示格式化字符串，加 f 后可以在字符串里面使用用花括号括起来的变量和表达式 {变量和表达式}，
# 格式化的字符串文字前缀为 f 和接受的格式字符串相似 str.format()。
w = 2
print('%.2f' %w)
print(f'w = {w:.2f}')
```

#### 列表转为字符串
1. join 方法
内置函数。

```python
list = ['1', '2', '3', '4']

# 输出 '1 2 3 4'
str = " ".join(list)
print(str)

# 输出 '1,2,3,4'
str = ",".join(list)
print(str)
```

2. 使用 `*` 号
列表前加个 * 号，是将列表拆分成单个元素，然后传入到函数中。
```python
a = [1, 2, 3, 4]
# 输出 1 2 3 4
print(*a)
```

* 一般用在传递列表参数到函数中。
```python
def plus(a, b):
  return a + b

list = [1, 2]
print(plus(*list))
```
## 文件目录
#### 当前目录、父目录、目录切换
当前目录和父目录获取。

```python
import os

# 当前工作目录
path = os.getcwd()
print("当前目录：" + path)  # 当前目录：d:\hkk\autotest00\program

# 返回当前目录的父目录 os.pardir()
parent = os.path.join(path, os.pardir)
print(parent)   # d:\hkk\autotest000\program\..
print("父目录：", os.path.abspath(parent))  # 父目录：d:\hkk\autotest00

# 切换目录
os.chdir(parent)
```

#### shutil 内置模块
管理文件和目录。

```python
import shutil
# 文件复制，目标文件无需存在
shutil.copyfile(src, dst)

# 仅 拷贝文件，内容、用户、组均不变，目标文件必须存在
shutil.copyfile(src, dst)

# 仅 拷贝状态的信息，包括：mode bits, atime, mtime, flags，目标文件必须存在
shutil.copystat(src, dst)

# 拷贝文件和权限
shutil.copy(src, dst)

# 拷贝文件和状态信息
shutil.copy2(src, dst)

# 递归的去拷贝文件夹
shutil.copytree(src, dst, symlinks=False, ignore=None)
# 目标目录不能存在，ignore 的意思是排除
shutil.copytree(src, dst, ignore=shutil.ignore_patterns('*.py', 'tmp*'))

# 递归的去删除文件
shutil.rmtree(path[,ignore_errors[,onerror]])

# 递归的移动文件，即重命名
shutil.move(src, dst)
```

## 其它
#### zip()
内置函数，用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，返回一个对象。

如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。

```python
a = [1,2,3]
b = [4,5,6]
zipped = zip(a,b)           # 返回一个对象

# 结果: <zip object at 0x103abc288>
zipped

# 结果: [(1, 4), (2, 5), (3, 6)]
list(zipped)                # list() 转换为列表

a1, a2 = zip(*zip(a,b))     # 与 zip 相反，zip(*) 可理解为解压，返回二维矩阵式
# 结果: [1, 2, 3]
list(a1)
# 结果: [4, 5, 6]
list(a2)
```

#### glob()
glob 模块的主要方法是 glob()，该方法返回一个 List，其中元素为所有匹配的文件路径；
该方法需要一个参数用来指定匹配的路径字符串（相对路径/绝对路径均可），需要注意的是，返回的文件名List只包括当前目录下的文件名，不包括子文件夹中的文件。

用法：`glob( path + '*.某格式' )`

说明：得到 path 下某格式的全部文件名的 List（包含路径），例如 *.png 是获取所有 png 图片。

这个用法很容易让人想到 `os.listdir( path )`，得到的是 path 下的全部文件名的 List（不包含路径）。

区别在于：
- 是否包含路径
- glob 可以指定格式，listdir 则是全部文件

```python
from glob import glob

# 访问某个 path 下的所有 txt 文件
glob("path/*.txt")
```
