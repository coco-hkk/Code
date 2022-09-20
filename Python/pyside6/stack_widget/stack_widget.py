import sys
from PySide6.QtWidgets import *
from stack import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.window_init()

    def window_init(self):
        self.pushButton.clicked.connect(self.display_file)
        self.pushButton_2.clicked.connect(self.display_click)

    def display_file(self):
        self.stackedWidget.setCurrentIndex(1)

    def display_click(self):
        self.stackedWidget.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())