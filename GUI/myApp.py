# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myApp.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import yfinance as yf
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget, QHeaderView, QMessageBox
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
import qdarkstyle

from parse import parsing_RBC, parsing_moex, parsing_invest_funds
from Portfolio import set_port_and_portfolio
from Sectors_and_countries import tsectors, set_t_port_sect, plot_s, tcapa, plot_c
from Recommendations import set_recom
from Stock import plot_stock, get_stock_quarterly_earnings, get_stock, get_stock_quarterly_balance_sheet, \
    get_stock_quarterly_cashflow, get_stock_isin
from PortfolioTab import set_assets, plot_p, set_stock_growth, plot_common
from canvas import GraphicsCanvas
from pandasmodel import PandasModel


def main():  # ф-ция рассчета размера окна
    sizeObject = QDesktopWidget().screenGeometry(-1)  # -1 означает, что мы берем на измерение текущий экран
    heignt = sizeObject.height()
    width = sizeObject.width()
    return [int(heignt), int(width)]


def read_port():  # ф-ция читки портфеля
    l = []
    with open('proj.txt', 'r') as txt:
        while 1:
            s = txt.readline().replace('\n', '')
            if not s:
                break
            l.append(s)
    return l


def rewrite_port(str):  # ф-ция переписывания (добавления эл-та в портфель)
    with open('proj.txt', 'a') as txt:
        txt.write(str + '\n')


def remove_from_port(str):  # ф-ция удаления эл-та из портфеля
    with open("proj.txt", "r") as f:
        lines = f.readlines()
    with open("proj.txt", "w") as f:
        if str + '\n' in lines:
            lines.remove(str + '\n')
        for line in lines:
            f.write(line)


