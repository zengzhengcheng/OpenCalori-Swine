import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
from PySide6 import QtCore, QtGui, QtWidgets

from icon_manager import setup_all_button_icons, setup_app_icon
from language_manager import LanguageManager
from qss_styles import get_global_stylesheet
from ui_loader import load_main_window


class ValueDict(dict):
    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, attr, value):
        self[attr] = value


def getvalue(dsn, dsw, jiange, pingjun, qshangxian, qxiaxian):
    jiangemessage = []
    tubianmessage = {}
    shangmessage = {}
    jingqimessage = {}
    delta = timedelta(minutes=-1 * jiange)
    head = True
    answer = []
    vd = ValueDict()
    columns = [chr(index) for index in range(ord("h"), ord("z") + 1)]
    columns.extend(["a" + chr(index) for index in range(ord("a"), ord("h") + 1)])
    df = pd.DataFrame(columns=columns)
    namecolumns = [
        "时间差",
        "室外O2浓度(%)",
        "室外NH3浓度(ppm)",
        "室外CH4浓度(ppm)",
        "室外CO2浓度(ppm)",
        "室内O2浓度(%)",
        "室内NH3浓度(ppm)",
        "室内CH4浓度(ppm)",
        "室内CO2浓度(ppm)",
        "小室温度(℃)",
        "小室湿度(%)",
        "排气流量(L/M)",
        "仪表流量(L/M)",
        "进气压力(kPa)",
        "小室压力(kPa)",
        "小室风速(m/s)",
        "水蒸气压",
        "流量L/M",
        "呼吸室体积L",
        "标准状况流量L/M",
        "呼吸室标准容积L",
        "氧含量L",
        "氨气含量L",
        "甲烷含量L",
        "二氧化碳含量L",
        "呼吸熵",
        "HP产热(kcal)",
    ]
    i = -1
    for _, row in dsn.iterrows():
        sntime = row["sntime"]
        qreuslt = dsw[str(sntime + delta):str(sntime)]
        try:
            if not qreuslt.empty:
                i += 1
                swrow = qreuslt.iloc[-1]
                vd.i, vd.j, vd.k, vd.l = swrow.values
                for index in range(ord("m"), ord("w") + 1):
                    key = chr(index)
                    vd[key] = row[key]
                if vd.v == 0:
                    vd.v = vd.u - 1
                if not head:
                    if abs(vd.m - vd.lastm) > 0.1:
                        tubianmessage[sntime] = i
                    vd.h = (sntime - lasttime).total_seconds()
                    vd.x = vd.r / 100 * (
                        3.999
                        + 0.45547 * vd.q
                        + 0.001708 * (vd.q ** 2)
                        + 0.000469 * (vd.q ** 3)
                    )
                    vd.y = (vd.s + vd.t) * vd.h / 60
                    vd.z = 7800
                    vd.aa = vd.y * (vd.v - vd.x) / 1013 * 273 / (273 + vd.q)
                    vd.ab = vd.z * (vd.v - vd.x) / 1013 * 273 / (273 + vd.q)
                    vd.ac = (vd.lastm - vd.m) * 0.01 * vd.ab + (vd.lasti - vd.lastm) * vd.aa * 0.01
                    vd.ad = (vd.n - vd.lastn) * 0.000001 * vd.ab + (vd.lastn - vd.lastj) * vd.aa * 0.000001
                    vd.ae = (vd.o - vd.lasto) * 0.000001 * vd.ab + (vd.lasto - vd.lastk) * vd.aa * 0.000001
                    vd.af = (vd.p - vd.lastp) * 0.000001 * vd.ab + (vd.lastp - vd.lastl) * vd.aa * 0.000001
                    if vd.ac <= 0:
                        tubianmessage[sntime] = i
                    vd.ag = np.inf if vd.ac == 0 else vd.af / vd.ac
                    if vd.ag < qxiaxian or vd.ag > qshangxian:
                        shangmessage[sntime] = i
                    vd.ah = (3.866 * vd.ac + 1.2 * vd.af - 0.518 * vd.ae) / vd.h * pingjun
                    answer.append(vd.ah)
                    for index in range(ord("i"), ord("w") + 1):
                        key = chr(index)
                        vd["last" + key] = vd[key]
                    lasttime = sntime

                    data = []
                    for index in range(ord("h"), ord("z") + 1):
                        data.append(vd[chr(index)])
                    for index in range(ord("a"), ord("h") + 1):
                        data.append(vd["a" + chr(index)])
                    df.loc[sntime] = data
                else:
                    head = False
                    for index in range(ord("i"), ord("w") + 1):
                        key = chr(index)
                        vd["last" + key] = vd[key]
                    lasttime = sntime
            else:
                jiangemessage.append(
                    f"{sntime}前{jiange}分钟内无对应室外数据，因此未计算该时间段的产热，如需调整，请增加时间间隔"
                )
                head = True

        except Exception as exc:
            print(exc)
            print(sntime)
    df.columns = namecolumns
    message = (jiangemessage, tubianmessage, shangmessage, jingqimessage)
    return df, message


