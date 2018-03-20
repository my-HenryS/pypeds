from pypeds.scene import *
from pypeds.gui.ui.mainwindow_main import Ui_MainWindow_Main
from pypeds.gui.ui.mainwindow_setting import Ui_MainWindow_Setting
from pypeds.gui.drawer.drawer_register import SceneDrawerRegister
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDesktopWidget
from pypeds.example.generator import *
from pypeds.example.model.sfmodel import SFModel
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui
from pypeds.example.strategy import NearestGoalStrategy
from pypeds.example.listener import PedestrianEscapeListener, Average_velocity, timer


class Panel(SceneListener):
    """
    Wraps window class with scene listener. panel--window has a 1-to-1 relationship
    """

    def __init__(self, window, title="", fps=16):
        super().__init__()

        self.default_drawer_register = True
        self.drawer_register = None

        self.window = window
        self.painter = self.window.painter

    def register_drawer(self, drawer_register):
        """ Give value to attribute 'drawer_register'.
        And call add_drawer_support() to register entities and shapes with drawer in self.scene.
        Shall be called after assigned a listening scene.1
        Set drawer_register's device to self.painter
        :param drawer_register: a scene_drawer_register
        """
        self.drawer_register = drawer_register
        if self.drawer_register.device is not self.painter:
            self.drawer_register.device = self.painter
        self.drawer_register.add_drawer_support(self.scene)

    def on_added(self):
        """ After being added,  # TODO define behaviours

        :return:
        """
        pass

    def on_begin(self):
        """ When added to scene, Panel call drawer_register to register its entities and shapes with drawers.
        If default_drawer_register is set to True, the drawer_register uses 'default' mode.
        :param scene: the listening scene
        """
        if self.default_drawer_register:
            self.register_drawer(SceneDrawerRegister(self.painter, mode="default"))

    def on_stepped(self):
        """ At each step, we call scene drawer to draw.

        """

    def on_removed(self):
        pass


class MainWindow(Ui_MainWindow_Main):
    """
    Extends UI class with window and drawer methods
    """

    def __init__(self, title, fps=16):
        super().__init__()
        self._translate = QtCore.QCoreApplication.translate
        self.setupUi(self)
        self.setWindowTitle(title)
        self.center()
        self.retranslateUi(self)
        # init paint area and assigned to scroll area
        self.area = PaintArea(self, fps)
        self.scrollArea.setWidget(self.area)
        self.panel = Panel(self)
        self.settingwindow = SettingWindow("Setting", 16, self)
        self.scenePool = self.settingwindow.scenePool
        self.enable = False
        self.pause_flag = False
        self.pushButton_11.clicked.connect(self.hide)
        self.pushButton_11.clicked.connect(self.settingwindow.handle_click)
        self.pushButton_13.clicked.connect(self.start)
        self.pushButton_12.clicked.connect(self.pause)
        self.pushButton_12.setEnabled(False)
        self.pushButton_14.setEnabled(False)
        self.horizontalSlider.valueChanged.connect(self.velocity_change)

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

    @property
    def painter(self):
        return self.area.painter

    def start(self):
        if self.enable == False:
            self.scene.start()
            self.pushButton_13.setText(self._translate("MainWindow", "Terminate"))
            self.pushButton_12.setEnabled(True)
            self.pushButton_14.setEnabled(True)
            self.enable = not self.enable
            return

        if self.enable == True:
            self.scene.stop()
            self.pushButton_13.setText(self._translate("MainWindow", "Run"))
            self.pushButton_12.setEnabled(False)
            self.pushButton_12.setText(self._translate("MainWindow", "Pause"))
            self.pushButton_14.setEnabled(False)
            self.enable = not self.enable

    def pause(self):
        if self.pause_flag == False:
            self.pushButton_12.setText(self._translate("MainWindow", "Resume"))
            self.pause_flag = not self.pause_flag
            return

        if self.pause_flag == True:
            self.pushButton_12.setText(self._translate("MainWindow", "Pause"))
            self.pause_flag = not self.pause_flag

    def velocity_change(self):
        self.scene.model.time_per_step = self.horizontalSlider.value() * 0.0001919 + 0.001
        # self.horizontalSlider.value()*0.0001919+0.001)

    def handle_click(self):
        for scene in self.scenePool:
            if self.panel in scene._listeners:
                scene.remove_listener(self.panel)
        if not self.isVisible():
            self.show()

    def default_generate(self):
        pass


