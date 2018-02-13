from unittest import TestCase

from pypeds.shape2d import *


class TestBox2D(TestCase):
    def setUp(self):
        self.box_test = Box2D(Point2D(1.5, 2), 3, 4)
        self.point_a = Point2D(1, 1)
        self.point_b = Point2D(6, 8)
        self.point_c = Point2D(3, 0)
        self.point_d = Point2D(1, -5)
        self.circle_in = Circle2D(Point2D(-2.4, -3.2), 5)
        self.circle_on = Circle2D(Point2D(-5, 4), 5)
        self.circle_out = Circle2D(Point2D(10, 0), 5)

    def test_distance(self):
        dist, dirt = self.box_test.distance(self.point_a)
        self.assertAlmostEqual(dist, -1, delta=1.0e-10)
        self.assertAlmostEqual(dirt.x, 1, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, 0, delta=1.0e-10)

        dist, dirt = self.box_test.distance(self.point_b)
        self.assertAlmostEqual(dist, 5, delta=1.0e-10)
        self.assertAlmostEqual(dirt.x, 0.6, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, 0.8, delta=1.0e-10)

        dist, dirt = self.box_test.distance(self.point_c)
        self.assertAlmostEqual(dist, 0, delta=1.0e-10)
        self.assertAlmostEqual(dirt.x, 0, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, 0, delta=1.0e-10)

        dist, dirt = self.box_test.distance(self.point_d)
        self.assertAlmostEqual(dist, 5, delta=1.0e-10)
        self.assertAlmostEqual(dirt.x, 0, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, -1, delta=1.0e-10)

        dist, dirt = self.box_test.distance(self.circle_in)
        self.assertAlmostEqual(dist, -1, delta=1.0e-10)
        self.assertAlmostEqual(dirt.x, 0.6, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, 0.8, delta=1.0e-10)

        dist, dirt = self.box_test.distance(self.circle_on)
        self.assertAlmostEqual(dist, 0, delta=1.0e-10)
        self.assertAlmostEqual(dirt.x, 1, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, 0, delta=1.0e-10)

        dist, dirt = self.box_test.distance(self.circle_out)
        self.assertAlmostEqual(dist, 2, delta=1.0e-10)
        self.assertAlmostEqual(dirt.x, 1, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, 0, delta=1.0e-10)
