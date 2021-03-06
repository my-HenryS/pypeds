from unittest import TestCase
from pypeds.gui.ui.mainwindow_setting import Ui_MainWindow_Setting
from PyQt5 import QtWidgets
import sys
import qdarkstyle

class TestUI(TestCase):

    def test_ui(self):
        app = QtWidgets.QApplication(sys.argv)
        win = Ui_MainWindow_Setting()
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        win.show()
        sys.exit(app.exec_())