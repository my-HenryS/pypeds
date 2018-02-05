from pypeds.entity import *


class Pedestrian(Agent):  # FIXME remove it after use
    def __init__(self, shape):
        super(Pedestrian, self).__init__(shape)
        self.mass = 80


