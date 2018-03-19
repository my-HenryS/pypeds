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
    scene = Scene()
    model = SFModel(0.0001)
    scene.model = model
    # panel = Panel("Simulation")
    # scene.add_listener(panel)
    # scene.add_listener(PedestrianEscapeListener())
    # scene.add_listener(NearestGoalStrategy())
    # scene.add_listener(Average_velocity())
    # scene.add_listener(timer())
    # panel.show()
    # m=MainWindow(panel,"Simulation").show()
    # print(panel.window==m)
    m=MainWindow("MainWindow")
    m.show()
    app.exec_()
    scene.stop()
