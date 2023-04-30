import sys
import os
import time
from datetime import timedelta,datetime

import numpy as np
import pandas as pd
from PySide6.QtWidgets import QApplication,QFileDialog,QMainWindow,QMessageBox
class ValueDict(dict):
    def __getattr__(self,attr):
        return self[attr]
    def __setattr__(self,attr,value):
        self[attr]=value
from mainwindow import Ui_MainWindow
def getvalue(dsn,dsw,jiange):
    jiangemessage=[]
    tubianmessage={}
    delta = timedelta(minutes=-1*(jiange))
    head = True
    answer = []
    vd = ValueDict()
    columns = [chr(index) for index in range(ord("h"), ord("z") + 1)]
    columns.extend(["a" + chr(index) for index in range(ord("a"), ord("h") + 1)])
    df = pd.DataFrame(columns=columns)
    i = -1
    for row in dsn.iterrows():
        rowindex = row[0]
        row = row[1]
        sntime = row["sntime"]
        qreuslt = dsw[str(sntime + delta):str(sntime)]
        try:
            if (not qreuslt.empty):
                i += 1
                swrow = qreuslt.iloc[-1]
                vd.i, vd.j, vd.k, vd.l = swrow.values
                for index in range(ord("m"), ord("w") + 1):
                    index = chr(index)
                    vd[index] = row[index]
                if (not head):
                    if ((vd.m - vd.lastm) > 0.1 or (vd.lastm - vd.m) > 0.1):
                        tubianmessage[sntime] = i
                    vd.h = sntime - lasttime
                    vd.h = vd.h.total_seconds()
                    vd.x = vd.r / 100 * (3.999 + 0.45547 * vd.q + 0.001708 * (vd.q ** 2) + 0.000469 * (vd.q ** 3))
                    vd.y = (vd.s + vd.t) * vd.h / 60
                    vd.z = 7800
                    vd.aa = vd.y * (vd.v - vd.x) / 1013 * 273 / (273 + vd.q)
                    vd.ab = vd.z * (vd.v - vd.x) / 1013 * 273 / (273 + vd.q)
                    vd.ac = (vd.lastm - vd.m) * 0.01 * vd.ab + (vd.lasti - vd.lastm) * vd.aa * 0.01
                    vd.ad = (vd.n - vd.lastn) * 0.000001 * vd.ab + (vd.lastn - vd.lastj) * vd.aa * 0.000001
                    vd.ae = (vd.o - vd.lasto) * 0.000001 * vd.ab + (vd.lasto - vd.lastk) * vd.aa * 0.000001
                    vd.af = (vd.p - vd.lastp) * 0.000001 * vd.ab + (vd.lastp - vd.lastl) * vd.aa * 0.000001
                    if (vd.ac == 0):
                        print(rowindex)
                    vd.ag = vd.af / vd.ac
                    vd.ah = (3.866 * vd.ac + 1.2 * vd.af - 0.518 * vd.ae) / vd.h * 300
                    answer.append(vd.ah)
                    for index in range(ord("i"), ord("w") + 1):
                        index = chr(index)
                        vd["last" + index] = vd[index]
                        lasttime = sntime
                    data = []
                    for index in range(ord("h"), ord("z") + 1):
                        index = chr(index)
                        data.append(vd[index])
                    for index in range(ord("a"), ord("h") + 1):
                        index = chr(index)
                        index = "a" + index
                        data.append(vd[index])
                    df.loc[sntime] = data
                else:
                    head = False
                    for index in range(ord("i"), ord("w") + 1):
                        index = chr(index)
                        vd["last" + index] = vd[index]
                        lasttime = sntime
            else:
                jiangemessage.append(f"{sntime}前{jiange}分钟内无对应室外数据，因此未计算该时间段的产热，如需调整，请增加时间间隔")
                head = True
            namecolumns = "时间差,O2浓度（%）,NH3浓度（ppm）,CH4浓度（ppm）,CO2浓度（ppm）,O2浓度（%）,NH3浓度（ppm）,CH4浓度（ppm）," \
                          "CO2浓度（ppm）,小室温度（℃）,小室湿度（%）,排气流量（L/M）,仪表流量（L/M）,进气压力（Hpa）,小室压力（Hpa）,小室风速（m/s）,水蒸气压,流量L/M,呼吸室体积L," \
                          "标准状况流量L/M,呼吸室标准容积L,氧含量L,氨气含量L,甲烷含量L,二氧化碳含量L,呼吸熵,HP产热 (kcal)".split(",")
            df.columns = namecolumns
        except Exception as e:
            print(e)
            print(sntime)
        message = (jiangemessage, tubianmessage)
    return df,message
