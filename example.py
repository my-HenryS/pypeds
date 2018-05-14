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
    scene = Scene()
    scene.model = SFModel(0.004)
    scene.add_listener(PedestrianEscapeListener())
    scene.add_listener(NearestGoalStrategy())
    scene.add_entity(Pedestrian(Ellipse2D(Point2D(3, 4), 0.45 / 2, 0.3 / 2, 0)))
    scene.add_entity(Pedestrian(Ellipse2D(Point2D(3, 5), 0.45 / 2, 0.3 / 2, 0)))
    scene.add_entity(Pedestrian(Ellipse2D(Point2D(3, 6), 0.45 / 2, 0.3 / 2, 0)))
    scene.add_entity(Pedestrian(Ellipse2D(Point2D(3, 7), 0.45 / 2, 0.3 / 2, 0)))
    scene.add_entity(Pedestrian(Ellipse2D(Point2D(3, 8), 0.45 / 2, 0.3 / 2, 0)))
    scene.add_entity(Pedestrian(Ellipse2D(Point2D(4, 4), 0.45 / 2, 0.3 / 2, 0)))
    scene.add_entity(Pedestrian(Ellipse2D(Point2D(4, 5), 0.45 / 2, 0.3 / 2, 0)))
    scene.add_entity(Pedestrian(Ellipse2D(Point2D(4, 6), 0.45 / 2, 0.3 / 2, 0)))
    scene.add_entity(Pedestrian(Ellipse2D(Point2D(4, 7), 0.45 / 2, 0.3 / 2, 0)))
    scene.add_entity(Pedestrian(Ellipse2D(Point2D(4, 8), 0.45 / 2, 0.3 / 2, 0)))
    generator = Generator()
    #generator.grid_generate(scene, Box2D(Point2D(5,5),6,6), "Ped", "Circle", 0.5/2, 0, 0, 10, 0, 0, 0, 1)
    #scene.add_entity(SafetyRegion(Box2D(Point2D(10, 30), 1, 4)))
    scene.add_entity(SafetyRegion(Circle2D(Point2D(10, 30), 4)))
    scene.to_json("scene1.json")


    m.add_scene(scene)
    m.show()
    sys.exit(app.exec_())
