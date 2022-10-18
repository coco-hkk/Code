"""ini 格式文件解析

作者：coco-hkk
日期：2022年9月9日
"""
import configparser

def ini_config(ini_file):
    '''解析 ini 配置文件

    Args:
        ini_file: 配置文件
    
    Returns:
        返回一个 ini 配置信息的字典
    '''
    cfg = configparser.ConfigParser()

    # 读取 ini 配置文件
    cfg.read(ini_file)

    # 读取 sections
    sections = cfg.sections()

    # 读取 secs
    sections_options = {}
    for sec in sections:
        options = cfg.options(sec)
        sections_options[sec] = options
    
    # 读取 sec 对应的 value
    all_info = {}
    for sec in sections:
        sec_values = {}
        for option in sections_options[sec]:
            value = cfg.get(sec, option)
            sec_values[option] = value
    
        all_info[sec] = sec_values

    return all_info

if __name__ == '__main__':
    info = ini_config('test.ini')
    print(info)