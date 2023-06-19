# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sotrudniki.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setSizeIncrement(QtCore.QSize(800, 600))
        MainWindow.setBaseSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("background-color: rgb(245, 245, 220);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Add = QtWidgets.QPushButton(self.centralwidget)
        self.Add.setGeometry(QtCore.QRect(30, 40, 101, 31))
        self.Add.setStyleSheet("background-color: rgb(169, 169, 169);\n"
"border-radius: 5px;")
        self.Add.setObjectName("Add")
        self.Change = QtWidgets.QPushButton(self.centralwidget)
        self.Change.setGeometry(QtCore.QRect(30, 80, 101, 31))
        self.Change.setStyleSheet("background-color: rgb(169, 169, 169);\n"
"border-radius: 5px;")
        self.Change.setObjectName("Change")
        self.Dell = QtWidgets.QPushButton(self.centralwidget)
        self.Dell.setGeometry(QtCore.QRect(30, 120, 101, 31))
        self.Dell.setStyleSheet("background-color: rgb(169, 169, 169);\n"
"border-radius: 5px;")
        self.Dell.setObjectName("Dell")
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(700, 0, 101, 31))
        self.Back.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(169, 169, 169);")
        self.Back.setObjectName("Back")
        self.Open = QtWidgets.QPushButton(self.centralwidget)
        self.Open.setGeometry(QtCore.QRect(30, 160, 101, 31))
        self.Open.setStyleSheet("background-color: rgb(169, 169, 169);\n"
"border-radius: 5px;")
        self.Open.setObjectName("Open")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(35, 221, 731, 351))
        self.tableWidget.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(169, 169, 169);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.DellLine = QtWidgets.QLineEdit(self.centralwidget)
        self.DellLine.setGeometry(QtCore.QRect(140, 120, 71, 31))
        self.DellLine.setStyleSheet("background-color: rgb(169, 169, 169);\n"
"border-radius: 5px;")
        self.DellLine.setObjectName("DellLine")
        self.AddLine = QtWidgets.QLineEdit(self.centralwidget)
        self.AddLine.setGeometry(QtCore.QRect(140, 40, 71, 31))
        self.AddLine.setStyleSheet("background-color: rgb(169, 169, 169);\n"
"border-radius: 5px;")
        self.AddLine.setObjectName("AddLine")
        self.AddLine_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.AddLine_2.setGeometry(QtCore.QRect(220, 40, 71, 31))
        self.AddLine_2.setStyleSheet("background-color: rgb(169, 169, 169);\n"
"border-radius: 5px;")
        self.AddLine_2.setObjectName("AddLine_2")
        self.AddLine_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.AddLine_3.setGeometry(QtCore.QRect(300, 40, 71, 31))
        self.AddLine_3.setStyleSheet("background-color: rgb(169, 169, 169);\n"
"border-radius: 5px;")
        self.AddLine_3.setObjectName("AddLine_3")
        self.AddLine_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.AddLine_4.setGeometry(QtCore.QRect(380, 40, 71, 31))
        self.AddLine_4.setStyleSheet("background-color: rgb(169, 169, 169);\n"
"border-radius: 5px;")
        self.AddLine_4.setObjectName("AddLine_4")
        self.AddLine_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.AddLine_5.setGeometry(QtCore.QRect(460, 40, 71, 31))
        self.AddLine_5.setStyleSheet("background-color: rgb(169, 169, 169);\n"
"border-radius: 5px;")
        self.AddLine_5.setObjectName("AddLine_5")
        self.AddLine_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.AddLine_6.setGeometry(QtCore.QRect(540, 40, 71, 31))
        self.AddLine_6.setStyleSheet("background-color: rgb(169, 169, 169);\n"
"border-radius: 5px;")
        self.AddLine_6.setObjectName("AddLine_6")
        self.AddLine_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.AddLine_7.setGeometry(QtCore.QRect(620, 40, 71, 31))
        self.AddLine_7.setStyleSheet("background-color: rgb(169, 169, 169);\n"
"border-radius: 5px;")
        self.AddLine_7.setObjectName("AddLine_7")
        self.ChangeLine = QtWidgets.QLineEdit(self.centralwidget)
        self.ChangeLine.setGeometry(QtCore.QRect(140, 80, 71, 31))
        self.ChangeLine.setStyleSheet("background-color: rgb(169, 169, 169);\n"
"border-radius: 5px;")
        self.ChangeLine.setObjectName("ChangeLine")
        self.ChangeLine_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.ChangeLine_2.setGeometry(QtCore.QRect(220, 80, 71, 31))
        self.ChangeLine_2.setStyleSheet("background-color: rgb(169, 169, 169);\n"
"border-radius: 5px;")
        self.ChangeLine_2.setObjectName("ChangeLine_2")
        self.ChangeLine_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.ChangeLine_3.setGeometry(QtCore.QRect(300, 80, 71, 31))
        self.ChangeLine_3.setStyleSheet("background-color: rgb(169, 169, 169);\n"
"border-radius: 5px;")
        self.ChangeLine_3.setObjectName("ChangeLine_3")
        self.ChangeLine_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.ChangeLine_4.setGeometry(QtCore.QRect(380, 80, 71, 31))
        self.ChangeLine_4.setStyleSheet("background-color: rgb(169, 169, 169);\n"
"border-radius: 5px;")
        self.ChangeLine_4.setObjectName("ChangeLine_4")
        self.ChangeLine_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.ChangeLine_5.setGeometry(QtCore.QRect(460, 80, 71, 31))
        self.ChangeLine_5.setStyleSheet("background-color: rgb(169, 169, 169);\n"
"border-radius: 5px;")
        self.ChangeLine_5.setObjectName("ChangeLine_5")
        self.ChangeLine_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.ChangeLine_6.setGeometry(QtCore.QRect(540, 80, 71, 31))
        self.ChangeLine_6.setStyleSheet("background-color: rgb(169, 169, 169);\n"
"border-radius: 5px;")
        self.ChangeLine_6.setObjectName("ChangeLine_6")
        self.ChangeLine_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.ChangeLine_7.setGeometry(QtCore.QRect(620, 80, 71, 31))
        self.ChangeLine_7.setStyleSheet("background-color: rgb(169, 169, 169);\n"
"border-radius: 5px;")
        self.ChangeLine_7.setObjectName("ChangeLine_7")
        self.ChangeLine_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.ChangeLine_8.setGeometry(QtCore.QRect(700, 80, 71, 31))
        self.ChangeLine_8.setStyleSheet("background-color: rgb(169, 169, 169);\n"
"border-radius: 5px;")
        self.ChangeLine_8.setObjectName("ChangeLine_8")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Add.setText(_translate("MainWindow", "Добавить данные"))
        self.Change.setText(_translate("MainWindow", "Изменение данных"))
        self.Dell.setText(_translate("MainWindow", "Удаление данных"))
        self.Back.setText(_translate("MainWindow", "Обратно в меню"))
        self.Open.setText(_translate("MainWindow", "Открыть таблицу"))
