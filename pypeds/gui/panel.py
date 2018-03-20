from pypeds.scene import *
from pypeds.gui.ui.mainwindow_main import Ui_MainWindow_Main
from pypeds.gui.ui.mainwindow_setting import Ui_MainWindow_Setting
from pypeds.gui.drawer.drawer_register import SceneDrawerRegister
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDesktopWidget
from pypeds.generator import *
from pypeds.example.model.sfmodel import SFModel
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui
from pypeds.example.strategy import NearestGoalStrategy
from pypeds.example.listener import PedestrianEscapeListener


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
        self.settingwindow = SettingWindow("Setting", 16, self)
        self.scenePool = self.settingwindow.scenePool
        self.scene = None
        self.enable = False
        self.pause_flag = False
        self.pushButton_11.clicked.connect(self.hide)
        self.pushButton_11.clicked.connect(self.settingwindow.handle_click)
        self.pushButton_13.clicked.connect(self.start)
        self.pushButton_12.clicked.connect(self.pause)
        self.pushButton_12.setEnabled(False)
        self.pushButton_14.setEnabled(False)
        self.horizontalSlider.valueChanged.connect(self.velocity_change)
        self.comboBox.currentIndexChanged.connect(self.scene_select)

    def center(self):
        """
        move window to screen center
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

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
        self.scene_select()
        if not self.isVisible():
            self.show()

    def default_generate(self):
        pass

    def scene_select(self):
        self.scene = self.scenePool[self.comboBox.currentIndex()]


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
        self.scene = None
        # init paint area and assigned to scroll area
        self.area = PaintArea(self, fps)
        self.scrollArea.setWidget(self.area)
        self.pushButton_11.clicked.connect(self.hide)
        self.pushButton_11.clicked.connect(self.mainwindow.handle_click)
        self.pushButton_12.clicked.connect(self.hide)
        self.pushButton_12.clicked.connect(self.mainwindow.handle_click)
        self.pushButton_26.clicked.connect(self.common_generate)
        self.pushButton_25.clicked.connect(self.random_generate)
        self.pushButton_24.clicked.connect(self.grid_generate)
        self.pushButton_19.clicked.connect(self.remove_all_entity)
        self.pushButton_20.clicked.connect(self.create_scene)
        self.comboBox.currentIndexChanged.connect(self.scene_select)

    def create_scene(self):
        """
        use the button to create a scene(Thread)
        :return:
        """
        scene = Scene()
        scene.model = SFModel(0.004)
        scene.add_listener(PedestrianEscapeListener())
        scene.add_listener(NearestGoalStrategy())
        self.scenePool.append(scene)
        self.comboBox.addItem(scene.getName())
        self.mainwindow.comboBox.addItem(scene.getName())

    def scene_select(self):
        self.scene = self.scenePool[self.comboBox.currentIndex()]

    def center(self):
        """
        move window to screen center
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def handle_click(self):
        if not self.isVisible():
            self.show()

    def grid_generate(self):
        """
        use the setting window to generate the pedes in grid way
        :return: pedes generated in grid way
        """
        x = float(self.lineEdit_54.text())
        y = float(self.lineEdit_55.text())
        l = float(self.lineEdit_36.text())
        w = float(self.lineEdit_37.text())
        self.generator.grid_generate(self.scene, Box2D(Point2D(x,y), l ,w), self.comboBox_5.currentText(),
                                     self.comboBox_3.currentText(), int(self.lineEdit_56.text()), int(self.lineEdit_52.text()))

    def random_generate(self):
        """
        use the setting window to generate the pedes in random way
        :return: pedes generated in random way
        """
        pass

    def common_generate(self):
        """
        use the setting window to generate the item
        :return:
        """
        self.generator.common_generate(self.scene, self.comboBox_9.currentText(), self.comboBox_7.currentText())

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

    def paintEvent(self, e):
        """ Define that window will call scene's drawer to draw themselves (and it then will call entities
         & then shapes to draw)

        :param e: painter event, not yet used
        :return:
        """
        #print(self.window)
        self.painter.begin(self)
        self.painter.translate(self.offset_x, self.offset_y)
        self.painter.scale(self.zoom, self.zoom)
        if self.scene is not None:
            if self.scene.drawer is None or self.scene.drawer.device is not self.painter:
                self.register_drawer(SceneDrawerRegister(self.painter, mode="default"))   #fixme remove hard code
            self.scene.drawer.draw(self.scene)
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
