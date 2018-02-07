from unittest import TestCase

from pypeds.shape2d import *
import math


class TestSegment2D(TestCase):
    def setUp(self):
        self.segment1 = Segment2D(Point2D(1, 0), 2, 0)
        self.segment2 = Segment2D(Point2D(0, 1), 2, math.pi / 2)
        self.segment3 = Segment2D(Point2D(-1, 1), 2 * math.sqrt(2), math.pi * 3 / 4)

    def test_distance(self):
        dist, dirt = self.segment1.distance(Point2D(1, 1))
        self.assertAlmostEqual(dist, 1)
        self.assertAlmostEqual(dirt.x, 0, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, 1, delta=1.0e-10)

        dist, dirt = self.segment1.distance(Point2D(0, 0))
        self.assertAlmostEqual(dist, 0)
        self.assertAlmostEqual(dirt.x, 0, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, 0, delta=1.0e-10)

        dist, dirt = self.segment1.distance(Point2D(3, 0))
        self.assertAlmostEqual(dist, 1)
        self.assertAlmostEqual(dirt.x, 1, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, 0, delta=1.0e-10)

        dist, dirt = self.segment1.distance(Point2D(-1, -1))
        self.assertEqual(dist, math.sqrt(2))
        self.assertAlmostEqual(dirt.x, - math.sqrt(2) / 2, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, - math.sqrt(2) / 2, delta=1.0e-10)

        dist, dirt = self.segment2.distance(Point2D(1, 1))
        self.assertAlmostEqual(dist, 1)
        self.assertAlmostEqual(dirt.x, 1, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, 0, delta=1.0e-10)

        dist, dirt = self.segment2.distance(Point2D(0, 2))
        self.assertAlmostEqual(dist, 0)
        self.assertAlmostEqual(dirt.x, 0, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, 0, delta=1.0e-10)

        dist, dirt = self.segment2.distance(Point2D(0, -1))
        self.assertAlmostEqual(dist, 1)
        self.assertAlmostEqual(dirt.x, 0, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, -1, delta=1.0e-10)

        dist, dirt = self.segment2.distance(Point2D(1, -1))
        self.assertAlmostEqual(dist, math.sqrt(2))
        self.assertAlmostEqual(dirt.x, math.sqrt(2) / 2, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, - math.sqrt(2) / 2, delta=1.0e-10)

        dist, dirt = self.segment3.distance(Point2D(-2, 0))
        self.assertAlmostEqual(dist, math.sqrt(2))
        self.assertAlmostEqual(dirt.x, - math.sqrt(2) / 2, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, - math.sqrt(2) / 2, delta=1.0e-10)

        dist, dirt = self.segment3.distance(Point2D(0, 0))
        self.assertAlmostEqual(dist, 0)
        self.assertAlmostEqual(dirt.x, 0, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, 0, delta=1.0e-10)

        dist, dirt = self.segment3.distance(Point2D(1, -1))
        self.assertAlmostEqual(dist, math.sqrt(2))
        self.assertAlmostEqual(dirt.x, math.sqrt(2) / 2, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, - math.sqrt(2) / 2, delta=1.0e-10)

        dist, dirt = self.segment3.distance(Point2D(1, 0))
        self.assertAlmostEqual(dist, 1)
        self.assertAlmostEqual(dirt.x, 1, delta=1.0e-10)
        self.assertAlmostEqual(dirt.y, 0, delta=1.0e-10)
