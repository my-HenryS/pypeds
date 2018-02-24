from pypeds.example.model.sfmodel import SFModel
from pypeds.example.entity import *
from pypeds.example.listener import PedestrianEscapeListener
from pypeds.example.strategy import NearestGoalStrategy
from pypeds.scene import Scene
from pypeds.shape2d import *
from pypeds.gui.panel import *
from PyQt5 import QtWidgets
import sys
import qdarkstyle


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    scene = Scene()
    model = SFModel(0.004)
    scene.model = model
    for i in range(1,40):
        scene.add_entity(Pedestrian(Circle2D(center=Point2D(4*i, 11.5), radius=0.243)))
    #scene.add_entity(Pedestrian(Circle2D(center=Point2D(11.6, 11.5), radius=1)))
    s=Ui_MainWindow_Setting()
    panel = Panel(s,"Simulation")
    scene.add_listener(panel)
    scene.add_listener(PedestrianEscapeListener())
    scene.add_listener(NearestGoalStrategy())
    panel.show()
    app.exec_()
    scene.stop()