from abc import ABC, abstractmethod

__all__ = ['Shape2D', 'Circle2D', 'Box2D']


class Shape2D(ABC):

    @abstractmethod
    def center(self) -> tuple:
        """
        :return: the center point (as a tuple) of the self
        """
        pass

    @abstractmethod
    def move_to(self, pos):
        """ move the center point of self to 'pos'
        :param pos: the new center point for shape
        """
        pass

    @abstractmethod
    def area(self) -> float:
        """
        :return: the area of self
        """
        pass

    @abstractmethod
    def contains(self, point) -> bool:
        """
        :param point: point (as a tuple)
        :return: whether self contains 'point'
        """
        pass

    def distance(self, other) -> (float, tuple):
        """We define the distance between two shapes as the minimum distance between any two points
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
        :param other: the other shape
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
    @classmethod
    def distance(cls, shape, other) -> (float, tuple):
        return 0, (0, 0)


class Circle2D(Shape2D):

    def __init__(self, center, radius):
        self.center, self.radius = center, radius

    def center(self) -> tuple:
        return self.center

    def move_to(self, pos):
        self.center = pos


class Box2D(Shape2D):

    def __init__(self, center, width, height):
        self.center = center
        self.w, self.h = width, height

    def center(self) -> tuple:
        return self.center

    def move_to(self, pos):
        self.center = pos



