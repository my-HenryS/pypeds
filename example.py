# from pypeds.example.model.sfmodel import SFModel
# from pypeds.example.listener import *
# from pypeds.example.strategy import NearestGoalStrategy
# from pypeds.scene import Scene
# from pypeds.gui.panel import *
# from pypeds.gui.ui.mainwindow_main import *
# from PyQt5 import QtWidgets
# import sys
# import qdarkstyle
#
# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
#     m = MainWindow("MainWindow")
#     scene = Scene()
#     scene.model = SFModel(0.004)
#     scene.add_listener(PedestrianEscapeListener())
#     scene.add_listener(NearestGoalStrategy())
#
#     scene.add_entity(Wall(Box2D(Point2D(20.5, 22.5), 1, 5)))
#     scene.add_entity(Wall(Box2D(Point2D(25.5, 22.5), 1, 5)))
#     scene.add_entity(Wall(Box2D(Point2D(23, 25.5), 6, 1)))
#     scene.add_entity(Wall(Box2D(Point2D(21.75, 20.5), 1.5, 1)))
#     scene.add_entity(Wall(Box2D(Point2D(24.25, 20.5), 1.5, 1)))
#     scene.add_entity(SafetyRegion(Box2D(Point2D(23, 15), 2, 1)))
#
#     #scene.add_entity(Pedestrian(Circle2D(Point2D(21.5, 22), 0.45 / 2)))
#     #scene.add_entity(Pedestrian(Circle2D(Point2D(21.5, 22.5), 0.45 / 2)))
#     #scene.add_entity(Pedestrian(Circle2D(Point2D(21.5, 23), 0.45 / 2)))
#     scene.add_entity(Pedestrian(Circle2D(Point2D(21.5, 23.5), 0.45 / 2)))
#     scene.add_entity(Pedestrian(Circle2D(Point2D(21.5, 24), 0.45 / 2)))
#     scene.add_entity(Pedestrian(Circle2D(Point2D(21.5, 24.5), 0.45 / 2)))
#
#     #scene.add_entity(Pedestrian(Circle2D(Point2D(22.5, 22), 0.45 / 2)))
#     #scene.add_entity(Pedestrian(Circle2D(Point2D(22.5, 22.5), 0.45 / 2)))
#     #scene.add_entity(Pedestrian(Circle2D(Point2D(22.5, 23), 0.45 / 2)))
#     scene.add_entity(Pedestrian(Circle2D(Point2D(22.5, 23.5), 0.45 / 2)))
#     scene.add_entity(Pedestrian(Circle2D(Point2D(22.5, 24), 0.45 / 2)))
#     scene.add_entity(Pedestrian(Circle2D(Point2D(22.5, 24.5), 0.45 / 2)))
#
#     #scene.add_entity(Pedestrian(Circle2D(Point2D(23.5, 22), 0.45 / 2)))
#     #scene.add_entity(Pedestrian(Circle2D(Point2D(23.5, 22.5), 0.45 / 2)))
#     #scene.add_entity(Pedestrian(Circle2D(Point2D(23.5, 23), 0.45 / 2)))
#     scene.add_entity(Pedestrian(Circle2D(Point2D(23.5, 23.5), 0.45 / 2)))
#     scene.add_entity(Pedestrian(Circle2D(Point2D(23.5, 24), 0.45 / 2)))
#     scene.add_entity(Pedestrian(Circle2D(Point2D(23.5, 24.5), 0.45 / 2)))
#
#     #scene.add_entity(Pedestrian(Circle2D(Point2D(24.5, 22), 0.45 / 2)))
#     #scene.add_entity(Pedestrian(Circle2D(Point2D(24.5, 22.5), 0.45 / 2)))
#     #scene.add_entity(Pedestrian(Circle2D(Point2D(24.5, 23), 0.45 / 2)))
#     scene.add_entity(Pedestrian(Circle2D(Point2D(24.5, 23.5), 0.45 / 2)))
#     scene.add_entity(Pedestrian(Circle2D(Point2D(24.5, 24), 0.45 / 2)))
#     scene.add_entity(Pedestrian(Circle2D(Point2D(24.5, 24.5), 0.45 / 2)))
#
#
#
#     generator = Generator()
#     #generator.grid_generate(scene, Box2D(Point2D(5,5),6,6), "Ped", "Circle", 0.5/2, 0, 0, 10, 0, 0, 0, 1)
#     #scene.add_entity(SafetyRegion(Box2D(Point2D(10, 30), 1, 4)))
#
#     #scene.to_json("scene1.json")
#
#
#     m.add_scene(scene)
#     m.show()
#     sys.exit(app.exec_())