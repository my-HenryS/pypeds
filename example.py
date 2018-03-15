from pypeds.example.model.sfmodel import SFModel
from pypeds.example.listener import PedestrianEscapeListener
from pypeds.example.strategy import NearestGoalStrategy
from pypeds.scene import Scene
from pypeds.gui.panel import *
from pypeds.gui.ui.mainwindow_main import *
from pypeds.gui.ui.mainwindow_setting import *
from PyQt5 import QtWidgets
import sys
import qdarkstyle

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    scene = Scene()
    model = SFModel(0.0001)
    scene.model = model
    ex = Ui_MainWindow_Main()
    s = Ui_MainWindow_Setting()
    panel_setting=Panel(s,"Setting")
    panel_main = Panel(ex, "Simulation")
    scene.add_listener(panel_main)
    scene.add_listener(PedestrianEscapeListener())
    scene.add_listener(NearestGoalStrategy())
    panel_main.show()
    app.exec_()
    scene.stop()
