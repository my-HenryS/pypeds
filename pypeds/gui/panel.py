from pypeds.gui.drawer.drawer_register import SceneDrawerRegister
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from pypeds.gui.ui.mainwindow_main import *
from pypeds.gui.ui.mainwindow_setting import *
from pypeds.scene import SceneListener
from pypeds.example.generator import *

class Panel(SceneListener):
    """
    Wraps window class with scene listener. panel--window has a 1-to-1 relationship
    """

    def __init__(self, setting_panel, title="", fps=16):
        super().__init__()

        self.default_drawer_register = True
        self.drawer_register = None

        self.window = MainWindow(self, title, fps, setting_panel)
        self.painter = self.window.painter

    def register_drawer(self, drawer_register):
        """ Give value to attribute 'drawer_register'.
        And call add_drawer_support() to register entities and shapes with drawer in self.scene.
        Shall be called after assigned a listening scene.
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

    def show(self):
        self.window.show()


class MainWindow(Ui_MainWindow_Main):
    """
    Extends UI class with window and drawer methods
    """

    def __init__(self, panel, title, fps, setting_panel):
        super().__init__()
        self._translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(title)
        self.center()
        self.panel = panel
        self.retranslateUi(self)
        # init paint area and assigned to scroll area
        self.area = PaintArea(self, fps)
        self.scrollArea.setWidget(self.area)
        self.settingwindow = SettingWindow("setting", 16, self,setting_panel)
        self.generator = Generator
        self.enable = False
        self.pause_flag = False
        self.pushButton_2.clicked.connect(self.start)
        self.pushButton_4.clicked.connect(self.pause)
        self.pushButton_4.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        # self.pushButton_8.clicked.connect(self.item_generate)
        self.horizontalSlider.valueChanged.connect(self.velocity_change)
        self.pushButton.clicked.connect(self.hide)
        self.pushButton.clicked.connect(self.settingwindow.handle_clicked)
        # self.pushButton_12.clicked.connect(self.grid_generate)
        # self.pushButton_11.clicked.connect(self.random_generate)
        # self.pushButton_10.clicked.connect(self.default_generate)

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
            self.pushButton_2.setText(self._translate("MainWindow", "Terminate"))
            self.pushButton_4.setEnabled(True)
            self.pushButton_3.setEnabled(True)
            self.enable = not self.enable
            return

        if self.enable == True:
            self.pushButton_2.setText(self._translate("MainWindow", "Run"))
            self.pushButton_4.setEnabled(False)
            self.pushButton_4.setText(self._translate("MainWindow", "Pause"))
            self.pushButton_3.setEnabled(False)
            self.enable = not self.enable

    def pause(self):
        if self.pause_flag == False:
            self.pushButton_4.setText(self._translate("MainWindow", "Resume"))
            self.pause_flag = not self.pause_flag
            return

        if self.pause_flag == True:
            self.pushButton_4.setText(self._translate("MainWindow", "Pause"))
            self.pause_flag = not self.pause_flag

    def velocity_change(self):
        self.scene.model.time_per_step = self.horizontalSlider.value() * 0.0001919 + 0.001
        # self.horizontalSlider.value()*0.0001919+0.001)

    def handle_clicked(self):
        if not self.isVisible():
            self.show()

    # def handle_close(self):
    #     self.close()

    def default_generate(self):
        """

        :return:the default generate of the scene
        """
        pass

    def grid_generate(self):
        """

        :return:pedestrain generate in grid way
        """
        self.generator(self.scene).grid_generate(
            Box2D(Point2D(int(self.lineEdit_12.text()), int(self.lineEdit_13.text())), int(self.lineEdit_16.text()),
                  int(self.lineEdit_15.text())), int(self.lineEdit_11.text()), int(self.lineEdit_14.text()),
            int(self.lineEdit_10.text()))

    def random_generate(self):
        """

        :return:pedestrain generate in random way
        """
        self.generator(self.scene).random_generate(
            Box2D(Point2D(int(self.lineEdit_12.text()), int(self.lineEdit_13.text())), int(self.lineEdit_16.text()),
                  int(self.lineEdit_15.text())), int(self.lineEdit_11.text()), int(self.lineEdit_14.text()))

    def item_generate(self):
        """

        :return:item generate
        """
        if self.comboBox_3.currentText() == "Circle":
            self.generator(self.scene).item_generate(Wall, Circle2D(
                Point2D(int(self.lineEdit_4.text()), int(self.lineEdit_7.text())),
                int(self.lineEdit_3.text())))  # FIXME remove the hard code

    def mousePressEvent(self, e):
        print("1")
        QPushButton.mousePressEvent(self.pushButton, e)

        if e.button() == Qt.LeftButton:
            print("2")


class SettingWindow(Ui_MainWindow_Setting):
    def __init__(self, title, fps, mainwindow, panel):
        super(SettingWindow, self).__init__()
        self.setWindowTitle(title)
        self.center()
        self.retranslateUi(self)
        self.mainwindow = mainwindow
        self.panel = panel
        # init paint area and assigned to scroll area
        self.area = PaintSetting(self, fps)
        self.scrollArea.setWidget(self.area)
        self.generator = Generator
        self.enable = False
        self.pause_flag = False
        self.pushButton_13.clicked.connect(self.hide)
        self.pushButton_13.clicked.connect(self.mainwindow.handle_clicked)
        self.pushButton_14.clicked.connect(self.hide)
        self.pushButton_14.clicked.connect(self.mainwindow.handle_clicked)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def handle_clicked(self):
        if not self.isVisible():
            self.show()

class PaintSetting(QWidget):
    def __init__(self,window,fps):
        super(PaintSetting, self).__init__()
        self.window=window
        self.painter=QPainter()
        self.checkThreadTimer = QtCore.QTimer(self)
        self.checkThreadTimer.start(fps)
        self.checkThreadTimer.timeout.connect(self.update)
        self.zoom = 1.0
        self.offset_x = 0.0
        self.offset_y = 0.0
        self.last_x = -1
        self.last_y = -1

    def paintEvent(self, QPaintEvent):
        self.painter.begin(self)
        self.painter.translate(self.offset_x, self.offset_y)
        self.painter.scale(self.zoom, self.zoom)
        Circle2DDrawer.draw(Circle2D(Point2D(50,50),3))
        self.painter.end()


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
        self.painter.translate(self.offset_x, self.offset_y)
        self.painter.scale(self.zoom, self.zoom)
        if self.scene.drawer is not None:
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
