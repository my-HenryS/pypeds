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

    scene.add_entity(Wall(Box2D(Point2D(18, 25), 1, 10)))
    scene.add_entity(Wall(Box2D(Point2D(28, 25), 1, 10)))
    scene.add_entity(Wall(Box2D(Point2D(23, 29.5), 9, 1)))
    scene.add_entity(Wall(Box2D(Point2D(20.5, 20.5), 4, 1)))
    scene.add_entity(Wall(Box2D(Point2D(25.5, 20.5), 4, 1)))
    scene.add_entity(SafetyRegion(Box2D(Point2D(23, 15), 2, 1)))

    scene.add_entity(RotatePedestrian(Ellipse2D(Point2D(21.5, 23), 0.45 / 2, 0.25 / 2, math.pi)))
    scene.add_entity(RotatePedestrian(Ellipse2D(Point2D(22.5, 23.5), 0.45 / 2, 0.25 / 2, math.pi)))
    scene.add_entity(RotatePedestrian(Ellipse2D(Point2D(21.5, 24), 0.45 / 2, 0.25 / 2, math.pi)))
    scene.add_entity(RotatePedestrian(Ellipse2D(Point2D(22.5, 24.5), 0.45 / 2, 0.25 / 2, math.pi)))
    scene.add_entity(RotatePedestrian(Ellipse2D(Point2D(21.5, 25), 0.45 / 2, 0.25 / 2, math.pi)))

    scene.add_entity(RotatePedestrian(Ellipse2D(Point2D(23.5, 23), 0.45 / 2, 0.25 / 2, math.pi)))
    scene.add_entity(RotatePedestrian(Ellipse2D(Point2D(24.5, 23.5), 0.45 / 2, 0.25 / 2, math.pi)))
    scene.add_entity(RotatePedestrian(Ellipse2D(Point2D(23.5, 24), 0.45 / 2, 0.25 / 2, math.pi)))
    scene.add_entity(RotatePedestrian(Ellipse2D(Point2D(24.5, 24.5), 0.45 / 2, 0.25 / 2, math.pi)))
    scene.add_entity(RotatePedestrian(Ellipse2D(Point2D(23.5, 25), 0.45 / 2, 0.25 / 2, math.pi)))

    scene.add_entity(RotatePedestrian(Ellipse2D(Point2D(21.5, 24), 0.45 / 2, 0.25 / 2, math.pi)))
    scene.add_entity(RotatePedestrian(Ellipse2D(Point2D(22.5, 24.5), 0.45 / 2, 0.25 / 2, math.pi)))
    scene.add_entity(RotatePedestrian(Ellipse2D(Point2D(21.5, 25), 0.45 / 2, 0.25 / 2, math.pi)))
    scene.add_entity(RotatePedestrian(Ellipse2D(Point2D(22.5, 25.5), 0.45 / 2, 0.25 / 2, math.pi)))
    scene.add_entity(RotatePedestrian(Ellipse2D(Point2D(21.5, 26), 0.45 / 2, 0.25 / 2, math.pi)))

    scene.add_entity(RotatePedestrian(Ellipse2D(Point2D(23.5, 24), 0.45 / 2, 0.25 / 2, math.pi)))
    scene.add_entity(RotatePedestrian(Ellipse2D(Point2D(24.5, 24.5), 0.45 / 2, 0.25 / 2, math.pi)))
    scene.add_entity(RotatePedestrian(Ellipse2D(Point2D(23.5, 25), 0.45 / 2, 0.25 / 2, math.pi)))
    scene.add_entity(RotatePedestrian(Ellipse2D(Point2D(24.5, 25.5), 0.45 / 2, 0.25 / 2, math.pi)))
    scene.add_entity(RotatePedestrian(Ellipse2D(Point2D(23.5, 26), 0.45 / 2, 0.25 / 2, math.pi)))


    generator = Generator()
    m.add_scene(scene)
    m.show()
    sys.exit(app.exec_())
