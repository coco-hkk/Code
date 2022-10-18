# Cython
1. Cython 是一种编程语言，它使得为 Python 编写 C 扩展就像 Python 本身一样容易。
2. 它旨在成为 Python 的超集，赋予它高级、面向对象、函数式和动态编程。
3. 此外，它的主要功能是支持作为语言一部分的可选静态类型声明。源代码被翻译成优化的 C/C++ 代码并编译为 Python 扩展模块。

安装 cython：`pip install cython`

# 代码实例
## hello.pyx
```python
#cython: language_level=3

def say_hello(name):
    print("Hello " + name + "!")
```

1. 使用 cython 将 hello.pyx 编译成 .c 文件。
2. .c 文件由 C 编译器编译成一个 `.so` 文件（在 windows 上是 `.pyd`），该文件可由 import 直接调用。

## setup.py
```python
from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Hello world app',
    ext_modules=cythonize("hello.pyx"),
    zip_safe=False,
)
```

运行指令 `python setup.py build_ext --inplace` 即可生成 .pyd 文件。

## 测试代码
```python
# 运行结果为：Hello Mr!
import hello
hello.say_hello("Mr")
```

# easycython
使用 easycython 不需要编写 setup.py 文件。

安装 easycython：`pip install easycython`