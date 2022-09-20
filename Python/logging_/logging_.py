"""Log 日志输出模块

内置模块
默认情况下，logging 模块将日志打印到了标准输出，且只显示大于等于 WARNING 级别的
日志。日志级别为： CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET

作者：coco-hkk
日期：2022年9月9日
"""
import sys
import logging
import logging.config

class LevelFilter(logging.Filter):
    """log 级别过滤"""
    def filter(self, record):
        if record.levelno < logging.WARNING:
            return False
        return True

class StringFilter(logging.Filter):
    """log 字符串过滤"""
    def filter(self, record):
        if record.msg.find('abc') == -1:
            return True
        return False

def logger_filter():
    """带有过滤功能的 log 输出"""
    local_log = logging.getLogger('test')
    local_log.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler(sys.stdout)
    local_log.addHandler(stream_handler)
    local_log.warning('this is warning-1')
    local_log.info('this is info-1')

    local_log.addFilter(LevelFilter())
    local_log.warning('this is warning-2')
    local_log.info('this is info-2')

    stream_handler.addFilter(StringFilter())
    local_log.warning('this is warning-3')
    local_log.info('this is info-3')
    local_log.warning('this is warning-abc')

def logger(filename, logger_name=__file__):
    """log 输出到终端和文件中

    Args:
        filename: 日志文件路径
        logger_name: 记录器名字
    Returns:
        返回操作日志输出的句柄
    """
    # 创建一个记录器
    local_log = logging.getLogger(logger_name)

    # 设置日志级别为 DEBUG，只有日志级别大于等于 DEBUG 的日志才会输出
    local_log.setLevel(logging.DEBUG)

    # 创建 stream 类型的处理器，默认为标准输出
    stream_handler = logging.StreamHandler(stream=None)
    # 指定日志级别，低于这个级别的日志将被忽略
    stream_handler.setLevel(logging.DEBUG)

    # 创建 file 类型的处理器，输出到文件中
    file_handler = logging.FileHandler(filename, mode='a', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)

    # 本质上它是个“什么都不做”的 handler，由库开发者使用
    # null_handler = logging.NullHandler()

    # 设置日志消息格式
    # fmt 是消息的格式化字符串，如果不指明 fmt，将使用'%(message)s'
    # %(levelno)s    打印日志级别的数值
    # %(levelname)s  打印日志级别名称
    # %(pathname)s   打印当前执行程序的路径
    # %(filename)s   打印当前执行程序名称
    # %(funcName)s   打印日志的当前函数
    # %(lineno)d     打印日志的当前行号
    # %(asctime)s    打印日志的时间
    # %(thread)d     打印线程 ID
    # %(threadName)s 打印线程名称
    # %(process)d    打印进程 ID
    # %(message)s    打印日志信息
    #
    # datefmt 是日期字符串，如果不指明 datefmt，将使用 ISO8601 日期格式。
    # %a 本地的缩写工作日名称
    # %A 本地的完整工作日名称
    # %b 本地的缩写月份名称
    # %B 本地的全月名称
    # %c 本地的适当日期和时间表示
    # %d 每月的一天作为小数 [01，31]
    # %H 小时（24 小时时钟）作为小数 [00，23]
    # %I 小时（12 小时时钟）作为小数目 [01，12]
    # %j 一年中的一天作为小数 [001，366]
    # %m 月作为小数 [01，12]
    # %M 分钟作为小数 [00，59]
    # %p 本地相当于上午或下午
    # %S 第二为小数 [00，61]
    # %U 年度周数（星期日为一周的第一天）为小数 [00，53] 第一个星期天前的新年中的所有日子都被认为是在第 0 周
    # %w 平日作为小数 [0 （星期日）， 6]
    # %W 年度周数（星期一为一周的第一天）为小数 [00，53] 第一个星期一之前的新年的所有日子都被认为是在第 0 周
    # %x 本地的适当日期表示
    # %X 本地的适当时间表示
    # %y 没有世纪的年份作为小数 [00，99]
    # %Y 以世纪为小数的年份
    # %Z 时区名称（如果没有时区，则不存在字符）
    # %% 字面意思 %
    # logging.Formatter(fmt, datefmt)
    formatter = logging.Formatter("%(asctime)s %(lineno)s \t %(message)s",
                                      datefmt="%H:%M:%S")
    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # 为 log 增加处理器
    local_log.addHandler(stream_handler)
    local_log.addHandler(file_handler)

    # 删除处理器
    #local_log.removeHandler(file_handler)

    return local_log

def logger_fileconfig(config_name, logger_name):
    """从配置文件中读取 logging 配置"""
    logging.config.fileConfig(config_name)

    return logging.getLogger(logger_name)

def logging_basic():
    """简单例子"""
    # 为日志模块配置基础信息，这里将日志格式定为 时间-日志级别-消息，最低可显示的级别定为 DEBUG
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
    logging.debug('test debug')
    logging.error('test error')

    # 禁用日志功能，CRITICAL 为最高级别的日志类别，所有的日志都会被禁用
    # 该语句应该放在其它所有 logging 语句之前
    logging.disable(logging.CRITICAL)

def logging_exception():
    """将异常记录到 test.txt 文件中"""
    logging.basicConfig(filename="test.txt", level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
    try:
        raise Exception("test")
    except Exception as e:
        logging.exception(e)

if __name__ == "__main__":
    log = logger("test.txt")
    log.debug('debug message')
    log.info('info message')
    log.warning('warning message')
    log.error('error message')
    log.critical('critical message')

    log1 = logger_fileconfig("./logging.conf", "example01")
    log1.debug('debug message')
    log1.info('info message')
    log1.warning('warning message')
    log1.error('error message')
    log1.critical('critical message')

    logger_filter()
