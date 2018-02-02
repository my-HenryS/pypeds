from pypeds.scene import *
from pypeds.entity import *
from pypeds.shape import *
from pypeds.gui.panel import *



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    scene = Scene()
    scene.add_entity(Agent(Circle2D(center=(4, 4), radius=5)))
    panel = Panel("Simulation")
    scene.add_listener(panel)
    panel.show()
    scene.run()
    app.exec_()