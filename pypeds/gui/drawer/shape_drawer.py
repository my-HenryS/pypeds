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


class Ellipse2DDrawer(ShapeDrawer):

    def __init__(self, device):
        super().__init__(device)
        self.color = QColor(0, 0, 0, 200)

    def draw(self, ellipse):
        x, y = ellipse.center.x, ellipse.center.y
        a, b = ellipse.a, ellipse.b
        self.device.setBrush(self.color)
        self.device.translate(x, y)
        self.device.rotate(-ellipse.angle)
        self.device.drawEllipse(QPointF(0, 0), a, b)  # draw ellipse by defining its bound box
        self.device.rotate(ellipse.angle)
        self.device.translate(-x, -y)

class Box2DDrawer(ShapeDrawer):

    def __init__(self, device):
        super().__init__(device)
        self.color = QColor(0, 0, 0, 200)

    def draw(self, box):
        l, d, w, h = box.x_min, box.y_min, box.length, box.width
        self.device.setBrush(self.color)
        self.device.drawRect(QRectF(l, d, w, h))
