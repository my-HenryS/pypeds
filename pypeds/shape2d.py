from abc import ABC, abstractmethod
import math
from functools import lru_cache
#todo provide multiple init methods for shape


def create_vector(type, *args):   # TODO: consider upgrade it to create_shape
    if type == Vector2D:
        return Vector2D(*args)

    if type == Point2D:
        return Point2D(*args)


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return create_vector(type(self), self.x+other.x, self.y+other.y)

    add = __add__

    def __sub__(self, other):
        return create_vector(type(self), self.x-other.x, self.y-other.y)   # FIXME consider degrading it to vector

    sub = __sub__

    def __mul__(self, other):
        if isinstance(other, Vector2D):
            return (self.x * other.x) + (self.y * other.y)
        elif isinstance(other, float) or isinstance(other, int):
            return create_vector(type(self), other * self.x, other * self.y)
        else:
            raise ArithmeticError("Vector2D cannot multiply with %s object." % type(other))

    __rmul__ = __mul__
    mul = __mul__

    def __truediv__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return create_vector(type(self), self.x / other, self.y / other)
        else:
            raise ArithmeticError("Vector2D cannot be divided by %s object." % type(other))

    div = __truediv__

    def dist(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __str__(self):
        return "(%.2f,%.2f)" % (self.x, self.y)

    def __repr__(self):
        return "Vector2D(%.2f,%.2f)" % (self.x, self.y)

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __cmp__(self, other):
        return 0

    def unit(self):
        if abs(self) != 0:
            return self / abs(self)
        else:
            return create_vector(Vector2D, 0, 0)

    def rotate(self, angle):
        """ Rotate anticlockwise angle
        :param angle: in radian measure
        """

        self.x, self.y = self.__rotate(angle)

    def get_rotation(self, angle):
        """ Get the rotated vector (another vector) of self

        :return: rotated vector
        """
        new_x, new_y = self.__rotate(angle)
        return create_vector(Vector2D, new_x, new_y)

    def __rotate(self, angle):
        if self.x != 0:
            ori_angle = math.atan(self.y / self.x)
        elif self.y > 0:
            ori_angle = math.pi / 2
        elif self.y < 0:
            ori_angle = math.pi * 3 / 2
        else:
            return 0, 0
        r = abs(self)
        new_x = r * math.cos(ori_angle + angle)
        new_y = r * math.sin(ori_angle + angle)
        return new_x, new_y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Point2D(Vector2D):
    def __repr__(self):
        return "Point2D(%.2f,%.2f)" % (self.x, self.y)

    def __hash__(self):
        return hash(self.x)+hash(self.y)

    pass



class Segment2D:
    def __init__(self, center, length, angle):
        self.center = center
        self.length = length
        self.angle = angle

    @property
    def x_left(self):
        return self.center.x - self.length * math.cos(self.angle) / 2

    @property
    def y_left(self):
        return self.center.y - self.length * math.sin(self.angle) / 2

    @property
    def x_right(self):
        return self.center.x + self.length * math.cos(self.angle) / 2

    @property
    def y_right(self):
        return self.center.y + self.length * math.sin(self.angle) / 2

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
        dist = math.sqrt(tx * tx + ty * ty)
        if -1.0e-10 < dist < 1.0e-10:
            return 0, Vector2D(0, 0)
        return dist, Vector2D(-tx/dist, -ty/dist)

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

    @property
    @abstractmethod
    def bound(self):
        """
        :return: the outbound (as a Box2D) of self
        """
        pass

    def intersects(self, other, tlr_dist=0) -> bool:
        """
        :param other: the other shape
        :return: whether the two shapes are intersected
        """
        dist, dirt = self.distance(other)
        return dist <= tlr_dist

    @abstractmethod
    def contains(self, point) -> bool:
        """
        :param point: the point in the space
        :return: whether the point is in the shape
        """
        pass

    @abstractmethod
    def get_expand(self, degree):
        """
        :param degree: the expand degree
        :return: expand shape in specifically defined direction by degree
        """
        pass

    @abstractmethod
    def to_dict(self):
        """

        :return:
        """

class DistanceCalculator(object):
    @staticmethod
    def distance(shape, other) -> (float, Vector2D):  # todo add rect
        """
        There are 5 kinds of shape : Vector2D(point2D), Circle2D, Box2D, Ellipse2D, Rectangle2D
        The combination of <shape * other> is divided to 5 * 5 conditions
        :param cls:
        :param shape:
        :param other:the distance and distance between two shapes(distance defined as a unit vector)
        :return:
        """
        if isinstance(shape, Point2D):
            if isinstance(other, Point2D):
                dist = other.dist(shape)
                if dist == 0:
                    return 0, Vector2D(0, 0)
                return dist, Vector2D((other.x - shape.x) / dist, (other.y - shape.y) / dist)

            elif isinstance(other, Circle2D):
                dist, dirt = DistanceCalculator.distance(shape, other.center)
                dist -= other.radius
                return dist, dirt

            elif isinstance(other, Ellipse2D):
                dist, dirt = DistanceCalculator.distance(other, shape)
                return dist, dirt * (-1)

            elif isinstance(other, Box2D):
                dist1, dirt1 = other.left_edge.distance(shape)
                dist2, dirt2 = other.right_edge.distance(shape)
                dist3, dirt3 = other.low_edge.distance(shape)
                dist4, dirt4 = other.upper_edge.distance(shape)
                dist = (dist1, dist2, dist3, dist4)
                dirt = (dirt1, dirt2, dirt3, dirt4)
                if other.contains(shape):
                    return - min(dist), dirt[dist.index(min(dist))]
                return min(dist), dirt[dist.index(min(dist))] * (-1)

        if isinstance(shape, Circle2D):
            if isinstance(other, Point2D):
                dist, dirt = DistanceCalculator.distance(other, shape)
                return dist, dirt * (-1)

            elif isinstance(other, Circle2D) or isinstance(other, Box2D) or isinstance(other, Ellipse2D):
                dist, dirt = DistanceCalculator.distance(shape.center, other)
                return dist - shape.radius, dirt

        if isinstance(shape, Ellipse2D):
            l_dist, l_dirt = DistanceCalculator.distance(shape.c_left, other)
            r_dist, r_dirt = DistanceCalculator.distance(shape.c_right, other)
            m_dist, m_dirt = DistanceCalculator.distance(shape.center, other)
            l_dist -= (shape.a - shape.b) / 2
            r_dist -= (shape.a - shape.b) / 2
            m_dist -= shape.b
            dist = (l_dist, r_dist, m_dist)
            dirt = (l_dirt, r_dirt, m_dirt)
            return min(dist), dirt[dist.index(min(dist))]


        if isinstance(shape, Box2D):
            if isinstance(other, Box2D):
                pass

            else:
                dist, dirt = DistanceCalculator.distance(other, shape)
                return dist, dirt * (-1)




class Circle2D(Shape2D):

    def __init__(self, center, radius):
        super().__init__(center)
        self.radius = radius

    def area(self) -> float:
        return math.pi() * self.radius * self.radius

    @property
    def bound(self):
        return Box2D(self.center, 2 * self.radius, 2 * self.radius)

    def get_expand(self, degree):
        return Circle2D(self.center, self.radius + degree)

    def contains(self, point) -> bool:
        dist, dirt = DistanceCalculator.distance(self.center, point)
        return dist <= self.radius

    def to_dict(self):
        return {"Circle2D": {"center": str(self.center), "radius": self.radius}}

    def from_dict(self, s_dict):
        """
        read from s_dict to generate a circle
        :param s_dict:
        :return:
        """
        center = s_dict["Circle2D"]["center"]
        radius = s_dict["Circle2D"]["radius"]
        return Circle2D(center, radius)

class Box2D(Shape2D):

    def __init__(self, center, length, width):
        super().__init__(center)
        self.length, self.width = length, width
        self.l_left, self.l_right = Segment2D(Point2D(0, 0), 0, 0), Segment2D(Point2D(0, 0), 0, 0)
        self.l_down, self.l_up = Segment2D(Point2D(0, 0), 0, 0), Segment2D(Point2D(0, 0), 0, 0)

    @property
    def x_min(self):
        return self.center.x - self.length / 2

    @property
    def x_max(self):
        return self.center.x + self.length / 2

    @property
    def y_min(self):
        return self.center.y - self.width / 2

    @property
    def y_max(self):
        return self.center.y + self.width / 2

    @property
    def left_edge(self):
        return self.l_left.moveto(Point2D(self.x_min, self.center.y), self.width, math.pi / 2)

    @property
    def right_edge(self):
        return self.l_right.moveto(Point2D(self.x_max, self.center.y), self.width, math.pi / 2)

    @property
    def low_edge(self):
        return self.l_down.moveto(Point2D(self.center.x, self.y_min), self.length, 0)

    @property
    def upper_edge(self):
        return self.l_up.moveto(Point2D(self.center.x, self.y_max), self.length, 0)

    def area(self) -> float:
        return self.length * self.width

    @property
    def bound(self):
        return self

    def get_expand(self, degree):
        return Box2D(self.center, self.length + 2 * degree, self.width + 2 * degree)

    def contains(self, point) -> bool:
        return self.x_min <= point.x <= self.x_max and self.y_min <= point.y <= self.y_max

    def to_dict(self):
        return {"Box2D": {"center": str(self.center), "length": self.length, "width": self.width}}

    def from_dict(self, s_dict):
        """
        read from s_dict to generate a box
        :param s_dict:
        :return:
        """
        center = s_dict["Box2D"]["center"]
        length = s_dict["Box2D"]["length"]
        width = s_dict["Box2D"]["width"]
        return Box2D(center, length, width)


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
        return Point2D(self.center.x - (self.a + self.b) * math.cos(self.angle) / 2,
                       self.center.y - (self.a + self.b) * math.sin(self.angle) / 2)

    @property
    def c_right(self):
        return Point2D(self.center.x + (self.a + self.b) * math.cos(self.angle) / 2,
                       self.center.y + (self.a + self.b) * math.sin(self.angle) / 2)

    def area(self) -> float:
        return math.pi() * self.a * self.b

    @property
    def bound(self):
        """
        Three stances of ellipse：horizontal, vertical, oblique
        :return:
        """
        if -1.0e-10 < self.angle % math.pi < 1.0e-10:
            return Box2D(self.center, 2 * self.a, 2 * self.b)
        elif -1.0e-10 < math.fabs(self.angle % math.pi) - math.pi / 2 < 1.0e-10:
            return Box2D(self.center, 2 * self.b, 2 * self.a)
        else:
            k = - math.tan(self.angle)
            h_width = math.sqrt((self.a * self.a * k * k + self.b * self.b) / (k * k + 1))
            h_length = math.sqrt(self.a * self.a + self.b * self.b - h_width * h_width)
            return Box2D(self.center, 2 * h_length, 2 * h_width)

    def get_expand(self, degree):
        return Ellipse2D(self.center, self.a + degree, self.b + degree, self.angle)

    def contains(self, point) -> bool:
        return DistanceCalculator.distance(self.center, point) <= self.b or DistanceCalculator.distance(self.c_left,
                                                                                                        point) <= (
                           self.a - self.b) / 2 or DistanceCalculator.distance(self.c_right, point) <= (
                           self.a - self.b) / 2

    def to_dict(self):
        return {"Ellipse2D": {"center": str(self.center), "a": self.a, "b": self.b, "angle": self.angle}}

    def from_dict(self, s_dict):
        """
        read from s_dict to generate a ellipse
        :param s_dict:
        :return:
        """
        center = s_dict["Ellipse2D"]["center"]
        a = s_dict["Ellipse2D"]["a"]
        b = s_dict["Ellipse2D"]["b"]
        angle = s_dict["Ellipse2D"]["angle"]
        return Ellipse2D(center, a, b, angle)


class Rectangle2D(Shape2D):

    def __init__(self, center, length, width, angle):
        super().__init__(center)
        self.length, self.width, self.angle = length, width, angle
        self.l_left, self.l_right = Segment2D(Point2D(0, 0), 0, 0), Segment2D(Point2D(0, 0), 0, 0)
        self.l_down, self.l_up = Segment2D(Point2D(0, 0), 0, 0), Segment2D(Point2D(0, 0), 0, 0)

    @property
    def left_edge(self):
        return self.l_left.moveto(Point2D(self.center.x - self.length * math.cos(self.angle) / 2,
                                   self.center.y - self.length * math.sin(self.angle) / 2), self.width,
                                  math.pi / 2 + self.angle)
    @property
    def right_edge(self):
        return self.l_right.moveto(Point2D(self.center.x + self.length * math.cos(self.angle) / 2,
                                    self.center.y + self.length * math.sin(self.angle) / 2), self.width,
                                   math.pi / 2 + self.angle)

    @property
    def low_edge(self):
        return self.l_down.moveto(Point2D(self.center.x + self.width * math.sin(self.angle) / 2,
                                   self.center.y - self.width * math.cos(self.angle) / 2), self.length, self.angle)

    @property
    def upper_edge(self):
        return self.l_up.moveto(Point2D(self.center.x - self.width * math.sin(self.angle) / 2,
                                 self.center.y + self.width * math.cos(self.angle) / 2), self.length, self.angle)

    def area(self) -> float:
        return self.length * self.width

    @property
    def bound(self):
        return Box2D(self.center,
                     self.length * math.fabs(math.cos(self.angle)) + self.width * math.fabs(math.sin(self.angle)),
                     self.length * math.fabs(math.sin(self.angle)) + self.width * math.fabs(math.cos(self.angle)))

    def get_expand(self, degree):
        return Rectangle2D(self.center, self.length + degree, self.width + degree, self.angle)

    def contains(self, point) -> bool:
        p_trans = Point2D(
            (point.x - self.center.x) * math.cos(self.angle) + (point.y - self.center.y) * math.sin(self.angle),
            - (point.x - self.center.x) * math.sin(self.angle) + (point.y - self.center.y) * math.cos(self.angle))
        return Box2D(self.center, self.length, self.width).contains(p_trans)

    def to_dict(self):
        return {"Rectangle2D": {"center": str(self.center), "length": self.length, "width": self.width, "angle": self.angle}}

    def from_dict(self, s_dict):
        """
        read from s_dict to generate a rectangle
        :param s_dict:
        :return:
        """
        center = s_dict["Rectangle2D"]["center"]
        length = s_dict["Rectangle2D"]["length"]
        width = s_dict["Rectangle2D"]["width"]
        angle = s_dict["Rectangle2D"]["angle"]
        return Rectangle2D(center, length, width, angle)