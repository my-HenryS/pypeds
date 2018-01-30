from abc import ABC, abstractmethod
import math
__all__ = ['Shape2D', 'Circle2D', 'Box2D']


class Shape2D(ABC):

    def __init__(self, center):
        self.center = center
        self.drawer = None

    @abstractmethod
    def area(self) -> float:
        """
        :return: the area of self
        """
        pass

    def distance(self, other) -> (float, tuple):
        """ We define the distance between two shapes as the minimum distance between any two points
         (assume to be point A and B) selected respectively from shape 'self' and 'other'.

        It should later be implemented in a Distance Calculator.
        :param other: the other shape
        :return: the distance between  A and B, and a vector (as a tuple) from A to B (e.g. return 3.0, (2.5, -2.1))
        """
        return DistanceCalculator.distance(self, other)

    @abstractmethod
    def bounds(self):
        """
        :return: the outbound (as a Box2D) of self
        """
        pass

    def hits(self, other) -> bool:
        """
        :param other: the other shape, including point
        :return: whether the two shapes are intersected
        """
        dist, dirt = self.distance(other)
        return dist <= 0

    @abstractmethod
    def expand(self, degree):
        """
        TODO: implement formal definition
        :param degree:
        :return:
        """
        pass


class DistanceCalculator(object):
    @staticmethod
    def distance(cls, shape, other) -> (float, tuple):
        return 0, (0, 0)


class Circle2D(Shape2D):

    def __init__(self, center, radius):
        super().__init__(center)
        self.radius = radius

    def area(self) -> float:
        return math.pi() * self.radius * self.radius

    def bounds(self):
        return Box2D(self.center, 2 * self.radius, 2 * self.radius)

    def expand(self, degree):
        self.radius += degree
        return self


class Box2D(Shape2D):

    def __init__(self, center, width, height):
        super().__init__(center)
        self.width, self.height = width, height

    @property
    def e_left(self):
        return self.center[0] - self.width / 2

    @property
    def e_right(self):
        return self.center[0] + self.width / 2

    @property
    def e_down(self):
        return self.center[1] - self.height / 2

    @property
    def e_up(self):
        return self.center[1] + self.height / 2

    def area(self) -> float:
        return self.w * self.h

    def bounds(self):
        pass

    def expand(self, degree):
        pass