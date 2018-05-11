# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_main.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow_Main(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1293, 732)
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
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(940, 560, 211, 30))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(1060, 600, 211, 30))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(820, 600, 211, 30))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(940, 640, 211, 30))
        self.pushButton_14.setObjectName("pushButton_14")
        # self.label_3 = QtWidgets.QLabel(self.centralwidget)
        # self.label_3.setGeometry(QtCore.QRect(820, 110, 211, 30))
        # self.label_3.setStyleSheet("QLabel{\n"
# "\n"
# "     border-width: 1px;\n"
# "\n"
# "     border-style: solid;\n"
# "\n"
# "     border-color: rgb(96, 96, 96);\n"
# "\n"
# "}")
#         self.label_3.setObjectName("label_3")
#         self.label_4 = QtWidgets.QLabel(self.centralwidget)
#         self.label_4.setGeometry(QtCore.QRect(1060, 110, 211, 30))
#         self.label_4.setStyleSheet("QLabel{\n"
# "\n"
# "     border-width: 1px;\n"
# "\n"
# "     border-style: solid;\n"
# "\n"
# "     border-color: rgb(96, 96, 96);\n"
# "\n"
# "}")
#         self.label_4.setObjectName("label_4")
#         self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
#         self.lineEdit.setGeometry(QtCore.QRect(820, 150, 211, 30))
#         self.lineEdit.setObjectName("lineEdit")
#         self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
#         self.lineEdit_2.setGeometry(QtCore.QRect(1060, 150, 211, 30))
#         self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(820, 190, 211, 30))
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
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(820, 230, 451, 16))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(820, 70, 451, 30))
        self.comboBox.setObjectName("comboBox")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(820, 30, 91, 30))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1293, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_98 = QtWidgets.QLabel(self.centralwidget)
        self.label_98.setGeometry(QtCore.QRect(820, 255, 211, 30))
        self.label_98.setStyleSheet("QLabel{\n"
                                    "\n"
                                    "     border-width: 1px;\n"
                                    "\n"
                                    "     border-style: solid;\n"
                                    "\n"
                                    "     border-color: rgb(96, 96, 96);\n"
                                    "\n"
                                    "}")
        self.label_98.setObjectName("label_98")
        self.label_99 = QtWidgets.QLabel(self.centralwidget)
        self.label_99.setGeometry(QtCore.QRect(820, 295, 211, 30))
        self.label_99.setStyleSheet("QLabel{\n"
                                    "\n"
                                    "     border-width: 1px;\n"
                                    "\n"
                                    "     border-style: solid;\n"
                                    "\n"
                                    "     border-color: rgb(96, 96, 96);\n"
                                    "\n"
                                    "}")
        self.label_99.setObjectName("label_98")
        self.label_100 = QtWidgets.QLabel(self.centralwidget)
        self.label_100.setGeometry(QtCore.QRect(1060, 295, 211, 30))
        self.label_100.setStyleSheet("QLabel{\n"
                                    "\n"
                                    "     border-width: 1px;\n"
                                    "\n"
                                    "     border-style: solid;\n"
                                    "\n"
                                    "     border-color: rgb(96, 96, 96);\n"
                                    "\n"
                                    "}")
        self.label_100.setObjectName("label_98")



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_11.setText(_translate("MainWindow", "Setting"))
        self.pushButton_12.setText(_translate("MainWindow", "Pause"))
        self.pushButton_13.setText(_translate("MainWindow", "Run"))
        self.pushButton_14.setText(_translate("MainWindow", "Skip"))
        # self.label_3.setText(_translate("MainWindow", "Average Velocity"))
        # self.label_4.setText(_translate("MainWindow", "Running Time"))
        self.label_5.setText(_translate("MainWindow", "Velocity Control"))
        self.label_6.setText(_translate("MainWindow", "Scene"))
        self.label_98.setText(_translate("MainWindow", "Mouse Pos"))

    # def eventFilter(self, source, event):
    #     if event.type() == QtCore.QEvent.MouseMove:
    #         if event.buttons() == QtCore.Qt.NoButton:
    #             pos = event.windowPos()
    #             if pos.x()<801 and pos.y()<674 and pos.x()>20 and pos.y()>20:
    #                 self.label_99.setText(str(pos.x()-20))
    #                 self.label_100.setText(str(pos.y()-20))
    #             else:
    #                 self.label_99.setText("")
    #                 self.label_100.setText("")
    #     return QtWidgets.QMainWindow.eventFilter(self, source, event)