def clear_all():  # ф-ция очистки портфеля
    with open('proj.txt', 'w'):
        pass


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.uni_var = set_port_and_portfolio(read_port())
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(main()[1], main()[0])

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, main()[1], main()[0]))
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
        self.comboBox_NEWS = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_NEWS.setGeometry(QtCore.QRect(20, 20, 171, 41))
        self.comboBox_NEWS.setObjectName("comboBox_NEWS")
        self.comboBox_NEWS.addItem("")
        self.comboBox_NEWS.addItem("")
        self.comboBox_NEWS.addItem("")
        self.comboBox_NEWS.activated['QString'].connect(self.path_to_the_page)
        self.NEWS_label = QtWidgets.QLabel(self.tab_2)
        self.NEWS_label.setGeometry(QtCore.QRect(20, 70, 271, 41))
        self.NEWS_label.setObjectName("NEWS_label")
        self.news_NEWS = QtWidgets.QTextBrowser(self.tab_2)
        self.news_NEWS.setGeometry(QtCore.QRect(20, 110, main()[1] - 50, main()[0] - 350))
        self.news_NEWS.setObjectName("news_NEWS")
        self.tabWidget.addTab(self.tab_2, "")

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.view = QtWidgets.QTableView(self.tab_3)
        self.view.setGeometry(QtCore.QRect(50, 50, 1200, 328))
        self.view.setObjectName("table_data_1")
        self.model = PandasModel(tsectors, headers_column=['Trough', 'Expansion', 'Peak', 'Recession'],
                                 headers_row=['1', '2', '3', '4', '5', '6', '',
                                              'Recommendations'])  # создаепм модель готового класса
        self.view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.view.setModel(self.model)  # добавляем модель в поле показа таблицы

        self.view_2 = QtWidgets.QTableView(self.tab_3)
        self.view_2.setGeometry(QtCore.QRect(50, 400, 700, 439))
        self.view_2.setObjectName("table_data_2")
        self.model_2 = PandasModel(tcapa, headers_column=['Country', 'Calculated Using', 'Index'],
                                   headers_row=[str(i) for i in range(1, tcapa.shape[0] + 1)])
        self.view_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.view_2.setModel(self.model_2)

        self.view_3 = QtWidgets.QTableView(self.tab_3)
        self.view_3.setGeometry(QtCore.QRect(770, 400, 480, 254))
        self.view_3.setObjectName("table_data_3")
        self.model_3 = PandasModel(set_t_port_sect(self.uni_var), headers_column=['Stocks', 'Number', 'Countries', 'Sectors'],
                                   headers_row=[str(i) for i in range(1, set_t_port_sect(self.uni_var).shape[0] + 1)])
        self.view_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.view_3.setModel(self.model_3)

        self.widget_for_g_1 = QtWidgets.QWidget(self.tab_3)  # создаем виджет для добавления графика
        self.widget_for_g_1.setGeometry(1250, 0, 500, 480)

        self.widget_for_g_2 = QtWidgets.QWidget(self.tab_3)
        self.widget_for_g_2.setGeometry(1250, 480, 600, 480)

        self.fig_1 = plot_c(uni_var)  # график
        self.fig_2 = plot_s(uni_var)
        self.layout_for_mpl_1 = QtWidgets.QVBoxLayout(self.widget_for_g_1)  # виджет для компоновки объектов
        self.layout_for_mpl_2 = QtWidgets.QVBoxLayout(self.widget_for_g_2)
        self.canvas_1 = GraphicsCanvas(self.fig_1)  # создаем холст для прорисовки графика
        self.canvas_2 = GraphicsCanvas(self.fig_2)
        self.layout_for_mpl_1.addWidget(self.canvas_1)  # добавляем холст в лэйаут
        self.layout_for_mpl_2.addWidget(self.canvas_2)
        self.toolbar_1 = NavigationToolbar(self.canvas_1,
                                           MainWindow)  # создаем панель управления, берем ее с графика mpl
        self.toolbar_2 = NavigationToolbar(self.canvas_2, MainWindow)
        self.layout_for_mpl_1.addWidget(self.toolbar_1)  # добавляем панель управления в лэйаут
        self.layout_for_mpl_2.addWidget(self.toolbar_2)
        self.tabWidget.addTab(self.tab_3, "")

        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.edit = QtWidgets.QTextEdit(self.tab_4)
        self.edit.setGeometry(QtCore.QRect(20, 40, 200, 50))
        self.edit.setObjectName("editable_stock")
        self.edit_n = QtWidgets.QTextEdit(self.tab_4)
        self.edit_n.setGeometry(QtCore.QRect(20, 120, 200, 50))
        self.edit_n.setObjectName("editable_number")
        self.add_btn = QtWidgets.QPushButton(self.tab_4)
        self.add_btn.setGeometry(QtCore.QRect(720, 20, 230, 50))
        self.add_btn.setObjectName("add_btn")
        self.add_btn.setText("Add stock into the portfolio")
        self.remove_btn = QtWidgets.QPushButton(self.tab_4)
        self.remove_btn.setGeometry(QtCore.QRect(1000, 20, 300, 50))
        self.remove_btn.setObjectName("remove_btn")
        self.remove_btn.setText("Remove the stock from the portfolio")
        self.clear_all_btn = QtWidgets.QPushButton(self.tab_4)
        self.clear_all_btn.setGeometry(QtCore.QRect(1500, 20, 200, 50))
        self.clear_all_btn.setObjectName("clear_btn")
        self.clear_all_btn.setText("Clear the portfolio")
        self.renew_assets = QtWidgets.QPushButton(self.tab_4)
        self.renew_assets.setGeometry(QtCore.QRect(1500, 80, 200, 50))
        self.renew_assets.setObjectName("renew_assets ")
        self.renew_assets.setText("Renew table")

        self.view_5 = QtWidgets.QTableView(self.tab_4)
        self.view_5.setGeometry(QtCore.QRect(30, 200, 1847, 254))
        self.view_5.setObjectName("table_data_5")
        self.model_5 = PandasModel(set_assets(self.uni_var), headers_column=['Stocks', 'Number', 'Open', 'High', 'Low', 'Close',
                                                           'Volume', 'Div. (per year)',
                                                           '% of Shares Held by All Insider',
                                                           '% of Shares Held by Inst.',
                                                           '% of Float Held by Inst.',
                                                           'Number of Inst. Hold. Shares'],
                                   headers_row=[str(i) for i in range(1, set_assets(self.uni_var).shape[0] + 1)])
        self.view_5.setModel(self.model_5)
        for i in range(int(set_assets(self.uni_var).shape[1]/2) + 1):  # изменения размера колонок
            self.view_5.setColumnWidth(i, 100)
        for i in range(int(set_assets(self.uni_var).shape[1]/2) + 2, set_assets(self.uni_var).shape[1] + 1):
            self.view_5.setColumnWidth(i, 250)

        self.view_6 = QtWidgets.QTableView(self.tab_4)
        self.view_6.setGeometry(QtCore.QRect(30, 500, 500, 254))
        self.view_6.setObjectName("table_data_6")
        self.model_6 = PandasModel(set_stock_growth(self.uni_var), headers_column=['Stocks', 'Stock growth %', 'Stock growth, RUB'],
                                   headers_row=[str(i) for i in range(1, set_stock_growth(self.uni_var).shape[0] + 1)])
        self.view_6.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.view_6.setModel(self.model_6)

        self.widget_for_g_p = QtWidgets.QWidget(self.tab_4)
        self.widget_for_g_p.setGeometry(550, 480, 500, 480)

        self.widget_for_g_c = QtWidgets.QWidget(self.tab_4)
        self.widget_for_g_c.setGeometry(1100, 480, 800, 480)

        self.fig_p = plot_p(uni_var)
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_4.setGeometry(QtCore.QRect(1292, 500, 100, 31))
        self.comboBox_4.setObjectName("set_period")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.activated['QString'].connect(self.set_period)

        self.fig_c = plot_common(40, uni_var)
        self.layout_for_mpl_p = QtWidgets.QVBoxLayout(self.widget_for_g_p)
        self.layout_for_mpl_c = QtWidgets.QVBoxLayout(self.widget_for_g_c)
        self.canvas_p = GraphicsCanvas(self.fig_p)
        self.canvas_c = GraphicsCanvas(self.fig_c)
        self.layout_for_mpl_p.addWidget(self.canvas_p)
        self.layout_for_mpl_c.addWidget(self.canvas_c)
        self.toolbar_p = NavigationToolbar(self.canvas_p, MainWindow)
        self.toolbar_c = NavigationToolbar(self.canvas_c, MainWindow)
        self.layout_for_mpl_p.addWidget(self.toolbar_p)
        self.layout_for_mpl_c.addWidget(self.toolbar_c)
        self.tabWidget.addTab(self.tab_4, "")

        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.comboBox_5 = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_5.setGeometry(QtCore.QRect(30, 20, 200, 50))
        self.comboBox_5.setObjectName("set_strategy")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.activated['QString'].connect(self.set_strategy)

        self.view_7 = QtWidgets.QTableView(self.tab_5)
        self.view_7.setGeometry(QtCore.QRect(30, 150, 1300, 254))
        self.view_7.setObjectName("table_data_7")
        self.columns_ = ['Stocks', 'SMA', 'twoSMA', 'EMA', 'DEMA', 'TEMA', 'MACD',
                         'CHV', 'RSI', 'bulls', 'bears', 'ER', 'MI', 'Agg']
        self.rows_ = [str(i) for i in range(1, set_recom(1, self.uni_var).shape[0] + 1)]
        self.model_7 = PandasModel(set_recom(1, self.uni_var), headers_column=self.columns_,
                                   headers_row=self.rows_)
        self.view_7.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.view_7.setModel(self.model_7)
        self.tabWidget.addTab(self.tab_5, "")

        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.write_stock = QtWidgets.QTextEdit(self.tab_6)
        self.write_stock.setGeometry(QtCore.QRect(20, 20, 200, 50))
        self.write_stock.setObjectName("write_stock")
        self.comboBox_6 = QtWidgets.QComboBox(self.tab_6)
        self.comboBox_6.setGeometry(QtCore.QRect(20, 100, 200, 50))
        self.comboBox_6.setObjectName("set_period_for_stock")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.activated['QString'].connect(self.set_period_current_stock)
        self.isin = QtWidgets.QLabel(self.tab_6)
        self.isin.setGeometry(QtCore.QRect(300, 100, 200, 50))
        self.isin.setText(get_stock_isin(get_stock('msft')))
        self.widget_for_stock_p = QtWidgets.QWidget(self.tab_6)
        self.widget_for_stock_p.setGeometry(20, 150, 600, 450)
        self.fig = plot_stock('MSFT', 150)
        self.layout_for_mpl_stock = QtWidgets.QVBoxLayout(self.widget_for_stock_p)
        self.canvas_stock = GraphicsCanvas(self.fig)
        self.layout_for_mpl_stock.addWidget(self.canvas_stock)
        self.toolbar_stock = NavigationToolbar(self.canvas_stock, MainWindow)
        self.layout_for_mpl_stock.addWidget(self.toolbar_stock)

        self.view_8 = QtWidgets.QTableView(self.tab_6)
        self.view_8.setGeometry(QtCore.QRect(20, 650, 500, 180))
        self.view_8.setObjectName("table_data_8")
        self.rows_ = [str(i) for i in range(1, get_stock_quarterly_earnings(get_stock('msft')).shape[0] + 1)]
        self.model_8 = PandasModel(get_stock_quarterly_earnings(get_stock('msft')),
                                   headers_column=['Quarter', 'Revenue', 'Earnings'],
                                   headers_row=self.rows_)
        self.view_8.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.view_8.setModel(self.model_8)

        self.view_9 = QtWidgets.QTableView(self.tab_6)
        self.view_9.setGeometry(QtCore.QRect(700, 100, 900, 800))
        self.view_9.setObjectName("table_data_9")
        self.rows_ = [str(i) for i in range(1, get_stock_quarterly_cashflow(get_stock('msft')).shape[0] + 1)]
        self.model_9 = PandasModel(get_stock_quarterly_cashflow(get_stock('msft')),
                                   headers_column=get_stock_quarterly_cashflow(get_stock('msft')).columns.tolist(),
                                   headers_row=self.rows_)
        self.view_9.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.view_9.setModel(self.model_9)
        self.tabWidget.addTab(self.tab_6, "")

        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget.addTab(self.tab_7, "")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.news_NEWS.setText(parsing_RBC())
        self.news_NEWS.setOpenExternalLinks(True)  # опция для перенаправления при нажатии на ссылку
        self.add_btn.clicked.connect(self.add_to_the_portfolio)  # добавляем обработчик событий:
        # при нажатии на кнопку происходит действие переданной ф-ции
        self.remove_btn.clicked.connect(self.remove_the_stock)
        self.clear_all_btn.clicked.connect(clear_all)

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
        self.NEWS_label.setText(_translate("MainWindow", "RBC"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Page 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page 3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Page 4"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "20"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "150"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "360"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Long-term strategy"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "Medium strategy"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "Quick strategy"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "20"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "150"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "360"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Page 5"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Page 6"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Page 7"))

    def path_to_the_page(self, text):
        if text == 'RBC':
            self.NEWS_label.setText('RBS')
            self.news_NEWS.setText(parsing_RBC())
        elif text == 'Invest Funds: Today News':
            self.NEWS_label.setText('Invest Funds: Today News')
            self.news_NEWS.setText(parsing_invest_funds())
            if len(parsing_invest_funds()) == 0:
                self.news_NEWS.setText("News can't be founded today. Go to sleep and wait for it!")
        elif text == 'MOEX':
            self.NEWS_label.setText('MOEX')
            self.news_NEWS.setText(parsing_moex())

    def set_period(self, period):
        if period != '':
            self.layout_for_mpl_c.removeWidget(self.canvas_c)  # удаление старых данных с виджета
            self.layout_for_mpl_c.removeWidget(self.toolbar_c)
            self.toolbar_c.deleteLater()
            self.canvas_c.deleteLater()
            self.canvas_c.hide()
            self.toolbar_c.hide()
            if period == '20':  # добавление новых данных в зависимости от текста внутри combobox
                self.fig_c = plot_common(20, set_port_and_portfolio(read_port()))
            elif period == '150':
                self.fig_c = plot_common(150, set_port_and_portfolio(read_port()))
            elif period == '360':
                self.fig_c = plot_common(360, set_port_and_portfolio(read_port()))
            self.canvas_c = GraphicsCanvas(self.fig_c)
            self.layout_for_mpl_c.addWidget(self.canvas_c)
            self.toolbar_c = NavigationToolbar(self.canvas_c, MainWindow)
            self.layout_for_mpl_c.addWidget(self.toolbar_c)

    def set_period_current_stock(self, period):
        if self.write_stock.toPlainText() != '':
            if len(yf.Ticker(self.write_stock.toPlainText()).info) != 2:
                self.layout_for_mpl_stock.removeWidget(self.canvas_stock)
                self.layout_for_mpl_stock.removeWidget(self.toolbar_stock)
                self.toolbar_stock.deleteLater()
                self.canvas_stock.deleteLater()
                self.canvas_stock.hide()
                self.toolbar_stock.hide()
                if period == '20':
                    self.fig = plot_stock(self.write_stock.toPlainText().upper(), 20)
                elif period == '150':
                    self.fig = plot_stock(self.write_stock.toPlainText().upper(), 150)
                elif period == '360':
                    self.fig = plot_stock(self.write_stock.toPlainText().upper(), 360)
                self.canvas_stock = GraphicsCanvas(self.fig)
                self.layout_for_mpl_stock.addWidget(self.canvas_stock)
                self.toolbar_stock = NavigationToolbar(self.canvas_stock, MainWindow)
                self.layout_for_mpl_stock.addWidget(self.toolbar_stock)
            else:
                error = QMessageBox()
                error.setWindowTitle("Ошибка набора")
                error.setText("Такой акции не существует")
                error.setIcon(QMessageBox.Warning)
                error.exec_()
        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка набора")
            error.setText("Пустой текст")
            error.setIcon(QMessageBox.Warning)
            error.exec_()

    def set_strategy(self, strategy):
        if strategy == 'Long-term strategy':
            self.model = PandasModel(set_recom(1, self.uni_var),
                                       headers_column=self.columns_,
                                       headers_row=self.rows_)
        if strategy == 'Medium strategy':
            self.model = PandasModel(set_recom(2, self.uni_var),
                                     headers_column=self.columns_,
                                     headers_row=self.rows_)
        if strategy == 'Quick strategy':
            self.model = PandasModel(set_recom(3, self.uni_var),
                                     headers_column=self.columns_,
                                     headers_row=self.rows_)
        self.view_7.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.view_7.setModel(self.model)



    def add_to_the_portfolio(self):
        if (self.edit.toPlainText() == '') | (self.edit_n.toPlainText() == ''):
            error = QMessageBox()
            error.setWindowTitle("Ошибка набора")
            error.setText("Пустой текст")
            error.setIcon(QMessageBox.Warning)
            error.exec_()
        else:
            try:
                n = int(self.edit_n.toPlainText())
                stock = self.edit.toPlainText().upper()
                if len(yf.Ticker(self.edit.toPlainText()).info) != 2:
                    while n > 0:
                        rewrite_port(stock)
                        n = n - 1
                else:
                    error = QMessageBox()
                    error.setWindowTitle("Ошибка набора")
                    error.setText("Такой акции не существует")
                    error.setIcon(QMessageBox.Warning)
                    error.exec_()
            except ValueError:
                error = QMessageBox()
                error.setWindowTitle("Ошибка набора")
                error.setText("Неверный формат текста")
                error.setIcon(QMessageBox.Warning)
                error.exec_()
        self.edit.clear()
        self.edit_n.clear()

    def remove_the_stock(self):
        if (self.edit.toPlainText() == '') | (self.edit_n.toPlainText() == ''):
            error = QMessageBox()
            error.setWindowTitle("Ошибка набора")
            error.setText("Пустой текст")
            error.setIcon(QMessageBox.Warning)
            error.exec_()
        else:
            try:
                n = int(self.edit_n.toPlainText())
                stock = self.edit.toPlainText().upper()
                if read_port().count(stock) >= n:
                    while n > 0:
                        remove_from_port(stock)
                        n = n - 1
                else:
                    error = QMessageBox()
                    error.setWindowTitle("Ошибка набора")
                    error.setText("У Вас осталось " + str(read_port().count(stock)) + " акций")
                    error.setIcon(QMessageBox.Warning)
                    error.exec_()
            except ValueError:
                error = QMessageBox()
                error.setWindowTitle("Ошибка набора")
                error.setText("Неверный формат текста")
                error.setIcon(QMessageBox.Warning)
                error.exec_()
            self.edit.clear()
            self.edit_n.clear()


if __name__ == "__main__":
    import sys
    uni_var = set_port_and_portfolio(read_port())
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())  # изменение темы приложения
    MainWindow.show()
    sys.exit(app.exec_())
