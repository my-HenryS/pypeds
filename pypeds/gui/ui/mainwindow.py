# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
<<<<<<< HEAD
        MainWindow.resize(1508, 700)
=======
        MainWindow.resize(1508, 685)
>>>>>>> origin/master
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 130, 30))
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
        self.label_2.setGeometry(QtCore.QRect(170, 30, 110, 30))
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
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(20, 150, 251, 16))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 110, 131, 30))
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
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 180, 131, 30))
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
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 220, 231, 31))
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 70, 130, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1020, 30, 91, 30))
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
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(1020, 70, 441, 30))
        self.comboBox.setObjectName("comboBox")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1020, 110, 131, 30))
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
<<<<<<< HEAD
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1020, 490, 61, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1100, 490, 61, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1180, 490, 131, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1330, 490, 131, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(1020, 530, 91, 30))
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
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(1020, 570, 441, 30))
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1060, 610, 90, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(1195, 610, 91, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(1330, 610, 89, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(300, 20, 700, 621))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 698, 619))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(170, 70, 110, 30))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(1020, 150, 211, 30))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(1020, 450, 131, 30))
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
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(1020, 190, 471, 251))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_10.setGeometry(QtCore.QRect(350, 50, 104, 31))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(10, 10, 91, 30))
        self.label_15.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(self.tab)
        self.label_17.setGeometry(QtCore.QRect(240, 90, 91, 30))
        self.label_17.setStyleSheet("QLabel{\n"
=======
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1020, 230, 91, 30))
        self.label_5.setStyleSheet("QLabel{\n"
>>>>>>> origin/master
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
<<<<<<< HEAD
        self.label_17.setObjectName("label_17")
        self.radioButton_3 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_3.setGeometry(QtCore.QRect(350, 14, 112, 23))
        self.radioButton_3.setObjectName("radioButton_3")
        self.label_18 = QtWidgets.QLabel(self.tab)
        self.label_18.setGeometry(QtCore.QRect(10, 90, 91, 30))
        self.label_18.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_18.setObjectName("label_18")
        self.radioButton_4 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_4.setGeometry(QtCore.QRect(240, 14, 112, 23))
        self.radioButton_4.setObjectName("radioButton_4")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_11.setGeometry(QtCore.QRect(120, 10, 104, 31))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_19 = QtWidgets.QLabel(self.tab)
        self.label_19.setGeometry(QtCore.QRect(10, 130, 91, 30))
        self.label_19.setStyleSheet("QLabel{\n"
=======
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1020, 270, 91, 30))
        self.label_8.setStyleSheet("QLabel{\n"
>>>>>>> origin/master
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
<<<<<<< HEAD
        self.label_19.setObjectName("label_19")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab)
        self.pushButton_11.setGeometry(QtCore.QRect(240, 170, 211, 30))
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_20 = QtWidgets.QLabel(self.tab)
        self.label_20.setGeometry(QtCore.QRect(240, 50, 91, 30))
        self.label_20.setStyleSheet("QLabel{\n"
=======
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1020, 310, 91, 30))
        self.label_9.setStyleSheet("QLabel{\n"
>>>>>>> origin/master
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
<<<<<<< HEAD
        self.label_20.setObjectName("label_20")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_12.setGeometry(QtCore.QRect(120, 90, 104, 31))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_13.setGeometry(QtCore.QRect(350, 90, 104, 31))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_14.setGeometry(QtCore.QRect(120, 50, 104, 31))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_15.setGeometry(QtCore.QRect(350, 130, 104, 31))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_21 = QtWidgets.QLabel(self.tab)
        self.label_21.setGeometry(QtCore.QRect(240, 130, 91, 30))
        self.label_21.setStyleSheet("QLabel{\n"
=======
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1250, 310, 91, 30))
        self.label_10.setStyleSheet("QLabel{\n"
>>>>>>> origin/master
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
<<<<<<< HEAD
        self.label_21.setObjectName("label_21")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab)
        self.pushButton_12.setGeometry(QtCore.QRect(10, 170, 211, 30))
        self.pushButton_12.setObjectName("pushButton_12")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_16.setGeometry(QtCore.QRect(120, 130, 104, 31))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_22 = QtWidgets.QLabel(self.tab)
        self.label_22.setGeometry(QtCore.QRect(10, 50, 91, 30))
        self.label_22.setStyleSheet("QLabel{\n"
=======
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1020, 350, 91, 30))
        self.label_11.setStyleSheet("QLabel{\n"
>>>>>>> origin/master
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
<<<<<<< HEAD
        self.label_22.setObjectName("label_22")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(240, 50, 91, 30))
        self.label_10.setStyleSheet("QLabel{\n"
=======
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(1250, 350, 91, 30))
        self.label_12.setStyleSheet("QLabel{\n"
>>>>>>> origin/master
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
<<<<<<< HEAD
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(10, 50, 91, 30))
        self.label_9.setStyleSheet("QLabel{\n"
=======
        self.label_12.setObjectName("label_12")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1020, 470, 61, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1100, 470, 61, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1180, 470, 131, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1330, 470, 131, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(1020, 510, 91, 30))
        self.label_13.setStyleSheet("QLabel{\n"
>>>>>>> origin/master
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
<<<<<<< HEAD
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(10, 90, 91, 30))
        self.label_11.setStyleSheet("QLabel{\n"
=======
        self.label_13.setObjectName("label_13")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(1020, 550, 441, 30))
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1060, 590, 90, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(1195, 590, 91, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(1330, 590, 89, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(300, 20, 700, 600))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 698, 598))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(1250, 270, 91, 30))
        self.label_14.setStyleSheet("QLabel{\n"
>>>>>>> origin/master
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
<<<<<<< HEAD
        self.label_11.setObjectName("label_11")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 50, 104, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(350, 50, 104, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 10, 104, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(350, 90, 104, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(240, 90, 91, 30))
        self.label_12.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_12.setObjectName("label_12")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(125, 170, 211, 30))
        self.pushButton_8.setObjectName("pushButton_8")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 90, 104, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 91, 30))
        self.label_8.setStyleSheet("QLabel{\n"
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
        self.label_8.setObjectName("label_8")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(240, 10, 91, 30))
        self.label_14.setStyleSheet("QLabel{\n"
=======
        self.label_14.setObjectName("label_14")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(1020, 390, 211, 30))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(1250, 390, 211, 30))
        self.pushButton_9.setObjectName("pushButton_9")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(1130, 230, 104, 31))
        self.lineEdit_2.setText("10")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(1130, 270, 104, 31))
        self.lineEdit_3.setText("2")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(1130, 310, 104, 31))
        self.lineEdit_4.setText("500")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(1130, 350, 104, 31))
        self.lineEdit_5.setText("100")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(1360, 270, 104, 31))
        self.lineEdit_6.setText("10")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(1360, 310, 104, 31))
        self.lineEdit_7.setText("200")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(1360, 350, 104, 31))
        self.lineEdit_8.setText("50")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(170, 70, 110, 30))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(1020, 150, 211, 30))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(1020, 190, 131, 30))
        self.label_15.setStyleSheet("QLabel{\n"
>>>>>>> origin/master
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
<<<<<<< HEAD
        self.label_14.setObjectName("label_14")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_17.setGeometry(QtCore.QRect(350, 10, 104, 31))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_3.setGeometry(QtCore.QRect(120, 130, 331, 30))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_23 = QtWidgets.QLabel(self.tab_2)
        self.label_23.setGeometry(QtCore.QRect(10, 130, 91, 30))
        self.label_23.setStyleSheet("QLabel{\n"
=======
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(1020, 430, 131, 30))
        self.label_16.setStyleSheet("QLabel{\n"
>>>>>>> origin/master
"\n"
"     border-width: 1px;\n"
"\n"
"     border-style: solid;\n"
"\n"
"     border-color: rgb(96, 96, 96);\n"
"\n"
"}")
<<<<<<< HEAD
        self.label_23.setObjectName("label_23")
        self.tabWidget.addTab(self.tab_2, "")
=======
        self.label_16.setObjectName("label_16")
>>>>>>> origin/master
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1508, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
<<<<<<< HEAD
        self.tabWidget.setCurrentIndex(0)
=======
>>>>>>> origin/master
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Average Velocity"))
        self.label_2.setText(_translate("MainWindow", "Running Time"))
        self.label_6.setText(_translate("MainWindow", "Velocity Control"))
        self.label_7.setText(_translate("MainWindow", "Trace CSV save"))
        self.label_3.setText(_translate("MainWindow", "Scene"))
        self.label_4.setText(_translate("MainWindow", "Default Generate"))
<<<<<<< HEAD
=======
        self.label_5.setText(_translate("MainWindow", "Number"))
        self.label_8.setText(_translate("MainWindow", "Radius"))
        self.label_9.setText(_translate("MainWindow", "X"))
        self.label_10.setText(_translate("MainWindow", "Y"))
        self.label_11.setText(_translate("MainWindow", "Length"))
        self.label_12.setText(_translate("MainWindow", "Width"))
>>>>>>> origin/master
        self.pushButton.setText(_translate("MainWindow", "Agent"))
        self.pushButton_2.setText(_translate("MainWindow", "Wall"))
        self.pushButton_3.setText(_translate("MainWindow", "Generate Region"))
        self.pushButton_5.setText(_translate("MainWindow", "Safe Region"))
        self.label_13.setText(_translate("MainWindow", "Model"))
        self.pushButton_4.setText(_translate("MainWindow", "Run"))
        self.pushButton_6.setText(_translate("MainWindow", "Pause"))
        self.pushButton_7.setText(_translate("MainWindow", "Skip"))
<<<<<<< HEAD
        self.pushButton_10.setText(_translate("MainWindow", "Default Generate"))
        self.label_16.setText(_translate("MainWindow", "Manual Generate"))
        self.lineEdit_10.setText(_translate("MainWindow", "10"))
        self.label_15.setText(_translate("MainWindow", "Number"))
        self.label_17.setText(_translate("MainWindow", "Y"))
        self.radioButton_3.setText(_translate("MainWindow", "Eillpse"))
        self.label_18.setText(_translate("MainWindow", "X"))
        self.radioButton_4.setText(_translate("MainWindow", "Circle"))
        self.lineEdit_11.setText(_translate("MainWindow", "10"))
        self.label_19.setText(_translate("MainWindow", "Length"))
        self.pushButton_11.setText(_translate("MainWindow", "Random Generate"))
        self.label_20.setText(_translate("MainWindow", "Interval"))
        self.lineEdit_12.setText(_translate("MainWindow", "500"))
        self.lineEdit_13.setText(_translate("MainWindow", "200"))
        self.lineEdit_14.setText(_translate("MainWindow", "2"))
        self.lineEdit_15.setText(_translate("MainWindow", "50"))
        self.label_21.setText(_translate("MainWindow", "Width"))
        self.pushButton_12.setText(_translate("MainWindow", "Grid Generate"))
        self.lineEdit_16.setText(_translate("MainWindow", "100"))
        self.label_22.setText(_translate("MainWindow", "Radius"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "R/G Generate"))
        self.label_10.setText(_translate("MainWindow", "Y"))
        self.label_9.setText(_translate("MainWindow", "X"))
        self.label_11.setText(_translate("MainWindow", "Length"))
        self.lineEdit_4.setText(_translate("MainWindow", "500"))
        self.lineEdit_7.setText(_translate("MainWindow", "200"))
        self.lineEdit_3.setText(_translate("MainWindow", "2"))
        self.lineEdit_8.setText(_translate("MainWindow", "50"))
        self.label_12.setText(_translate("MainWindow", "Width"))
        self.pushButton_8.setText(_translate("MainWindow", "Item Generate"))
        self.lineEdit_5.setText(_translate("MainWindow", "100"))
        self.label_8.setText(_translate("MainWindow", "Radius"))
        self.label_14.setText(_translate("MainWindow", "Angle"))
        self.lineEdit_17.setText(_translate("MainWindow", "200"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Circle"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Box"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Rectangle"))
        self.label_23.setText(_translate("MainWindow", "Shape"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "item Generate"))
=======
        self.label_14.setText(_translate("MainWindow", "Interval"))
        self.pushButton_8.setText(_translate("MainWindow", "Grid Generate"))
        self.pushButton_9.setText(_translate("MainWindow", "Random Generate"))
        self.pushButton_10.setText(_translate("MainWindow", "Default Generate"))
        self.label_15.setText(_translate("MainWindow", "R/G Generate"))
        self.label_16.setText(_translate("MainWindow", "Manual Generate"))
>>>>>>> origin/master

