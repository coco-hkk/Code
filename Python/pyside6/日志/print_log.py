"""将 print 结果输出到 GUI"""
import sys
from PySide6.QtCore import QEventLoop, QTimer, QObject, Signal
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QTextCursor

from ui_mainwindow import Ui_Form


class EmittingStr(QObject):
    textWritten = Signal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

        loop = QEventLoop()
        QTimer.singleShot(100, loop.quit)
        loop.exec()
        QApplication.processEvents()

    def flush(self):
        pass


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # 将输出重定向到 textBrowser 中
        sys.stdout = EmittingStr()
        sys.stdout.textWritten.connect(self.outputWritten)

        self.pushButton.clicked.connect(lambda: print("打印 log"))

    def outputWritten(self, text):
        cursor = self.textBrowser.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.textBrowser.setTextCursor(cursor)
        self.textBrowser.ensureCursorVisible()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
