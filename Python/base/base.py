"""Python3 基础知识

作者: coco-hkk
日期: 2022年9月9日
"""

import os
import sys
import winreg

# 模块1
def typeof(variable):
    """变量类型判断

    type() 函数如果你只有第一个参数则返回对象的类型，三个参数返回新的类型对象。
    isinstance() 与 type() 区别：
        type() 不会认为子类是一种父类类型，不考虑继承关系。
        isinstance() 会认为子类是一种父类类型，考虑继承关系。
    如果要判断两个类型是否相同推荐使用 isinstance()。
    """
    type_ = None

    if isinstance(variable, int):
        type_ = 'int'
    elif isinstance(variable, str):
        type_ = 'str'
    elif isinstance(variable, float):
        type_ = 'float'
    elif isinstance(variable, list):
        type_ = 'list'
    elif isinstance(variable, tuple):
        type_ = 'tuple'
    elif isinstance(variable, dict):
        type_ = 'dict'
    elif isinstance(variable, set):
        type_ = 'set'

    return type_

# 模块2
def get_sub_classes(class_):
    """递归地显示某一类的所有子类"""
    for subclass in class_.__subclasses__():
        print(subclass)
        if len(class_.__subclasses__()) > 0:
            get_sub_classes(subclass)

# 模块3
def get_home_dir():
    '''获取当前 OS 的用户家目录'''
    if sys.platform == 'win32':
        homedir = os.environ['USERPROFILE']
    elif sys.platform == 'linux' or sys.platform == 'darwin':
        homedir = os.environ['HOME']
    else:
        raise NotImplemented(f'Error! Not this system. {sys.platform}')
    return homedir

# 模块4     参考：https://zhuanlan.zhihu.com/p/474712424
def get_chrome_version():
    '''从注册表获取 chrome 版本'''
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Google\Chrome\BLBeacon')
    chrome_version = winreg.QueryValueEx(key, 'version')[0]
    return chrome_version

if __name__ == '__main__':
    #get_sub_classes()
    print(get_home_dir())
    print(get_chrome_version())
