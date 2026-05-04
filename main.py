"""
main.py — 数据处理系统 · 主程序入口
====================================
职责：
  1. 创建 QApplication 实例
  2. 加载UI文件
  3. 应用样式、图标、语言
  4. 连接信号与槽
  5. 显示窗口并启动事件循环

所有具体逻辑已拆分到独立模块：
  - ui_loader.py        → UI文件加载
  - qss_styles.py       → 界面样式
  - icon_manager.py     → SVG图标管理
  - language_manager.py → 中英文切换
  - translations.py     → 翻译字典
  - slot_handlers.py    → 业务逻辑（后端接口）
"""

import sys
from PySide6 import QtWidgets, QtCore, QtGui

# 导入项目模块
from ui_loader import load_main_window
from qss_styles import get_global_stylesheet
from icon_manager import setup_all_button_icons, setup_app_icon
from language_manager import LanguageManager
from slot_handlers import SlotHandlers


class MainWindowWrapper(QtCore.QObject):
    """
    主窗口包装类。
    整合所有模块，完成界面初始化和事件绑定。
    """

    def __init__(self):
        super().__init__()

        # ---- 第1步：加载UI ----
        self.ui = load_main_window()
        if not self.ui:
            print("[致命错误] UI加载失败，程序退出")
            sys.exit(1)

        # ---- 第2步：应用全局QSS样式 ----
        self.ui.setStyleSheet(get_global_stylesheet())

        # ---- 第3步：设置应用图标 ----
        setup_app_icon(self.ui)

        # ---- 第4步：设置按钮SVG图标 ----
        setup_all_button_icons(self.ui)

        # ---- 第5步：初始化语言管理器（默认中文） ----
        self.lang_manager = LanguageManager(self.ui, default_lang="zh")
        self.lang_manager.apply_language()

        # ---- 第6步：初始化槽函数处理器并连接信号 ----
        self.slot_handlers = SlotHandlers(self.ui, self.lang_manager)
        self.slot_handlers.connect_all()

        # ---- 第7步：状态栏显示就绪 ----
        self.ui.statusbar.showMessage(
            self.lang_manager.get_text("status_ready")
        )

        print("[信息] 主窗口初始化完成")

    def show(self):
        """显示主窗口"""
        self.ui.show()


# ==========================================
# 程序入口
# ==========================================
if __name__ == '__main__':
    # 适配高分屏显示（兼容不同PySide6版本）
    if hasattr(QtCore.Qt.ApplicationAttribute, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(
            QtCore.Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True
        )
    if hasattr(QtCore.Qt.ApplicationAttribute, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(
            QtCore.Qt.ApplicationAttribute.AA_UseHighDpiPixmaps, True
        )

    # 创建应用实例
    app = QtWidgets.QApplication(sys.argv)

    # 设置全局字体（优先级从左到右，自动选择系统可用字体）
    font = QtGui.QFont()
    font.setFamilies([
        "Segoe UI",         # Windows 现代字体
        "SF Pro Display",   # macOS 系统字体
        "Noto Sans SC",     # Linux 中文字体
        "Microsoft YaHei",  # Windows 中文备选
        "PingFang SC",      # macOS 中文备选
    ])
    font.setPointSize(10)
    app.setFont(font)

    # 实例化主窗口并显示
    window = MainWindowWrapper()
    window.show()

    # 启动事件循环
    sys.exit(app.exec())
