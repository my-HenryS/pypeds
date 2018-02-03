# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow1.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import sys

class Ui_hhh(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_hhh, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)




    def setupUi(self, hhh):
        hhh.setObjectName("hhh")
        hhh.resize(756, 341)
        hhh.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(hhh)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 90, 89, 25))
        self.pushButton.setObjectName("pushButton")
        hhh.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(hhh)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 756, 28))
        self.menubar.setObjectName("menubar")
        hhh.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(hhh)
        self.statusbar.setEnabled(False)
        self.statusbar.setObjectName("statusbar")
        hhh.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(hhh)
        self.toolBar.setObjectName("toolBar")
        hhh.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(hhh)
        QtCore.QMetaObject.connectSlotsByName(hhh)

    def retranslateUi(self, hhh):
        _translate = QtCore.QCoreApplication.translate
        hhh.setWindowTitle(_translate("hhh", "MainWindow"))
        self.pushButton.setText(_translate("hhh", "PushButton"))
        self.toolBar.setWindowTitle(_translate("hhh", "toolBar"))



if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Ui_hhh()
    win.show()
    sys.exit(app.exec_())