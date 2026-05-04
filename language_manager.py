"""
language_manager.py — 语言切换管理器
=====================================
负责根据当前语言代码，将翻译字典中的文本
应用到UI窗口的所有控件上。
"""

from PySide6 import QtWidgets
from translations import TRANSLATIONS
from icon_manager import svg_to_icon, resource_path


class LanguageManager:
    """
    语言管理器类。
    管理当前语言状态，并提供切换和应用语言的方法。

    属性:
        current_lang (str): 当前语言代码，'zh' 或 'en'
        ui (QMainWindow):   UI窗口实例引用
    """

    def __init__(self, ui_window, default_lang="zh"):
        """
        初始化语言管理器。

        参数:
            ui_window:    QUiLoader加载的主窗口对象
            default_lang: 默认语言代码，'zh'（中文）或 'en'（英文）
        """
        self.ui = ui_window
        self.current_lang = default_lang

    def toggle_language(self):
        """
        切换语言（中↔英），并立即应用到整个界面。
        """
        self.current_lang = "en" if self.current_lang == "zh" else "zh"
        self.apply_language()

        # 切换后更新语言按钮的图标颜色
        lang_btn = self.ui.findChild(QtWidgets.QPushButton, "pushButton_language")
        if lang_btn:
            # 悬停态时图标为白色，正常态为主题色
            color = "#0EA5E9"
            icon = svg_to_icon(
                resource_path("resources/icon_language.svg"),
                size=24, color=color
            )
            lang_btn.setIcon(icon)

        print(f"[语言切换] 当前语言: {self.current_lang}")

    def get_text(self, key):
        """
        获取当前语言下指定键的翻译文本。

        参数:
            key: 翻译字典中的键名
        返回:
            str: 翻译后的文本，键不存在时返回键名本身
        """
        return TRANSLATIONS.get(self.current_lang, {}).get(key, key)

    def apply_language(self):
        """
        将当前语言的所有翻译文本应用到UI界面。
        包括：窗口标题、标签、按钮、输入框占位符、工具提示、状态栏。
        """
        t = TRANSLATIONS[self.current_lang]

        # ----- 窗口标题 -----
        self.ui.setWindowTitle(t["window_title"])

        # ----- 标签文本 -----
        label_map = {
            "label_app_title":      "app_title",
            "label_section_params": "section_params",
            "label_section_data":   "section_data",
            "label":                "label_jiange_desc",
            "label_2":              "label_pingjun_desc",
            "label_qshangxiaxian":  "label_qshangxiaxian",
            "label_jiange":         "label_jiange_status",
            "label_pingjun":        "label_pingjun_status",
        }
        for obj_name, key in label_map.items():
            widget = self.ui.findChild(QtWidgets.QLabel, obj_name)
            if widget:
                widget.setText(t[key])

        # ----- 按钮文本 -----
        btn_map = {
            "pushButton_xiugai":        "btn_xiugai",
            "pushButton_xiugaipingjun": "btn_xiugaipingjun",
            "pushButton_qshangxian":    "btn_qshangxian",
            "pushButton_qxiaxian":      "btn_qxiaxian",
            "pushButton_selectsw":      "btn_selectsw",
            "pushButton_selectsn":      "btn_selectsn",
            "pushButton_selectswall":   "btn_selectswall",
            "pushButton_selectsnall":   "btn_selectsnall",
            "pushButton":               "btn_export",
            "pushButton_language":      "btn_language",
        }
        for obj_name, key in btn_map.items():
            widget = self.ui.findChild(QtWidgets.QPushButton, obj_name)
            if widget:
                widget.setText(t[key])

        # ----- 输入框占位符 -----
        placeholder_map = {
            "lineEdit_jiange":     "ph_jiange",
            "lineEdit_pingjun":    "ph_pingjun",
            "lineEdit_qshangxian": "ph_shangxian",
            "lineEdit_qxiaxian":   "ph_xiaxian",
        }
        for obj_name, key in placeholder_map.items():
            widget = self.ui.findChild(QtWidgets.QLineEdit, obj_name)
            if widget:
                widget.setPlaceholderText(t[key])

        # ----- 工具提示 -----
        tooltip_map = {
            "pushButton_xiugai":        "tip_xiugai",
            "pushButton_xiugaipingjun": "tip_xiugaipingjun",
            "pushButton_qshangxian":    "tip_qshangxian",
            "pushButton_qxiaxian":      "tip_qxiaxian",
            "pushButton_selectsw":      "tip_selectsw",
            "pushButton_selectsn":      "tip_selectsn",
            "pushButton_selectswall":   "tip_selectswall",
            "pushButton_selectsnall":   "tip_selectsnall",
            "pushButton":               "tip_export",
            "pushButton_language":      "tip_language",
        }
        for obj_name, key in tooltip_map.items():
            widget = self.ui.findChild(QtWidgets.QPushButton, obj_name)
            if widget:
                widget.setToolTip(t[key])

        # ----- 状态栏 -----
        self.ui.statusbar.showMessage(t["status_ready"])
