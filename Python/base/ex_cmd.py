"""
author: 郝宽宽
date:   2022年9月19日19:15:40
description:

Python 调用外部命令

网络上可查到最普通的三种方法：
1. os.system()
2. os.popen()
3. subprocess
"""
import os
import subprocess


def system_method():
    """
    os.system() 工作：
    1. 从主进程中 fork 一个子进程。
    2. 在子进程中调用 python 的 exec 函数去执行命令。
    3. 在主进程中调用 wait（阻塞）等待子进程结束。

    如果对于fork失败，system() 函数返回-1。调用成功返回 0.

    缺点：无法获取调用后的返回结果
    """
    # 查看 ip
    os.system('ifconfig')

    # 查看返回值，调用成功返回 0，不能通过 os.system() 获得命令输出的结果
    print(os.system('ifconfig'))

    # 如要获得命令输出结果，只能通过文件中转，如 result.txt
    os.system('ifconfig > result.txt')


def popen_method():
    """
    os.popen() 的调用方式和 os.system() 类似，不过它是通过创建一个管道的方式来fork子进程实现调用程序的。
    通过读取 popen 的返回对象，获取执行结果。
    """
    out = os.popen('ifconfig')

    # 获得命令输出结果
    print(out.read())


def subprocess_method():
    """
    subprocess 这个模块在 Python 用于产生子进程，可以连接子进程的标准输入输出，并且可以得到子进程的返回值。
    """
    # 1. Popen 执行终端命令，执行结果会直接打印出来
    # 2. 不是阻塞式调用，如果 popen 没有调用成功，还会执行后面语句
    subprocess.Popen('ipconfig', shell=True)

    # 1. check_output 执行终端命令，以字节的方式返回；但是执行结果不会打印出来
    # 2. 是阻塞式调用，如果 check_output 没有调用成功，不会执行后面的语句
    data = subprocess.check_output('ipconfig')
    print(data)
    # 3. 可以将返回的字节解码，打印出字符
    print(data.decode())

    # run 底层调用了 Popen
    test = subprocess.run('ipconfig', capture_output=True)
    print(test.stdout.decode())


if __name__ == '__main__':
    subprocess_method()
