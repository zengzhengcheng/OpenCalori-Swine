"""
ui_loader.py — UI文件加载器
============================
负责动态加载 mainwindow.ui 文件并返回窗口实例。
"""

import os
import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
from icon_manager import resource_path


def load_main_window():
    """
    动态加载 mainwindow.ui 文件。

    返回:
        QMainWindow: 加载成功时返回窗口实例
        None: 加载失败时返回None
    """
    ui_path = resource_path('mainwindow.ui')

    # 检查文件是否存在
    if not os.path.exists(ui_path):
        print(f"[错误] 找不到UI文件: {ui_path}")
        return None

    # 打开文件
    ui_file = QFile(ui_path)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"[错误] 无法打开UI文件: {ui_file.errorString()}")
        return None

    # 使用QUiLoader加载
    loader = QUiLoader()
    ui_window = loader.load(ui_file)
    ui_file.close()

    if ui_window is None:
        print("[错误] QUiLoader 加载UI文件失败")
        return None

    print("[信息] UI文件加载成功")
    return ui_window
