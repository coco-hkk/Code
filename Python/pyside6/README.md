PySide6 基础知识。

- [PySide6](#pyside6)
- [模板](#模板)

# PySide6
Qt6 的 python 版本。

```bat
:: 使用 Qt Designer 设计图形界面。
pyside6-designer.exe

:: 使用 pyside6-uic.exe 将 .ui 文件转换为 .py 文件。
pyside6-uic.exe test.ui -o test.py
```

# 模板
- 打开文件对话框，file.py
- 信息提示对话框，dialog.py
- 按钮选项卡切换，stack_widget
- print 重定向到 GUI，print_display