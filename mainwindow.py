# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 236)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_selectsw = QPushButton(self.centralwidget)
        self.pushButton_selectsw.setObjectName(u"pushButton_selectsw")

        self.gridLayout.addWidget(self.pushButton_selectsw, 2, 0, 1, 1)

        self.lineEdit_jiange = QLineEdit(self.centralwidget)
        self.lineEdit_jiange.setObjectName(u"lineEdit_jiange")

        self.gridLayout.addWidget(self.lineEdit_jiange, 0, 1, 1, 1)

        self.pushButton_selectsn = QPushButton(self.centralwidget)
        self.pushButton_selectsn.setObjectName(u"pushButton_selectsn")

        self.gridLayout.addWidget(self.pushButton_selectsn, 2, 1, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton_xiugai = QPushButton(self.centralwidget)
        self.pushButton_xiugai.setObjectName(u"pushButton_xiugai")

        self.gridLayout.addWidget(self.pushButton_xiugai, 1, 0, 1, 1)

        self.label_jiange = QLabel(self.centralwidget)
        self.label_jiange.setObjectName(u"label_jiange")

        self.gridLayout.addWidget(self.label_jiange, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_selectsw.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5ba4\u5916\u6570\u636e", None))
        self.pushButton_selectsn.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5ba4\u5185\u6570\u636e", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u6570\u636e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5141\u8bb8\u6700\u957f\u7684\u65f6\u95f4\u95f4\u9694\uff0c\u9ed8\u8ba410\u5206\u949f\uff0c\u53ef\u4ee5\u4fee\u6539\uff0c\u8d85\u8fc7\u95f4\u9694\u65f6\u95f4\uff0c\u4e2d\u95f4\u4ea7\u70ed\u4e0d\u8fdb\u884c\u8ba1\u7b97", None))
        self.pushButton_xiugai.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u65f6\u95f4\u95f4\u9694", None))
        self.label_jiange.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u65f6\u95f4\u95f4\u969410\u5206\u949f", None))
    # retranslateUi

