from pypeds.entity import *
from pypeds.shape2d import *

class Pedestrian(Agent):
    def __init__(self, shape):
        super(Pedestrian, self).__init__(shape)
        self.mass = 80

    def to_dict(self):
        return {"pedestrian": {"shape": self.shape.to_dict(), "velocity":self.velocity, "mass": self.mass}}

class Wall(Movable):
    def __init__(self,shape):
        super(Wall, self).__init__(shape)

    def affected(self, affection):
        pass

class SafetyRegion(Goal):
    pass


class RotatePedestrian(RotateAgent):
    def __init__(self, shape):
        super(RotatePedestrian, self).__init__(shape)
        self.mass = 80
        self.inertia = 4
