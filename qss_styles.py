"""
qss_styles.py — 全局QSS样式定义
================================
所有界面样式在此统一管理。
颜色体系：
  - 主色调：天蓝 #0EA5E9（Sky-500）
  - 强调色：靛紫 #6366F1（Indigo-500）
  - 辅助色：青色 #06B6D4（Cyan-500）
  - 背景色：浅灰蓝 #F0F4F8
  - 卡片色：纯白 #FFFFFF
  - 文字色：深灰 #334155 / #1E293B
"""


def get_global_stylesheet():
    """
    返回完整的全局QSS样式表字符串。
    将此字符串通过 QWidget.setStyleSheet() 应用到主窗口即可。
    """
    return _GLOBAL_STYLE


# ==========================================
# QSS 样式定义（私有常量）
# ==========================================
_GLOBAL_STYLE = """

/* ============================================================
   1. 主窗口 & 顶级容器
   ============================================================ */
QMainWindow {
    background-color: #F0F4F8;
}
QWidget#centralwidget {
    background-color: #F0F4F8;
}

/* ============================================================
   2. 菜单栏 — 与主界面背景色一致，不显得突兀
   ============================================================ */
QMenuBar {
    background-color: #F0F4F8;
    border: none;
    padding: 2px 0px;
    color: #334155;
    font-size: 13px;
}
QMenuBar::item {
    background: transparent;
    padding: 4px 12px;
    border-radius: 4px;
}
QMenuBar::item:selected {
    background-color: #E2E8F0;
}

/* ============================================================
   3. 状态栏
   ============================================================ */
QStatusBar {
    background-color: #F0F4F8;
    border-top: 1px solid #E2E8F0;
    color: #64748B;
    font-size: 12px;
    padding: 2px 8px;
}

/* ============================================================
   4. 卡片面板（QFrame）
   ============================================================ */
QFrame#frame_params,
QFrame#frame_data {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
}

/* ============================================================
   5. 分割线
   ============================================================ */
QFrame#line_top,
QFrame#line_params {
    color: #E2E8F0;
    background-color: #E2E8F0;
    max-height: 1px;
    border: none;
}

/* ============================================================
   6. 标签（QLabel）
   ============================================================ */

/* 通用标签 */
QLabel {
    font-size: 13px;
    color: #334155;
    background: transparent;
    border: none;
    padding: 0px;
}

/* 应用主标题 */
QLabel#label_app_title {
    font-size: 20px;
    font-weight: bold;
    color: #0F172A;
    letter-spacing: 1px;
    padding: 4px 0px;
}

/* 区块标题 */
QLabel#label_section_params,
QLabel#label_section_data {
    font-size: 14px;
    font-weight: bold;
    color: #1E293B;
    padding-bottom: 4px;
    border: none;
}

/* 参数描述文字 */
QLabel#label,
QLabel#label_2 {
    font-size: 13px;
    color: #475569;
    padding: 2px 0px;
    line-height: 1.4;
}

/* 状态标签（高亮显示当前值） */
QLabel#label_jiange,
QLabel#label_pingjun {
    color: #0EA5E9;
    font-size: 13px;
    font-weight: bold;
    padding: 2px 4px;
    border: none;
}

/* 呼吸商状态标签 */
QLabel#label_qshangxiaxian {
    color: #6366F1;
    font-size: 13px;
    font-weight: bold;
    padding: 2px 0px;
}

/* ============================================================
   7. 输入框（QLineEdit）
   ============================================================ */
QLineEdit {
    border: 1.5px solid #CBD5E1;
    border-radius: 8px;
    padding: 7px 12px;
    background-color: #F8FAFC;
    font-size: 13px;
    color: #1E293B;
    selection-background-color: #0EA5E9;
    selection-color: #FFFFFF;
}
QLineEdit:hover {
    border-color: #94A3B8;
}
QLineEdit:focus {
    border-color: #0EA5E9;
    background-color: #FFFFFF;
}

/* ============================================================
   8. 按钮（QPushButton）— 通用基础样式
   ============================================================ */
QPushButton {
    background-color: #0EA5E9;
    color: #FFFFFF;
    border: none;
    border-radius: 8px;
    padding: 8px 18px;
    font-size: 13px;
    font-weight: 500;
}
QPushButton:hover {
    background-color: #38BDF8;
}
QPushButton:pressed {
    background-color: #0284C7;
}
QPushButton:disabled {
    background-color: #CBD5E1;
    color: #94A3B8;
}

/* ============================================================
   9. 修改参数按钮 — 靛紫色系
   ============================================================ */
QPushButton#pushButton_xiugai,
QPushButton#pushButton_xiugaipingjun,
QPushButton#pushButton_qshangxian,
QPushButton#pushButton_qxiaxian {
    background-color: #6366F1;
    border-radius: 8px;
}
QPushButton#pushButton_xiugai:hover,
QPushButton#pushButton_xiugaipingjun:hover,
QPushButton#pushButton_qshangxian:hover,
QPushButton#pushButton_qxiaxian:hover {
    background-color: #818CF8;
}
QPushButton#pushButton_xiugai:pressed,
QPushButton#pushButton_xiugaipingjun:pressed,
QPushButton#pushButton_qshangxian:pressed,
QPushButton#pushButton_qxiaxian:pressed {
    background-color: #4F46E5;
}

/* ============================================================
   10. 数据选择按钮 — 天蓝 & 青色双色系
   ============================================================ */
QPushButton#pushButton_selectsw,
QPushButton#pushButton_selectsn {
    background-color: #0EA5E9;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 500;
}
QPushButton#pushButton_selectsw:hover,
QPushButton#pushButton_selectsn:hover {
    background-color: #38BDF8;
}
QPushButton#pushButton_selectsw:pressed,
QPushButton#pushButton_selectsn:pressed {
    background-color: #0284C7;
}

QPushButton#pushButton_selectswall,
QPushButton#pushButton_selectsnall {
    background-color: #06B6D4;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 500;
}
QPushButton#pushButton_selectswall:hover,
QPushButton#pushButton_selectsnall:hover {
    background-color: #22D3EE;
}
QPushButton#pushButton_selectswall:pressed,
QPushButton#pushButton_selectsnall:pressed {
    background-color: #0891B2;
}

/* ============================================================
   11. 输出数据按钮 — 渐变主操作按钮
   ============================================================ */
QPushButton#pushButton {
    background-color: qlineargradient(
        x1:0, y1:0, x2:1, y2:0,
        stop:0 #0EA5E9, stop:1 #6366F1
    );
    font-size: 16px;
    font-weight: bold;
    letter-spacing: 3px;
    border-radius: 10px;
    padding: 12px 0px;
}
QPushButton#pushButton:hover {
    background-color: qlineargradient(
        x1:0, y1:0, x2:1, y2:0,
        stop:0 #38BDF8, stop:1 #818CF8
    );
}
QPushButton#pushButton:pressed {
    background-color: qlineargradient(
        x1:0, y1:0, x2:1, y2:0,
        stop:0 #0284C7, stop:1 #4F46E5
    );
}

/* ============================================================
   12. 语言切换按钮 — 描边透明样式
   ============================================================ */
QPushButton#pushButton_language {
    background-color: transparent;
    color: #0EA5E9;
    border: 2px solid #0EA5E9;
    border-radius: 8px;
    font-size: 13px;
    font-weight: bold;
    padding: 5px 14px;
}
QPushButton#pushButton_language:hover {
    background-color: #0EA5E9;
    color: #FFFFFF;
}
QPushButton#pushButton_language:pressed {
    background-color: #0284C7;
    border-color: #0284C7;
    color: #FFFFFF;
}

/* ============================================================
   13. 滚动区域（日志/提示）
   ============================================================ */
QScrollArea#scrollArea_tishi {
    border: 1px solid #E2E8F0;
    border-radius: 10px;
    background-color: #FFFFFF;
}
QScrollArea#scrollArea_tishi > QWidget > QWidget {
    background-color: #FFFFFF;
}

/* 滚动条美化 */
QScrollBar:vertical {
    background: #F1F5F9;
    width: 8px;
    border-radius: 4px;
    margin: 2px;
}
QScrollBar::handle:vertical {
    background: #CBD5E1;
    border-radius: 4px;
    min-height: 30px;
}
QScrollBar::handle:vertical:hover {
    background: #94A3B8;
}
QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {
    height: 0px;
}

/* ============================================================
   14. 工具提示
   ============================================================ */
QToolTip {
    background-color: #1E293B;
    color: #F8FAFC;
    border: none;
    border-radius: 6px;
    padding: 6px 12px;
    font-size: 12px;
}
"""
