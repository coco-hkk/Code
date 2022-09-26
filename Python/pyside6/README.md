PySide6 基础知识。

- [PySide6](#pyside6)
- [模板](#模板)
  - [对话框](#对话框)
  - [布局](#布局)
  - [日志](#日志)
  - [线程](#线程)

# PySide6
Qt6 的 python 版本。

```bat
:: 使用 Qt Designer 设计图形界面。
pyside6-designer.exe

:: 使用 pyside6-uic.exe 将 .ui 文件转换为 .py 文件。
pyside6-uic.exe mainwindow.ui -o ui_mainwindow.py
```

# 模板
## 对话框
1. 文件对话框 `file.py`
2. 信息提示对话框 `dialog.py`

## 布局
1. stack 页面及切换 `stack_00.py`

## 日志
1. print 重定向到 widget `print_log.py`
2. logging 模块日志输出 `logging_log.py`

## 线程
1. 线程 `thread_00.py`