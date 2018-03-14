from abc import ABC, abstractmethod

from PyQt5.QtCore import QPointF, QRectF
from PyQt5.QtGui import *


class ShapeDrawer(ABC):
    def __init__(self, device):
        self.device = device

    @abstractmethod
    def draw(self, shape):
        """ Call painter to draw shape with proposed color

        :param shape: the drawable shape object
        :return:
        """


class Circle2DDrawer(ShapeDrawer):

    def __init__(self, device):
        super().__init__(device)
        self.color = QColor(0, 0, 0, 200)

    def draw(self, circle):
        x, y = circle.center.x, circle.center.y
        r = circle.radius
        self.device.setBrush(self.color)
        self.device.drawEllipse(QPointF(x, y), r, r)  # draw ellipse by defining its bound box


class Box2DDrawer(ShapeDrawer):

    def __init__(self, device):
        super().__init__(device)
        self.color = QColor(0, 0, 0, 200)

    def draw(self, box):
        l, d, w, h = box.e_left, box.e_down, box.length, box.width
        self.device.setBrush(self.color)
        self.device.drawRect(QRectF(l, d, w, h))



