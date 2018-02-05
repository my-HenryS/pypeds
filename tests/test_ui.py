from unittest import TestCase
from pypeds.gui.panel import MainWindow
from PyQt5 import QtWidgets
import sys

class TestUI(TestCase):

    def test_ui(self):
        app = QtWidgets.QApplication(sys.argv)
        win = MainWindow()
        win.show()
        sys.exit(app.exec_())