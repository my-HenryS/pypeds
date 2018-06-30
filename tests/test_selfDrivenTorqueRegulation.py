from unittest import TestCase

from pypeds.example.model.regulation import SelfDrivenTorqueRegulation, SelfDampingTorqueRegulation
from pypeds.example.model.sfmodel import SFModel
from pypeds.example.entity import RotatePedestrian
from pypeds.shape2d import Ellipse2D, Point2D, Vector2D
import math


class TestSelfDrivenTorqueRegulation(TestCase):
    def setUp(self):
        self.model = SFModel(0.004)
        self.regulation_1 = SelfDrivenTorqueRegulation(self.model)
        self.regulation_2 = SelfDampingTorqueRegulation(self.model, 0.5)
        self.entity_1 = RotatePedestrian(Ellipse2D(Point2D(19.5, 26), 0.45 / 2, 0.25 / 2, 0))
        self.entity_1.model = self.model

    def test_torque(self):
        n = 0
        while n < 1000:
            self.regulation_1.exert(self.entity_1)
            print(self.entity_1.angle, self.entity_1.palstance, self.entity_1.angular_acc)
            self.regulation_2.exert(self.entity_1)
            print(self.entity_1.angle, self.entity_1.palstance, self.entity_1.angular_acc)
            self.entity_1.move()
            print(self.entity_1.angle, self.entity_1.palstance, self.entity_1.angular_acc)
            n += 1

    def tearDown(self):
        pass
