from pypeds.entity import *
from pypeds.shape2d import *

class Pedestrian(Agent):
    def __init__(self, shape):
        super(Pedestrian, self).__init__(shape)
        self.mass = 80

class Wall(Movable):
    def __init__(self,shape):
        super(Wall, self).__init__(shape)

    def affected(self, affection):
        pass

class SafetyRegion(Goal):
    pass

