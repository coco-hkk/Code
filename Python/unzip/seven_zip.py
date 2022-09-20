"""解压缩 7z 文件"""
from py7zr import SevenZipFile as unzip

def seven_unzip(file_path, dir_path, pwd=None):
    """解压 7z 文件

    Args:
        file_path: 7z 文件
        dir_path: 解压目录
        pwd: 解压密码
    """
    with unzip(file_path, mode='r', password=pwd) as seven_z: 
        # 解压到当前目录
        seven_z.extractall()
        # 解压到指定目录
        seven_z.extractall(dir_path)

if __name__ == '__main__':
    seven_unzip("test.7z", "./")