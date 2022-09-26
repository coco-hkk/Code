import sys
import time
import logging

from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtGui import QTextCursor
from PySide6.QtCore import QThread, QObject, Signal, Slot
from ui_mainwindow import Ui_Form


# 定义传递日志的信号
class Signaller(QObject):
    """定义传递 log 的信号，为了正确初始化需要继承 QObject 或其子类"""
    signal = Signal(str, logging.LogRecord)


# 定义日志输出格式
class Formatter(logging.Formatter):
    def formatException(self, e):
        result = super(Formatter, self).formatException(e)
        return result

    def format(self, record):
        s = super(Formatter, self).format(record)
        if record.exc_text:
            s = s.replace('\n', '')
        return s


class GuiHandler(logging.Handler):
    """自定义 logging handler，将 log 输出到 widget"""

    def __init__(self, slot_func, *args, **kwargs):
        super(GuiHandler, self).__init__(*args, **kwargs)
        self.signaller = Signaller()
        self.signaller.signal.connect(slot_func)

    def emit(self, record):
        msg = self.format(record)
        self.signaller.signal.emit(msg, record)


class ButtonTest(QObject):
    """定义线程"""
    def __init__(self, logger=None):
        super(ButtonTest, self).__init__()
        self.logger = logger

    @Slot()
    def run(self):
        num = 5
        while True:
            self.logger.debug(f"test {num}")
            num -= 1
            time.sleep(2)
            try:
                result = 10 / 0
            except Exception:
                # 捕获 traceback
                self.logger.error('Faild to get result', exc_info = True)

            if num == 0:
                break


class MainWindow(QWidget, Ui_Form):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.logger = self.logger_init("test", self.show_text)

        self.setup_thread()

    def logger_init(self, logger_name, slot_func, *args, **kwargs):
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)

        my_handler = GuiHandler(slot_func, *args, **kwargs)

        format = Formatter(
            '%(asctime)s %(filename)s: %(lineno)-8d %(message)s', datefmt='%m月%d日 %H:%M')

        my_handler.setFormatter(format)
        my_handler.setLevel(logging.DEBUG)

        logger.addHandler(my_handler)
        return logger

    def setup_thread(self):
        self.thread1 = QThread(self)
        self.test_button = ButtonTest(self.logger)
        self.test_button.moveToThread(self.thread1)
        self.pushButton.clicked.connect(self.thread1.start)
        self.pushButton.clicked.connect(self.test_button.run)
        self.pushButton.clicked.connect(
            lambda: self.pushButton.setEnabled(False))

    def show_text(self, text):
        cursor = self.textBrowser.textCursor()
        cursor.movePosition(QTextCursor.NextRow)
        cursor.insertText(text)
        cursor.insertBlock()
        self.textBrowser.setTextCursor(cursor)
        self.textBrowser.ensureCursorVisible()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