class SettingWindow(Ui_MainWindow_Setting):
    def __init__(self, title, fps, mainwindow):
        super(SettingWindow, self).__init__()
        self._translate = QtCore.QCoreApplication.translate
        self.setupUi(self)
        self.setWindowTitle(title)
        self.center()
        self.retranslateUi(self)
        self.generator = Generator(self)
        self.mainwindow = mainwindow
        self.scenePool = []
        # init paint area and assigned to scroll area
        self.area = PaintArea(self, fps)
        self.scrollArea.setWidget(self.area)
        self.panel = self.mainwindow.panel
        self.pushButton_11.clicked.connect(self.hide)
        self.pushButton_11.clicked.connect(self.mainwindow.handle_click)
        self.pushButton_12.clicked.connect(self.hide)
        self.pushButton_12.clicked.connect(self.mainwindow.handle_click)
        self.pushButton_25.clicked.connect(self.random_generate)
        self.pushButton_24.clicked.connect(self.grid_generate)
        self.pushButton_19.clicked.connect(self.remove_all_entity)
        self.pushButton_20.clicked.connect(self.create_scene)
        self.comboBox.currentIndexChanged.connect(self.scene_select)

    @property
    def scene(self):
        return self.mainwindow.scene

    @property
    def painter(self):
        return self.area.painter

    def create_scene(self):
        """
        use the button to create a scene(Thread)
        :return:
        """
        scene = Scene()
        scene.model = SFModel(0.0001)
        scene.add_listener(PedestrianEscapeListener())
        scene.add_listener(Average_velocity())
        scene.add_listener(timer())
        scene.add_listener(NearestGoalStrategy())
        self.scenePool.append(scene)
        self.comboBox.addItem(scene.getName())
        self.mainwindow.comboBox.addItem(scene.getName())

    def scene_select(self):
        for index in self.scenePool:
            if index.getName() == self.comboBox.currentText():
                index.add_listener(self.mainwindow.panel)
                print(index._listeners)

    def center(self):
        """
        move window to screen center
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def handle_click(self):
        for scene in self.scenePool:
            if self.panel in scene._listeners:
                scene.remove_listener(self.panel)
        if not self.isVisible():
            self.show()

    def grid_generate(self):
        """
        use the setting window to generate the pedes in grid way
        :return: pedes generated in grid way
        """
        pass

    def random_generate(self):
        """
        use the setting window to generate the pedes in random way
        :return: pedes generated in random way
        """
        pass

    def item_generate(self):
        """
        use the setting window to generate the item
        :return:
        """
        pass

    def remove_all_entity(self):
        """
        use the setting window to remove the entities in the entityPool
        :return:
        """
        self.mainwindow.scene._entities = EntityPool()


class PaintArea(QWidget):
    """
    A paint area that shows the whole scene
    """

    def __init__(self, window, fps):
        super().__init__()
        self.window = window
        self.painter = QPainter()
        # set clock timer to
        self.checkThreadTimer = QtCore.QTimer(self)
        self.checkThreadTimer.start(fps)
        self.checkThreadTimer.timeout.connect(self.update)
        self.zoom = 1.0
        self.offset_x = 0.0
        self.offset_y = 0.0
        self.last_x = -1
        self.last_y = -1

    @property
    def scene(self):
        return self.window.scene

    def add_panel(self):
        """
        when the current window's comboBox select a scene's name,give panel to the scene
        :return:scene with a panel
        """
        scene_selected = [x for x in self.window.scenePool if x.getName() == self.window.comboBox.currentText()]
        if scene_selected != [] and not self.window.panel in scene_selected[0]._listeners:
            scene_selected[0].add_listener(self.window.panel)

    def settingwindow_job(self):
        """
        when PaintAre's window is settingwindow, do the job below to paint the shapes in the screen
        :return:
        """
        pass
        # if isinstance(self.window, SettingWindow) and self.scene is not None:
        #     if self.window.comboBox.currentText() in self.window.generator.ped_initial_pos:
        #         for index in self.window.generator.initial_pos[self.window.comboBox.currentText()]:
        #             Circle2DDrawer(self.painter).draw(Circle2D(Point2D(index[0], index[1]), index[2]))
        #     if self.window.comboBox.currentText() in self.window.generator.item_initial_pos:
        #         for index in self.window.generator.initial_pos[self.window.comboBox.currentText()]:
        #             if isinstance(index, Circle2D):
        #                 Circle2DDrawer(self.painter).draw(index)
        #             if isinstance(index, Box2D):
        #                 Box2DDrawer(self.painter).draw(index)

    def mainwindow_job(self):
        """
        when PaintAre's window is mainwindow, do the job below to paint the shapes in the screen
        :return:
        """
        pass
        # if isinstance(self.window, MainWindow) and self.scene is not None and self.scene.drawer is not None:
        #     self.scene.drawer.draw(self.scene)

    def paintEvent(self, e):
        """ Define that window will call scene's drawer to draw themselves (and it then will call entities
         & then shapes to draw)

        :param e: painter event, not yet used
        :return:
        """
        self.painter.begin(self)
        self.painter.translate(self.offset_x, self.offset_y)
        self.painter.scale(self.zoom, self.zoom)
        self.add_panel()
        self.settingwindow_job()
        self.mainwindow_job()
        self.painter.end()

    def wheelEvent(self, event: QtGui.QWheelEvent):
        self.zoom = self.zoom + event.angleDelta().y() / 1200.0
        if self.zoom < 1:
            self.zoom = 1

    def mousePressEvent(self, event: QtGui.QMouseEvent):
        if self.last_x is not -1:
            self.offset_x += event.pos().x() - self.last_x
            self.offset_y += event.pos().y() - self.last_y
        else:
            self.last_x = event.pos().x()
            self.last_y = event.pos().y()

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent):
        self.last_x = -1
        self.last_y = -1
