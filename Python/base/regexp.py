"""正则表达式

1. re.match
2. re.search
3. re.findall
4. re.sub
5. re.finditer

re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回 None.
re.search 匹配整个字符串，直到找到一个匹配。
"""
import re


def compile_func():
    """compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。"""
    pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字
    m = pattern.match('one12twothree34four')        # 查找头部，没有匹配
    print(m)


def match_func():
    """
    re.match 尝试从字符串的 起始位置 匹配一个模式，如果不是起始位置匹配成功的话，match() 就返回 None

    使用 group(num) 或 groups() 匹配对象函数来获取匹配表达式。
    """
    # 在起始位置匹配，返回匹配索引 (0, 3)，索引号遵循左闭右开
    print(re.match('www', 'www.runoob.com').span())
    # 返回匹配的值
    print(re.match('www', 'www.runoob.com').group())
    # 不在起始位置匹配，返回 None
    print(re.match('com', 'www.runoob.com'))

    line = "Cats are smarter than dogs"

    # .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
    # (.*?) 表示"非贪婪"模式，只保存第一个匹配到的子串
    matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

    if matchObj:
        # 返回匹配到的字符串
        print("matchObj.group() : ", matchObj.group())
        print("matchObj.group(1) : ", matchObj.group(1))
        print("matchObj.group(2) : ", matchObj.group(2))
    else:
        print("No match!!")


def search_func():
    """
    re.search 扫描整个字符串并返回第一个成功的匹配。匹配成功返回一个匹配的对象，否则返回 None。

    使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。
    """
    # 在起始位置匹配，返回索引
    print(re.search('www', 'www.runoob.com').span())
    # 不在起始位置匹配，返回索引
    print(re.search('com', 'www.runoob.com').span())


def sub_func():
    """re.sub 用于替换字符串中的匹配项
    语法：
        re.sub(pattern, repl, string, count=0, flags=0)
    其中，repl 可以是函数
    """
    phone = "2004-959-559 # 这是一个电话号码"

    # 删除注释
    num = re.sub(r'#.*$', "", phone)
    print("电话号码 : ", num)

    # 移除非数字的内容
    num = re.sub(r'\D', "", phone)
    print("电话号码 : ", num)


def findall_func():
    """
    在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果有多个匹配模式，则返回元组列表，如果没有找到匹配的，则返回空列表 []。

    match 和 search 匹配一次，而 findall 匹配所有。
    match 和 search 没找到匹配返回 None，而 findall 返回 [].

    re.findall(pattern, string, flags=0)
    或
    pattern.findall(string[, pos[, endpos]])

    参数：
    pattern     匹配模式。
    string      待匹配的字符串。
    pos         可选参数，指定字符串的起始位置，默认为 0。
    endpos      可选参数，指定字符串的结束位置，默认为字符串的长度。
    """
    result1 = re.findall(r'\d+', 'runoob 123 google 456')

    pattern = re.compile(r'\d+')   # 查找数字
    result2 = pattern.findall('runoob 123 google 456')
    result3 = pattern.findall('run88oob123google456', 0, 10)

    print(result1)
    print(result2)
    print(result3)

    # 多个匹配模式，返回元组列表
    result = re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
    print(result)


def finditer_func():
    """和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。"""
    it = re.finditer(r"\d+", "12a32bc43jf3")
    for match in it:
        print(match.group())


def split_func():
    """
    split 方法按照能够匹配的子串将字符串分割后返回列表
    对于一个找不到匹配的字符串而言，split 不会对其作出分割
    """
    s = '1,2,3,4,a,5,6,7,b,9,10,11'

    # 分割次数，maxsplit=1 分割一次，默认为 0，不限制次数。
    res = re.split(',[a-b],', s, maxsplit=0, flags=0)
    print(res)


if __name__ == '__main__':
    # compile_func()
    # match_func()
    # search_func()
    # sub_func()
    # findall_func()
    # finditer_func()
    split_func()
