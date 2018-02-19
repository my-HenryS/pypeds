from unittest import TestCase
from pypeds.gui.ui.mainwindow_main import Ui_MainWindow_Main,Event
from pypeds.gui.ui.mainwindow_setting import Ui_MainWindow_Setting
from PyQt5 import QtWidgets
import sys
import qdarkstyle

class TestUI(TestCase):

    def test_ui(self):
        app = QtWidgets.QApplication(sys.argv)
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        ex = Ui_MainWindow_Main()
        s = Ui_MainWindow_Setting()
        Event(ex, s)
        ex.show()
        sys.exit(app.exec_())