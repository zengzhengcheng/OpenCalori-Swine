"""
slot_handlers.py — 信号槽处理函数（后端接口层）
================================================
本模块包含所有按钮点击的槽函数实现。
客户应在此文件中编写自己的核心业务逻辑。

每个槽函数都有清晰的注释说明：
  - 对应的按钮 objectName
  - 关联的输入控件
  - 期望的业务逻辑
"""

from PySide6 import QtWidgets


class SlotHandlers:
    """
    槽函数处理类。
    所有按钮点击事件的处理逻辑集中在此类中。

    客户使用方式：
      1. 直接修改本类中对应的方法，添加业务逻辑
      2. 或继承本类，在子类中覆写需要的方法
    """

    def __init__(self, ui_window, lang_manager):
        """
        初始化槽函数处理器。

        参数:
            ui_window:    QUiLoader加载的主窗口对象
            lang_manager: LanguageManager实例，用于获取当前语言
        """
        self.ui = ui_window
        self.lang = lang_manager

    def connect_all(self):
        """
        将所有按钮的 clicked 信号连接到对应的槽函数。
        此方法应在初始化完成后调用一次。
        """
        # 参数修改按钮
        self._connect_button("pushButton_xiugai",        self.on_xiugai_jiange)
        self._connect_button("pushButton_xiugaipingjun", self.on_xiugai_pingjun)
        self._connect_button("pushButton_qshangxian",    self.on_xiugai_shangxian)
        self._connect_button("pushButton_qxiaxian",      self.on_xiugai_xiaxian)

        # 数据选择按钮
        self._connect_button("pushButton_selectsw",      self.on_select_sw_data)
        self._connect_button("pushButton_selectsn",      self.on_select_sn_data)
        self._connect_button("pushButton_selectswall",   self.on_select_sw_folder)
        self._connect_button("pushButton_selectsnall",   self.on_select_sn_folder)

        # 输出数据按钮
        self._connect_button("pushButton",               self.on_output_data)

        # 语言切换按钮
        self._connect_button("pushButton_language",      self.on_toggle_language)

        print("[信息] 所有信号槽已连接")

    def _connect_button(self, object_name, slot_func):
        """
        内部辅助方法：将指定按钮的clicked信号连接到槽函数。

        参数:
            object_name: 按钮的objectName
            slot_func:   要连接的槽函数
        """
        btn = self.ui.findChild(QtWidgets.QPushButton, object_name)
        if btn:
            btn.clicked.connect(slot_func)
        else:
            print(f"[警告] 未找到按钮: {object_name}")

    # ==========================================
    # 语言切换
    # ==========================================
    def on_toggle_language(self):
        """
        槽函数：中英文切换
        ──────────────────
        对应按钮: pushButton_language
        """
        self.lang.toggle_language()

    # ==========================================
    # 参数修改槽函数
    # ==========================================
    def on_xiugai_jiange(self):
        """
        槽函数：修改时间间隔
        ──────────────────
        对应按钮:  pushButton_xiugai
        关联输入:  lineEdit_jiange（用户输入的分钟数）
        关联标签:  label_jiange（显示当前间隔值）

        客户在此编写时间间隔修改逻辑。
        """
        line_edit = self.ui.findChild(QtWidgets.QLineEdit, "lineEdit_jiange")
        label = self.ui.findChild(QtWidgets.QLabel, "label_jiange")

        if line_edit and label:
            value = line_edit.text().strip()
            if value:
                # 根据当前语言更新状态标签
                fmt_key = "label_jiange_fmt"
                fmt_str = self.lang.get_text(fmt_key)
                label.setText(fmt_str.format(value=value))
                print(f"[参数修改] 时间间隔 → {value} 分钟")
            else:
                print("[参数修改] 未输入时间间隔值")

    def on_xiugai_pingjun(self):
        """
        槽函数：修改产热平均时间间隔
        ──────────────────────────
        对应按钮:  pushButton_xiugaipingjun
        关联输入:  lineEdit_pingjun（用户输入的秒数）
        关联标签:  label_pingjun（显示当前间隔值）

        客户在此编写平均时间间隔修改逻辑。
        """
        line_edit = self.ui.findChild(QtWidgets.QLineEdit, "lineEdit_pingjun")
        label = self.ui.findChild(QtWidgets.QLabel, "label_pingjun")

        if line_edit and label:
            value = line_edit.text().strip()
            if value:
                fmt_key = "label_pingjun_fmt"
                fmt_str = self.lang.get_text(fmt_key)
                label.setText(fmt_str.format(value=value))
                print(f"[参数修改] 产热平均时间间隔 → {value}s")
            else:
                print("[参数修改] 未输入平均时间间隔值")

    def on_xiugai_shangxian(self):
        """
        槽函数：修改呼吸商上限
        ──────────────────
        对应按钮:  pushButton_qshangxian
        关联输入:  lineEdit_qshangxian（用户输入的上限值）
        关联标签:  label_qshangxiaxian（显示当前上下限）

        客户在此编写上限修改逻辑。
        """
        line_edit = self.ui.findChild(QtWidgets.QLineEdit, "lineEdit_qshangxian")
        if line_edit:
            value = line_edit.text().strip()
            if value:
                print(f"[参数修改] 呼吸商上限 → {value}")
                # TODO: 客户在此添加上限修改的业务逻辑
                # 例如：更新 label_qshangxiaxian 的显示文本
            else:
                print("[参数修改] 未输入上限值")

    def on_xiugai_xiaxian(self):
        """
        槽函数：修改呼吸商下限
        ──────────────────
        对应按钮:  pushButton_qxiaxian
        关联输入:  lineEdit_qxiaxian（用户输入的下限值）
        关联标签:  label_qshangxiaxian（显示当前上下限）

        客户在此编写下限修改逻辑。
        """
        line_edit = self.ui.findChild(QtWidgets.QLineEdit, "lineEdit_qxiaxian")
        if line_edit:
            value = line_edit.text().strip()
            if value:
                print(f"[参数修改] 呼吸商下限 → {value}")
                # TODO: 客户在此添加下限修改的业务逻辑
            else:
                print("[参数修改] 未输入下限值")

    # ==========================================
    # 数据选择槽函数
    # ==========================================
    def on_select_sw_data(self):
        """
        槽函数：选择室外数据文件
        ──────────────────────
        对应按钮: pushButton_selectsw

        客户在此编写文件选择对话框逻辑。
        示例代码已注释在下方。
        """
        print("[数据选择] 选择室外数据文件")
        # ===== 客户示例代码 =====
        # file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
        #     self.ui,
        #     "选择室外数据" if self.lang.current_lang == "zh" else "Select Outdoor Data",
        #     "",
        #     "CSV Files (*.csv);;Excel Files (*.xlsx);;All Files (*)"
        # )
        # if file_path:
        #     print(f"已选择: {file_path}")
        #     # 在此处理选中的文件...

    def on_select_sn_data(self):
        """
        槽函数：选择室内数据文件
        ──────────────────────
        对应按钮: pushButton_selectsn

        客户在此编写文件选择对话框逻辑。
        """
        print("[数据选择] 选择室内数据文件")
        # ===== 客户示例代码 =====
        # file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
        #     self.ui,
        #     "选择室内数据" if self.lang.current_lang == "zh" else "Select Indoor Data",
        #     "",
        #     "CSV Files (*.csv);;Excel Files (*.xlsx);;All Files (*)"
        # )
        # if file_path:
        #     print(f"已选择: {file_path}")

    def on_select_sw_folder(self):
        """
        槽函数：选择室外数据文件夹
        ────────────────────────
        对应按钮: pushButton_selectswall

        客户在此编写文件夹选择对话框逻辑。
        """
        print("[数据选择] 选择室外数据文件夹")
        # ===== 客户示例代码 =====
        # folder = QtWidgets.QFileDialog.getExistingDirectory(
        #     self.ui,
        #     "选择室外数据文件夹" if self.lang.current_lang == "zh" else "Select Outdoor Data Folder"
        # )
        # if folder:
        #     print(f"已选择文件夹: {folder}")

    def on_select_sn_folder(self):
        """
        槽函数：选择室内数据文件夹
        ────────────────────────
        对应按钮: pushButton_selectsnall

        客户在此编写文件夹选择对话框逻辑。
        """
        print("[数据选择] 选择室内数据文件夹")
        # ===== 客户示例代码 =====
        # folder = QtWidgets.QFileDialog.getExistingDirectory(
        #     self.ui,
        #     "选择室内数据文件夹" if self.lang.current_lang == "zh" else "Select Indoor Data Folder"
        # )
        # if folder:
        #     print(f"已选择文件夹: {folder}")

    # ==========================================
    # 数据输出槽函数
    # ==========================================
    def on_output_data(self):
        """
        槽函数：输出数据（核心功能入口）
        ──────────────────────────────
        对应按钮: pushButton

        这是整个应用的核心操作入口。
        客户应在此编写数据处理与导出的完整业务逻辑。
        """
        print("[数据输出] 触发输出数据")

        title = self.lang.get_text("msgbox_title")
        message = self.lang.get_text("msgbox_export")
        QtWidgets.QMessageBox.information(self.ui, title, message)

        # ===== 客户核心业务逻辑入口 =====
        # 1. 读取用户选择的室内/室外数据
        # 2. 根据参数设置进行数据处理
        # 3. 导出处理结果
        # 示例:
        # try:
        #     result = self.process_data()
        #     self.export_result(result)
        #     self.log_message("数据处理完成！")
        # except Exception as e:
        #     QtWidgets.QMessageBox.critical(self.ui, "错误", str(e))

    # ==========================================
    # 辅助方法（供客户扩展使用）
    # ==========================================
    def get_widget(self, object_name):
        """
        便捷方法：通过objectName获取UI中的任意控件。

        参数:
            object_name: 控件的objectName字符串
        返回:
            QWidget: 找到的控件对象，未找到则返回None
        """
        return self.ui.findChild(QtWidgets.QWidget, object_name)

    def log_message(self, message):
        """
        向滚动区域（日志面板）追加一条消息。

        参数:
            message: 要显示的消息文本
        """
        scroll_widget = self.ui.findChild(
            QtWidgets.QWidget, "scrollAreaWidgetContents"
        )
        if scroll_widget:
            # 确保滚动区域有布局
            from PySide6.QtCore import Qt
            if not scroll_widget.layout():
                from PySide6.QtWidgets import QVBoxLayout
                layout = QVBoxLayout(scroll_widget)
                layout.setAlignment(Qt.AlignTop)
                layout.setContentsMargins(10, 8, 10, 8)
                layout.setSpacing(4)

            label = QtWidgets.QLabel(message)
            label.setStyleSheet("color: #475569; font-size: 12px; padding: 2px 0;")
            label.setWordWrap(True)
            scroll_widget.layout().addWidget(label)
