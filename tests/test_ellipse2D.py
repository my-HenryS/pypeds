from unittest import TestCase

from pypeds.shape2d import *
import math


class TestEllipse2D(TestCase):
    def setUp(self):
        self.ellipse_test = Ellipse2D(Point2D(4, 4), 4 * math.sqrt(2), 3 * math.sqrt(2), math.pi / 4)
        self.point_in = Point2D(0.5, 0)
        self.point_on = Point2D(0, 0)
        self.point_out = Point2D(8, 0)
        self.circle_in = Circle2D(Point2D(8, 0), 2 * math.sqrt(2))
        self.circle_on = Circle2D(Point2D(0, 8), math.sqrt(2))
        self.circle_out = Circle2D(Point2D(9, 7.5), math.sqrt(2) / 2)
        self.ellipse_in = Ellipse2D(Point2D(4, -4), 4 * math.sqrt(2), 3 * math.sqrt(2), 3 * math.pi / 4)
        self.ellipse_on = Ellipse2D(Point2D(7.5 + 4.5 * math.sqrt(2), 7.5), 4 * math.sqrt(2), 3 * math.sqrt(2), 0)
        self.ellipse_out = Ellipse2D(Point2D(4, 4 + 8 * math.sqrt(2)), 4 * math.sqrt(2), 3 * math.sqrt(2), math.pi / 2)
        self.box_in = Box2D(Point2D(0, -2), 2, 4)
        self.box_on = Box2D(Point2D(9, 0), 4, 2)
        self.box_out = Box2D(Point2D(-1.5, 5), 3, 4)

    def test_distance(self):
        dist, dirt = self.ellipse_test.distance(self.point_in)
        self.assertAlmostEqual(dist, (1 - math.sqrt(2)) / 2, delta=1.0e-10)
        self.assertAlmostEqual(dirt.x, 0, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, 1, delta=1.0e-10)

        dist, dirt = self.ellipse_test.distance(self.point_on)
        self.assertAlmostEqual(dist, 0, delta=1.0e-10)
        self.assertAlmostEqual(dirt.x, math.sqrt(2) / 2, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, math.sqrt(2) / 2, delta=1.0e-10)

        dist, dirt = self.ellipse_test.distance(self.point_out)
        self.assertAlmostEqual(dist, math.sqrt(2), delta=1.0e-10)
        self.assertAlmostEqual(dirt.x, math.sqrt(2) / 2, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, - math.sqrt(2) / 2, delta=1.0e-10)

        dist, dirt = self.ellipse_test.distance(self.circle_in)
        self.assertAlmostEqual(dist, - math.sqrt(2), delta=1.0e-10)
        self.assertAlmostEqual(dirt.x, - math.sqrt(2) / 2, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, math.sqrt(2) / 2, delta=1.0e-10)

        dist, dirt = self.ellipse_test.distance(self.circle_on)
        self.assertAlmostEqual(dist, 0, delta=1.0e-10)
        self.assertAlmostEqual(dirt.x, math.sqrt(2) / 2, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, - math.sqrt(2) / 2, delta=1.0e-10)

        dist, dirt = self.ellipse_test.distance(self.circle_out)
        self.assertAlmostEqual(dist, 1.5 - math.sqrt(2), delta=1.0e-10)
        self.assertAlmostEqual(dirt.x, 1, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, 0, delta=1.0e-10)

        dist, dirt = self.ellipse_test.distance(self.ellipse_in)
        self.assertAlmostEqual(dist, 8 - 6 * math.sqrt(2), delta=1.0e-10)
        self.assertAlmostEqual(dirt.x, 0, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, 1, delta=1.0e-10)

        dist, dirt = self.ellipse_test.distance(self.ellipse_on)
        self.assertAlmostEqual(dist, 0, delta=1.0e-10)
        self.assertAlmostEqual(dirt.x, -1, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, 0, delta=1.0e-10)

        dist, dirt = self.ellipse_test.distance(self.ellipse_out)
        self.assertAlmostEqual(dist, math.sqrt(2), delta=1.0e-10)
        self.assertAlmostEqual(dirt.x, 0, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, 1, delta=1.0e-10)

        dist, dirt = self.ellipse_test.distance(self.box_in)
        self.assertAlmostEqual(dist, (1 - math.sqrt(2)) / 2, delta=1.0e-10)
        self.assertAlmostEqual(dirt.x, 0, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, 1, delta=1.0e-10)

        dist, dirt = self.ellipse_test.distance(self.box_on)
        self.assertAlmostEqual(dist, 0, delta=1.0e-10)
        self.assertAlmostEqual(dirt.x, - math.sqrt(2) / 2, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, math.sqrt(2) / 2, delta=1.0e-10)

        dist, dirt = self.ellipse_test.distance(self.box_out)
        self.assertAlmostEqual(dist, 4 - 3 * math.sqrt(2), delta=1.0e-10)
        self.assertAlmostEqual(dirt.x, 1, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, 0, delta=1.0e-10)
