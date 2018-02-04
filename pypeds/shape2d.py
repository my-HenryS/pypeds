from abc import ABC, abstractmethod
import math


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Vector2D(self.x-other.x, self.y-other.y)

    def __mul__(self, other):
        if isinstance(other, Vector2D):
            return (self.x * other.x) + (self.y * other.y)
        elif isinstance(other, float) or isinstance(other, int):
            return Vector2D(other * self.x, other * self.y)
        else:
            raise ArithmeticError("Vector2D cannot multiply with %s object." % type(other))

    def __truediv__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return Vector2D(self.x / other,  self.y / other)
        else:
            raise ArithmeticError("Vector2D cannot be divided by %s object." % type(other))

    def dist(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __str__(self):
        return "(%.2f,%.2f)" % (self.x, self.y)


class Point2D(Vector2D):
    pass


class Segment2D:
    def __init__(self, center, length, angle):
        self.center = center
        self.length = length
        self.angle = angle

    @property
    def x_left(self):
        return self.center[0] - self.length * math.cos(self.angle) / 2

    @property
    def y_left(self):
        return self.center[1] - self.length * math.sin(self.angle) / 2

    @property
    def x_right(self):
        return self.center[0] + self.length * math.cos(self.angle) / 2

    @property
    def y_right(self):
        return self.center[1] + self.length * math.sin(self.angle) / 2

    def distance(self, point) -> (float, Vector2D):
        dx_self = self.x_right - self.x_left
        dy_self = self.y_right - self.y_left
        dx_inter = point.x - self.x_left
        dy_inter = point.y - self.y_left
        scale = (dx_inter * dx_self + dy_inter * dy_self) / (dx_self * dx_self + dy_self * dy_self)
        if scale < 0:
            tx = self.x_left
            ty = self.y_left
        elif scale > 1:
            tx = self.x_right
            ty = self.y_right
        else:
            tx = self.x_left + scale * dx_self
            ty = self.y_left + scale * dy_self
        tx -= point.x
        ty -= point.y
        dis = math.sqrt(tx * tx + ty * ty)
        return dis, (-tx/dis, -ty/dis)

    def moveto(self, center, length, angle):
        self.center = center
        self.length = length
        self.angle = angle
        return self


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

    def distance(self, other) -> (float, Vector2D):
        """ We define the distance between two shapes as the minimum distance between any two points
         (assume to be point A and B) selected respectively from shape 'self' and 'other'.

        It should later be implemented in a Distance Calculator.
        :param other: the other shape
        :return: the distance between  A and B, and a unit vector (as a Vector2D) from A to B (e.g. 3.0, (0.6, -0.8))
        """
        return DistanceCalculator.distance(self, other)

    @abstractmethod
    def bound(self):
        """
        :return: the outbound (as a Box2D) of self
        """
        pass

    def intersects(self, other) -> bool:
        """
        :param other: the other shape
        :return: whether the two shapes are intersected
        """
        dist, dirt = self.distance(other)
        return dist <= 0

    @abstractmethod
    def contains(self, point) -> bool:
        """
        :param point: the point in the space
        :return: whether the point is in the shape
        """
        pass

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
    def distance(cls, shape, other) -> (float, Vector2D):
        """
        There are 5 kinds of shape : Vector2D(point2D), Circle2D, Box2D, Ellipse2D, Rectangle2D
        The combination of <shape * other> is divided to 5 * 5 conditions
        :param cls:
        :param shape:
        :param other:the distance and distance between two shapes(distance defined as a unit vector)
        :return:
        """
        if isinstance(other, Point2D):
            if isinstance(shape, Point2D):
                dis = other.dist(shape)
                return dis, ((other.x - shape.x) / dis, (other.y - shape.y) / dis)
            if isinstance(shape, Circle2D):
                dis, dir = DistanceCalculator.distance(shape.center, other)
                return dis - shape.radius, dir
            if isinstance(shape, Ellipse2D):
                dis, dir = DistanceCalculator.distance(other, shape)
                return dis, dir.mul(-1)
            if isinstance(shape, Box2D or Rectangle2D):
                dis1, dir1 = DistanceCalculator.distance(shape.get_left, other)
                dis2, dir2 = DistanceCalculator.distance(shape.get_right, other)
                dis3, dir3 = DistanceCalculator.distance(shape.get_down, other)
                dis4, dir4 = DistanceCalculator.distance(shape.get_up, other)
                dis = (dis1, dis2, dis3, dis4)
                dir = (dir1, dir2, dir3, dir4)
                if not shape.contains(other):
                    return min(dis), dir[dis.index(min(dis))]
                else:
                    return (-1) * min(dis), dir[dis.index(min(dis))]
        if isinstance(other, Circle2D):
            dis, dir = DistanceCalculator.distance(shape, other.center)
            return dis - other.radius, dir
        if isinstance(other, Ellipse2D):
            l_dis, l_dir = DistanceCalculator.distance(shape, other.c_left)
            r_dis, r_dir = DistanceCalculator.distance(shape, other.c_right)
            m_dis, m_dir = DistanceCalculator.distance(shape, other.center)
            l_dis -= (other.a - other.b) / 2
            r_dis -= (other.a - other.b) / 2
            m_dis -= other.b
            if l_dis < r_dis:
                if l_dis < m_dis:
                    return l_dis, l_dir
                else:
                    return m_dis, m_dir
            else:
                if r_dis < m_dis:
                    return r_dis, r_dir
                else:
                    return m_dis, m_dir
        if isinstance(other, Box2D or Rectangle2D):
            dis, dir = DistanceCalculator.distance(other, shape)
            return dis, dir.mul(-1)


class Circle2D(Shape2D):

    def __init__(self, center, radius):
        super().__init__(center)
        self.radius = radius

    def area(self) -> float:
        return math.pi() * self.radius * self.radius

    def bound(self):
        return Box2D(self.center, 2 * self.radius, 2 * self.radius)

    def expand(self, degree):
        self.radius += degree
        return self

    def contains(self, point) -> bool:
        dis, dir = DistanceCalculator.distance(self.center, point)
        return dis <= self.radius


class Box2D(Shape2D):

    def __init__(self, center, length, width):
        super().__init__(center)
        self.length, self.width = length, width
        self.l_left, self.l_right, self.l_down, self.l_up = ((0, 0), 0, 0), ((0, 0), 0, 0), ((0, 0), 0, 0), ((0, 0), 0, 0)

    @property
    def e_left(self):
        return self.center.x - self.length / 2

    @property
    def e_right(self):
        return self.center.x + self.length / 2

    @property
    def e_down(self):
        return self.center.y - self.width / 2

    @property
    def e_up(self):
        return self.center.y + self.width / 2

    @property
    def get_left(self):
        return self.l_left.moveto((self.e_left, self.center[1]), self.width, math.pi/2)

    @property
    def get_right(self):
        return self.l_right.moveto((self.e_right, self.center[1]), self.width, math.pi/2)

    @property
    def get_down(self):
        return self.l_down.moveto((self.center[0], self.e_down), self.length, 0)

    @property
    def get_up(self):
        return self.l_up.moveto((self.center[0], self.e_up), self.length, 0)

    def area(self) -> float:
        return self.length * self.width

    def bound(self):
        return self

    def expand(self, degree):
        self.length += 2 * degree
        self.width += 2 * degree
        return self

    def contains(self, point) -> bool:
        return self.e_left <= point.x <= self.e_right and self.e_down <= point.y <= self.e_up


class Ellipse2D(Shape2D):

    def __init__(self, center, a, b, angle):
        super().__init__(center)
        if a > b:
            self.a, self.b = a, b
        else:
            self.a, self.b = b, a
        self.angle = angle

    @property
    def c_left(self):
        return Point2D(self.center.x + (self.a + self.b) * math.cos(self.angle) / (-2),
                       self.center.y + (self.a + self.b) * math.sin(self.angle) / (-2))

    @property
    def c_right(self):
        return Point2D(self.center.x + (self.a + self.b) * math.cos(self.angle) / 2,
                       self.center.y + (self.a + self.b) * math.sin(self.angle) / 2)

    def area(self) -> float:
        return math.pi() * self.a * self.b

    def bound(self):
        """
        Three stances of ellipse：horizontal, vertical, oblique
        :return:
        """
        if self.angle % math.pi() == 0:
            return Box2D(self.center, 2 * self.a, 2 * self.b)
        elif math.fabs(self.angle % math.pi()) - math.pi() / 2 == 0:
            return Box2D(self.center, 2 * self.b, 2 * self.a)
        else:
            k = (-1) * math.tan(self.angle)
            h_height = math.sqrt((self.a * self.a * k * k + self.b * self.b) / (k * k + 1))
            h_width = math.sqrt(self.a * self.a + self.b * self.b - h_height * h_height)
            return Box2D(self.center, 2 * h_width, 2 * h_height)

    def expand(self, degree):
        self.a += degree
        self.b += degree
        return self

    def contains(self, point) -> bool:
        return DistanceCalculator.distance(self.center, point) <= self.b and DistanceCalculator.distance(self.c_left, point) \
               <= (self.a - self.b) / 2 and DistanceCalculator.distance(self.c_right, point) <= (self.a - self.b) / 2


class Rectangle2D(Shape2D):

    def __init__(self, center, length, width, angle):
        super().__init__(center)
        self.length, self.width, self.angle = length, width, angle
        self.l_left, self.l_right, self.l_down, self.l_up = ((0, 0), 0, 0), ((0, 0), 0, 0), ((0, 0), 0, 0), ((0, 0), 0, 0)

    @property
    def get_left(self):
        return self.l_left.moveto((self.center[0] - self.length * math.cos(self.angle) / 2,
                                   self.center[1] - self.length * math.sin(self.angle) / 2), self.width,
                                  math.pi / 2 + self.angle)
    @property
    def get_right(self):
        return self.l_left.moveto((self.center[0] + self.length * math.cos(self.angle) / 2,
                                   self.center[1] + self.length * math.sin(self.angle) / 2), self.width,
                                  math.pi / 2 + self.angle)

    @property
    def get_down(self):
        return self.l_left.moveto((self.center[0] + self.length * math.sin(self.angle) / 2,
                                   self.center[1] - self.length * math.cos(self.angle) / 2), self.length, self.angle)

    @property
    def get_up(self):
        return self.l_left.moveto((self.center[0] - self.length * math.sin(self.angle) / 2,
                                   self.center[1] + self.length * math.cos(self.angle) / 2), self.length, self.angle)

    def area(self) -> float:
        return self.length * self.width

    def bound(self):
        return Box2D(self.center, self.length * math.cos(self.angle) + self.width * math.sin(self.angle),
                     self.length * math.sin(self.angle) + self.width * math.cos(self.angle))

    def expand(self, degree):
        self.length += 2 * degree
        self.width += 2 * degree
        return self

    def contains(self, point) -> bool:
        pass

v1 = Vector2D(1,2)
v2 = Vector2D(3,4)
r = 3
print(v1*v2)
print(v1*r)
print(v1-v2)
print(v1/r)
print(v1/v2)