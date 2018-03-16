from pypeds.example.model.sfmodel import SFModel
from pypeds.example.entity import *
from pypeds.example.listener import PedestrianEscapeListener
from pypeds.example.strategy import NearestGoalStrategy
from pypeds.scene import Scene
from pypeds.shape2d import *
from pypeds.gui.panel import *
from pypeds.gui.ui.mainwindow_main import *
from pypeds.example.generator import *
from pypeds.gui.ui.mainwindow import *
from PyQt5 import QtWidgets
import sys
import qdarkstyle

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    scene = Scene()
    model = SFModel(0.0001)
    scene.model = model
    s = Ui_MainWindow_Main()
    panel = Panel(s, "Simulation")
    scene.add_listener(panel)
    scene.add_listener(PedestrianEscapeListener())
    scene.add_listener(NearestGoalStrategy())
    panel.show()
    app.exec_()
    scene.stop()
