一些实用的 Python 代码。

- [生成 exe](#生成-exe)
- [反编译](#反编译)
  - [pyinstxtractor.py](#pyinstxtractorpy)
  - [uncompyle6](#uncompyle6)
  - [pycdc](#pycdc)
- [反反编译](#反反编译)
- [Excel 操作](#excel-操作)
- [log 操作](#log-操作)
- [验证码识别](#验证码识别)
- [人脸识别](#人脸识别)
- [格式文件解析](#格式文件解析)
- [html 操作](#html-操作)
- [图形界面编程 Pyside6](#图形界面编程-pyside6)
- [SMTP 邮件发送](#smtp-邮件发送)
- [selenium 网页自动化](#selenium-网页自动化)
- [unzip 解压缩](#unzip-解压缩)
- [网络操作](#网络操作)
- [线程](#线程)
- [其它](#其它)

# 生成 exe
参考 compile 目录。

1. 安装 pyinstaller 包，`pip install pyinstaller -i https://mirrors.aliyun.com/pypi/simple`
2. 在 .py 文件所在目录，运行指令 `pyinstaller -F xxx.py`
3. 生成的 EXE 文件在目录 dist

也可以使用图形界面工具生成 EXE 程序。
1. 安装 auto-py-to-exe，`pip install auto-py-to-exe -i https://mirrors.aliyun.com/pypi/simple`
2. 在命令行运行 auto-py-to-exe.exe 即可。

# 反编译
参考 compile 目录。

## pyinstxtractor.py
[pyinstxtractor.py](https://github.com/extremecoders-re/pyinstxtractor) 是 Pyinstaller 提取器，用于提取由 pyinstaller 生成的 exe 文件。

提取 exe 文件指令 `python pyinstxtractor.py xxx.exe`，提取内容在目录 `xxx.exe_extracted` 中。

## uncompyle6
安装 uncompyle6 反编译，`pip install uncompyle6`.

- 文件 `xxx` 不带后缀 .pyc，它缺少一些信息，需要修复。如，python3.7 及以上的二进制文件中，头部除了四字节 `Magic Number`，
  还有四个字节的空位和八个字节的时间戳及大小信息。需通过十六进制编辑工具增加头部信息，可从其它相同版本的 pyc 拷贝。
- 添加后缀为 `xxx.pyc`，使用 uncompyle6 反编译 pyc 得到 py 文件，`uncompyle6.exe xxx.pyc -o xxx.py`。目前 uncompyle6 只支持到 python3.8.

## pycdc
对于 python3.10 可以使用 `pycdc` 反编译 pyc 文件，指令 `pycdc.exe xxx.pyc -o xxx.py`。需要确保 python 和 pyinstxtractor.py 版本保持一致，否则 pycdc 解析报错。

[pycdc](https://github.com/zrax/pycdc) 需要自己下载编译。

编译指令：
```bash
git clone https://github.com/zrax/pycdc
cd pycdc
cmake .

# 若生成 Makefile 则使用 make
make
# 若生成 .vcxproj 工程，则打开 Visual Studio 编译
```

# 反反编译
参考 compile 目录。

.pyc 文件容易被工具反编译，而 .pyd 则不容易被反编译。

1. 使用 cython 生成 .pyd 文件，`pip install cython`。
2. 使用 easycython 生成 .pyd 文件，`pip install easycython`。优点较 cython 在于不用 `setup.py`。

- cython 工具需要 Microsoft Visual C++ 14.0 以上版本支持。
- cython 不支持 goto 语句。
- python3 版本需要在首行添加代码段 `#cython: language_level=3`.

# Excel 操作
参考 openpyxl_ 目录。

使用 openpyxl 3.0.10 模块实现 .xlsx Excel 各种操作。

`pip install openpyxl -i https://mirrors.aliyun.com/pypi/simple`

- open 打开 Excel
- read_row_data_dict 按行读数据
- write 写数据
- cell_fillcolor_set 设置单元格填充色
- save 保存关闭

# log 操作
参考 logging_ 目录。

自带模块。

可以通过配置文件配置 log 的输出方式，级别，甚至可以过滤。

logging.conf 为配置文件

# 验证码识别
参考 ddddocr_ 目录。

`pip install ddddocr -i https://mirrors.aliyun.com/pypi/simple`

- 截屏
- 确定识别区域坐标，参考这里 https://zhangweixi.cc/static/windows-xy.html

截屏后确定验证码位置，返回验证码内容。

# 人脸识别
参考 face_recog 目录。

使用 [face_recognition](https://github.com/ageitgey/face_recognition) 库实现。

- `pip install numpy`
- `pip install matplotlib`
- `pip install opencv-python`
- `pip install dlib`
- `pip install face_recognition`

实现捕捉摄像头中的人脸，并标识其姓名。

实在是卡顿，工程中应该不会使用。

# 格式文件解析
参考 parse 目录。

1. `.ini` 格式，使用内置库 ConfigParser。
2. `json` 格式，使用内置库 json。

# html 操作
参考 html

使用内置库 html.parser。

```python
from html.parser import HTMLParser
```

使用该库解析 html 各个标签及其属性，文本。

# 图形界面编程 Pyside6
参考 Pyside6 目录。

`pip install pyside6`

# SMTP 邮件发送
参考 SMTP 目录。

内置模块 smtplib，email。

```python
import smtplib

# host:   SMTP 服务器主机。 你可以指定主机的 ip 地址或者域名如 :runoob.com，这个是可选参数。
# port:   如果你提供了 host 参数, 你需要指定 SMTP 服务使用的端口号，一般情况下 SMTP 端口号为 25。
# local_hostname: 如果SMTP在你的本机上，你只需要指定服务器地址为 localhost 即可。
smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )

# Python SMTP 对象使用 sendmail 方法发送邮件，语法如下：
# from_addr:  邮件发送者地址。
# to_addrs:   字符串列表，邮件发送地址。
# msg:        发送消息
# 这里要注意一下第三个参数，msg 是字符串，表示邮件。
# 我们知道邮件一般由标题，发信人，收件人，邮件内容，附件等构成，发送邮件的时候，要注意msg的格式。这个格式就是smtp协议中定义的格式。
smtpObj.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options]
```

# selenium 网页自动化
参考 selenium 目录。

`pip install selenium`

# unzip 解压缩
1. ZipFile

   内置模块 ZipFile，解压缩 .zip 文件，参考 unzip/zip.py 文件。

2. 7z

   参考 unzip/seven_zip.py 文件。

   `pip install py7zr`

# 网络操作
参考 web 目录。

内置模块 urllib 或安装 requests 模块，`pip install requests`

1. 下载整个网页

# 线程
参考 thread 目录。

内置模块 threading.

1. 创建线程
2. 使用互斥锁

# 其它
1. 获取用户家目录 `base/base.py`
2. 递归显示某一类的所有子类 `base/base.py`
3. 变量类型判断 `base/base.py`
4. 注册表读取，获取 chrome 版本 `base/base.py`
5. 异常、异常重定向、断言 `base/debug.py`
6. 运行外部命令 `base/ex_cmd.py`
7. 正则表达式 `base/regexp.py`