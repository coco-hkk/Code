"""python 调试相关"""
import traceback

# 异常抛出
def exception_example():
    """
    正常情况下，当 python 尝试执行无效代码时，就会抛出异常。
    这些异常都是程序提前定义好的，可以使用 try-except 来处理异常。
    """
    number = input("请输入大于 2 的数字：")
    if number <= 2:
        # 人为抛出异常
        raise Exception("数字小于 2！")
    else:
        print(number)

    """此时结合 try-exception 处理"""
    try:
        number = int(input("请输入一个大于 2 的数字："))
        if number <= 2:
            # 人为抛出异常
            raise Exception("数字小于 2！")
        else:
            print(number)
    except Exception:
        print("数字输入不符合要求！")
        

# 异常重定向
def exception_rewrite():
    """
    这里再介绍一种异常重定向的方法，也可避免异常抛出直接导致的程序崩溃。
    通过使用 traceback.format_exc 将异常重定向为字符串，同时可再将该
    字符串写入一个文本文件中，用于后续日志查询定位。
    """
    try:
        raise Exception("This is a exception")
    except Exception:
        with open(r'test.txt', 'w', encoding='utf-8') as f:
            f.write(traceback.format_exc())

# 断言
def assert_example():
    """
    使用 python 中的断言机制判断程序是否存在 bug(检查不通过会抛出异常)
    通过 assert 判断真假，回显内容字符串的格式，
    当判断为真(True)，则不抛出异常
    当判断为假(False)，则抛出 AssertionError 异常，并显示“回显内容字符串”
    """
    # 假定 door_status 值为 open，而实际赋值也为 open，故这里断言检测通过，不会抛出异常
    door_status = 'open'
    assert door_status == 'open', 'The door need to be "open".'

    door_status = 'I can\'t do that.'
    assert door_status == 'open', 'The door need to be "open".'

if __name__ == "__main__":
    #exception_rewrite()
    assert_example()