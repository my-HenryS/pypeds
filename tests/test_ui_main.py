from unittest import TestCase
from pypeds.gui.ui.mainwindow_main import Ui_MainWindow_Main
from PyQt5 import QtWidgets
import sys
import qdarkstyle

class TestUI(TestCase):

    def test_ui(self):
        app = QtWidgets.QApplication(sys.argv)
        win = Ui_MainWindow_Main()
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        win.show()
        sys.exit(app.exec_())