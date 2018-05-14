from PyQt5.QtGui import *
from PyQt5.QtCore import QPointF, QRectF


class SceneDrawer(object):
    def __init__(self, device, register):
        self.device = device
        self.background_color = QColor(255, 255, 255)
        self.entity_register = register

    def draw(self, scene):
        self.device.setBrush(self.background_color)
        self.device.drawRect(QRectF(-300, -300, 600, 600))  # todo remove hard code
        for entity in scene.entities:
            if entity.drawer is not None:
                entity.drawer.draw(entity)
            else:
                self.entity_register.add_drawer_support(entity)
                entity.drawer.draw(entity)

