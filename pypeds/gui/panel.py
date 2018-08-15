from pypeds.scene import *
from pypeds.gui.ui.mainwindow_main import Ui_MainWindow_Main
from pypeds.gui.ui.mainwindow_setting import Ui_MainWindow_Setting, Dragebutton
from pypeds.gui.drawer.drawer_register import SceneDrawerRegister
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDesktopWidget
from pypeds.generator import *
from pypeds.example.model.sfmodel import SFModel
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui
from pypeds.example.strategy import NearestGoalStrategy
from pypeds.example.listener import PedestrianEscapeListener
from PyQt5.QtCore import Qt


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

    def handle_click(self):
        self.scene_select()
        if not self.isVisible():
            self.show()

    def default_generate(self):
        pass

    def scene_select(self):
        if self.scene != None and self.scene.is_alive():
            self.scene.stop()
            self.pushButton_13.setText(self._translate("MainWindow", "Run"))
            self.pushButton_12.setEnabled(False)
            self.pushButton_12.setText(self._translate("MainWindow", "Pause"))
            self.pushButton_14.setEnabled(False)
            self.enable = False
        if self.scenePool != None and self.comboBox.currentIndex() != -1:
            self.scene = self.scenePool[self.comboBox.currentIndex()]


class SettingWindow(Ui_MainWindow_Setting):
    def __init__(self, title, fps, mainwindow):
        super(SettingWindow, self).__init__()
        self._translate = QtCore.QCoreApplication.translate
        self.setupUi(self)
        self.setWindowTitle(title)
        self.center()
        self.retranslateUi(self)
        self.scene = None
        self.generator = Generator(self.scene)
        self.mainwindow = mainwindow
        self.scenePool = []
        self.drag_entity = ''
        # init paint area and assigned to scroll area
        self.area = PaintArea(self, fps)
        self.scrollArea.setWidget(self.area)
        self.setAcceptDrops(True)
        self.dragbutton = Dragebutton("Agent", self)
        self.dragbutton.setGeometry(820, 520, 81, 30)
        self.dragbutton_2 = Dragebutton("Wall", self)
        self.dragbutton_2.setGeometry(910, 520, 81, 30)
        self.dragbutton_3 = Dragebutton("Generate Region", self)
        self.dragbutton_3.setGeometry(1000, 520, 141, 30)
        self.dragbutton_4 = Dragebutton("Safe Region", self)
        self.dragbutton_4.setGeometry(1150, 520, 151, 30)
        self.pushButton_11.clicked.connect(self.hide)
        self.pushButton_11.clicked.connect(self.mainwindow.handle_click)
        self.pushButton_26.clicked.connect(self.common_generate)
        self.pushButton_25.clicked.connect(self.random_generate)
        self.pushButton_24.clicked.connect(self.grid_generate)
        self.pushButton_19.clicked.connect(self.remove_all_entity)
        self.pushButton_20.clicked.connect(self.create_scene)
        self.pushButton_21.clicked.connect(self.cancel)
        self.comboBox.currentIndexChanged.connect(self.scene_select)

    def create_scene(self):
        """
        use the button to create a scene(Thread)
        :return:
        """
        #change the model from the SFM to CSVmodel
        scene = Scene()
        # scene.model = SFModel(0.004)
        scene.add_model(CSVModel(0.004,"/home/hdl/PycharmProjects/pypeds/pypeds/example/resources/ffffffffffff.csv", scene))
        print(scene.entities)
        # scene.add_listener(PedestrianEscapeListener())
        # scene.add_listener(NearestGoalStrategy())
        self.scenePool.append(scene)
        self.comboBox.addItem(scene.getName())
        self.mainwindow.comboBox.addItem(scene.getName())

    def scene_select(self):
        # print(self.scene)
        if self.scene !=None:
            pass
            # print(self.scene.entities)
        self.scene = self.scenePool[self.comboBox.currentIndex()]

    def cancel(self):
        for entity in self.generator.last_time_generate:
            self.scene.remove_entity(entity)

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):

        radius = float(self.lineEdit_49.text())
        length = float(self.lineEdit_50.text())
        width = float(self.lineEdit_51.text())
        shape = self.comboBox_7.currentText()
        a = float(self.lineEdit_64.text())
        b = float(self.lineEdit_65.text())
        angle = float(self.lineEdit_66.text())

        position = e.pos()
        if self.drag_entity == "Agent":
            self.generator.common_generate(self.scene, "Ped", shape, position.x()-20, position.y()-20, radius, length, width,
                                           a, b,
                                           angle)
        if self.drag_entity == "Wall":
            self.generator.common_generate(self.scene, "Wall", shape, position.x()-20, position.y()-20, radius, length, width,
                                           a, b,
                                           angle)
        if self.drag_entity == "Generate Region":
            pass
        if self.drag_entity == "Safe Region":
            self.generator.common_generate(self.scene, "Safe-Region", shape, position.x()-20, position.y()-20, radius, length,
                                           width,
                                           a, b,
                                           angle)
        e.setDropAction(Qt.MoveAction)
        e.accept()

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
        entity = self.comboBox_5.currentText()
        shape = self.comboBox_3.currentText()
        radius = float(self.lineEdit_43.text())
        length = float(self.lineEdit_44.text())
        width = float(self.lineEdit_45.text())
        number = int(self.lineEdit_56.text())
        intervel = int(self.lineEdit_52.text())
        a = float(self.lineEdit_38.text())
        b = float(self.lineEdit_59.text())
        angle = float(self.lineEdit_60.text())
        self.generator.grid_generate(self.scene, Box2D(Point2D(x, y), l, w), entity, shape, radius, length, width,
                                     number, a, b, angle, intervel)

    def random_generate(self):
        """
        use the setting window to generate the pedes in random way
        :return: pedes generated in random way
        """
        x = float(self.lineEdit_39.text())
        y = float(self.lineEdit_41.text())
        l = float(self.lineEdit_40.text())
        w = float(self.lineEdit_42.text())
        entity = self.comboBox_6.currentText()
        shape = self.comboBox_4.currentText()
        radius = float(self.lineEdit_46.text())
        length = float(self.lineEdit_47.text())
        width = float(self.lineEdit_48.text())
        number = int(self.lineEdit_53.text())
        a = float(self.lineEdit_61.text())
        b = float(self.lineEdit_62.text())
        angle = float(self.lineEdit_63.text())
        self.generator.random_generate(self.scene, Box2D(Point2D(x, y), l, w), entity, shape, radius, length,
                                       width, number, a, b, angle)

    def common_generate(self):
        """
        use the setting window to generate the item
        :return:
        """
        center_x = float(self.lineEdit_57.text())
        center_y = float(self.lineEdit_58.text())
        radius = float(self.lineEdit_49.text())
        length = float(self.lineEdit_50.text())
        width = float(self.lineEdit_51.text())
        entity = self.comboBox_9.currentText()
        shape = self.comboBox_7.currentText()
        a = float(self.lineEdit_64.text())
        b = float(self.lineEdit_65.text())
        angle = float(self.lineEdit_66.text())
        self.generator.common_generate(self.scene, entity, shape, center_x, center_y, radius, length, width, a, b,
                                       angle)

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
        self.painter.begin(self)
        self.painter.scale(self.zoom, self.zoom)
        if self.scene is not None:
            if self.scene.drawer is None or self.scene.drawer.device is not self.painter:
                self.register_drawer(SceneDrawerRegister(self.painter, mode="default"))  # fixme remove hard code
            self.scene.drawer.draw(self.scene)
        self.painter.end()

    def wheelEvent(self, event: QtGui.QWheelEvent):
        pass

    def mousePressEvent(self, event: QtGui.QMouseEvent):
        pass

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent):
        pass

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
