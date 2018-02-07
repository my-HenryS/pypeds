from unittest import TestCase

from pypeds.shape2d import *


class TestCircle2D(TestCase):
    def setUp(self):
        self.circle_test = Circle2D(Point2D(3, 4), 5)
        self.point_in = Point2D(3, 0)
        self.point_on = Point2D(0, 0)
        self.point_out = Point2D(9, 4)
        self.circle_in = Circle2D(Point2D(3, -5), 5)
        self.circle_on = Circle2D(Point2D(9, 12), 5)
        self.circle_out = Circle2D(Point2D(15, 4), 5)
        self.box_in = Box2D(Point2D(-1.5, 2), 3, 4)
        self.box_on = Box2D(Point2D(2, -3), 4, 4)
        self.box_out = Box2D(Point2D(-3.6, -4.8), 3, 4)

    def test_distance(self):
        dist, dirt = self.circle_test.distance(self.point_in)
        self.assertAlmostEqual(dist, -1, delta=1.0e-10)
        self.assertAlmostEqual(dirt.x, 0, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, 1, delta=1.0e-10)

        dist, dirt = self.circle_test.distance(self.point_on)
        self.assertAlmostEqual(dist, 0, delta=1.0e-10)
        self.assertAlmostEqual(dirt.x, 0.6, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, 0.8, delta=1.0e-10)

        dist, dirt = self.circle_test.distance(self.point_out)
        self.assertAlmostEqual(dist, 1, delta=1.0e-10)
        self.assertAlmostEqual(dirt.x, 1, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, 0, delta=1.0e-10)

        dist, dirt = self.circle_test.distance(self.circle_in)
        self.assertAlmostEqual(dist, -1, delta=1.0e-10)
        self.assertAlmostEqual(dirt.x, 0, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, 1, delta=1.0e-10)

        dist, dirt = self.circle_test.distance(self.circle_on)
        self.assertAlmostEqual(dist, 0, delta=1.0e-10)
        self.assertAlmostEqual(dirt.x, -0.6, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, -0.8, delta=1.0e-10)

        dist, dirt = self.circle_test.distance(self.circle_out)
        self.assertAlmostEqual(dist, 2, delta=1.0e-10)
        self.assertAlmostEqual(dirt.x, 1, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, 0, delta=1.0e-10)

        dist, dirt = self.circle_test.distance(self.box_in)
        self.assertAlmostEqual(dist, -1, delta=1.0e-10)
        self.assertAlmostEqual(dirt.x, 1, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, 0, delta=1.0e-10)

        dist, dirt = self.circle_test.distance(self.box_on)
        self.assertAlmostEqual(dist, 0, delta=1.0e-10)
        self.assertAlmostEqual(dirt.x, 0, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, 1, delta=1.0e-10)

        dist, dirt = self.circle_test.distance(self.box_out)
        self.assertAlmostEqual(dist, 1, delta=1.0e-10)
        self.assertAlmostEqual(dirt.x, -0.6, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, -0.8, delta=1.0e-10)