def gettime(x):
    d=x.values
    d=d[:6]
    dd=np.append([int(i) for i in d ],[0,0,0])
    a=tuple(dd)
    return datetime.fromtimestamp(time.mktime(a))
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.pushButton_selectsn.clicked.connect(self.getsnfilepath)
        self.pushButton_selectsw.clicked.connect(self.getswfilepath)
        self.pushButton.clicked.connect(self.write)
        self.pushButton_xiugai.clicked.connect(self.xiugaijiange)
        self.jiange=30
    def xiugaijiange(self):
        jiange=self.lineEdit_jiange.text()
        try:
            jiange=int(jiange)
            self.jiange=jiange
            self.label_jiange.setText(f"当前时间间隔{jiange}分钟")
        except:
            QMessageBox.information(self, "警告", "请输入整数")
    def getsnfilepath(self):

        filepath, _ = QFileDialog.getOpenFileNames(self, "打开室内数据文件",
                                                        os.getcwd(), "(*.xls)")
        if (not filepath):
            QMessageBox.information(self, "警告", "请选择文件")
            return
        datasn = pd.read_excel(filepath[0], sheet_name=None)
        first = True
        dsn = None
        for i in datasn:
            shape = datasn[i].shape
            if (shape[0] >= 2):
                if (first):
                    dsn = datasn[i]
                    first = False
                else:
                    data = datasn[i]
                    dsn = pd.concat([dsn, data])
        t = dsn.apply(gettime, axis=1)
        dsn.drop(dsn.columns[:6], axis=1, inplace=True)
        # dsn.columns=["sno","snn","snch","snco","snwd","snsd","paiqi","yibiao","jinqiya","snya","snfs"]
        dsn.columns = [chr(i) for i in range(ord("m"), ord("w") + 1)]
        dsn.insert(0, "sntime", t)
        dsn.insert(0, "swtime", t)
        dsn = dsn.set_index(["sntime"])
        dsn = dsn.sort_index()
        dsn.reset_index(inplace=True)
        # dsn.drop(dsw.columns[4:],axis=1,inplace=True)
        self.dsn=dsn
    def getswfilepath(self):
        filepath, _ = QFileDialog.getOpenFileNames(self, "打开室外数据文件",
                                                        os.getcwd(), "(*.xls)")
        if(not filepath):
            QMessageBox.information(self, "警告", "请选择文件")
            return
        datasw = pd.read_excel(filepath[0], sheet_name=None)
        first = True
        dsw = None
        for i in datasw:
            shape = datasw[i].shape
            if (shape[0] >= 2):
                if (first):
                    dsw = datasw[i]
                    first = False
                else:
                    data = datasw[i]
                    dsw = pd.concat([dsw, data])
        t = dsw.apply(gettime, axis=1)
        dsw.drop(dsw.columns[:6], axis=1, inplace=True)
        dsw.drop(dsw.columns[4:], axis=1, inplace=True)
        # dsw.columns=["swo","swn","swch","swco"]
        dsw.columns = [i for i in "ijkl"]
        dsw.insert(0, "swtime", t)
        dsw = dsw.set_index(["swtime"])
        dsw = dsw.sort_index()
        self.dsw=dsw
    def write(self):
        fname = QFileDialog.getSaveFileName(self, "文件保存", os.getcwd(), "xlsx Files (*.xlsx)")  # 写入文件首先获取文件路径
        df,message=getvalue(self.dsn,self.dsw,self.jiange)
        tubianmessage=message[1]
        jiangemessage=message[0]
        if fname[0]:  # 如果获取的路径非空
            name=fname[0]
            #df.to_excel(name, index=True)
            writer = pd.ExcelWriter(name, engine='xlsxwriter')
            df.to_excel(writer, index=True, sheet_name='sheet')
            workbook = writer.book
            sheet_table = writer.sheets['sheet']
            sheet_table.set_column('A:A', 30)
            sheet_table.write(0,0,"datetime")
            workfomat = workbook.add_format({
                'fg_color': 'red',  # 单元格背景颜色
            })

            for i in tubianmessage.keys():
                sheet_table.write(tubianmessage[i], 0, str(i), workfomat)
            workbook.close()
            writer.close()
            mname=name[:-5]+".txt"
            with open(mname,"w") as f:
                for i in tubianmessage.keys():
                    f.write(f"{i}室内氧气含量骤变，请检查是否因为开门导致\n")
                for i in jiangemessage:
                    f.write(f"{i}\n")
        else:
            QMessageBox.information(self, "警告", "请输入保存文件路径")
if __name__=="__main__":
    app=QApplication(sys.argv)
    mw=MainWindow()
    mw.show()
    sys.exit(app.exec())
