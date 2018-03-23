# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_setting.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt,QMimeData
from PyQt5.QtGui import QDrag

class Ui_MainWindow_Setting(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1327, 732)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 20, 781, 651))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 779, 649))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        # self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_2.setGeometry(QtCore.QRect(910, 520, 81, 30))
        # self.pushButton_2.setObjectName("pushButton_2")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(820, 560, 91, 30))
        self.label_13.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_13.setObjectName("label_13")
        # self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton.setGeometry(QtCore.QRect(820, 520, 81, 30))
        # self.pushButton.setObjectName("pushButton")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(820, 600, 481, 30))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(820, 100, 131, 30))
        self.label_4.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(820, 60, 481, 30))
        self.comboBox.setObjectName("comboBox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(820, 20, 91, 30))
        self.label_3.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_3.setObjectName("label_3")
        # self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_3.setGeometry(QtCore.QRect(1000, 520, 141, 30))
        # self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(820, 140, 221, 30))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(820, 480, 131, 30))
        self.label_16.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_16.setObjectName("label_16")
        # self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_5.setGeometry(QtCore.QRect(1150, 520, 151, 30))
        # self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(820, 640, 481, 30))
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(820, 180, 131, 30))
        self.label_5.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_5.setObjectName("label_5")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(1080, 100, 221, 30))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(920, 20, 111, 30))
        self.pushButton_20.setObjectName("pushButton_20")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(820, 220, 491, 251))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.pushButton_24 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_24.setGeometry(QtCore.QRect(10, 170, 451, 30))
        self.pushButton_24.setObjectName("pushButton_24")
        self.label_57 = QtWidgets.QLabel(self.tab_7)
        self.label_57.setGeometry(QtCore.QRect(10, 10, 91, 30))
        self.label_57.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_57.setObjectName("label_57")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_7)
        self.comboBox_3.setGeometry(QtCore.QRect(110, 90, 91, 30))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.insertItem(0, "Circle")
        self.comboBox_3.insertItem(1, "Box")
        self.comboBox_3.insertItem(2, "Ellipse")
        self.label_63 = QtWidgets.QLabel(self.tab_7)
        self.label_63.setGeometry(QtCore.QRect(10, 90, 91, 30))
        self.label_63.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_63.setObjectName("label_63")
        self.stackedWidget = QtWidgets.QStackedWidget(self.tab_7)
        self.stackedWidget.setGeometry(QtCore.QRect(210, 90, 251, 71))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_58 = QtWidgets.QLabel(self.page_3)
        self.label_58.setGeometry(QtCore.QRect(0, 0, 131, 30))
        self.label_58.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_58.setObjectName("label_58")
        self.lineEdit_43 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_43.setGeometry(QtCore.QRect(140, 0, 111, 31))
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_76 = QtWidgets.QLabel(self.page_4)
        self.label_76.setGeometry(QtCore.QRect(0, 0, 131, 30))
        self.label_76.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_76.setObjectName("label_76")
        self.lineEdit_44 = QtWidgets.QLineEdit(self.page_4)
        self.lineEdit_44.setGeometry(QtCore.QRect(140, 0, 111, 31))
        self.lineEdit_44.setObjectName("lineEdit_44")
        self.label_77 = QtWidgets.QLabel(self.page_4)
        self.label_77.setGeometry(QtCore.QRect(0, 40, 131, 30))
        self.label_77.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_77.setObjectName("label_77")
        self.lineEdit_45 = QtWidgets.QLineEdit(self.page_4)
        self.lineEdit_45.setGeometry(QtCore.QRect(140, 40, 111, 31))
        self.lineEdit_45.setObjectName("lineEdit_45")
        self.stackedWidget.addWidget(self.page_4)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_89 = QtWidgets.QLabel(self.page)
        self.label_89.setGeometry(QtCore.QRect(0, 0, 61, 30))
        self.label_89.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_89.setObjectName("label_89")
        self.lineEdit_38 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_38.setGeometry(QtCore.QRect(70, 0, 51, 31))
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.label_90 = QtWidgets.QLabel(self.page)
        self.label_90.setGeometry(QtCore.QRect(130, 0, 61, 30))
        self.label_90.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_90.setObjectName("label_90")
        self.lineEdit_59 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_59.setGeometry(QtCore.QRect(200, 0, 51, 31))
        self.lineEdit_59.setObjectName("lineEdit_59")
        self.label_91 = QtWidgets.QLabel(self.page)
        self.label_91.setGeometry(QtCore.QRect(60, 40, 61, 30))
        self.label_91.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_91.setObjectName("label_91")
        self.lineEdit_60 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_60.setGeometry(QtCore.QRect(130, 40, 51, 31))
        self.lineEdit_60.setObjectName("lineEdit_60")
        self.stackedWidget.addWidget(self.page)
        self.label_65 = QtWidgets.QLabel(self.tab_7)
        self.label_65.setGeometry(QtCore.QRect(110, 50, 91, 30))
        self.label_65.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_65.setObjectName("label_65")
        self.lineEdit_36 = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit_36.setGeometry(QtCore.QRect(210, 50, 71, 31))
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.label_67 = QtWidgets.QLabel(self.tab_7)
        self.label_67.setGeometry(QtCore.QRect(290, 50, 91, 30))
        self.label_67.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_67.setObjectName("label_67")
        self.lineEdit_37 = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit_37.setGeometry(QtCore.QRect(390, 50, 81, 31))
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.label_68 = QtWidgets.QLabel(self.tab_7)
        self.label_68.setGeometry(QtCore.QRect(10, 130, 91, 30))
        self.label_68.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_68.setObjectName("label_68")
        self.comboBox_5 = QtWidgets.QComboBox(self.tab_7)
        self.comboBox_5.setGeometry(QtCore.QRect(110, 130, 91, 30))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.label_82 = QtWidgets.QLabel(self.tab_7)
        self.label_82.setGeometry(QtCore.QRect(10, 50, 41, 30))
        self.label_82.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_82.setObjectName("label_82")
        self.lineEdit_52 = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit_52.setGeometry(QtCore.QRect(60, 50, 41, 31))
        self.lineEdit_52.setObjectName("lineEdit_52")
        self.label_84 = QtWidgets.QLabel(self.tab_7)
        self.label_84.setGeometry(QtCore.QRect(110, 10, 61, 30))
        self.label_84.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_84.setObjectName("label_84")
        self.lineEdit_54 = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit_54.setGeometry(QtCore.QRect(180, 10, 51, 31))
        self.lineEdit_54.setObjectName("lineEdit_54")
        self.label_85 = QtWidgets.QLabel(self.tab_7)
        self.label_85.setGeometry(QtCore.QRect(240, 10, 61, 30))
        self.label_85.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_85.setObjectName("label_85")
        self.lineEdit_55 = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit_55.setGeometry(QtCore.QRect(310, 10, 51, 31))
        self.lineEdit_55.setObjectName("lineEdit_55")
        self.label_86 = QtWidgets.QLabel(self.tab_7)
        self.label_86.setGeometry(QtCore.QRect(370, 10, 51, 30))
        self.label_86.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_86.setObjectName("label_86")
        self.lineEdit_56 = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit_56.setGeometry(QtCore.QRect(430, 10, 41, 31))
        self.lineEdit_56.setObjectName("lineEdit_56")
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.label_61 = QtWidgets.QLabel(self.tab_8)
        self.label_61.setGeometry(QtCore.QRect(10, 10, 91, 30))
        self.label_61.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_61.setObjectName("label_61")
        self.label_62 = QtWidgets.QLabel(self.tab_8)
        self.label_62.setGeometry(QtCore.QRect(10, 90, 91, 30))
        self.label_62.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_62.setObjectName("label_62")
        self.label_69 = QtWidgets.QLabel(self.tab_8)
        self.label_69.setGeometry(QtCore.QRect(110, 10, 61, 30))
        self.label_69.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_69.setObjectName("label_69")
        self.label_70 = QtWidgets.QLabel(self.tab_8)
        self.label_70.setGeometry(QtCore.QRect(110, 50, 91, 30))
        self.label_70.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_70.setObjectName("label_70")
        self.lineEdit_39 = QtWidgets.QLineEdit(self.tab_8)
        self.lineEdit_39.setGeometry(QtCore.QRect(180, 10, 51, 31))
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.lineEdit_40 = QtWidgets.QLineEdit(self.tab_8)
        self.lineEdit_40.setGeometry(QtCore.QRect(210, 50, 71, 31))
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.label_71 = QtWidgets.QLabel(self.tab_8)
        self.label_71.setGeometry(QtCore.QRect(240, 10, 61, 30))
        self.label_71.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_71.setObjectName("label_71")
        self.label_72 = QtWidgets.QLabel(self.tab_8)
        self.label_72.setGeometry(QtCore.QRect(290, 50, 91, 30))
        self.label_72.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_72.setObjectName("label_72")
        self.lineEdit_41 = QtWidgets.QLineEdit(self.tab_8)
        self.lineEdit_41.setGeometry(QtCore.QRect(310, 10, 51, 31))
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.lineEdit_42 = QtWidgets.QLineEdit(self.tab_8)
        self.lineEdit_42.setGeometry(QtCore.QRect(390, 50, 81, 31))
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_8)
        self.comboBox_4.setGeometry(QtCore.QRect(110, 90, 91, 30))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.insertItem(0, "Circle")
        self.comboBox_4.insertItem(1, "Box")
        self.comboBox_4.insertItem(2, "Ellipse")
        self.label_73 = QtWidgets.QLabel(self.tab_8)
        self.label_73.setGeometry(QtCore.QRect(10, 130, 91, 30))
        self.label_73.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_73.setObjectName("label_73")
        self.pushButton_25 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_25.setGeometry(QtCore.QRect(10, 170, 451, 30))
        self.pushButton_25.setObjectName("pushButton_25")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.tab_8)
        self.stackedWidget_2.setGeometry(QtCore.QRect(210, 90, 251, 71))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_59 = QtWidgets.QLabel(self.page_5)
        self.label_59.setGeometry(QtCore.QRect(0, 0, 131, 30))
        self.label_59.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_59.setObjectName("label_59")
        self.lineEdit_46 = QtWidgets.QLineEdit(self.page_5)
        self.lineEdit_46.setGeometry(QtCore.QRect(140, 0, 111, 31))
        self.lineEdit_46.setObjectName("lineEdit_46")
        self.stackedWidget_2.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.label_78 = QtWidgets.QLabel(self.page_6)
        self.label_78.setGeometry(QtCore.QRect(0, 0, 131, 30))
        self.label_78.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_78.setObjectName("label_78")
        self.lineEdit_47 = QtWidgets.QLineEdit(self.page_6)
        self.lineEdit_47.setGeometry(QtCore.QRect(140, 0, 111, 31))
        self.lineEdit_47.setObjectName("lineEdit_47")
        self.label_79 = QtWidgets.QLabel(self.page_6)
        self.label_79.setGeometry(QtCore.QRect(0, 40, 131, 30))
        self.label_79.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_79.setObjectName("label_79")
        self.lineEdit_48 = QtWidgets.QLineEdit(self.page_6)
        self.lineEdit_48.setGeometry(QtCore.QRect(140, 40, 111, 31))
        self.lineEdit_48.setObjectName("lineEdit_48")
        self.stackedWidget_2.addWidget(self.page_6)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_92 = QtWidgets.QLabel(self.page_2)
        self.label_92.setGeometry(QtCore.QRect(0, 0, 61, 30))
        self.label_92.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_92.setObjectName("label_92")
        self.lineEdit_61 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_61.setGeometry(QtCore.QRect(70, 0, 51, 31))
        self.lineEdit_61.setObjectName("lineEdit_61")
        self.label_93 = QtWidgets.QLabel(self.page_2)
        self.label_93.setGeometry(QtCore.QRect(130, 0, 61, 30))
        self.label_93.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_93.setObjectName("label_93")
        self.lineEdit_62 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_62.setGeometry(QtCore.QRect(200, 0, 51, 31))
        self.lineEdit_62.setObjectName("lineEdit_62")
        self.label_94 = QtWidgets.QLabel(self.page_2)
        self.label_94.setGeometry(QtCore.QRect(60, 40, 61, 30))
        self.label_94.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_94.setObjectName("label_94")
        self.lineEdit_63 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_63.setGeometry(QtCore.QRect(130, 40, 51, 31))
        self.lineEdit_63.setObjectName("lineEdit_63")
        self.stackedWidget_2.addWidget(self.page_2)
        self.comboBox_6 = QtWidgets.QComboBox(self.tab_8)
        self.comboBox_6.setGeometry(QtCore.QRect(110, 130, 91, 30))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.label_83 = QtWidgets.QLabel(self.tab_8)
        self.label_83.setGeometry(QtCore.QRect(370, 10, 51, 30))
        self.label_83.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_83.setObjectName("label_83")
        self.lineEdit_53 = QtWidgets.QLineEdit(self.tab_8)
        self.lineEdit_53.setGeometry(QtCore.QRect(430, 10, 41, 31))
        self.lineEdit_53.setObjectName("lineEdit_53")
        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_74 = QtWidgets.QLabel(self.tab)
        self.label_74.setGeometry(QtCore.QRect(10, 10, 91, 30))
        self.label_74.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_74.setObjectName("label_74")
        self.comboBox_7 = QtWidgets.QComboBox(self.tab)
        self.comboBox_7.setGeometry(QtCore.QRect(10, 50, 91, 30))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.insertItem(0, "Circle")
        self.comboBox_7.insertItem(1, "Box")
        self.comboBox_7.insertItem(2, "Ellispse")
        self.label_75 = QtWidgets.QLabel(self.tab)
        self.label_75.setGeometry(QtCore.QRect(10, 90, 91, 30))
        self.label_75.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_75.setObjectName("label_75")
        self.pushButton_26 = QtWidgets.QPushButton(self.tab)
        self.pushButton_26.setGeometry(QtCore.QRect(10, 170, 451, 30))
        self.pushButton_26.setObjectName("pushButton_26")
        self.stackedWidget_3 = QtWidgets.QStackedWidget(self.tab)
        self.stackedWidget_3.setGeometry(QtCore.QRect(110, 10, 341, 111))
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.label_60 = QtWidgets.QLabel(self.page_7)
        self.label_60.setGeometry(QtCore.QRect(0, 0, 131, 30))
        self.label_60.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_60.setObjectName("label_60")
        self.lineEdit_49 = QtWidgets.QLineEdit(self.page_7)
        self.lineEdit_49.setGeometry(QtCore.QRect(140, 0, 111, 31))
        self.lineEdit_49.setObjectName("lineEdit_49")
        self.stackedWidget_3.addWidget(self.page_7)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.label_80 = QtWidgets.QLabel(self.page_8)
        self.label_80.setGeometry(QtCore.QRect(0, 0, 131, 30))
        self.label_80.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_80.setObjectName("label_80")
        self.lineEdit_50 = QtWidgets.QLineEdit(self.page_8)
        self.lineEdit_50.setGeometry(QtCore.QRect(140, 0, 111, 31))
        self.lineEdit_50.setObjectName("lineEdit_50")
        self.label_81 = QtWidgets.QLabel(self.page_8)
        self.label_81.setGeometry(QtCore.QRect(0, 40, 131, 30))
        self.label_81.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_81.setObjectName("label_81")
        self.lineEdit_51 = QtWidgets.QLineEdit(self.page_8)
        self.lineEdit_51.setGeometry(QtCore.QRect(140, 40, 111, 31))
        self.lineEdit_51.setObjectName("lineEdit_51")
        self.stackedWidget_3.addWidget(self.page_8)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.label_95 = QtWidgets.QLabel(self.page_9)
        self.label_95.setGeometry(QtCore.QRect(0, 0, 131, 30))
        self.label_95.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_95.setObjectName("label_95")
        self.lineEdit_64 = QtWidgets.QLineEdit(self.page_9)
        self.lineEdit_64.setGeometry(QtCore.QRect(140, 0, 71, 31))
        self.lineEdit_64.setObjectName("lineEdit_64")
        self.label_96 = QtWidgets.QLabel(self.page_9)
        self.label_96.setGeometry(QtCore.QRect(0, 40, 131, 30))
        self.label_96.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_96.setObjectName("label_96")
        self.lineEdit_65 = QtWidgets.QLineEdit(self.page_9)
        self.lineEdit_65.setGeometry(QtCore.QRect(140, 40, 71, 31))
        self.lineEdit_65.setObjectName("lineEdit_65")
        self.label_97 = QtWidgets.QLabel(self.page_9)
        self.label_97.setGeometry(QtCore.QRect(0, 80, 131, 30))
        self.label_97.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_97.setObjectName("label_97")
        self.lineEdit_66 = QtWidgets.QLineEdit(self.page_9)
        self.lineEdit_66.setGeometry(QtCore.QRect(140, 80, 71, 31))
        self.lineEdit_66.setObjectName("lineEdit_66")
        self.stackedWidget_3.addWidget(self.page_9)
        self.comboBox_9 = QtWidgets.QComboBox(self.tab)
        self.comboBox_9.setGeometry(QtCore.QRect(10, 130, 91, 30))
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.label_87 = QtWidgets.QLabel(self.tab)
        self.label_87.setGeometry(QtCore.QRect(110, 130, 91, 30))
        self.label_87.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_87.setObjectName("label_87")
        self.lineEdit_57 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_57.setGeometry(QtCore.QRect(210, 130, 71, 31))
        self.lineEdit_57.setObjectName("lineEdit_57")
        self.label_88 = QtWidgets.QLabel(self.tab)
        self.label_88.setGeometry(QtCore.QRect(290, 130, 91, 30))
        self.label_88.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_88.setObjectName("label_88")
        self.lineEdit_58 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_58.setGeometry(QtCore.QRect(390, 130, 71, 31))
        self.lineEdit_58.setObjectName("lineEdit_58")
        self.tabWidget_2.addTab(self.tab, "")
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(1080, 140, 221, 30))
        self.pushButton_21.setObjectName("pushButton_21")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1327, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.connectstack()
        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.pushButton_2.setText(_translate("MainWindow", "Wall"))
        self.label_13.setText(_translate("MainWindow", "Model"))
        # self.pushButton.setText(_translate("MainWindow", "Agent"))
        self.label_4.setText(_translate("MainWindow", "Default Generate"))
        self.label_3.setText(_translate("MainWindow", "Scene"))
        # self.pushButton_3.setText(_translate("MainWindow", "Generate Region"))
        self.pushButton_10.setText(_translate("MainWindow", "Default Generate"))
        self.label_16.setText(_translate("MainWindow", "Manual Generate"))
        # self.pushButton_5.setText(_translate("MainWindow", "Safe Region"))
        self.pushButton_11.setText(_translate("MainWindow", "Confirm"))
        self.label_5.setText(_translate("MainWindow", "Semi-Generate"))
        self.pushButton_19.setText(_translate("MainWindow", "Remove all entity"))
        self.pushButton_20.setText(_translate("MainWindow", "Create Scene"))
        self.pushButton_24.setText(_translate("MainWindow", "Grid Generate"))
        self.label_57.setText(_translate("MainWindow", "Region"))
        self.label_63.setText(_translate("MainWindow", "Shape"))
        self.label_58.setText(_translate("MainWindow", "radius"))
        self.lineEdit_43.setText(_translate("MainWindow", "2"))
        self.label_76.setText(_translate("MainWindow", "Length Of Box"))
        self.lineEdit_44.setText(_translate("MainWindow", "10"))
        self.label_77.setText(_translate("MainWindow", "Width Of Box"))
        self.lineEdit_45.setText(_translate("MainWindow", "10"))
        self.label_89.setText(_translate("MainWindow", "a"))
        self.lineEdit_38.setText(_translate("MainWindow", "4"))
        self.label_90.setText(_translate("MainWindow", "b"))
        self.lineEdit_59.setText(_translate("MainWindow", "2"))
        self.label_91.setText(_translate("MainWindow", "Angle"))
        self.lineEdit_60.setText(_translate("MainWindow", "30"))
        self.label_65.setText(_translate("MainWindow", "Length"))
        self.lineEdit_36.setText(_translate("MainWindow", "100"))
        self.label_67.setText(_translate("MainWindow", "Width"))
        self.lineEdit_37.setText(_translate("MainWindow", "50"))
        self.label_68.setText(_translate("MainWindow", "Entity"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Ped"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "Wall"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "Safe-Region"))
        self.label_82.setText(_translate("MainWindow", "INTV"))
        self.lineEdit_52.setText(_translate("MainWindow", "10"))
        self.label_84.setText(_translate("MainWindow", "X"))
        self.lineEdit_54.setText(_translate("MainWindow", "500"))
        self.label_85.setText(_translate("MainWindow", "Y"))
        self.lineEdit_55.setText(_translate("MainWindow", "200"))
        self.label_86.setText(_translate("MainWindow", "Num"))
        self.lineEdit_56.setText(_translate("MainWindow", "10"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("MainWindow", "Gird-Generate"))
        self.label_61.setText(_translate("MainWindow", "Region"))
        self.label_62.setText(_translate("MainWindow", "Shape"))
        self.label_69.setText(_translate("MainWindow", "X"))
        self.label_70.setText(_translate("MainWindow", "Length"))
        self.lineEdit_39.setText(_translate("MainWindow", "500"))
        self.lineEdit_40.setText(_translate("MainWindow", "100"))
        self.label_71.setText(_translate("MainWindow", "Y"))
        self.label_72.setText(_translate("MainWindow", "Width"))
        self.lineEdit_41.setText(_translate("MainWindow", "200"))
        self.lineEdit_42.setText(_translate("MainWindow", "50"))
        self.label_73.setText(_translate("MainWindow", "Entity"))
        self.pushButton_25.setText(_translate("MainWindow", "Random Generate"))
        self.label_59.setText(_translate("MainWindow", "radius"))
        self.lineEdit_46.setText(_translate("MainWindow", "2"))
        self.label_78.setText(_translate("MainWindow", "Length Of Box"))
        self.lineEdit_47.setText(_translate("MainWindow", "10"))
        self.label_79.setText(_translate("MainWindow", "Width Of Box"))
        self.lineEdit_48.setText(_translate("MainWindow", "10"))
        self.label_92.setText(_translate("MainWindow", "a"))
        self.lineEdit_61.setText(_translate("MainWindow", "4"))
        self.label_93.setText(_translate("MainWindow", "b"))
        self.lineEdit_62.setText(_translate("MainWindow", "2"))
        self.label_94.setText(_translate("MainWindow", "Angle"))
        self.lineEdit_63.setText(_translate("MainWindow", "30"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Ped"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "Wall"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "Safe-Region"))
        self.label_83.setText(_translate("MainWindow", "Num"))
        self.lineEdit_53.setText(_translate("MainWindow", "10"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("MainWindow", "Random-Generate"))
        self.label_74.setText(_translate("MainWindow", "Shape"))
        self.label_75.setText(_translate("MainWindow", "Entity"))
        self.pushButton_26.setText(_translate("MainWindow", "Common Generate"))
        self.label_60.setText(_translate("MainWindow", "radius"))
        self.lineEdit_49.setText(_translate("MainWindow", "2"))
        self.label_80.setText(_translate("MainWindow", "Length Of Box"))
        self.lineEdit_50.setText(_translate("MainWindow", "10"))
        self.label_81.setText(_translate("MainWindow", "Width Of Box"))
        self.lineEdit_51.setText(_translate("MainWindow", "10"))
        self.label_95.setText(_translate("MainWindow", "a"))
        self.lineEdit_64.setText(_translate("MainWindow", "500"))
        self.label_96.setText(_translate("MainWindow", "b"))
        self.lineEdit_65.setText(_translate("MainWindow", "500"))
        self.label_97.setText(_translate("MainWindow", "Angle"))
        self.lineEdit_66.setText(_translate("MainWindow", "500"))
        self.comboBox_9.setItemText(0, _translate("MainWindow", "Ped"))
        self.comboBox_9.setItemText(1, _translate("MainWindow", "Wall"))
        self.comboBox_9.setItemText(2, _translate("MainWindow", "Safe-Region"))
        self.label_87.setText(_translate("MainWindow", "X"))
        self.lineEdit_57.setText(_translate("MainWindow", "500"))
        self.label_88.setText(_translate("MainWindow", "Y"))
        self.lineEdit_58.setText(_translate("MainWindow", "200"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "Common-Generate"))
        self.pushButton_21.setText(_translate("MainWindow", "Cancel "))

    def connectstack(self):
        self.comboBox_3.currentIndexChanged.connect(self.display_one)
        self.comboBox_4.currentIndexChanged.connect(self.display_two)
        self.comboBox_7.currentIndexChanged.connect(self.display_three)

    def display_one(self, i):
        self.stackedWidget.setCurrentIndex(i)

    def display_two(self, i):
        self.stackedWidget_2.setCurrentIndex(i)

    def display_three(self, i):
        self.stackedWidget_3.setCurrentIndex(i)


class Dragebutton(QtWidgets.QPushButton):
    def __init__(self, title, parent):
        super(Dragebutton, self).__init__(title, parent)
        self.parent=parent

    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.LeftButton:
            return

        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())

        dropAction = drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, e):
        QtWidgets.QPushButton.mousePressEvent(self, e)

        if e.button() == Qt.LeftButton:
            self.parent.drag_entity=self.text()
