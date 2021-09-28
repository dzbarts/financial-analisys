# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myApp.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from parse import parsing_RBC, parsing_moex, parsing_invest_funds
from Table import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(902, 639)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 901, 611))
        self.tabWidget.setIconSize(QtCore.QSize(50, 20))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.comboBox = QtWidgets.QComboBox(self.tab_1)
        self.comboBox.setGeometry(QtCore.QRect(20, 20, 181, 41))
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.tab_2)
        self.stackedWidget.setGeometry(QtCore.QRect(-10, 0, 901, 581))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.comboBox_NEWS = QtWidgets.QComboBox(self.page_1)
        self.comboBox_NEWS.setGeometry(QtCore.QRect(20, 20, 171, 41))
        self.comboBox_NEWS.setObjectName("comboBox_NEWS")
        self.comboBox_NEWS.addItem("")
        self.comboBox_NEWS.addItem("")
        self.comboBox_NEWS.addItem("")
        self.renew_btn_NEWS = QtWidgets.QPushButton(self.page_1)
        self.renew_btn_NEWS.setGeometry(QtCore.QRect(720, 20, 141, 31))
        self.renew_btn_NEWS.setObjectName("renew_btn_NEWS")
        self.NEWS_label = QtWidgets.QLabel(self.page_1)
        self.NEWS_label.setGeometry(QtCore.QRect(20, 70, 271, 41))
        self.NEWS_label.setObjectName("NEWS_label")
        self.news_NEWS = QtWidgets.QTextBrowser(self.page_1)
        self.news_NEWS.setGeometry(QtCore.QRect(20, 110, 881, 461))
        self.news_NEWS.setObjectName("news_NEWS")
        self.stackedWidget.addWidget(self.page_1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.table = QtWidgets.QTableView(self.tab_3)
        self.table.setGeometry(QtCore.QRect(20, 110, 881, 461))
        self.table.setObjectName("table_data")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_4.setGeometry(QtCore.QRect(20, 20, 181, 41))
        self.comboBox_4.setEditable(True)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.comboBox_5 = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_5.setGeometry(QtCore.QRect(20, 20, 181, 41))
        self.comboBox_5.setEditable(True)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.comboBox_6 = QtWidgets.QComboBox(self.tab_6)
        self.comboBox_6.setGeometry(QtCore.QRect(20, 20, 181, 41))
        self.comboBox_6.setEditable(True)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.comboBox_7 = QtWidgets.QComboBox(self.tab_7)
        self.comboBox_7.setGeometry(QtCore.QRect(20, 20, 181, 41))
        self.comboBox_7.setEditable(True)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.tabWidget.addTab(self.tab_7, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 902, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.news_NEWS.setText(parsing_RBC())
        self.renew_btn_NEWS.clicked.connect(self.path_to_the_page)
        self.news_NEWS.setOpenExternalLinks(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "New Item 1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "New Item 2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "New Item 3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Page 1"))
        self.comboBox_NEWS.setItemText(0, _translate("MainWindow", "RBC"))
        self.comboBox_NEWS.setItemText(1, _translate("MainWindow", "Invest Funds: Today News"))
        self.comboBox_NEWS.setItemText(2, _translate("MainWindow", "MOEX"))
        self.renew_btn_NEWS.setText(_translate("MainWindow", "RENEW"))
        self.NEWS_label.setText(_translate("MainWindow", "RBC"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Page 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page 3"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "New Item 1"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "New Item 2"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "New Item 3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Page 4"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "New Item 1"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "New Item 2"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "New Item 3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Page 5"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "New Item 1"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "New Item 2"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "New Item 3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Page 6"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "New Item 1"))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "New Item 2"))
        self.comboBox_7.setItemText(2, _translate("MainWindow", "New Item 3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Page 7"))

    def path_to_the_page(self):
        if self.comboBox_NEWS.currentText() == 'RBC':
            self.NEWS_label.setText('RBS')
            self.news_NEWS.setText(parsing_RBC())
        elif self.comboBox_NEWS.currentText() == 'Invest Funds: Today News':
            self.NEWS_label.setText('Invest Funds: Today News')
            self.news_NEWS.setText(parsing_invest_funds())
            if len(parsing_invest_funds()) == 0:
                self.news_NEWS.setText("News can't be founded today. Go to sleep and wait for it!")
        elif self.comboBox_NEWS.currentText() == 'MOEX':
            self.NEWS_label.setText('MOEX')
            self.news_NEWS.setText(parsing_moex())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
