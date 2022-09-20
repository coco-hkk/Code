"""解压缩 .zip 文件"""
import sys
from zipfile import ZipFile as unzip

"""
# getinfo 支持的属性
# ZipInfo.filename        获取文件名称。
# ZipInfo.date_time       获取文件最后修改时间。返回一个包含6个元素的元组：(年, 月, 日, 时, 分, 秒)
# ZipInfo.compress_type   压缩类型。
# ZipInfo.comment         文档说明。
# ZipInfo.extr            扩展项数据。
# ZipInfo.create_system   获取创建该zip文档的系统。
# ZipInfo.create_version  获取、创建zip文档的PKZIP版本。
# ZipInfo.extract_versio  获取、解压zip文档所需的PKZIP版本。
# ZipInfo.reserved        预留字段，当前实现总是返回0。
# ZipInfo.flag_bits       zip标志位。
# ZipInfo.volume          文件头的卷标。
# ZipInfo.internal_attr   内部属性。
# ZipInfo.external_attr   外部属性。
# ZipInfo.header_offset   文件头偏移位。
# ZipInfo.CRC             未压缩文件的CRC-32。
# ZipInfo.compress_size   获取压缩后的大小。
# ZipInfo.file_size       获取未压缩的文件大小
ZipFile.getinfo(name)   # 获取zip文档内指定文件的信息。返回一个zipfile.ZipInfo对象，它包括文件的详细信息

ZipFile.infolist()      # 获取zip文档内所有文件的信息，返回一个zipfile.ZipInfo的列表
ZipFile.namelist()      # 获取zip文档内所有文件的名称列表

# 将zip文档内的指定文件解压到当前目录
# member      指定要解压的文件名称或对应的ZipInfo对象
# path        指定解析文件保存的文件夹
# pwd         解压密码
ZipFile.extractall(member[, path[, pwd]])
ZipFile.extract(member[, path[, pwd]])

ZipFile.printdir()          # 将 zip 文档内的信息打印到控制台上
ZipFile.setpassword(pwd)    # 设置 zip 文档的密码
ZipFile.read(name[,pwd])    # 获取zip文档内指定文件的二进制数据

# 将指定文件添加到zip文档中
# filename      文件路径
# arcname       添加到zip文档之后保存的名称
# compress_type 压缩方法，它的值可以是 zipfile.ZIP_STORED 或 zipfile.ZIP_DEFLATED
ZipFile.write(filename[, arcname[, compress_type]])

ZipFile.writestr(zinfo_or_arcname, bytes)   # 支持将二进制数据直接写入到压缩文档
"""

def unzip_file(file_path, dir_path):
    """解压文件
    
    Args:
        file_path: 待解压文件
        dir_path: 解压目录
    """
    zip = unzip(file_path,'r')
    for file in zip.namelist():
        zip.extract(file, dir_path)
    zip.close()
    print('解压成功！')

if __name__ == '__main__':
    unzip_file(sys.argv[1], sys.argv[2])