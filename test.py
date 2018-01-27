from Box2D import *

class P(object):
    def __init__(self, x):
        self.__x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new_x):
        self.__x = new_x

p = P([1])
p.x = [10002]
p.x.append(1)
Box2D.b2CircleShape()
print(p.x)
