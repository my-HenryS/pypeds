from pypeds.example.model.sfmodel import SFModel
from pypeds.example.listener import *
from pypeds.example.strategy import NearestGoalStrategy
from pypeds.scene import Scene
from pypeds.gui.panel import *
from pypeds.gui.ui.mainwindow_main import *
from PyQt5 import QtWidgets
import sys
import qdarkstyle

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    m = MainWindow("MainWindow")
    m.show()
    app.installEventFilter(m)
    sys.exit(app.exec_())
