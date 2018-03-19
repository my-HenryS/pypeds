# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_setting.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow_Setting(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1315, 732)
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
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(910, 520, 81, 30))
        self.pushButton_2.setObjectName("pushButton_2")
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
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(820, 520, 81, 30))
        self.pushButton.setObjectName("pushButton")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(820, 600, 471, 30))
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
        self.comboBox.setGeometry(QtCore.QRect(820, 60, 471, 30))
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
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1000, 520, 141, 30))
        self.pushButton_3.setObjectName("pushButton_3")
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
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1150, 520, 141, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(820, 640, 221, 30))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(1060, 640, 231, 30))
        self.pushButton_12.setObjectName("pushButton_12")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(820, 220, 471, 251))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_28 = QtWidgets.QLabel(self.tab_3)
        self.label_28.setGeometry(QtCore.QRect(10, 50, 91, 30))
        self.label_28.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.tab_3)
        self.label_29.setGeometry(QtCore.QRect(10, 130, 91, 30))
        self.label_29.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_29.setObjectName("label_29")
        self.pushButton_16 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_16.setGeometry(QtCore.QRect(240, 170, 211, 30))
        self.pushButton_16.setObjectName("pushButton_16")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_21.setGeometry(QtCore.QRect(120, 130, 104, 31))
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 91, 30))
        self.label_7.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_7.setObjectName("label_7")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_22.setGeometry(QtCore.QRect(120, 10, 104, 31))
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_23.setGeometry(QtCore.QRect(350, 90, 104, 31))
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.label_30 = QtWidgets.QLabel(self.tab_3)
        self.label_30.setGeometry(QtCore.QRect(240, 50, 91, 30))
        self.label_30.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.tab_3)
        self.label_31.setGeometry(QtCore.QRect(240, 90, 91, 30))
        self.label_31.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_31.setObjectName("label_31")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_24.setGeometry(QtCore.QRect(120, 50, 104, 31))
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.label_32 = QtWidgets.QLabel(self.tab_3)
        self.label_32.setGeometry(QtCore.QRect(10, 90, 91, 30))
        self.label_32.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_32.setObjectName("label_32")
        self.pushButton_17 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_17.setGeometry(QtCore.QRect(10, 170, 211, 30))
        self.pushButton_17.setObjectName("pushButton_17")
        self.label_33 = QtWidgets.QLabel(self.tab_3)
        self.label_33.setGeometry(QtCore.QRect(240, 130, 91, 30))
        self.label_33.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_33.setObjectName("label_33")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_25.setGeometry(QtCore.QRect(120, 90, 104, 31))
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_26.setGeometry(QtCore.QRect(350, 130, 104, 31))
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_27.setGeometry(QtCore.QRect(350, 50, 104, 31))
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.radioButton_5 = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_5.setGeometry(QtCore.QRect(240, 15, 112, 23))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_6.setGeometry(QtCore.QRect(350, 15, 112, 23))
        self.radioButton_6.setObjectName("radioButton_6")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_28.setGeometry(QtCore.QRect(350, 50, 104, 31))
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.label_34 = QtWidgets.QLabel(self.tab_4)
        self.label_34.setGeometry(QtCore.QRect(240, 50, 91, 30))
        self.label_34.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_34.setObjectName("label_34")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_29.setGeometry(QtCore.QRect(120, 10, 104, 31))
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.lineEdit_30 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_30.setGeometry(QtCore.QRect(350, 90, 104, 31))
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.pushButton_18 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_18.setGeometry(QtCore.QRect(125, 170, 211, 30))
        self.pushButton_18.setObjectName("pushButton_18")
        self.label_35 = QtWidgets.QLabel(self.tab_4)
        self.label_35.setGeometry(QtCore.QRect(10, 50, 91, 30))
        self.label_35.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.tab_4)
        self.label_36.setGeometry(QtCore.QRect(240, 90, 91, 30))
        self.label_36.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.tab_4)
        self.label_37.setGeometry(QtCore.QRect(10, 10, 91, 30))
        self.label_37.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_37.setObjectName("label_37")
        self.lineEdit_31 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_31.setGeometry(QtCore.QRect(120, 50, 104, 31))
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.lineEdit_32 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_32.setGeometry(QtCore.QRect(120, 90, 104, 31))
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.label_38 = QtWidgets.QLabel(self.tab_4)
        self.label_38.setGeometry(QtCore.QRect(10, 90, 91, 30))
        self.label_38.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_38.setObjectName("label_38")
        self.radioButton_7 = QtWidgets.QRadioButton(self.tab_4)
        self.radioButton_7.setGeometry(QtCore.QRect(240, 15, 112, 23))
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(self.tab_4)
        self.radioButton_8.setGeometry(QtCore.QRect(350, 15, 112, 23))
        self.radioButton_8.setObjectName("radioButton_8")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_4.setGeometry(QtCore.QRect(10, 130, 441, 30))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.tabWidget.addTab(self.tab_4, "")
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
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1060, 100, 131, 30))
        self.label_6.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_6.setObjectName("label_6")
        self.label_39 = QtWidgets.QLabel(self.centralwidget)
        self.label_39.setGeometry(QtCore.QRect(1060, 140, 91, 30))
        self.label_39.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.centralwidget)
        self.label_40.setGeometry(QtCore.QRect(1060, 180, 91, 30))
        self.label_40.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_40.setObjectName("label_40")
        self.lineEdit_33 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_33.setGeometry(QtCore.QRect(1170, 140, 104, 31))
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.lineEdit_34 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_34.setGeometry(QtCore.QRect(1170, 180, 104, 31))
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(1080, 20, 211, 30))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(920, 20, 111, 30))
        self.pushButton_20.setObjectName("pushButton_20")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1315, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Wall"))
        self.label_13.setText(_translate("MainWindow", "Model"))
        self.pushButton.setText(_translate("MainWindow", "Agent"))
        self.label_4.setText(_translate("MainWindow", "Default Generate"))
        self.label_3.setText(_translate("MainWindow", "Scene"))
        self.pushButton_3.setText(_translate("MainWindow", "Generate Region"))
        self.pushButton_10.setText(_translate("MainWindow", "Default Generate"))
        self.label_16.setText(_translate("MainWindow", "Manual Generate"))
        self.pushButton_5.setText(_translate("MainWindow", "Safe Region"))
        self.pushButton_11.setText(_translate("MainWindow", "Confirm"))
        self.pushButton_12.setText(_translate("MainWindow", "Cancel"))
        self.label_28.setText(_translate("MainWindow", "Radius"))
        self.label_29.setText(_translate("MainWindow", "Length"))
        self.pushButton_16.setText(_translate("MainWindow", "Random Generate"))
        self.lineEdit_21.setText(_translate("MainWindow", "100"))
        self.label_7.setText(_translate("MainWindow", "Number"))
        self.lineEdit_22.setText(_translate("MainWindow", "10"))
        self.lineEdit_23.setText(_translate("MainWindow", "200"))
        self.label_30.setText(_translate("MainWindow", "Interval"))
        self.label_31.setText(_translate("MainWindow", "Y"))
        self.lineEdit_24.setText(_translate("MainWindow", "2"))
        self.label_32.setText(_translate("MainWindow", "X"))
        self.pushButton_17.setText(_translate("MainWindow", "Grid Generate"))
        self.label_33.setText(_translate("MainWindow", "Width"))
        self.lineEdit_25.setText(_translate("MainWindow", "500"))
        self.lineEdit_26.setText(_translate("MainWindow", "50"))
        self.lineEdit_27.setText(_translate("MainWindow", "10"))
        self.radioButton_5.setText(_translate("MainWindow", "Circle"))
        self.radioButton_6.setText(_translate("MainWindow", "Eilppse"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Pesdes"))
        self.lineEdit_28.setText(_translate("MainWindow", "200"))
        self.label_34.setText(_translate("MainWindow", "Y"))
        self.lineEdit_29.setText(_translate("MainWindow", "10"))
        self.lineEdit_30.setText(_translate("MainWindow", "50"))
        self.pushButton_18.setText(_translate("MainWindow", "Item Generate"))
        self.label_35.setText(_translate("MainWindow", "X"))
        self.label_36.setText(_translate("MainWindow", "Width"))
        self.label_37.setText(_translate("MainWindow", "Radius"))
        self.lineEdit_31.setText(_translate("MainWindow", "200"))
        self.lineEdit_32.setText(_translate("MainWindow", "50"))
        self.label_38.setText(_translate("MainWindow", "Length"))
        self.radioButton_7.setText(_translate("MainWindow", "Wall"))
        self.radioButton_8.setText(_translate("MainWindow", "Safe Region"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Circle"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Box"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Item"))
        self.label_5.setText(_translate("MainWindow", "Semi-Generate"))
        self.label_6.setText(_translate("MainWindow", "Setting Goal"))
        self.label_39.setText(_translate("MainWindow", "X"))
        self.label_40.setText(_translate("MainWindow", "Y"))
        self.lineEdit_33.setText(_translate("MainWindow", "10"))
        self.lineEdit_34.setText(_translate("MainWindow", "10"))
        self.pushButton_19.setText(_translate("MainWindow", "Remove all entity"))
        self.pushButton_20.setText(_translate("MainWindow", "Create Scene"))

