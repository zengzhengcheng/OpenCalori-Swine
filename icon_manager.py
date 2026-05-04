"""
icon_manager.py — SVG图标加载与管理模块
=======================================
提供将SVG文件渲染为QIcon的工具函数，
以及统一管理所有按钮图标的分配逻辑。
"""

import os
from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QIcon, QPixmap, QPainter
from PySide6.QtCore import QSize
from PySide6.QtSvg import QSvgRenderer


def resource_path(relative_path):
    """
    获取资源文件的绝对路径。
    兼容开发环境和 PyInstaller 打包后的路径。

    参数:
        relative_path: 相对于项目根目录的路径，如 'resources/app_icon.svg'
    返回:
        str: 资源文件的绝对路径
    """
    base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)


def svg_to_icon(svg_path, size=24, color="#FFFFFF"):
    """
    将SVG文件渲染为指定颜色和尺寸的QIcon。

    原理：
      1. 读取SVG源码
      2. 将 stroke="currentColor" 替换为指定颜色
      3. 通过 QSvgRenderer 渲染到 QPixmap
      4. 封装为 QIcon 返回

    参数:
        svg_path: SVG文件的绝对路径
        size:     图标尺寸（像素，正方形）
        color:    图标颜色（十六进制，如 "#FFFFFF"）
    返回:
        QIcon: 渲染后的图标对象，若文件不存在则返回空图标
    """
    if not os.path.exists(svg_path):
        print(f"[图标警告] SVG文件不存在: {svg_path}")
        return QIcon()

    # 读取SVG源码并替换颜色标记
    with open(svg_path, 'r', encoding='utf-8') as f:
        svg_content = f.read()

    svg_content = svg_content.replace('stroke="currentColor"', f'stroke="{color}"')
    svg_content = svg_content.replace('fill="currentColor"', f'fill="{color}"')

    # 渲染SVG到位图
    renderer = QSvgRenderer(QtCore.QByteArray(svg_content.encode('utf-8')))
    pixmap = QPixmap(size, size)
    pixmap.fill(QtCore.Qt.transparent)

    painter = QPainter(pixmap)
    renderer.render(painter)
    painter.end()

    return QIcon(pixmap)


# ==========================================
# 图标-按钮映射配置
# ==========================================
# 格式: { 按钮objectName: (SVG文件名, 图标颜色) }
BUTTON_ICON_MAP = {
    "pushButton_xiugai":        ("icon_edit.svg",     "#FFFFFF"),
    "pushButton_xiugaipingjun": ("icon_edit.svg",     "#FFFFFF"),
    "pushButton_qshangxian":    ("icon_edit.svg",     "#FFFFFF"),
    "pushButton_qxiaxian":      ("icon_edit.svg",     "#FFFFFF"),
    "pushButton_selectsw":      ("icon_file.svg",     "#FFFFFF"),
    "pushButton_selectsn":      ("icon_file.svg",     "#FFFFFF"),
    "pushButton_selectswall":   ("icon_folder.svg",   "#FFFFFF"),
    "pushButton_selectsnall":   ("icon_folder.svg",   "#FFFFFF"),
    "pushButton":               ("icon_export.svg",   "#FFFFFF"),
    "pushButton_language":      ("icon_language.svg",  "#0EA5E9"),
}


def setup_all_button_icons(ui_window):
    """
    为UI窗口中所有已映射的按钮设置SVG图标。

    参数:
        ui_window: QUiLoader加载的主窗口对象
    """
    icon_size = QSize(18, 18)

    for obj_name, (svg_name, color) in BUTTON_ICON_MAP.items():
        btn = ui_window.findChild(QtWidgets.QPushButton, obj_name)
        if btn:
            svg_path = resource_path(f"resources/{svg_name}")
            icon = svg_to_icon(svg_path, size=24, color=color)
            btn.setIcon(icon)
            btn.setIconSize(icon_size)


def setup_app_icon(ui_window):
    """
    设置应用程序图标，同时作用于窗口标题栏和任务栏。

    参数:
        ui_window: QUiLoader加载的主窗口对象
    """
    icon_path = resource_path('resources/app_icon.svg')
    if os.path.exists(icon_path):
        # 应用图标需要较大尺寸
        app_icon = svg_to_icon(icon_path, size=64, color="#0EA5E9")
        ui_window.setWindowIcon(app_icon)
        # 设置应用级图标（影响任务栏）
        app_instance = QtWidgets.QApplication.instance()
        if app_instance:
            app_instance.setWindowIcon(app_icon)
    else:
        print(f"[图标警告] 应用图标不存在: {icon_path}")
