# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 464)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_jiange = QLabel(self.centralwidget)
        self.label_jiange.setObjectName(u"label_jiange")

        self.gridLayout.addWidget(self.label_jiange, 1, 1, 1, 1)

        self.pushButton_xiugaipingjun = QPushButton(self.centralwidget)
        self.pushButton_xiugaipingjun.setObjectName(u"pushButton_xiugaipingjun")

        self.gridLayout.addWidget(self.pushButton_xiugaipingjun, 3, 0, 1, 1)

        self.pushButton_selectswall = QPushButton(self.centralwidget)
        self.pushButton_selectswall.setObjectName(u"pushButton_selectswall")

        self.gridLayout.addWidget(self.pushButton_selectswall, 9, 0, 1, 1)

        self.pushButton_selectsw = QPushButton(self.centralwidget)
        self.pushButton_selectsw.setObjectName(u"pushButton_selectsw")

        self.gridLayout.addWidget(self.pushButton_selectsw, 8, 0, 1, 1)

        self.pushButton_xiugai = QPushButton(self.centralwidget)
        self.pushButton_xiugai.setObjectName(u"pushButton_xiugai")

        self.gridLayout.addWidget(self.pushButton_xiugai, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 10, 0, 1, 2)

        self.pushButton_selectsn = QPushButton(self.centralwidget)
        self.pushButton_selectsn.setObjectName(u"pushButton_selectsn")

        self.gridLayout.addWidget(self.pushButton_selectsn, 8, 1, 1, 1)

        self.label_qshangxiaxian = QLabel(self.centralwidget)
        self.label_qshangxiaxian.setObjectName(u"label_qshangxiaxian")

        self.gridLayout.addWidget(self.label_qshangxiaxian, 4, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")

        self.gridLayout.addWidget(self.groupBox, 7, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton_selectsnall = QPushButton(self.centralwidget)
        self.pushButton_selectsnall.setObjectName(u"pushButton_selectsnall")

        self.gridLayout.addWidget(self.pushButton_selectsnall, 9, 1, 1, 1)

        self.pushButton_qshangxian = QPushButton(self.centralwidget)
        self.pushButton_qshangxian.setObjectName(u"pushButton_qshangxian")

        self.gridLayout.addWidget(self.pushButton_qshangxian, 5, 0, 1, 1)

        self.lineEdit_pingjun = QLineEdit(self.centralwidget)
        self.lineEdit_pingjun.setObjectName(u"lineEdit_pingjun")

        self.gridLayout.addWidget(self.lineEdit_pingjun, 2, 1, 1, 1)

        self.label_pingjun = QLabel(self.centralwidget)
        self.label_pingjun.setObjectName(u"label_pingjun")

        self.gridLayout.addWidget(self.label_pingjun, 3, 1, 1, 1)

        self.lineEdit_jiange = QLineEdit(self.centralwidget)
        self.lineEdit_jiange.setObjectName(u"lineEdit_jiange")

        self.gridLayout.addWidget(self.lineEdit_jiange, 0, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_qshangxian = QLineEdit(self.centralwidget)
        self.lineEdit_qshangxian.setObjectName(u"lineEdit_qshangxian")

        self.gridLayout.addWidget(self.lineEdit_qshangxian, 5, 1, 1, 1)

        self.scrollArea_tishi = QScrollArea(self.centralwidget)
        self.scrollArea_tishi.setObjectName(u"scrollArea_tishi")
        self.scrollArea_tishi.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 780, 97))
        self.scrollArea_tishi.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea_tishi, 11, 0, 1, 2)

        self.pushButton_qxiaxian = QPushButton(self.centralwidget)
        self.pushButton_qxiaxian.setObjectName(u"pushButton_qxiaxian")

        self.gridLayout.addWidget(self.pushButton_qxiaxian, 6, 0, 1, 1)

        self.lineEdit_qxiaxian = QLineEdit(self.centralwidget)
        self.lineEdit_qxiaxian.setObjectName(u"lineEdit_qxiaxian")

        self.gridLayout.addWidget(self.lineEdit_qxiaxian, 6, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_jiange.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u65f6\u95f4\u95f4\u969410\u5206\u949f", None))
        self.pushButton_xiugaipingjun.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u4ea7\u70ed\u5e73\u5747\u65f6\u95f4\u95f4\u9694", None))
        self.pushButton_selectswall.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5ba4\u5916\u6570\u636e\u6587\u4ef6\u5939", None))
        self.pushButton_selectsw.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5ba4\u5916\u6570\u636e", None))
        self.pushButton_xiugai.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u65f6\u95f4\u95f4\u9694", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u6570\u636e", None))
        self.pushButton_selectsn.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5ba4\u5185\u6570\u636e", None))
        self.label_qshangxiaxian.setText(QCoreApplication.translate("MainWindow", u"\u547c\u5438\u5546\u5f02\u5e38\u503c\u4e0a\u96501.2\uff0c\u4e0b\u96500.8", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u4ea7\u70ed\u6570\u636e\u7684\u5e73\u5747\u65f6\u95f4\u95f4\u9694\uff0c\u9ed8\u8ba4\u4e3a300\u79d2\uff0c\u4f46\u662f\u5b66\u6821\u5c0f\u5ba4A1\u5e94\u8be5\u8c03\u6574\u4e3a150\u79d2", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.pushButton_selectsnall.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5ba4\u5185\u6570\u636e\u6587\u4ef6\u5939", None))
        self.pushButton_qshangxian.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u4e0a\u9650", None))
        self.label_pingjun.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u65f6\u95f4\u95f4\u9694300s", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5141\u8bb8\u6700\u957f\u7684\u65f6\u95f4\u95f4\u9694\uff0c\u9ed8\u8ba410\u5206\u949f\uff0c\u53ef\u4ee5\u4fee\u6539\uff0c\u8d85\u8fc7\u95f4\u9694\u65f6\u95f4\uff0c\u4e2d\u95f4\u4ea7\u70ed\u4e0d\u8fdb\u884c\u8ba1\u7b97", None))
        self.pushButton_qxiaxian.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u4e0b\u9650", None))
    # retranslateUi

