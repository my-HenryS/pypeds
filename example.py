from pypeds.example.model.sfmodel import SFModel
from pypeds.shape2d import *
from pypeds.gui.panel import *
import sys
import qdarkstyle


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    scene = Scene()
    model = SFModel(0.004)
    scene.model = model
    scene.add_entity(Movable(Circle2D(center=Point2D(4, 4), radius=5)))
    scene.add_entity(Movable(Box2D(center=Point2D(11, 6), length=4, width=10)))
    panel = Panel("Simulation")
    scene.add_listener(panel)
    panel.show()
    scene.start()
    sys.exit(app.exec_())