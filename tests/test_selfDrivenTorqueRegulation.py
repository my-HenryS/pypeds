from unittest import TestCase

from pypeds.example.model.regulation import SelfDrivenTorqueRegulation
from pypeds.example.model.sfmodel import SFModel
from pypeds.example.entity import RotatePedestrian
from pypeds.shape2d import Ellipse2D, Point2D, Vector2D
import math


class TestSelfDrivenTorqueRegulation(TestCase):
    def setUp(self):
        self.model = SFModel(0.004)
        self.regulation = SelfDrivenTorqueRegulation(self.model)
        self.entity_1 = RotatePedestrian(Ellipse2D(Point2D(19.5, 26), 0.45 / 2, 0.25 / 2, math.pi / (4)))
        self.entity_1.model = self.model


    def test_torque(self):
        print(self.entity_1.angle, self.entity_1.palstance, self.entity_1.angular_acc)
        self.regulation.exert(self.entity_1)
        print(self.entity_1.angle, self.entity_1.palstance, self.entity_1.angular_acc)
        self.entity_1.move()
        print(self.entity_1.angle, self.entity_1.palstance, self.entity_1.angular_acc)


    def tearDown(self):
        pass
