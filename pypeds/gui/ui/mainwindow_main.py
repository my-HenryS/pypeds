# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_main.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow_Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow_Main, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1382, 711)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 20, 891, 631))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 889, 629))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1040, 530, 211, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(930, 570, 211, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1040, 610, 211, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1150, 570, 211, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(930, 30, 201, 31))
        self.label.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1160, 30, 201, 31))
        self.label_2.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(930, 80, 201, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(1160, 80, 201, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(930, 130, 201, 31))
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
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(930, 180, 430, 20))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1382, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Setting"))
        self.pushButton_2.setText(_translate("MainWindow", "Run"))
        self.pushButton_3.setText(_translate("MainWindow", "Skip"))
        self.pushButton_4.setText(_translate("MainWindow", "Pause"))
        self.label.setText(_translate("MainWindow", "        Average Velocity"))
        self.label_2.setText(_translate("MainWindow", "          Running Time"))
        self.label_3.setText(_translate("MainWindow", "        Average Velocity"))

