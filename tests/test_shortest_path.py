from unittest import TestCase

from pypeds.shape2d import Point2D
from pypeds.utils import shortest_path


class TestShortest_path(TestCase):
    def test_shortest_path(self):
        map = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        dest = Point2D(0, 0)

        print(shortest_path(map, dest))   # fixme