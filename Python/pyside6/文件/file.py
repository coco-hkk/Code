"""文件相关 UI
1. 选择文件
2. 选择目录
"""
import sys
from PySide6.QtWidgets import *

class FileWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("文件相关操作")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """UI 初始化"""
        self.button1 = QPushButton("文件")
        self.button2 = QPushButton("目录")
        self.lineEdit = QLineEdit(self)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)

        self.button1.clicked.connect(self.select_file_path)
        self.button2.clicked.connect(self.select_dir_path)

        self.show()

    def select_file_path(self):
        """QFileDialog 获取文件路径"""
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        file_path_list, _ = QFileDialog.getOpenFileNames(self, 
                                                         "请选择文本",
                                                         "",
                                                         "All Files (*);;Python Files (*.py)",
                                                         options=options)
        file_path = ",".join(str(i) for i in file_path_list)
        self.lineEdit.setText(file_path)

    def select_dir_path(self):
        """QFileDialog 获取目录路径"""
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        dir_path = QFileDialog.getExistingDirectory(self,
                                                    "请选择目录",
                                                    "",
                                                    options=options)
        self.lineEdit.setText(dir_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = FileWidget()
    sys.exit(app.exec())
