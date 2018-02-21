from pypeds.entity import *


class Pedestrian(Agent):
    def __init__(self, shape):
        super(Pedestrian, self).__init__(shape)
        self.mass = 80


class SafetyRegion(Goal):
    pass

