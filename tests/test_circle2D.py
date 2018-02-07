from unittest import TestCase

from pypeds.shape2d import *
import math


class TestCircle2D(TestCase):
    def setUp(self):
        self.circle_test = Circle2D(Point2D(3, 4), 5)

    def test_distance(self):
        dist, dirt = self.circle_test.distance(Point2D(3, 0))
        self.assertAlmostEqual(dist, -2, delta=1.0e-10)
