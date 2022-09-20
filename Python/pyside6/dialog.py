import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(431, 166)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 50, 91, 41))
        #font = QtGui.QFont()
        #font.setFamily("YaHei Consolas Hybrid")
        #font.setPointSize(10)
        #self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "对话框"))
        self.pushButton.setText(_translate("Form", "弹出对话框"))

class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self):
        super(MyMainForm, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_message)

    def show_message(self):
        QMessageBox.information(self, '信息提示对话框', 'Info', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        QMessageBox.question(self, "提问对话框", "Question", QMessageBox.Yes | QMessageBox.No)
        QMessageBox.warning(self, "警告对话框", "Warning", QMessageBox.Yes | QMessageBox.No)
        QMessageBox.critical(self, "严重错误对话框", "Error", QMessageBox.Yes | QMessageBox.No)
        QMessageBox.about(self, "关于对话框", "About Me")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyMainForm()
    win.show()
    sys.exit(app.exec())