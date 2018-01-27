from abc import ABC, abstractmethod

__all__ = ['Shape2D', 'Circle2D']


class Shape2D(ABC):

    @abstractmethod
    def center(self) -> tuple:
        pass

    @abstractmethod
    def move_to(self, pos):
        pass

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def contains(self, point) -> bool:
        pass

    @abstractmethod
    def distance(self, other) -> int:
        pass

    @abstractmethod
    def bounds(self):
        pass

    def hits(self, other) -> bool:
        return self.distance(other) <= 0

    @abstractmethod
    def expand(self, degree):
        pass


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



