from tkinter import *
from .drawer.drawer_register import *

# TODO write docs


class Panel(SceneListener):

    def __init__(self, title="", scene=None, width=200, height=200):
        super().__init__(scene)
        self.window = Tk()
        self.window.title(title)
        self.config_window()   # configure the window to stay in center of screen
        self.canvas = Canvas(self.window, width=width, height=height)
        self.canvas.pack()

        self.scene = None

        self.default_drawer_register = True
        self.drawer_register = None

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
            self.register_drawer(SceneDrawerRegister(self.canvas, mode="default"))

    def on_stepped(self):
        """ At each step, we call scene drawer to draw.

        """
        self.scene.drawer.draw(self.scene)

    def on_removed(self):
        pass

    def config_window(self):
        """ Let window init at the center of screen
        :return:
        """
        window = self.window
        # window.resizable(False, False)  we remain the window resizable
        window.update()  # update window ,must do
        curWidth = window.winfo_reqwidth()  # get current width
        curHeight = window.winfo_height()  # get current height
        scnWidth, scnHeight = window.maxsize()  # get screen width and height
        # now generate configuration information
        cnf = '%dx%d+%d+%d' % (curWidth, curHeight,
                                  (scnWidth - curWidth) / 2, (scnHeight - curHeight) / 2)
        window.geometry(cnf)

