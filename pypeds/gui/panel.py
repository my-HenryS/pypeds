from pypeds.gui.drawer.drawer_register import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pypeds.gui.ui.main_window import *


class Panel(SceneListener):
    """
    Wraps window class with scene listener. panel--window has a 1-to-1 relationship
    """
    def __init__(self, title="", scene=None, width=200, height=200):
        super().__init__(scene)
        self.scene = scene

        self.default_drawer_register = True
        self.drawer_register = None

        self.window = MainWindow(title, self)
        self.painter = self.window.painter

    def register_drawer(self, drawer_register):
        """ Give value to attribute 'drawer_register'.
        And call add_drawer_support() to register entities and shapes with drawer in self.scene.
        Shall be called after assigned a listening scene.
        :param drawer_register: a scene_drawer_register
        """
        self.drawer_register = drawer_register
        self.drawer_register.add_drawer_support(self.scene)

    def on_added(self, scene):
        """ When added to scene, Panel call drawer_register to register its entities and shapes with drawers.
        If default_drawer_register is set to True, the drawer_register uses 'default' mode.
        :param scene: the listening scene
        """
        self.scene = scene
        if self.default_drawer_register:
            self.register_drawer(SceneDrawerRegister(self.painter, mode="default"))

    def on_stepped(self):
        """ At each step, we call scene drawer to draw.

        """
        self.window.paintEvent(None)

    def on_removed(self):
        pass

    def show(self):
        self.window.show()


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Extends UI class with window and drawer methods
    """
    def __init__(self, title="", panel=None):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(title)
        self.center()
        self.painter = QPainter()
        self.panel = panel

    def center(self):
        """
        move window to screen center
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    @property
    def scene(self):
        return self.panel.scene

    def paintEvent(self, e):
        """ Define that window will call scene's drawer to draw themselves (and it then will call entities
         & then shapes to draw)

        :param e: painter event, not yet used
        :return:
        """
        self.painter.begin(self)
        self.scene.drawer.draw(self.scene)
        self.painter.end()