def gettime(x):
    values = x.values[:6]
    time_tuple = tuple(np.append([int(i) for i in values], [0, 0, 0]))
    return datetime.fromtimestamp(time.mktime(time_tuple))


class MainWindowController(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.ui = load_main_window()
        if not self.ui:
            raise RuntimeError("UI load failed.")

        self.ui.setStyleSheet(get_global_stylesheet())
        setup_app_icon(self.ui)
        setup_all_button_icons(self.ui)

        self.currentPath = str(Path.cwd())
        self.jiange = 30
        self.pingjun = 300
        self.qshangxian = 1.2
        self.qxiaxian = 0.8
        self.dsn = None
        self.dsw = None

        self.lang_manager = LanguageManager(self.ui, default_lang="zh")
        self.lang_manager.apply_language()
        self._connect_signals()
        self.refresh_runtime_texts()
        self.set_status("status_ready")

    def _connect_signals(self):
        self._button("pushButton_selectsn").clicked.connect(self.getSNFilePath)
        self._button("pushButton_selectsw").clicked.connect(self.getSWFilePath)
        self._button("pushButton_selectswall").clicked.connect(self.getSWAllFile)
        self._button("pushButton_selectsnall").clicked.connect(self.getSNAllFile)
        self._button("pushButton").clicked.connect(self.write)
        self._button("pushButton_xiugai").clicked.connect(self.xiugaijiange)
        self._button("pushButton_xiugaipingjun").clicked.connect(self.xiugaipingjun)
        self._button("pushButton_qshangxian").clicked.connect(self.xiugaiqshangxian)
        self._button("pushButton_qxiaxian").clicked.connect(self.xiugaiqxiaxian)
        self._button("pushButton_language").clicked.connect(self.toggle_language)

    def _button(self, name):
        return self.ui.findChild(QtWidgets.QPushButton, name)

    def _label(self, name):
        return self.ui.findChild(QtWidgets.QLabel, name)

    def _line_edit(self, name):
        return self.ui.findChild(QtWidgets.QLineEdit, name)

    def tr(self, key):
        return self.lang_manager.get_text(key)

    def show(self):
        self.ui.show()

    def set_status(self, key, **kwargs):
        self.ui.statusbar.showMessage(self.tr(key).format(**kwargs))

    def log(self, key, **kwargs):
        message = self.tr(key).format(**kwargs)
        container = self.ui.findChild(QtWidgets.QWidget, "scrollAreaWidgetContents")
        if not container:
            return

        if not container.layout():
            layout = QtWidgets.QVBoxLayout(container)
            layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
            layout.setContentsMargins(10, 8, 10, 8)
            layout.setSpacing(4)

        label = QtWidgets.QLabel(message)
        label.setWordWrap(True)
        label.setStyleSheet("color: #475569; font-size: 12px; padding: 2px 0;")
        container.layout().addWidget(label)

    def show_info(self, key, **kwargs):
        QtWidgets.QMessageBox.information(
            self.ui,
            self.tr("msgbox_info_title"),
            self.tr(key).format(**kwargs),
        )

    def show_warning(self, key, **kwargs):
        QtWidgets.QMessageBox.warning(
            self.ui,
            self.tr("msgbox_warning_title"),
            self.tr(key).format(**kwargs),
        )

    def refresh_runtime_texts(self):
        self._label("label_jiange").setText(self.tr("label_jiange_fmt").format(value=self.jiange))
        self._label("label_pingjun").setText(self.tr("label_pingjun_fmt").format(value=self.pingjun))
        self._label("label_qshangxiaxian").setText(
            self.tr("label_qshangxiaxian_fmt").format(
                upper=self.qshangxian,
                lower=self.qxiaxian,
            )
        )

    def toggle_language(self):
        self.lang_manager.toggle_language()
        self.refresh_runtime_texts()
        self.set_status("status_language_switched", lang=self.tr("language_name"))
        self.log("log_language_switched", lang=self.tr("language_name"))

    def xiugaiqshangxian(self):
        try:
            self.qshangxian = float(self._line_edit("lineEdit_qshangxian").text())
            self.refresh_runtime_texts()
            self.set_status("status_limits_updated")
        except ValueError:
            self.show_warning("warn_float_required")

    def xiugaiqxiaxian(self):
        try:
            self.qxiaxian = float(self._line_edit("lineEdit_qxiaxian").text())
            self.refresh_runtime_texts()
            self.set_status("status_limits_updated")
        except ValueError:
            self.show_warning("warn_float_required")

    def xiugaipingjun(self):
        try:
            self.pingjun = int(self._line_edit("lineEdit_pingjun").text())
            self.refresh_runtime_texts()
            self.set_status("status_pingjun_updated", value=self.pingjun)
        except ValueError:
            self.show_warning("warn_pingjun_required")

    def xiugaijiange(self):
        try:
            self.jiange = int(self._line_edit("lineEdit_jiange").text())
            self.refresh_runtime_texts()
            self.set_status("status_jiange_updated", value=self.jiange)
        except ValueError:
            self.show_warning("warn_integer_required")

    def getSWAllFile(self):
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(
            self.ui,
            self.tr("dialog_select_sw_folder"),
            self.currentPath,
        )
        if not folder_path:
            return

        self.currentPath = str(Path(folder_path).resolve().parent)
        df_list = [self.getSWFileData(str(path.resolve())) for path in Path(folder_path).rglob("**/*.[xX][lL][sS]")]
        if not df_list:
            self.show_warning("warn_no_xls_found")
            return

        self.dsw = pd.concat(df_list).sort_index()
        self.set_status("status_selected_sw_folder")
        self.log("log_folder_selected", kind=self.tr("kind_outdoor_folder"), path=folder_path)

    def getSNAllFile(self):
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(
            self.ui,
            self.tr("dialog_select_sn_folder"),
            self.currentPath,
        )
        if not folder_path:
            return

        self.currentPath = str(Path(folder_path).resolve().parent)
        df_list = [self.getSNFileData(str(path.resolve())) for path in Path(folder_path).rglob("**/*.[xX][lL][sS]")]
        if not df_list:
            self.show_warning("warn_no_xls_found")
            return

        df = pd.concat(df_list).sort_values(by="sntime")
        sntime_converted = pd.to_datetime(df["sntime"], format="%Y-%m-%d %H:%M:%S", errors="coerce")
        duplicate_datetimes = sntime_converted[sntime_converted.duplicated(keep=False)]
        duplicate_dates = duplicate_datetimes.dt.date.unique() if not duplicate_datetimes.empty else []
        self.show_duplicate_dates(duplicate_dates)

        self.dsn = df
        self.set_status("status_selected_sn_folder")
        self.log("log_folder_selected", kind=self.tr("kind_indoor_folder"), path=folder_path)

    def getSNFilePath(self):
        filepath, _ = QtWidgets.QFileDialog.getOpenFileNames(
            self.ui,
            self.tr("dialog_select_sn_file"),
            self.currentPath,
            "(*.xls)",
        )
        if not filepath:
            self.show_warning("warn_select_file")
            return

        self.currentPath = str(Path(filepath[0]).resolve().parent)
        self.dsn = self.getSNFileData(filepath[0])
        self.set_status("status_selected_sn_file")
        self.log("log_file_selected", kind=self.tr("kind_indoor_file"), path=filepath[0])

    def getSWFilePath(self):
        filepath, _ = QtWidgets.QFileDialog.getOpenFileNames(
            self.ui,
            self.tr("dialog_select_sw_file"),
            self.currentPath,
            "(*.xls)",
        )
        if not filepath:
            self.show_warning("warn_select_file")
            return

        self.currentPath = str(Path(filepath[0]).resolve().parent)
        self.dsw = self.getSWFileData(filepath[0])
        self.set_status("status_selected_sw_file")
        self.log("log_file_selected", kind=self.tr("kind_outdoor_file"), path=filepath[0])

    def getSNFileData(self, filepath):
        datasn = pd.read_excel(filepath, sheet_name=None)
        first = True
        dsn = None
        for _, sheet in datasn.items():
            if sheet.shape[0] >= 2:
                if first:
                    dsn = sheet
                    first = False
                else:
                    dsn = pd.concat([dsn, sheet])
        dsn.dropna(axis=0, how="any", inplace=True)
        t = dsn.apply(gettime, axis=1)
        dsn.drop(dsn.columns[:6], axis=1, inplace=True)
        dsn.columns = [chr(i) for i in range(ord("m"), ord("w") + 1)]
        dsn.insert(0, "sntime", t)
        dsn.insert(0, "swtime", t)
        dsn = dsn.set_index(["sntime"]).sort_index().reset_index()
        return dsn

    def getSWFileData(self, filepath):
        datasw = pd.read_excel(filepath, sheet_name=None)
        first = True
        dsw = None
        for _, sheet in datasw.items():
            if sheet.shape[0] >= 2:
                if first:
                    dsw = sheet
                    first = False
                else:
                    dsw = pd.concat([dsw, sheet])
        dsw.dropna(axis=0, how="any", inplace=True)
        t = dsw.apply(gettime, axis=1)
        dsw.drop(dsw.columns[:6], axis=1, inplace=True)
        dsw.drop(dsw.columns[4:], axis=1, inplace=True)
        dsw.columns = list("ijkl")
        dsw.insert(0, "swtime", t)
        return dsw.set_index(["swtime"]).sort_index()

    def write(self):
        if self.dsn is None or self.dsw is None:
            self.show_warning("warn_missing_data")
            return

        fname, _ = QtWidgets.QFileDialog.getSaveFileName(
            self.ui,
            self.tr("dialog_save_file"),
            self.currentPath,
            "xlsx Files (*.xlsx)",
        )
        if not fname:
            return

        self.currentPath = str(Path(fname).resolve().parent)
        df, message = getvalue(
            self.dsn,
            self.dsw,
            self.jiange,
            self.pingjun,
            self.qshangxian,
            self.qxiaxian,
        )
        tubianmessage, jiangemessage, shangmessage, jingqimessage = message[1], message[0], message[2], message[3]
        allmessage = {}
        for item in (tubianmessage, shangmessage, jingqimessage):
            allmessage.update(item)

        with pd.ExcelWriter(fname, engine="xlsxwriter") as writer:
            df.to_excel(writer, index=True, sheet_name="sheet")
            workbook = writer.book
            sheet_table = writer.sheets["sheet"]
            sheet_table.set_column("A:A", 30)
            sheet_table.write(0, 0, "datetime")
            workformat = workbook.add_format({"fg_color": "red"})

            for _, index in allmessage.items():
                data_pos = max(0, min(index - 1, len(df.index) - 1))
                excel_row = data_pos + 1
                sheet_table.write(excel_row, 0, str(df.index[data_pos]), workformat)
                if data_pos > 0:
                    sheet_table.write(excel_row - 1, 0, str(df.index[data_pos - 1]), workformat)
                if data_pos < len(df.index) - 1:
                    sheet_table.write(excel_row + 1, 0, str(df.index[data_pos + 1]), workformat)

        txt_path = fname[:-5] + ".txt"
        with open(txt_path, "w", encoding="utf-8") as file:
            for timestamp in tubianmessage.keys():
                file.write(f"{timestamp}室内氧气含量跃变，请检查是否因为开门导致\n")
            for line in jiangemessage:
                file.write(f"{line}\n")

        self.set_status("status_export_success")
        self.log("log_export_success", path=fname)
        self.show_info("info_export_success", path=fname)

    def show_duplicate_dates(self, dates_list):
        if len(dates_list) == 0:
            return

        dates_str = "\n".join(str(date) for date in dates_list)
        QtWidgets.QMessageBox.warning(
            self.ui,
            self.tr("duplicate_dates_title"),
            self.tr("duplicate_dates_message").format(count=len(dates_list), dates=dates_str),
        )


if __name__ == "__main__":
    if hasattr(QtCore.Qt.ApplicationAttribute, "AA_EnableHighDpiScaling"):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt.ApplicationAttribute, "AA_UseHighDpiPixmaps"):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_UseHighDpiPixmaps, True)

    app = QtWidgets.QApplication(sys.argv)

    font = QtGui.QFont()
    font.setFamilies([
        "Segoe UI",
        "SF Pro Display",
        "Noto Sans SC",
        "Microsoft YaHei",
        "PingFang SC",
    ])
    font.setPointSize(10)
    app.setFont(font)

    window = MainWindowController()
    window.show()
    sys.exit(app.exec())
