import os
import re

list_dir = []
list_file = []

root_dir = os.path.dirname(os.path.abspath(__file__))

def get_filepath(dir_path, list_file_name, list_dir_name):
    """递归获取文件路径和目录路径"""
    for file in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file)
        if os.path.isdir(file_path):
            get_filepath(file_path, list_file_name, list_dir_name)
            # 注意目录赋值的位置，要放在下面，这样才会将最里面的目录放在前面，便于后面重命名操作
            list_dir_name.append(file_path)
        else:
            list_file_name.append(file_path)

get_filepath(root_dir, list_file, list_dir)

for file in list_file:
    # 获取路径
    path = os.path.dirname(file)
    # 获取文件名，包括后缀
    filename = os.path.basename(file)

    print('正在处理文件: ' + file)
    if filename == '600学习网资源互换.txt' or filename == '600学习网www.600xue.com.url':
        os.remove(file)
        continue
    
    # 正则匹配替换
    filename_sub = re.sub(r'【.{4}：600xue.com】', '', filename)
    # 未匹配替换返回原字符串
    if filename == filename_sub:
        continue

    file_sub = os.path.join(path, filename_sub)
    os.rename(file, file_sub)

for dir in list_dir:
    # 获取路径
    path = os.path.dirname(dir)
    # 获取目录名
    dirname = os.path.basename(dir)

    print('正在处理目录: ' + dir)

    # 正则匹配替换
    dirname_sub = re.sub(r'【.{4}：600xue.com】', '', dirname)
    # 未匹配替换返回原字符串
    if dirname == dirname_sub:
        continue

    dir_sub = os.path.join(path, dirname_sub)
    os.rename(dir, dir_sub)